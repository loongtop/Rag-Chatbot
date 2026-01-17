"""
Admin API routes.

Provides admin endpoints for product/document management and dashboard.

SPEC Reference:
- SPEC-004 (Product Data Admin)
- SPEC-006 (Knowledge Base Index)
- SPEC-019 (Admin Dashboard Shell)
- SPEC-020 (Product CRUD UI)
- SPEC-021 (Document CRUD & Upload UI)

IFC Reference: IFC-ADMIN-API
TBD Reference: TBD-L0-003 (Admin authentication)
"""

import secrets
from functools import wraps
from typing import Any, Callable

from fastapi import APIRouter, Depends, Header, HTTPException, Request, UploadFile, File
from pydantic import BaseModel, Field

from apps.api.core.errors import ForbiddenError, NotFoundError, UnauthorizedError
from apps.api.core.logging import audit_logger, get_logger
from apps.api.config.settings import get_settings

logger = get_logger(__name__)
router = APIRouter(prefix="/admin", tags=["admin"])


# =============================================================================
# Admin Authentication
# TBD-L0-003: Basic Auth for v0.1
# TODO: Implement proper SSO/JWT for production
# =============================================================================

async def verify_admin(authorization: str = Header(..., alias="Authorization")) -> str:
    """Verify admin credentials via Basic Auth.
    
    TBD-L0-003: Using Basic Auth for v0.1.
    TODO: Implement proper admin authentication (SSO, JWT, etc.)
    """
    settings = get_settings()
    
    if not authorization.startswith("Basic "):
        raise UnauthorizedError("Invalid authorization header")
    
    import base64
    try:
        credentials = base64.b64decode(authorization[6:]).decode("utf-8")
        username, password = credentials.split(":", 1)
    except Exception:
        raise UnauthorizedError("Invalid authorization header")
    
    if username != settings.admin_username or password != settings.admin_password:
        raise ForbiddenError("Invalid admin credentials")
    
    return username


# =============================================================================
# Product Models
# SPEC-004: Product Data Admin CRUD
# =============================================================================

class ProductCreate(BaseModel):
    """Product creation request."""
    id: str
    name: str
    category: str
    description: str | None = None
    specs: dict[str, Any] | None = None
    price: str | None = None
    active: bool = True


class ProductUpdate(BaseModel):
    """Product update request."""
    name: str | None = None
    category: str | None = None
    description: str | None = None
    specs: dict[str, Any] | None = None
    price: str | None = None
    active: bool | None = None


class ProductResponse(BaseModel):
    """Product response."""
    id: str
    name: str
    category: str
    description: str | None = None
    specs: dict[str, Any] | None = None
    price: str | None = None
    active: bool


class ProductListResponse(BaseModel):
    """Paginated product list response."""
    items: list[ProductResponse]
    total: int
    page: int
    page_size: int = Field(..., alias="pageSize")
    
    model_config = {"populate_by_name": True}


# =============================================================================
# Document Models
# SPEC-006: Knowledge Base Index
# =============================================================================

class DocumentCreate(BaseModel):
    """Document creation request."""
    title: str
    source_type: str = Field(..., alias="sourceType")  # manual, crawl, upload
    content: str | None = None
    url: str | None = None
    
    model_config = {"populate_by_name": True}


class DocumentUpdate(BaseModel):
    """Document update request."""
    title: str | None = None
    content: str | None = None
    active: bool | None = None


class DocumentResponse(BaseModel):
    """Document response."""
    id: str
    title: str
    source_type: str = Field(..., alias="sourceType")
    chunk_count: int = Field(0, alias="chunkCount")
    active: bool = True
    created_at: str = Field(..., alias="createdAt")
    
    model_config = {"populate_by_name": True}


class DocumentListResponse(BaseModel):
    """Paginated document list response."""
    items: list[DocumentResponse]
    total: int
    page: int
    page_size: int = Field(..., alias="pageSize")
    
    model_config = {"populate_by_name": True}


