"""
FastAPI middleware for the API server.

Provides:
- Request ID generation and propagation
- Error handling
- Request/response logging
- Rate limiting (basic implementation)

SPEC Reference:
- ARCH-API-001: Request ID for traceability
- REQ-L0-SEC-003: Rate limiting
"""

import time
import uuid
from collections import defaultdict
from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from apps.api.core.errors import APIError, ErrorCode, ErrorEnvelope, ErrorResponse
from apps.api.core.logging import get_logger, get_request_id, request_id_ctx

logger = get_logger(__name__)


def setup_middleware(app: FastAPI) -> None:
    """Configure all middleware for the application."""
    
    @app.middleware("http")
    async def request_id_middleware(request: Request, call_next: Callable) -> Response:
        """Add request_id to every request for traceability.
        
        Per ARCH-API-001: All responses must include traceable request_id.
        """
        # Generate or extract request ID
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4())[:12])
        request_id = f"req_{request_id}"
        
        # Set in context for logging
        token = request_id_ctx.set(request_id)
        
        try:
            response = await call_next(request)
            response.headers["X-Request-ID"] = request_id
            return response
        finally:
            request_id_ctx.reset(token)
    
    @app.middleware("http")
    async def logging_middleware(request: Request, call_next: Callable) -> Response:
        """Log all requests and responses."""
        start_time = time.perf_counter()
        
        # Log request
        logger.info(
            "request_started",
            method=request.method,
            path=request.url.path,
            query=str(request.query_params),
        )
        
        response = await call_next(request)
        
        # Log response
        duration_ms = (time.perf_counter() - start_time) * 1000
        logger.info(
            "request_completed",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=round(duration_ms, 2),
        )
        
        return response


def setup_exception_handlers(app: FastAPI) -> None:
    """Configure exception handlers for consistent error responses."""
    
    @app.exception_handler(APIError)
    async def api_error_handler(request: Request, exc: APIError) -> JSONResponse:
        """Handle APIError exceptions with consistent format."""
        error_response = ErrorEnvelope(
            error=ErrorResponse(
                code=exc.code,
                message=exc.message,
                details=[{"field": d["field"], "reason": d["reason"]} for d in exc.details]
                if exc.details else None,
                request_id=get_request_id(),
            )
        )
        return JSONResponse(
            status_code=exc.status_code,
            content=error_response.model_dump(exclude_none=True),
        )
    
    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception) -> JSONResponse:
        """Handle unexpected exceptions."""
        logger.exception("unhandled_exception", error=str(exc))
        
        error_response = ErrorEnvelope(
            error=ErrorResponse(
                code=ErrorCode.INTERNAL_ERROR,
                message="An internal error occurred",
                request_id=get_request_id(),
            )
        )
        return JSONResponse(
            status_code=500,
            content=error_response.model_dump(exclude_none=True),
        )


# =============================================================================
# Rate Limiting (Basic In-Memory Implementation)
# REQ-L0-SEC-003: API Rate Limiting
# TODO: Use Redis for distributed rate limiting in production
# =============================================================================

class RateLimiter:
    """Simple in-memory rate limiter.
    
    TODO: Replace with Redis-based implementation for production (SPEC-003)
    """
    
    def __init__(self) -> None:
        self._requests: dict[str, list[float]] = defaultdict(list)
    
    def is_allowed(
        self,
        key: str,
        limit: int,
        window_seconds: int = 60,
    ) -> bool:
        """Check if request is allowed under rate limit.
        
        Args:
            key: Unique identifier (e.g., IP address, user ID)
            limit: Maximum requests allowed in window
            window_seconds: Time window in seconds
            
        Returns:
            True if request is allowed, False otherwise
        """
        now = time.time()
        window_start = now - window_seconds
        
        # Clean old requests
        self._requests[key] = [
            req_time for req_time in self._requests[key]
            if req_time > window_start
        ]
        
        # Check limit
        if len(self._requests[key]) >= limit:
            return False
        
        # Record request
        self._requests[key].append(now)
        return True
    
    def get_retry_after(self, key: str, window_seconds: int = 60) -> int:
        """Get seconds until rate limit resets."""
        if not self._requests[key]:
            return 0
        oldest = min(self._requests[key])
        return max(0, int(oldest + window_seconds - time.time()))


# Global rate limiter instance
rate_limiter = RateLimiter()
