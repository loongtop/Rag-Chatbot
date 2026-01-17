"""
Handoff API routes.

Provides human agent handoff for Widget users who want to talk to a human.

SPEC Reference: SPEC-008 (Handoff Create & Queue Endpoint)
IFC Reference: IFC-CHAT-API
TBD Reference: TBD-L0-011 (Handoff implementation details)
"""

import uuid
import time
from enum import Enum

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from apps.api.core.errors import NotFoundError, RateLimitError
from apps.api.core.logging import get_logger
from apps.api.core.middleware import rate_limiter
from apps.api.config.settings import get_settings

logger = get_logger(__name__)
router = APIRouter(prefix="/handoff", tags=["handoff"])


# =============================================================================
# Models
# =============================================================================

class HandoffStatus(str, Enum):
    """Handoff request status."""
    PENDING = "pending"
    ACTIVE = "active"
    RESOLVED = "resolved"
    CANCELLED = "cancelled"
    TIMEOUT = "timeout"


class HandoffRequest(BaseModel):
    """Request for creating handoff."""
    session_id: str = Field(..., alias="sessionId")
    
    model_config = {"populate_by_name": True}


class HandoffResponse(BaseModel):
    """Response for handoff creation."""
    queue_position: int = Field(..., alias="queuePosition")
    
    model_config = {"populate_by_name": True}


class QueueStatusRequest(BaseModel):
    """Request for queue status."""
    session_id: str = Field(..., alias="sessionId")
    
    model_config = {"populate_by_name": True}


class QueueStatusResponse(BaseModel):
    """Response for queue status."""
    status: HandoffStatus
    queue_position: int | None = Field(None, alias="queuePosition")
    
    model_config = {"populate_by_name": True}


# =============================================================================
# In-Memory Queue (replace with database in production)
# TODO: Implement persistent storage (SPEC-008)
# =============================================================================

class HandoffQueue:
    """Simple in-memory handoff queue.
    
    TODO: Replace with database storage (SPEC-008)
    TBD-L0-011: Queue strategy and timeout handling
    """
    
    def __init__(self) -> None:
        self._queue: list[dict] = []
        self._requests: dict[str, dict] = {}  # session_id -> request details
    
    def create(self, session_id: str) -> int:
        """Create a handoff request and return queue position."""
        if session_id in self._requests:
            # Already in queue
            return self._get_position(session_id)
        
        request = {
            "id": f"handoff_{uuid.uuid4().hex[:8]}",
            "session_id": session_id,
            "status": HandoffStatus.PENDING,
            "created_at": time.time(),
        }
        self._queue.append(request)
        self._requests[session_id] = request
        
        return len(self._queue)
    
    def get_status(self, session_id: str) -> tuple[HandoffStatus, int | None]:
        """Get handoff status and queue position."""
        if session_id not in self._requests:
            return None, None
        
        request = self._requests[session_id]
        position = self._get_position(session_id) if request["status"] == HandoffStatus.PENDING else None
        return request["status"], position
    
    def _get_position(self, session_id: str) -> int:
        """Get queue position (1-indexed)."""
        for i, req in enumerate(self._queue):
            if req["session_id"] == session_id:
                return i + 1
        return 0


# Global queue
_handoff_queue = HandoffQueue()


# =============================================================================
# Routes
# =============================================================================

@router.post("", response_model=HandoffResponse)
async def create_handoff(request: Request, body: HandoffRequest) -> HandoffResponse:
    """Create a handoff request.
    
    SPEC-008: POST /api/handoff
    - Input: sessionId
    - Output: queuePosition
    
    Adds the session to the human agent queue.
    
    TBD-L0-011: Queue strategy, timeout, fallback to AI
    """
    settings = get_settings()
    client_ip = request.client.host if request.client else "unknown"
    
    # Rate limiting
    if not rate_limiter.is_allowed(f"handoff:{client_ip}", settings.rate_limit_chat, 60):
        raise RateLimitError("Rate limit exceeded.")
    
    logger.info("handoff_created", session_id=body.session_id)
    
    # TODO: Implement actual queue persistence (SPEC-008)
    position = _handoff_queue.create(body.session_id)
    
    return HandoffResponse(queue_position=position)


@router.get("/queue", response_model=QueueStatusResponse)
async def get_queue_status(session_id: str) -> QueueStatusResponse:
    """Get handoff queue status.
    
    SPEC-008: GET /api/handoff/queue
    - Input: sessionId (query param)
    - Output: status, queuePosition?
    
    Used by frontend for polling queue updates.
    """
    logger.info("handoff_queue_check", session_id=session_id)
    
    status, position = _handoff_queue.get_status(session_id)
    
    if status is None:
        raise NotFoundError(f"Handoff request not found for session {session_id}")
    
    return QueueStatusResponse(status=status, queue_position=position)
