"""
Session and Message models for the RAG Chatbot database.

SPEC Reference: 
- SPEC-002 (Chat RAG Endpoint)
- REQ-L2-API-003 (Session persistence)
"""

from datetime import datetime
from enum import Enum
from typing import Any

from sqlalchemy import JSON, DateTime, Enum as SQLEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.api.db.session import Base


class MessageRole(str, Enum):
    """Message role in conversation."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Session(Base):
    """Chat session entity.
    
    SPEC-002: Session management for multi-turn conversations
    REQ-L2-API-003: 会话和 token 用量持久化
    """
    
    __tablename__ = "sessions"
    
    # Primary key
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    
    # User (optional, for authenticated users)
    user_email: Mapped[str | None] = mapped_column(String(256), nullable=True, index=True)
    
    # Context (from widget)
    context_product_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    context_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    
    # Language preference
    language: Mapped[str] = mapped_column(String(8), default="zh", nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    last_message_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    
    # Relationships
    messages: Mapped[list["Message"]] = relationship(
        "Message", back_populates="session", cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"<Session {self.id}>"


class Message(Base):
    """Chat message entity.
    
    SPEC-002: Message persistence with references and token usage
    """
    
    __tablename__ = "messages"
    
    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Foreign key
    session_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False, index=True
    )
    
    # Message content
    role: Mapped[MessageRole] = mapped_column(SQLEnum(MessageRole), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    # References (JSON for flexibility)
    references: Mapped[list[dict[str, Any]] | None] = mapped_column(JSON, nullable=True)
    
    # Token usage tracking
    tokens_prompt: Mapped[int | None] = mapped_column(Integer, nullable=True)
    tokens_completion: Mapped[int | None] = mapped_column(Integer, nullable=True)
    model: Mapped[str | None] = mapped_column(String(64), nullable=True)
    
    # Error tracking
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    # Timestamp
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    
    # Relationships
    session: Mapped["Session"] = relationship("Session", back_populates="messages")
    
    def __repr__(self) -> str:
        return f"<Message {self.id}: {self.role.value} in {self.session_id}>"
