"""
RAG Chatbot API Server Main Application.

FastAPI application entry point with lifecycle management.

SPEC Reference:
- ARCH-API-001: Base URL /api, JSON format, unified error response
- REQ-L0-PERF-003: Support >= 100 concurrent sessions

Usage:
    uvicorn apps.api.main:app --reload
"""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.config.settings import get_settings
from apps.api.core.logging import get_logger, setup_logging
from apps.api.core.middleware import setup_exception_handlers, setup_middleware
from apps.api.db.session import close_db, init_db

# Setup logging first
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifecycle management.
    
    Handles:
    - Database initialization on startup
    - Resource cleanup on shutdown
    """
    settings = get_settings()
    logger.info(
        "application_starting",
        app_name=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )
    
    # Startup
    try:
        await init_db()
        logger.info("startup_complete")
    except Exception as e:
        logger.error("startup_failed", error=str(e))
        raise
    
    yield
    
    # Shutdown
    logger.info("application_shutting_down")
    await close_db()
    logger.info("shutdown_complete")


def create_app() -> FastAPI:
    """Application factory.
    
    Creates and configures the FastAPI application.
    """
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="RAG Chatbot API - 产品知识库问答、推荐、比较",
        docs_url="/api/docs" if settings.debug else None,
        redoc_url="/api/redoc" if settings.debug else None,
        openapi_url="/api/openapi.json" if settings.debug else None,
        lifespan=lifespan,
    )
    
    # CORS configuration
    # TODO: Configure allowed origins based on environment
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"] if settings.debug else ["https://example.com"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Setup middleware and exception handlers
    setup_middleware(app)
    setup_exception_handlers(app)
    
    # Register API routers
    from apps.api.api.chat import router as chat_router
    from apps.api.api.auth import router as auth_router
    from apps.api.api.handoff import router as handoff_router
    from apps.api.api.voice import router as voice_router
    from apps.api.api.upload import router as upload_router
    from apps.api.api.admin import router as admin_router
    
    app.include_router(chat_router, prefix="/api")
    app.include_router(auth_router, prefix="/api")
    app.include_router(handoff_router, prefix="/api")
    app.include_router(voice_router, prefix="/api")
    app.include_router(upload_router, prefix="/api")
    app.include_router(admin_router, prefix="/api")
    
    # Health check endpoint
    @app.get("/health", tags=["health"])
    async def health_check():
        """Health check endpoint for load balancers."""
        return {"status": "healthy", "version": settings.app_version}
    
    @app.get("/api/health", tags=["health"])
    async def api_health_check():
        """API health check with provider status.
        
        TODO: Add provider health checks (SPEC-003)
        """
        return {
            "status": "healthy",
            "version": settings.app_version,
            "providers": {
                "llm": settings.llm_provider,
                "embedding": settings.embedding_provider,
                "stt": settings.stt_provider,
                "tts": settings.tts_provider,
            },
        }
    
    return app


# Create application instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    settings = get_settings()
    uvicorn.run(
        "apps.api.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
