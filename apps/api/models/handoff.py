"""
Handoff model for the RAG Chatbot database.

SPEC Reference: SPEC-008 (Handoff Create & Queue Endpoint)
"""

from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from apps.api.db.session import Base


class HandoffStatus(str, Enum):
    """Handoff request status."""
    PENDING = "pending"
    ACTIVE = "active"
    RESOLVED = "resolved"
    CANCELLED = "cancelled"
    TIMEOUT = "timeout"


class Handoff(Base):
    """Human agent handoff request.
    
    SPEC-008: Handoff Create & Queue Endpoint
    SPEC-022: Handoff Console UI
    """
    
    __tablename__ = "handoffs"
    
    # Primary key
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    
    # Session reference
    session_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False, index=True
    )
    
    # Status
    status: Mapped[HandoffStatus] = mapped_column(
        SQLEnum(HandoffStatus), default=HandoffStatus.PENDING, nullable=False, index=True
    )
    
    # Queue position (calculated, may be null when not pending)
    queue_position: Mapped[int | None] = mapped_column(Integer, nullable=True)
    
    # Agent assignment
    assigned_agent: Mapped[str | None] = mapped_column(String(256), nullable=True)
    
    # Notes
    resolution_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    assigned_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    
    def __repr__(self) -> str:
        return f"<Handoff {self.id}: {self.status.value}>"
