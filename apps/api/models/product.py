"""
Product model for the RAG Chatbot database.

SPEC Reference: SPEC-004 (Product Data Admin)
"""

from datetime import datetime
from typing import Any

from sqlalchemy import JSON, Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from apps.api.db.session import Base


class Product(Base):
    """Product entity for the knowledge base.
    
    SPEC-004: Product Data Admin CRUD
    REQ-L2-ADM-002: 产品数据管理
    """
    
    __tablename__ = "products"
    
    # Primary key
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    
    # Basic info
    name: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    category: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    # Structured specs (JSON for flexibility)
    specs: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    
    # Pricing
    price: Mapped[str | None] = mapped_column(String(64), nullable=True)
    
    # Status
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    
    def __repr__(self) -> str:
        return f"<Product {self.id}: {self.name}>"
