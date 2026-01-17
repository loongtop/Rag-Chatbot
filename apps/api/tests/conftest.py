"""
Test configuration and fixtures.

提供测试所需的公共 fixtures，包括：
- 禁用 lifespan（不连接数据库）的测试客户端
- Mock Providers 注入
- 测试环境配置
"""

import os
from collections.abc import AsyncIterator
from unittest.mock import AsyncMock, patch

import pytest
from httpx import ASGITransport, AsyncClient

# 设置测试环境变量（在导入 app 之前）
os.environ["ENVIRONMENT"] = "test"
os.environ["DEBUG"] = "false"
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def test_client() -> AsyncIterator[AsyncClient]:
    """提供禁用 lifespan 的测试客户端。
    
    不会触发 init_db()，适合快速单元测试。
    """
    from apps.api.main import create_app
    
    # 创建不带 lifespan 的 app
    with patch("apps.api.main.lifespan", None):
        app = create_app()
        # 手动禁用 lifespan
        app.router.lifespan_context = None
        
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test"
        ) as client:
            yield client


@pytest.fixture
def mock_llm_provider():
    """Mock LLM Provider，返回确定性响应。"""
    from apps.api.providers.base import Message
    from apps.api.providers.llm import MockLLMProvider
    
    provider = MockLLMProvider()
    return provider


@pytest.fixture
def mock_embedding_provider():
    """Mock Embedding Provider，返回确定性向量。"""
    from apps.api.providers.embedding import MockEmbeddingProvider
    
    return MockEmbeddingProvider(dimension=1536)


@pytest.fixture
def mock_chat_service(mock_llm_provider, mock_embedding_provider):
    """提供注入了 Mock Providers 的 ChatService。"""
    from apps.api.services.chat import ChatService
    
    return ChatService(
        llm_provider=mock_llm_provider,
        embedding_provider=mock_embedding_provider,
    )


# =============================================================================
# 数据库 Fixtures（用于集成测试）
# =============================================================================

@pytest.fixture
async def db_session():
    """提供内存数据库会话（用于集成测试）。
    
    需要标记 @pytest.mark.integration
    """
    from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
    from apps.api.db.session import Base
    
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with session_factory() as session:
        yield session
    
    await engine.dispose()
