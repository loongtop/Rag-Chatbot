"""
Chat API routes.

Provides the main chat, recommend, and compare endpoints.

SPEC Reference: 
- SPEC-002 (Chat RAG Endpoint)
- SPEC-005 (Product Recommendation & Comparison)
IFC Reference: IFC-CHAT-API
"""

from fastapi import APIRouter, Depends, Request

from apps.api.api.schemas import (
    ChatRequest,
    ChatResponse,
    RecommendRequest,
    RecommendResponse,
    CompareRequest,
    CompareResponse,
    ProductSummary,
    ComparisonTable,
    ComparisonRow,
)
from apps.api.core.errors import RateLimitError, ValidationError
from apps.api.core.logging import get_logger
from apps.api.core.middleware import rate_limiter
from apps.api.config.settings import get_settings
from apps.api.services.chat import get_chat_service

logger = get_logger(__name__)
router = APIRouter(tags=["chat"])


def get_client_ip(request: Request) -> str:
    """Extract client IP for rate limiting."""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


@router.post("/chat", response_model=ChatResponse)
async def chat(request: Request, body: ChatRequest) -> ChatResponse:
    """RAG Chat endpoint.
    
    SPEC-002: POST /api/chat
    - Input: message, session_id?, language?, context?
    - Output: answer, references[], sessionId, tokenUsage
    
    Features:
    - Context-aware retrieval (productId/skuId/url)
    - Multi-turn conversation via session_id
    - Grounded answers with source references
    - Token usage tracking
    """
    settings = get_settings()
    client_ip = get_client_ip(request)
    
    # Rate limiting (REQ-L0-SEC-003)
    if not rate_limiter.is_allowed(f"chat:{client_ip}", settings.rate_limit_chat, 60):
        retry_after = rate_limiter.get_retry_after(f"chat:{client_ip}", 60)
        raise RateLimitError(f"Rate limit exceeded. Retry after {retry_after}s.")
    
    service = get_chat_service()
    return await service.chat(body)


@router.post("/recommend", response_model=RecommendResponse)
async def recommend(request: Request, body: RecommendRequest) -> RecommendResponse:
    """Product recommendation endpoint.
    
    SPEC-005: POST /api/recommend
    - Input: query, topN?, language?
    - Output: products[], reasons[]
    
    TODO: Implement actual recommendation logic (SPEC-005)
    Currently returns mock data.
    """
    settings = get_settings()
    client_ip = get_client_ip(request)
    
    # Rate limiting
    if not rate_limiter.is_allowed(f"recommend:{client_ip}", settings.rate_limit_chat, 60):
        raise RateLimitError("Rate limit exceeded.")
    
    logger.info("recommend_request", query=body.query, top_n=body.top_n)
    
    # TODO: Implement recommendation service (SPEC-005)
    # 1. Embed query
    # 2. Search products by embedding similarity
    # 3. Use LLM to generate reasons
    
    # Mock response
    logger.warning("recommend_mock", message="Using mock data - implement SPEC-005")
    return RecommendResponse(
        products=[
            ProductSummary(
                id="SKU-001",
                name="[Mock] 激光切割机 A 型",
                category="laser-cutter",
                short_description="高性价比机型，适合中小型企业",
                price="¥150,000",
                url="https://example.com/products/SKU-001",
            ),
            ProductSummary(
                id="SKU-002",
                name="[Mock] 激光切割机 B 型",
                category="laser-cutter",
                short_description="大功率机型，适合重工业",
                price="¥280,000",
                url="https://example.com/products/SKU-002",
            ),
        ][:body.top_n],
        reasons=[
            f"[Mock] 根据您的需求'{body.query}'，推荐以上产品。",
            "[Mock] 这些产品满足您的核心需求。",
        ],
    )


@router.post("/compare", response_model=CompareResponse)
async def compare(request: Request, body: CompareRequest) -> CompareResponse:
    """Product comparison endpoint.
    
    SPEC-005: POST /api/compare
    - Input: productIds (2-4), language?
    - Output: comparison table
    
    TODO: Implement actual comparison logic (SPEC-005)
    Currently returns mock data.
    """
    settings = get_settings()
    client_ip = get_client_ip(request)
    
    # Rate limiting
    if not rate_limiter.is_allowed(f"compare:{client_ip}", settings.rate_limit_chat, 60):
        raise RateLimitError("Rate limit exceeded.")
    
    # Validation
    if len(body.product_ids) < 2 or len(body.product_ids) > 4:
        raise ValidationError("productIds must contain 2-4 product IDs")
    
    logger.info("compare_request", product_ids=body.product_ids)
    
    # TODO: Implement comparison service (SPEC-005)
    # 1. Fetch products from database
    # 2. Compare specs
    # 3. Use LLM to generate structured comparison
    
    # Mock response
    logger.warning("compare_mock", message="Using mock data - implement SPEC-005")
    return CompareResponse(
        comparison=ComparisonTable(
            columns=body.product_ids,
            rows=[
                ComparisonRow(field="功率", values=["3000W", "6000W", "4500W", "3000W"][:len(body.product_ids)]),
                ComparisonRow(field="最大切割厚度", values=["20mm", "30mm", "25mm", "20mm"][:len(body.product_ids)]),
                ComparisonRow(field="工作台尺寸", values=["1.5m x 3m", "2m x 4m", "1.5m x 3m", "1m x 2m"][:len(body.product_ids)]),
                ComparisonRow(field="价格", values=["¥150,000", "¥280,000", "¥200,000", "¥120,000"][:len(body.product_ids)]),
            ],
        )
    )