# =============================================================================
# In-Memory Storage (replace with database in production)
# TODO: Implement database persistence (SPEC-004, SPEC-006)
# =============================================================================

_products: dict[str, ProductResponse] = {}
_documents: dict[str, DocumentResponse] = {}


# =============================================================================
# Product Routes
# SPEC-004: Product Data Admin CRUD
# =============================================================================

@router.get("/products", response_model=ProductListResponse)
async def list_products(
    page: int = 1,
    page_size: int = 20,
    category: str | None = None,
    admin: str = Depends(verify_admin),
) -> ProductListResponse:
    """List all products with pagination.
    
    SPEC-004: GET /api/admin/products
    """
    items = list(_products.values())
    
    if category:
        items = [p for p in items if p.category == category]
    
    total = len(items)
    start = (page - 1) * page_size
    end = start + page_size
    
    logger.info("admin_list_products", admin=admin, total=total)
    
    return ProductListResponse(
        items=items[start:end],
        total=total,
        page=page,
        page_size=page_size,
    )


@router.post("/products", response_model=ProductResponse)
async def create_product(
    body: ProductCreate,
    admin: str = Depends(verify_admin),
) -> ProductResponse:
    """Create a new product.
    
    SPEC-004: POST /api/admin/products
    """
    if body.id in _products:
        raise HTTPException(status_code=409, detail="Product ID already exists")
    
    product = ProductResponse(
        id=body.id,
        name=body.name,
        category=body.category,
        description=body.description,
        specs=body.specs,
        price=body.price,
        active=body.active,
    )
    _products[body.id] = product
    
    audit_logger.log_admin_action(
        action="create",
        resource="product",
        resource_id=body.id,
        admin_user=admin,
    )
    
    return product


@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: str,
    admin: str = Depends(verify_admin),
) -> ProductResponse:
    """Get a product by ID.
    
    SPEC-004: GET /api/admin/products/{id}
    """
    if product_id not in _products:
        raise NotFoundError(f"Product not found: {product_id}")
    
    return _products[product_id]


@router.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: str,
    body: ProductUpdate,
    admin: str = Depends(verify_admin),
) -> ProductResponse:
    """Update a product.
    
    SPEC-004: PUT /api/admin/products/{id}
    """
    if product_id not in _products:
        raise NotFoundError(f"Product not found: {product_id}")
    
    product = _products[product_id]
    update_data = body.model_dump(exclude_unset=True)
    
    updated = ProductResponse(**{**product.model_dump(), **update_data})
    _products[product_id] = updated
    
    audit_logger.log_admin_action(
        action="update",
        resource="product",
        resource_id=product_id,
        details=update_data,
        admin_user=admin,
    )
    
    return updated


@router.delete("/products/{product_id}")
async def delete_product(
    product_id: str,
    admin: str = Depends(verify_admin),
) -> dict:
    """Delete a product.
    
    SPEC-004: DELETE /api/admin/products/{id}
    """
    if product_id not in _products:
        raise NotFoundError(f"Product not found: {product_id}")
    
    del _products[product_id]
    
    audit_logger.log_admin_action(
        action="delete",
        resource="product",
        resource_id=product_id,
        admin_user=admin,
    )
    
    return {"message": "Product deleted"}


# =============================================================================
# Document Routes
# SPEC-006: Knowledge Base Index
# SPEC-021: Document CRUD & Upload UI
# =============================================================================

@router.get("/documents", response_model=DocumentListResponse)
async def list_documents(
    page: int = 1,
    page_size: int = 20,
    source_type: str | None = None,
    admin: str = Depends(verify_admin),
) -> DocumentListResponse:
    """List all documents with pagination.
    
    SPEC-006: GET /api/admin/documents
    """
    items = list(_documents.values())
    
    if source_type:
        items = [d for d in items if d.source_type == source_type]
    
    total = len(items)
    start = (page - 1) * page_size
    end = start + page_size
    
    return DocumentListResponse(
        items=items[start:end],
        total=total,
        page=page,
        page_size=page_size,
    )


