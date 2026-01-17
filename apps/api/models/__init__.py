"""
Database models for the RAG Chatbot API.

Import all models here to ensure they are registered with SQLAlchemy.
"""

from apps.api.models.product import Product
from apps.api.models.document import Document, DocumentChunk
from apps.api.models.session import Session, Message, MessageRole
from apps.api.models.handoff import Handoff, HandoffStatus
from apps.api.models.user import User

__all__ = [
    "Product",
    "Document",
    "DocumentChunk",
    "Session",
    "Message",
    "MessageRole",
    "Handoff",
    "HandoffStatus",
    "User",
]
