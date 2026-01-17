"""
Embedding Provider implementations and factory.

Provides concrete implementations for OpenAI and Ollama embedding providers.

SPEC Reference: SPEC-003 (Embedding Provider Abstraction)
"""

from typing import Any

import httpx

from apps.api.config.settings import Settings, get_settings
from apps.api.core.errors import ErrorCode, ProviderError
from apps.api.core.logging import get_logger
from apps.api.providers.base import BaseEmbeddingProvider, EmbeddingResponse

logger = get_logger(__name__)


class OpenAIEmbeddingProvider(BaseEmbeddingProvider):
    """OpenAI Embedding provider.
    
    SPEC-003: Embedding Provider for vector search
    """
    
    def __init__(
        self,
        api_key: str,
        api_base: str = "https://api.openai.com/v1",
        model: str = "text-embedding-3-small",
        dimension: int = 1536,
        timeout: float = 30.0,
    ) -> None:
        self._api_key = api_key
        self._api_base = api_base.rstrip("/")
        self._default_model = model
        self._dimension = dimension
        self._client = httpx.AsyncClient(
            base_url=self._api_base,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )
    
    @property
    def provider_name(self) -> str:
        return "openai"
    
    @property
    def dimension(self) -> int:
        return self._dimension
    
    async def embed(
        self,
        texts: list[str],
        *,
        model: str | None = None,
        **kwargs: Any,
    ) -> EmbeddingResponse:
        """Generate embeddings via OpenAI API."""
        model = model or self._default_model
        
        try:
            response = await self._client.post(
                "/embeddings",
                json={"model": model, "input": texts},
            )
            response.raise_for_status()
            data = response.json()
            
            embeddings = [item["embedding"] for item in data["data"]]
            usage = data.get("usage", {})
            
            return EmbeddingResponse(
                embeddings=embeddings,
                model=data["model"],
                token_usage={"prompt": usage.get("prompt_tokens", 0), "completion": 0},
            )
        except httpx.TimeoutException as e:
            logger.error("embedding_timeout", model=model)
            raise ProviderError("Embedding request timed out", ErrorCode.EMBEDDING_ERROR) from e
        except httpx.HTTPStatusError as e:
            logger.error("embedding_error", model=model, status=e.response.status_code)
            raise ProviderError(f"Embedding request failed: {e.response.text}", ErrorCode.EMBEDDING_ERROR) from e
        except Exception as e:
            logger.exception("embedding_unexpected_error", model=model)
            raise ProviderError(f"Unexpected error: {e}", ErrorCode.EMBEDDING_ERROR) from e
    
    async def health_check(self) -> bool:
        """Check if embedding service is accessible."""
        try:
            response = await self._client.get("/models")
            return response.status_code == 200
        except Exception:
            return False


class OllamaEmbeddingProvider(BaseEmbeddingProvider):
    """Ollama Embedding provider.
    
    SPEC-003: Local embedding via Ollama
    """
    
    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "nomic-embed-text",
        dimension: int = 768,
        timeout: float = 30.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._default_model = model
        self._dimension = dimension
        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            timeout=timeout,
        )
    
    @property
    def provider_name(self) -> str:
        return "ollama"
    
    @property
    def dimension(self) -> int:
        return self._dimension
    
    async def embed(
        self,
        texts: list[str],
        *,
        model: str | None = None,
        **kwargs: Any,
    ) -> EmbeddingResponse:
        """Generate embeddings via Ollama API."""
        model = model or self._default_model
        embeddings = []
        
        try:
            # Ollama embeds one text at a time
            for text in texts:
                response = await self._client.post(
                    "/api/embeddings",
                    json={"model": model, "prompt": text},
                )
                response.raise_for_status()
                data = response.json()
                embeddings.append(data["embedding"])
            
            return EmbeddingResponse(
                embeddings=embeddings,
                model=model,
                token_usage={"prompt": 0, "completion": 0},  # Ollama doesn't report tokens
            )
        except httpx.TimeoutException as e:
            logger.error("ollama_embedding_timeout", model=model)
            raise ProviderError("Embedding request timed out", ErrorCode.EMBEDDING_ERROR) from e
        except Exception as e:
            logger.exception("ollama_embedding_error", model=model)
            raise ProviderError(f"Embedding failed: {e}", ErrorCode.EMBEDDING_ERROR) from e
    
    async def health_check(self) -> bool:
        """Check if Ollama is running."""
        try:
            response = await self._client.get("/api/tags")
            return response.status_code == 200
        except Exception:
            return False


class MockEmbeddingProvider(BaseEmbeddingProvider):
    """Mock Embedding provider for testing."""
    
    def __init__(self, dimension: int = 1536) -> None:
        self._dimension = dimension
    
    @property
    def provider_name(self) -> str:
        return "mock"
    
    @property
    def dimension(self) -> int:
        return self._dimension
    
    async def embed(
        self,
        texts: list[str],
        *,
        model: str | None = None,
        **kwargs: Any,
    ) -> EmbeddingResponse:
        """Return mock embeddings (zeros)."""
        embeddings = [[0.0] * self._dimension for _ in texts]
        return EmbeddingResponse(
            embeddings=embeddings,
            model="mock-embedding",
            token_usage={"prompt": len(texts), "completion": 0},
        )
    
    async def health_check(self) -> bool:
        return True


# =============================================================================
# Factory
# =============================================================================

def create_embedding_provider(settings: Settings | None = None) -> BaseEmbeddingProvider:
    """Factory function to create Embedding provider based on configuration."""
    if settings is None:
        settings = get_settings()
    
    if settings.embedding_provider == "openai":
        if not settings.openai_api_key:
            logger.warning("openai_api_key_missing_for_embedding", fallback="mock mode")
            return MockEmbeddingProvider(settings.embedding_dimension)
        return OpenAIEmbeddingProvider(
            api_key=settings.openai_api_key,
            api_base=settings.openai_api_base,
            model=settings.embedding_model,
            dimension=settings.embedding_dimension,
        )
    elif settings.embedding_provider == "ollama":
        return OllamaEmbeddingProvider(
            base_url=settings.ollama_base_url,
            model=settings.embedding_model,
            dimension=settings.embedding_dimension,
        )
    else:
        raise ValueError(f"Unknown embedding provider: {settings.embedding_provider}")
