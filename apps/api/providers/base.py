"""
Base Provider Abstraction for LLM and Embedding services.

Defines the abstract interfaces that all providers must implement.
Enables swapping between OpenAI, Ollama, and other providers.

SPEC Reference: SPEC-003 (LLM Provider Abstraction & Factory)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, AsyncIterator


@dataclass
class Message:
    """Chat message."""
    role: str  # "system", "user", "assistant"
    content: str


@dataclass
class ChatResponse:
    """Response from chat completion.
    
    Includes token usage for cost tracking (REQ-L0-API-005).
    """
    content: str
    model: str
    token_usage: dict[str, int]  # {"prompt": N, "completion": M}
    finish_reason: str | None = None


@dataclass
class EmbeddingResponse:
    """Response from embedding generation."""
    embeddings: list[list[float]]
    model: str
    token_usage: dict[str, int]


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers.
    
    All LLM providers (OpenAI, Ollama, etc.) must implement this interface.
    
    SPEC-003: 
    - LLM Provider 可配置切换
    - 支持在线 OpenAI-Compatible API 与本地 Ollama
    """
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider name (e.g., 'openai', 'ollama')."""
        ...
    
    @abstractmethod
    async def chat(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs: Any,
    ) -> ChatResponse:
        """Generate chat completion.
        
        Args:
            messages: List of chat messages
            model: Model to use (optional, uses default if not specified)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Provider-specific arguments
            
        Returns:
            ChatResponse with content and token usage
        """
        ...
    
    @abstractmethod
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
        
        Args:
            messages: List of chat messages
            model: Model to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Yields:
            Content chunks as they are generated
        """
        ...
    
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is healthy and accessible.
        
        Used for graceful degradation (REQ-L0-STAB-002).
        """
        ...


class BaseEmbeddingProvider(ABC):
    """Abstract base class for Embedding providers.
    
    SPEC-003: Embedding Provider Abstraction
    """
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider name."""
        ...
    
    @property
    @abstractmethod
    def dimension(self) -> int:
        """Return the embedding dimension."""
        ...
    
    @abstractmethod
    async def embed(
        self,
        texts: list[str],
        *,
        model: str | None = None,
        **kwargs: Any,
    ) -> EmbeddingResponse:
        """Generate embeddings for texts.
        
        Args:
            texts: List of texts to embed
            model: Model to use
            
        Returns:
            EmbeddingResponse with embeddings and token usage
        """
        ...
    
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is healthy."""
        ...


class BaseSTTProvider(ABC):
    """Abstract base class for Speech-to-Text providers.
    
    SPEC-009: Voice STT API
    TODO: Implement actual providers (Whisper, etc.)
    """
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider name."""
        ...
    
    @abstractmethod
    async def transcribe(
        self,
        audio_data: bytes,
        *,
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        """Transcribe audio to text.
        
        Args:
            audio_data: Audio file bytes
            language: Language hint
            
        Returns:
            Transcribed text
        """
        ...


class BaseTTSProvider(ABC):
    """Abstract base class for Text-to-Speech providers.
    
    SPEC-009: Voice TTS API
    TODO: Implement actual providers (OpenAI TTS, etc.)
    """
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider name."""
        ...
    
    @abstractmethod
    async def synthesize(
        self,
        text: str,
        *,
        voice: str | None = None,
        speed: float = 1.0,
        **kwargs: Any,
    ) -> bytes:
        """Synthesize speech from text.
        
        Args:
            text: Text to synthesize
            voice: Voice to use
            speed: Speech speed
            
        Returns:
            Audio data bytes
        """
        ...