@router.post("/documents", response_model=DocumentResponse)
async def create_document(
    body: DocumentCreate,
    admin: str = Depends(verify_admin),
) -> DocumentResponse:
    """Create a new document.
    
    SPEC-006: POST /api/admin/documents
    
    TODO: Implement chunking and embedding (SPEC-006)
    """
    import uuid
    from datetime import datetime
    
    doc_id = f"doc_{uuid.uuid4().hex[:12]}"
    
    # TODO: Chunk document and generate embeddings
    # chunks = chunk_document(body.content)
    # embeddings = await embedding_provider.embed([c.text for c in chunks])
    # store_in_pgvector(chunks, embeddings)
    
    document = DocumentResponse(
        id=doc_id,
        title=body.title,
        source_type=body.source_type,
        chunk_count=0,  # TODO: Calculate actual chunks
        active=True,
        created_at=datetime.utcnow().isoformat(),
    )
    _documents[doc_id] = document
    
    audit_logger.log_admin_action(
        action="create",
        resource="document",
        resource_id=doc_id,
        admin_user=admin,
    )
    
    logger.warning(
        "document_created_without_indexing",
        doc_id=doc_id,
        note="TODO: Implement chunking and embedding (SPEC-006)",
    )
    
    return document


@router.post("/documents/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    admin: str = Depends(verify_admin),
) -> DocumentResponse:
    """Upload and process a document.
    
    SPEC-021: POST /api/admin/documents/upload
    
    TODO: Implement content extraction and indexing
    """
    import uuid
    from datetime import datetime
    
    content = await file.read()
    doc_id = f"doc_{uuid.uuid4().hex[:12]}"
    
    # TODO: Extract content, chunk, embed, store
    logger.warning(
        "document_upload_mock",
        filename=file.filename,
        size=len(content),
        note="TODO: Implement extraction and indexing (SPEC-021)",
    )
    
    document = DocumentResponse(
        id=doc_id,
        title=file.filename or "Untitled",
        source_type="upload",
        chunk_count=0,
        active=True,
        created_at=datetime.utcnow().isoformat(),
    )
    _documents[doc_id] = document
    
    audit_logger.log_admin_action(
        action="upload",
        resource="document",
        resource_id=doc_id,
        details={"filename": file.filename, "size": len(content)},
        admin_user=admin,
    )
    
    return document


@router.delete("/documents/{document_id}")
async def delete_document(
    document_id: str,
    admin: str = Depends(verify_admin),
) -> dict:
    """Delete a document.
    
    SPEC-006: DELETE /api/admin/documents/{id}
    
    TODO: Delete from pgvector as well
    """
    if document_id not in _documents:
        raise NotFoundError(f"Document not found: {document_id}")
    
    del _documents[document_id]
    
    # TODO: Delete embeddings from pgvector
    
    audit_logger.log_admin_action(
        action="delete",
        resource="document",
        resource_id=document_id,
        admin_user=admin,
    )
    
    return {"message": "Document deleted"}


# =============================================================================
# Dashboard Routes
# SPEC-019: Admin Dashboard Shell
# =============================================================================

@router.get("/dashboard/stats")
async def get_dashboard_stats(
    admin: str = Depends(verify_admin),
) -> dict:
    """Get dashboard statistics.
    
    SPEC-019: GET /api/admin/dashboard/stats
    
    TODO: Implement actual stats from database
    """
    logger.warning("dashboard_stats_mock", note="TODO: Implement actual stats")
    
    return {
        "products": {
            "total": len(_products),
            "active": len([p for p in _products.values() if p.active]),
        },
        "documents": {
            "total": len(_documents),
            "active": len([d for d in _documents.values() if d.active]),
            "chunks": sum(d.chunk_count for d in _documents.values()),
        },
        "sessions": {
            "today": 0,  # TODO: Implement
            "total": 0,
        },
        "handoffs": {
            "pending": 0,  # TODO: Get from handoff queue
            "today": 0,
        },
    }
