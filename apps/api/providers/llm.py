"""
LLM Provider implementations and factory.

Provides concrete implementations for OpenAI-compatible and Ollama providers.
Includes a factory for easy provider instantiation based on configuration.

SPEC Reference: SPEC-003 (LLM Provider Abstraction & Factory)
"""

from typing import Any, AsyncIterator

import httpx

from apps.api.config.settings import Settings, get_settings
from apps.api.core.errors import ErrorCode, ProviderError
from apps.api.core.logging import get_logger
from apps.api.providers.base import BaseLLMProvider, ChatResponse, Message

logger = get_logger(__name__)


class OpenAIProvider(BaseLLMProvider):
    """OpenAI-compatible LLM provider.
    
    Works with OpenAI API and compatible services (Azure, DeepSeek, etc.).
    
    SPEC-003: 支持在线 OpenAI-Compatible API
    """
    
    def __init__(
        self,
        api_key: str,
        api_base: str = "https://api.openai.com/v1",
        model: str = "gpt-4",
        timeout: float = 60.0,
    ) -> None:
        self._api_key = api_key
        self._api_base = api_base.rstrip("/")
        self._default_model = model
        self._timeout = timeout
        self._client = httpx.AsyncClient(
            base_url=self._api_base,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )
    
    @property
    def provider_name(self) -> str:
        return "openai"
    
    async def chat(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> ChatResponse:
        """Generate chat completion via OpenAI API."""
        model = model or self._default_model
        
        payload: dict[str, Any] = {
            "model": model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": temperature,
        }
        if max_tokens:
            payload["max_tokens"] = max_tokens
        
        try:
            response = await self._client.post("/chat/completions", json=payload)
            response.raise_for_status()
            data = response.json()
            
            choice = data["choices"][0]
            usage = data.get("usage", {})
            
            return ChatResponse(
                content=choice["message"]["content"],
                model=data["model"],
                token_usage={
                    "prompt": usage.get("prompt_tokens", 0),
                    "completion": usage.get("completion_tokens", 0),
                },
                finish_reason=choice.get("finish_reason"),
            )
        except httpx.TimeoutException as e:
            logger.error("openai_timeout", model=model, error=str(e))
            raise ProviderError("LLM request timed out", ErrorCode.LLM_TIMEOUT) from e
        except httpx.HTTPStatusError as e:
            logger.error("openai_error", model=model, status=e.response.status_code)
            raise ProviderError(f"LLM request failed: {e.response.text}") from e
        except Exception as e:
            logger.exception("openai_unexpected_error", model=model)
            raise ProviderError(f"Unexpected error: {e}") from e
    
    async def chat_stream(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        """Generate streaming chat completion.
        
        TODO: Implement SSE streaming for real-time responses.
        """
        # Fallback to non-streaming for now
        response = await self.chat(messages, model=model, temperature=temperature, max_tokens=max_tokens)
        yield response.content
    
    async def health_check(self) -> bool:
        """Check if OpenAI API is accessible."""
        try:
            response = await self._client.get("/models")
            return response.status_code == 200
        except Exception:
            return False


class OllamaProvider(BaseLLMProvider):
    """Ollama local LLM provider.
    
    SPEC-003: 支持本地 Ollama
    """
    
    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "llama3.2",
        timeout: float = 120.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._default_model = model
        self._timeout = timeout
        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            timeout=timeout,
        )
    
    @property
    def provider_name(self) -> str:
        return "ollama"
    
    async def chat(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> ChatResponse:
        """Generate chat completion via Ollama API."""
        model = model or self._default_model
        
        payload: dict[str, Any] = {
            "model": model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": False,
            "options": {"temperature": temperature},
        }
        if max_tokens:
            payload["options"]["num_predict"] = max_tokens
        
        try:
            response = await self._client.post("/api/chat", json=payload)
            response.raise_for_status()
            data = response.json()
            
            return ChatResponse(
                content=data["message"]["content"],
                model=data["model"],
                token_usage={
                    "prompt": data.get("prompt_eval_count", 0),
                    "completion": data.get("eval_count", 0),
                },
                finish_reason="stop",
            )
        except httpx.TimeoutException as e:
            logger.error("ollama_timeout", model=model, error=str(e))
            raise ProviderError("LLM request timed out", ErrorCode.LLM_TIMEOUT) from e
        except httpx.HTTPStatusError as e:
            logger.error("ollama_error", model=model, status=e.response.status_code)
            raise ProviderError(f"LLM request failed: {e.response.text}") from e
        except Exception as e:
            logger.exception("ollama_unexpected_error", model=model)
            raise ProviderError(f"Unexpected error: {e}") from e
    
    async def chat_stream(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        """Generate streaming chat completion.
        
        TODO: Implement Ollama streaming.
        """
        response = await self.chat(messages, model=model, temperature=temperature, max_tokens=max_tokens)
        yield response.content
    
    async def health_check(self) -> bool:
        """Check if Ollama is running."""
        try:
            response = await self._client.get("/api/tags")
            return response.status_code == 200
        except Exception:
            return False


# =============================================================================
# Factory
# =============================================================================

def create_llm_provider(settings: Settings | None = None) -> BaseLLMProvider:
    """Factory function to create LLM provider based on configuration.
    
    SPEC-003: LLM Provider 可配置切换
    
    Usage:
        provider = create_llm_provider()
        response = await provider.chat([Message(role="user", content="Hello")])
    """
    if settings is None:
        settings = get_settings()
    
    if settings.llm_provider == "openai":
        if not settings.openai_api_key:
            logger.warning("openai_api_key_missing", fallback="mock mode")
            # Return a mock provider for testing
            return MockLLMProvider()
        return OpenAIProvider(
            api_key=settings.openai_api_key,
            api_base=settings.openai_api_base,
            model=settings.openai_model,
        )
    elif settings.llm_provider == "ollama":
        return OllamaProvider(
            base_url=settings.ollama_base_url,
            model=settings.ollama_model,
        )
    else:
        raise ValueError(f"Unknown LLM provider: {settings.llm_provider}")


class MockLLMProvider(BaseLLMProvider):
    """Mock LLM provider for testing.
    
    Returns predefined responses for testing without real API calls.
    """
    
    @property
    def provider_name(self) -> str:
        return "mock"
    
    async def chat(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> ChatResponse:
        """Return mock response."""
        last_message = messages[-1].content if messages else ""
        return ChatResponse(
            content=f"[MOCK] Response to: {last_message[:50]}...",
            model="mock-model",
            token_usage={"prompt": 10, "completion": 20},
            finish_reason="stop",
        )
    
    async def chat_stream(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[str]:
        response = await self.chat(messages)
        yield response.content
    
    async def health_check(self) -> bool:
        return True
