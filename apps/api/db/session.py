"""
Database session management.

Provides async SQLAlchemy session for PostgreSQL + pgvector.

SPEC Reference:
- SPEC-006: Knowledge Base Index (pgvector)
- REQ-L0-DEP-005: PostgreSQL with pgvector extension

TODO: 
- Add connection pooling tuning for production
- Implement health check endpoint
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from apps.api.config.settings import get_settings
from apps.api.core.logging import get_logger

logger = get_logger(__name__)


class Base(DeclarativeBase):
    """SQLAlchemy declarative base for all models."""
    pass


# =============================================================================
# Engine and Session Factory
# =============================================================================

_engine = None
_session_factory = None


def get_engine():
    """Get or create async engine."""
    global _engine
    if _engine is None:
        settings = get_settings()
        # Convert postgresql:// to postgresql+asyncpg://
        db_url = settings.database_url
        if db_url.startswith("postgresql://"):
            db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
        
        _engine = create_async_engine(
            db_url,
            echo=settings.debug,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,
        )
        logger.info("database_engine_created", url=db_url.split("@")[-1])  # Log without credentials
    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    """Get or create session factory."""
    global _session_factory
    if _session_factory is None:
        engine = get_engine()
        _session_factory = async_sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _session_factory


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session with automatic cleanup.
    
    Usage:
        async with get_db_session() as session:
            result = await session.execute(query)
    """
    factory = get_session_factory()
    session = factory()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for FastAPI route injection.
    
    Usage:
        @app.get("/items")
        async def get_items(session: AsyncSession = Depends(get_session)):
            ...
    """
    async with get_db_session() as session:
        yield session


# =============================================================================
# Lifecycle
# =============================================================================

async def init_db() -> None:
    """Initialize database (create tables).
    
    Should be called on application startup.
    """
    engine = get_engine()
    async with engine.begin() as conn:
        # Import all models to ensure they're registered
        # from apps.api.models import *  # noqa
        await conn.run_sync(Base.metadata.create_all)
    logger.info("database_initialized")


async def close_db() -> None:
    """Close database connections.
    
    Should be called on application shutdown.
    """
    global _engine
    if _engine is not None:
        await _engine.dispose()
        _engine = None
        logger.info("database_closed")
