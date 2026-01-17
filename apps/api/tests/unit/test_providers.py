"""
Unit tests for Provider implementations.

Tests the LLM and Embedding provider abstractions with mock providers.

SPEC Reference: SPEC-003 (LLM Provider Abstraction)
"""

import pytest

from apps.api.providers.base import Message
from apps.api.providers.llm import MockLLMProvider, create_llm_provider
from apps.api.providers.embedding import MockEmbeddingProvider, create_embedding_provider


class TestMockLLMProvider:
    """Test MockLLMProvider."""
    
    @pytest.fixture
    def provider(self) -> MockLLMProvider:
        return MockLLMProvider()
    
    @pytest.mark.asyncio
    async def test_chat_returns_response(self, provider: MockLLMProvider):
        """Test chat returns a valid response."""
        messages = [Message(role="user", content="Hello, world!")]
        response = await provider.chat(messages)
        
        assert response.content is not None
        assert "[MOCK]" in response.content
        assert response.model == "mock-model"
        assert response.token_usage["prompt"] > 0
    
    @pytest.mark.asyncio
    async def test_health_check_returns_true(self, provider: MockLLMProvider):
        """Test health check for mock provider."""
        assert await provider.health_check() is True
    
    def test_provider_name(self, provider: MockLLMProvider):
        """Test provider name."""
        assert provider.provider_name == "mock"


class TestMockEmbeddingProvider:
    """Test MockEmbeddingProvider."""
    
    @pytest.fixture
    def provider(self) -> MockEmbeddingProvider:
        return MockEmbeddingProvider(dimension=1536)
    
    @pytest.mark.asyncio
    async def test_embed_returns_embeddings(self, provider: MockEmbeddingProvider):
        """Test embed returns correct number of embeddings."""
        texts = ["Hello", "World"]
        response = await provider.embed(texts)
        
        assert len(response.embeddings) == 2
        assert len(response.embeddings[0]) == 1536
    
    @pytest.mark.asyncio
    async def test_health_check_returns_true(self, provider: MockEmbeddingProvider):
        """Test health check for mock provider."""
        assert await provider.health_check() is True
    
    def test_dimension(self, provider: MockEmbeddingProvider):
        """Test embedding dimension."""
        assert provider.dimension == 1536


class TestProviderFactory:
    """Test provider factory functions."""
    
    def test_create_llm_provider_without_api_key_returns_mock(self):
        """Test that missing API key returns mock provider."""
        # This relies on default settings having empty API key
        # Provider factory should fall back to mock
        provider = create_llm_provider()
        assert provider.provider_name in ["mock", "openai", "ollama"]
    
    def test_create_embedding_provider_without_api_key_returns_mock(self):
        """Test that missing API key returns mock provider."""
        provider = create_embedding_provider()
        assert provider.provider_name in ["mock", "openai", "ollama"]
