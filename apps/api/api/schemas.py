"""
Chat API models (request/response schemas).

Pydantic models for the Chat API endpoint.

SPEC Reference: SPEC-002 (Chat RAG Endpoint)
IFC Reference: IFC-CHAT-API
"""

from typing import Any
from pydantic import BaseModel, Field


class ChatContext(BaseModel):
    """Context from the host page for context-aware retrieval.
    
    IFC Reference: IFC-WIDGET-CTX
    """
    product_id: str | None = Field(None, alias="productId")
    sku_id: str | None = Field(None, alias="skuId")
    url: str | None = None
    
    model_config = {"populate_by_name": True}


class ChatRequest(BaseModel):
    """Request body for POST /api/chat.
    
    SPEC-002: message + session_id? + language? + context?
    """
    message: str = Field(..., min_length=1, max_length=4000)
    session_id: str | None = Field(None, alias="sessionId")
    language: str = Field("zh", pattern="^(zh|en)$")
    context: ChatContext | None = None
    
    model_config = {"populate_by_name": True}


class Reference(BaseModel):
    """Source reference for grounded answers.
    
    Per ARCH-API-001 and REQ-L2-API-001: answers must include traceable references.
    """
    type: str = Field(..., description="Reference type: document_chunk, product")
    title: str
    snippet: str
    source: dict[str, Any] = Field(
        ..., 
        description="Source identifiers: documentId, chunkId, productId, etc."
    )
    url: str | None = None


class TokenUsage(BaseModel):
    """Token usage for cost tracking.
    
    REQ-L2-API-003: Record token usage per message.
    """
    prompt: int
    completion: int
    model: str | None = None


class ChatResponse(BaseModel):
    """Response body for POST /api/chat.
    
    SPEC-002: answer + references[] + sessionId + tokenUsage
    """
    answer: str
    references: list[Reference] = []
    session_id: str = Field(..., alias="sessionId")
    token_usage: TokenUsage = Field(..., alias="tokenUsage")
    
    model_config = {"populate_by_name": True}


# =============================================================================
# Recommend API Models
# SPEC Reference: SPEC-005 (Product Recommendation & Comparison)
# =============================================================================

class RecommendRequest(BaseModel):
    """Request body for POST /api/recommend."""
    query: str = Field(..., min_length=1, max_length=2000)
    top_n: int = Field(3, ge=1, le=10, alias="topN")
    language: str = Field("zh", pattern="^(zh|en)$")
    
    model_config = {"populate_by_name": True}


class ProductSummary(BaseModel):
    """Product summary for recommendations."""
    id: str
    name: str
    category: str
    short_description: str | None = Field(None, alias="shortDescription")
    price: str | None = None
    url: str | None = None
    
    model_config = {"populate_by_name": True}


class RecommendResponse(BaseModel):
    """Response body for POST /api/recommend."""
    products: list[ProductSummary]
    reasons: list[str]


# =============================================================================
# Compare API Models
# SPEC Reference: SPEC-005 (Product Recommendation & Comparison)
# =============================================================================

class CompareRequest(BaseModel):
    """Request body for POST /api/compare."""
    product_ids: list[str] = Field(
        ..., 
        min_length=2, 
        max_length=4, 
        alias="productIds"
    )
    language: str = Field("zh", pattern="^(zh|en)$")
    
    model_config = {"populate_by_name": True}


class ComparisonRow(BaseModel):
    """Single row in comparison table."""
    field: str
    values: list[str]


class ComparisonTable(BaseModel):
    """Structured comparison output."""
    columns: list[str]  # Product IDs/names
    rows: list[ComparisonRow]


class CompareResponse(BaseModel):
    """Response body for POST /api/compare."""
    comparison: ComparisonTable
