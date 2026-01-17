"""
User model for the RAG Chatbot database.

SPEC Reference: SPEC-007 (Email Verification Login)
"""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from apps.api.db.session import Base


class User(Base):
    """Widget user entity (email-verified).
    
    SPEC-007: Email Verification Login
    REQ-L2-WGT-003: 邮箱验证登录
    """
    
    __tablename__ = "users"
    
    # Primary key (email is the identifier)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Email (unique, indexed)
    email: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)
    
    # Status
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    
    def __repr__(self) -> str:
        return f"<User {self.email}>"
