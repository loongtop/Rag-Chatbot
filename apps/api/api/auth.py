"""
Authentication API routes and utilities.

Provides email verification code login for Widget users.

SPEC Reference: SPEC-007 (Email Verification Login)
IFC Reference: IFC-CHAT-API
TBD Reference: TBD-L0-010 (Email login implementation details)
"""

import secrets
import time
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel, EmailStr, Field

from apps.api.core.errors import (
    RateLimitError,
    UnauthorizedError,
    ValidationError,
)
from apps.api.core.logging import get_logger
from apps.api.core.middleware import rate_limiter
from apps.api.config.settings import get_settings

logger = get_logger(__name__)
router = APIRouter(prefix="/auth", tags=["auth"])


# =============================================================================
# Models
# =============================================================================

class SendCodeRequest(BaseModel):
    """Request for sending verification code."""
    email: EmailStr


class SendCodeResponse(BaseModel):
    """Response for send code request."""
    success: bool


class VerifyRequest(BaseModel):
    """Request for verifying email code."""
    email: EmailStr
    code: str = Field(..., min_length=6, max_length=6)


class UserInfo(BaseModel):
    """Basic user info returned after verification."""
    email: str


class VerifyResponse(BaseModel):
    """Response for verify request."""
    token: str
    user: UserInfo


# =============================================================================
# In-Memory Code Store (replace with Redis in production)
# TODO: Implement persistent storage (SPEC-007)
# =============================================================================

class CodeStore:
    """Simple in-memory verification code store.
    
    TODO: Replace with Redis for production (SPEC-007)
    """
    
    def __init__(self, expire_seconds: int = 300) -> None:
        self._codes: dict[str, tuple[str, float]] = {}
        self._expire_seconds = expire_seconds
    
    def store(self, email: str, code: str) -> None:
        """Store a verification code."""
        self._codes[email.lower()] = (code, time.time())
    
    def verify(self, email: str, code: str) -> bool:
        """Verify a code. Returns True if valid, False otherwise."""
        email_lower = email.lower()
        if email_lower not in self._codes:
            return False
        
        stored_code, timestamp = self._codes[email_lower]
        
        # Check expiration
        if time.time() - timestamp > self._expire_seconds:
            del self._codes[email_lower]
            return False
        
        # Check code
        if stored_code != code:
            return False
        
        # Code is valid, remove it
        del self._codes[email_lower]
        return True
    
    def cleanup(self) -> None:
        """Remove expired codes."""
        now = time.time()
        expired = [
            email for email, (_, timestamp) in self._codes.items()
            if now - timestamp > self._expire_seconds
        ]
        for email in expired:
            del self._codes[email]


# Global code store
_code_store = CodeStore()


# =============================================================================
# Token Generation (simple implementation)
# TODO: Implement proper JWT tokens (SPEC-007)
# =============================================================================

def generate_token(email: str) -> str:
    """Generate a simple opaque token.
    
    TODO: Implement proper JWT with expiration (SPEC-007)
    """
    random_part = secrets.token_urlsafe(32)
    return f"usr_{random_part}"


# =============================================================================
# Routes
# =============================================================================

@router.post("/send-code", response_model=SendCodeResponse)
async def send_code(request: Request, body: SendCodeRequest) -> SendCodeResponse:
    """Send verification code to email.
    
    SPEC-007: POST /api/auth/send-code
    - Input: email
    - Output: success
    
    Rate limited: 5 requests per 10 minutes per IP.
    
    TBD-L0-010: Email sending implementation
    TODO: Integrate with actual email service (SMTP/SendGrid/etc.)
    """
    settings = get_settings()
    client_ip = request.client.host if request.client else "unknown"
    
    # Strict rate limiting for auth (REQ-L0-SEC-003)
    if not rate_limiter.is_allowed(f"auth:{client_ip}", settings.rate_limit_auth, 600):
        retry_after = rate_limiter.get_retry_after(f"auth:{client_ip}", 600)
        raise RateLimitError(f"Too many requests. Retry after {retry_after}s.")
    
    # Generate 6-digit code
    code = "".join([str(secrets.randbelow(10)) for _ in range(6)])
    
    # Store code
    _code_store.store(body.email, code)
    
    # TODO: Send email via configured provider
    # For now, log the code (DEVELOPMENT ONLY!)
    logger.warning(
        "verification_code_generated",
        email=body.email[:3] + "***",  # Partial email for privacy
        code=code if settings.debug else "[HIDDEN]",  # Only show in debug mode!
        note="TODO: Implement email sending (TBD-L0-010)",
    )
    
    return SendCodeResponse(success=True)


@router.post("/verify", response_model=VerifyResponse)
async def verify(request: Request, body: VerifyRequest) -> VerifyResponse:
    """Verify email with code.
    
    SPEC-007: POST /api/auth/verify
    - Input: email, code
    - Output: token, user
    
    On success, returns a token for authenticated endpoints.
    """
    settings = get_settings()
    client_ip = request.client.host if request.client else "unknown"
    
    # Rate limiting
    if not rate_limiter.is_allowed(f"verify:{client_ip}", settings.rate_limit_auth * 2, 600):
        raise RateLimitError("Too many verification attempts.")
    
    # Verify code
    if not _code_store.verify(body.email, body.code):
        logger.info("verification_failed", email=body.email[:3] + "***")
        raise UnauthorizedError("Invalid or expired verification code.")
    
    # Generate token
    token = generate_token(body.email)
    
    logger.info("user_verified", email=body.email[:3] + "***")
    
    return VerifyResponse(
        token=token,
        user=UserInfo(email=body.email),
    )
