"""
Document and Chunk models for the RAG Chatbot database.

SPEC Reference: SPEC-006 (Knowledge Base Index)
"""

from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.api.db.session import Base


class Document(Base):
    """Document entity for the knowledge base.
    
    SPEC-006: Knowledge Base Index
    REQ-L2-ADM-003: 知识库文档管理
    """
    
    __tablename__ = "documents"
    
    # Primary key
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    
    # Basic info
    title: Mapped[str] = mapped_column(String(512), nullable=False, index=True)
    source_type: Mapped[str] = mapped_column(
        String(32), nullable=False, index=True
    )  # manual, crawl, upload
    
    # Content (raw)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    
    # Status
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Processing status
    indexed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    chunk_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    
    # Relationships
    chunks: Mapped[list["DocumentChunk"]] = relationship(
        "DocumentChunk", back_populates="document", cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"<Document {self.id}: {self.title}>"


class DocumentChunk(Base):
    """Document chunk with embedding for vector search.
    
    SPEC-006: Knowledge Base Index
    
    TODO: Add pgvector column for embeddings
    """
    
    __tablename__ = "document_chunks"
    
    # Primary key
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    
    # Foreign key
    document_id: Mapped[str] = mapped_column(
        String(64), ForeignKey("documents.id", ondelete="CASCADE"), nullable=False, index=True
    )
    
    # Chunk info
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Metadata
    title: Mapped[str | None] = mapped_column(String(512), nullable=True)
    
    # TODO: Add pgvector embedding column
    # from pgvector.sqlalchemy import Vector
    # embedding: Mapped[list[float]] = mapped_column(Vector(1536), nullable=True)
    
    # Relationships
    document: Mapped["Document"] = relationship("Document", back_populates="chunks")
    
    def __repr__(self) -> str:
        return f"<DocumentChunk {self.id}: doc={self.document_id}, seq={self.sequence}>"
