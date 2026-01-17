"""
Voice Provider stubs (STT/TTS).

Provides stub implementations that return 503 Service Unavailable.
Actual implementations to be added based on TBD-L0-007 decision.

SPEC Reference: SPEC-009 (Voice STT/TTS APIs)
TODO: Implement actual STT/TTS providers (Whisper, OpenAI TTS, etc.)
"""

from typing import Any

from apps.api.config.settings import Settings, get_settings
from apps.api.core.errors import ErrorCode, ServiceUnavailableError
from apps.api.core.logging import get_logger
from apps.api.providers.base import BaseSTTProvider, BaseTTSProvider

logger = get_logger(__name__)


class StubSTTProvider(BaseSTTProvider):
    """Stub STT provider that returns 503.
    
    SPEC-009: v0.1 uses stub with 503 + clear error code.
    TBD-L0-007: STT/TTS Provider 选择与部署方式
    
    TODO: Implement actual STT provider:
    - Whisper API
    - OpenAI Whisper
    - Azure Speech
    """
    
    @property
    def provider_name(self) -> str:
        return "stub"
    
    async def transcribe(
        self,
        audio_data: bytes,
        *,
        language: str | None = None,
        **kwargs: Any,
    ) -> str:
        """Raise ServiceUnavailableError for stub.
        
        Frontend should handle this and show degradation message.
        """
        logger.info("stt_stub_called", audio_size=len(audio_data), language=language)
        raise ServiceUnavailableError(
            "Speech-to-Text is not configured. Please configure STT provider.",
            ErrorCode.STT_UNAVAILABLE,
        )


class StubTTSProvider(BaseTTSProvider):
    """Stub TTS provider that returns 503.
    
    SPEC-009: v0.1 uses stub with 503 + clear error code.
    TBD-L0-007: STT/TTS Provider 选择与部署方式
    
    TODO: Implement actual TTS provider:
    - OpenAI TTS
    - Azure TTS
    - ElevenLabs
    """
    
    @property
    def provider_name(self) -> str:
        return "stub"
    
    async def synthesize(
        self,
        text: str,
        *,
        voice: str | None = None,
        speed: float = 1.0,
        **kwargs: Any,
    ) -> bytes:
        """Raise ServiceUnavailableError for stub.
        
        Frontend should handle this and show degradation message.
        """
        logger.info("tts_stub_called", text_length=len(text), voice=voice)
        raise ServiceUnavailableError(
            "Text-to-Speech is not configured. Please configure TTS provider.",
            ErrorCode.TTS_UNAVAILABLE,
        )


# =============================================================================
# Factory
# =============================================================================

def create_stt_provider(settings: Settings | None = None) -> BaseSTTProvider:
    """Factory function to create STT provider.
    
    Currently only returns stub. Implement actual providers based on TBD-L0-007.
    """
    if settings is None:
        settings = get_settings()
    
    if settings.stt_provider == "stub":
        return StubSTTProvider()
    # TODO: Add Whisper provider
    # elif settings.stt_provider == "whisper":
    #     return WhisperSTTProvider(...)
    else:
        logger.warning("unknown_stt_provider", provider=settings.stt_provider)
        return StubSTTProvider()


def create_tts_provider(settings: Settings | None = None) -> BaseTTSProvider:
    """Factory function to create TTS provider.
    
    Currently only returns stub. Implement actual providers based on TBD-L0-007.
    """
    if settings is None:
        settings = get_settings()
    
    if settings.tts_provider == "stub":
        return StubTTSProvider()
    # TODO: Add OpenAI TTS provider
    # elif settings.tts_provider == "openai":
    #     return OpenAITTSProvider(...)
    else:
        logger.warning("unknown_tts_provider", provider=settings.tts_provider)
        return StubTTSProvider()
