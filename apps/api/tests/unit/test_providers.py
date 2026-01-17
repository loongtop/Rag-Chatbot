"""
Unit tests for Provider implementations.

Tests the LLM and Embedding provider abstractions with mock providers.
断言策略：验证 schema/结构/字段，不验证模型生成的文本内容。

SPEC Reference: SPEC-003 (LLM Provider Abstraction)
"""

import pytest

from apps.api.providers.base import Message
from apps.api.providers.llm import MockLLMProvider, create_llm_provider
from apps.api.providers.embedding import MockEmbeddingProvider, create_embedding_provider


@pytest.mark.unit
class TestMockLLMProvider:
    """Test MockLLMProvider."""
    
    @pytest.fixture
    def provider(self) -> MockLLMProvider:
        return MockLLMProvider()
    
    @pytest.mark.asyncio
    async def test_chat_response_schema(self, provider: MockLLMProvider):
        """验证响应结构，不验证文本内容。"""
        messages = [Message(role="user", content="Hello, world!")]
        response = await provider.chat(messages)
        
        # 验证响应结构
        assert response.content is not None
        assert isinstance(response.content, str)
        assert response.model is not None
        assert "prompt" in response.token_usage
        assert "completion" in response.token_usage
        assert response.token_usage["prompt"] >= 0
    
    @pytest.mark.asyncio
    async def test_health_check_returns_true(self, provider: MockLLMProvider):
        """Test health check for mock provider."""
        assert await provider.health_check() is True
    
    def test_provider_name(self, provider: MockLLMProvider):
        """Test provider name."""
        assert provider.provider_name == "mock"


@pytest.mark.unit
class TestMockEmbeddingProvider:
    """Test MockEmbeddingProvider."""
    
    @pytest.fixture
    def provider(self) -> MockEmbeddingProvider:
        return MockEmbeddingProvider(dimension=1536)
    
    @pytest.mark.asyncio
    async def test_embed_response_schema(self, provider: MockEmbeddingProvider):
        """验证 embedding 结构：数量和维度。"""
        texts = ["Hello", "World"]
        response = await provider.embed(texts)
        
        # 验证结构
        assert len(response.embeddings) == 2  # 与输入数量匹配
        assert len(response.embeddings[0]) == 1536  # 维度正确
        assert all(isinstance(v, float) for v in response.embeddings[0])  # 类型正确
    
    @pytest.mark.asyncio
    async def test_embed_empty_input(self, provider: MockEmbeddingProvider):
        """边界测试：空输入。"""
        response = await provider.embed([])
        assert len(response.embeddings) == 0
    
    @pytest.mark.asyncio
    async def test_health_check_returns_true(self, provider: MockEmbeddingProvider):
        """Test health check for mock provider."""
        assert await provider.health_check() is True
    
    def test_dimension(self, provider: MockEmbeddingProvider):
        """Test embedding dimension."""
        assert provider.dimension == 1536


@pytest.mark.unit
class TestProviderFactory:
    """Test provider factory functions with dependency injection."""
    
    def test_create_llm_provider_returns_valid_provider(self):
        """验证工厂函数返回有效的 provider。"""
        provider = create_llm_provider()
        assert hasattr(provider, "chat")
        assert hasattr(provider, "health_check")
        assert provider.provider_name in ["mock", "openai", "ollama"]
    
    def test_create_embedding_provider_returns_valid_provider(self):
        """验证工厂函数返回有效的 provider。"""
        provider = create_embedding_provider()
        assert hasattr(provider, "embed")
        assert hasattr(provider, "health_check")
        assert provider.provider_name in ["mock", "openai", "ollama"]


@pytest.mark.performance
class TestProviderPerformance:
    """性能测试 - 使用 @pytest.mark.performance 标记，默认排除。
    
    运行方式：pytest -m performance
    """
    
    @pytest.mark.asyncio
    async def test_embedding_throughput(self):
        """测试 embedding 吞吐量。"""
        provider = MockEmbeddingProvider(dimension=1536)
        texts = ["Test sentence"] * 100
        
        import time
        start = time.time()
        await provider.embed(texts)
        duration = time.time() - start
        
        # 100 条应在 1 秒内完成
        assert duration < 1.0, f"Embedding took {duration:.2f}s for 100 texts"
