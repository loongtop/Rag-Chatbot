"""
Logging configuration for the API server.

Provides structured JSON logging for production and human-readable
format for development.

SPEC Reference:
- REQ-L0-SEC-003: Audit logging
- ARCH-API-001: Request traceability via request_id
"""

import logging
import sys
from contextvars import ContextVar
from typing import Any

import structlog

from apps.api.config.settings import get_settings

# Context variable for request ID
request_id_ctx: ContextVar[str] = ContextVar("request_id", default="")


def get_request_id() -> str:
    """Get current request ID from context."""
    return request_id_ctx.get()


def add_request_id(
    logger: logging.Logger,
    method_name: str,
    event_dict: dict[str, Any],
) -> dict[str, Any]:
    """Add request_id to all log entries."""
    request_id = get_request_id()
    if request_id:
        event_dict["request_id"] = request_id
    return event_dict


def setup_logging() -> None:
    """Configure structured logging.
    
    Uses JSON format in production, human-readable in development.
    """
    settings = get_settings()
    
    # Determine log level
    log_level = logging.DEBUG if settings.debug else logging.INFO
    if settings.environment == "production":
        log_level = logging.WARNING
    
    # Configure processors
    shared_processors: list[structlog.types.Processor] = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        add_request_id,
        structlog.processors.StackInfoRenderer(),
    ]
    
    if settings.environment == "production":
        # JSON format for production (machine-parseable)
        processors = shared_processors + [
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ]
    else:
        # Human-readable format for development
        processors = shared_processors + [
            structlog.dev.ConsoleRenderer(colors=True),
        ]
    
    # Configure structlog
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Configure stdlib logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=log_level,
    )
    
    # Reduce noise from third-party libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Get a logger instance with the given name.
    
    Usage:
        logger = get_logger(__name__)
        logger.info("message", key="value")
    """
    return structlog.get_logger(name)


# =============================================================================
# Audit Logger
# REQ-L0-SEC-003: 后台操作审计日志
# =============================================================================

class AuditLogger:
    """Audit logger for admin operations.
    
    TODO: Implement persistent audit log storage (SPEC-021)
    """
    
    def __init__(self) -> None:
        self._logger = get_logger("audit")
    
    def log_admin_action(
        self,
        action: str,
        resource: str,
        resource_id: str | None = None,
        details: dict[str, Any] | None = None,
        admin_user: str | None = None,
    ) -> None:
        """Log an admin action for audit purposes.
        
        Args:
            action: Action performed (create, update, delete, etc.)
            resource: Resource type (product, document, etc.)
            resource_id: Optional resource identifier
            details: Optional additional details
            admin_user: Admin user performing the action
        """
        self._logger.info(
            "admin_action",
            action=action,
            resource=resource,
            resource_id=resource_id,
            details=details,
            admin_user=admin_user,
        )


# Global audit logger instance
audit_logger = AuditLogger()
