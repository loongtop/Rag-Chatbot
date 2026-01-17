"""
Unified error handling for the API server.

Provides consistent error response format across all endpoints.
All errors include a request_id for traceability.

SPEC Reference: 
- ARCH-API-001: Unified error response format
- REQ-L0-SEC-004: Prompt Injection protection
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel


class ErrorCode(str, Enum):
    """Standardized error codes for the API.
    
    Format: DOMAIN_SPECIFIC_ERROR
    """
    # Validation errors
    VALIDATION_ERROR = "VALIDATION_ERROR"
    INVALID_INPUT = "INVALID_INPUT"
    
    # Authentication errors
    UNAUTHORIZED = "UNAUTHORIZED"
    INVALID_TOKEN = "INVALID_TOKEN"
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    
    # Authorization errors
    FORBIDDEN = "FORBIDDEN"
    ADMIN_REQUIRED = "ADMIN_REQUIRED"
    
    # Resource errors
    NOT_FOUND = "NOT_FOUND"
    PRODUCT_NOT_FOUND = "PRODUCT_NOT_FOUND"
    DOCUMENT_NOT_FOUND = "DOCUMENT_NOT_FOUND"
    SESSION_NOT_FOUND = "SESSION_NOT_FOUND"
    
    # Rate limiting
    RATE_LIMIT_EXCEEDED = "RATE_LIMIT_EXCEEDED"
    
    # Provider errors
    LLM_PROVIDER_ERROR = "LLM_PROVIDER_ERROR"
    LLM_TIMEOUT = "LLM_TIMEOUT"
    EMBEDDING_ERROR = "EMBEDDING_ERROR"
    
    # Service unavailable
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    STT_UNAVAILABLE = "STT_UNAVAILABLE"  # SPEC-009: Stub for v0.1
    TTS_UNAVAILABLE = "TTS_UNAVAILABLE"  # SPEC-009: Stub for v0.1
    
    # Internal errors
    INTERNAL_ERROR = "INTERNAL_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"


class ErrorDetail(BaseModel):
    """Detail for a specific field error."""
    field: str
    reason: str


class ErrorResponse(BaseModel):
    """Standardized API error response format.
    
    Per ARCH-API-001: All errors must include request_id.
    """
    code: ErrorCode
    message: str
    details: list[ErrorDetail] | None = None
    request_id: str


class ErrorEnvelope(BaseModel):
    """Wrapper for error response.
    
    Example response:
    {
        "error": {
            "code": "VALIDATION_ERROR",
            "message": "email 格式不正确",
            "details": [{"field": "email", "reason": "invalid format"}],
            "request_id": "req_01H..."
        }
    }
    """
    error: ErrorResponse


class APIError(Exception):
    """Base exception for API errors.
    
    Usage:
        raise APIError(
            code=ErrorCode.VALIDATION_ERROR,
            message="Invalid input",
            status_code=400
        )
    """
    
    def __init__(
        self,
        code: ErrorCode,
        message: str,
        status_code: int = 500,
        details: list[dict[str, Any]] | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details
        super().__init__(message)


class ValidationError(APIError):
    """Validation error (400)."""
    
    def __init__(self, message: str, details: list[dict[str, Any]] | None = None) -> None:
        super().__init__(
            code=ErrorCode.VALIDATION_ERROR,
            message=message,
            status_code=400,
            details=details,
        )


class UnauthorizedError(APIError):
    """Authentication required (401)."""
    
    def __init__(self, message: str = "Authentication required") -> None:
        super().__init__(
            code=ErrorCode.UNAUTHORIZED,
            message=message,
            status_code=401,
        )


class ForbiddenError(APIError):
    """Access denied (403)."""
    
    def __init__(self, message: str = "Access denied") -> None:
        super().__init__(
            code=ErrorCode.FORBIDDEN,
            message=message,
            status_code=403,
        )


class NotFoundError(APIError):
    """Resource not found (404)."""
    
    def __init__(self, message: str = "Resource not found") -> None:
        super().__init__(
            code=ErrorCode.NOT_FOUND,
            message=message,
            status_code=404,
        )


class RateLimitError(APIError):
    """Rate limit exceeded (429)."""
    
    def __init__(self, message: str = "Rate limit exceeded") -> None:
        super().__init__(
            code=ErrorCode.RATE_LIMIT_EXCEEDED,
            message=message,
            status_code=429,
        )


class ProviderError(APIError):
    """LLM/Embedding provider error (502)."""
    
    def __init__(self, message: str, code: ErrorCode = ErrorCode.LLM_PROVIDER_ERROR) -> None:
        super().__init__(
            code=code,
            message=message,
            status_code=502,
        )


class ServiceUnavailableError(APIError):
    """Service unavailable (503).
    
    Used for STT/TTS stubs in v0.1.
    """
    
    def __init__(self, message: str, code: ErrorCode = ErrorCode.SERVICE_UNAVAILABLE) -> None:
        super().__init__(
            code=code,
            message=message,
            status_code=503,
        )
