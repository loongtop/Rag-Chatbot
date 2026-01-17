"""
Voice API routes (STT/TTS).

Provides speech-to-text and text-to-speech endpoints.

SPEC Reference: SPEC-009 (Voice STT/TTS APIs)
IFC Reference: IFC-CHAT-API
TBD Reference: TBD-L0-007 (STT/TTS provider selection)

NOTE: v0.1 uses stub implementations that return 503.
"""

from fastapi import APIRouter, File, Request, UploadFile
from pydantic import BaseModel

from apps.api.core.logging import get_logger
from apps.api.core.middleware import rate_limiter
from apps.api.core.errors import RateLimitError
from apps.api.config.settings import get_settings
from apps.api.providers.voice import create_stt_provider, create_tts_provider

logger = get_logger(__name__)
router = APIRouter(prefix="/voice", tags=["voice"])


# =============================================================================
# Models
# =============================================================================

class STTResponse(BaseModel):
    """Response for STT endpoint."""
    text: str


class TTSRequest(BaseModel):
    """Request for TTS endpoint."""
    text: str


class TTSResponse(BaseModel):
    """Response for TTS endpoint."""
    audio_url: str


# =============================================================================
# Routes
# =============================================================================

@router.post("/stt", response_model=STTResponse)
async def speech_to_text(
    request: Request,
    audio: UploadFile = File(...),
    language: str = "zh",
) -> STTResponse:
    """Speech-to-text endpoint.
    
    SPEC-009: POST /api/voice/stt
    - Input: audio file (multipart/form-data)
    - Output: text
    
    TBD-L0-007: STT provider selection
    NOTE: v0.1 returns 503 (stub)
    """
    settings = get_settings()
    client_ip = request.client.host if request.client else "unknown"
    
    # Rate limiting
    if not rate_limiter.is_allowed(f"voice:{client_ip}", settings.rate_limit_upload, 600):
        raise RateLimitError("Rate limit exceeded.")
    
    logger.info(
        "stt_request",
        filename=audio.filename,
        content_type=audio.content_type,
        language=language,
    )
    
    # Read audio data
    audio_data = await audio.read()
    
    # Use STT provider (currently stub - returns 503)
    stt_provider = create_stt_provider()
    text = await stt_provider.transcribe(audio_data, language=language)
    
    return STTResponse(text=text)


@router.post("/tts", response_model=TTSResponse)
async def text_to_speech(request: Request, body: TTSRequest) -> TTSResponse:
    """Text-to-speech endpoint.
    
    SPEC-009: POST /api/voice/tts
    - Input: text
    - Output: audio_url (or audio bytes, TBD)
    
    TBD-L0-007: TTS provider selection
    NOTE: v0.1 returns 503 (stub)
    """
    settings = get_settings()
    client_ip = request.client.host if request.client else "unknown"
    
    # Rate limiting
    if not rate_limiter.is_allowed(f"voice:{client_ip}", settings.rate_limit_upload, 600):
        raise RateLimitError("Rate limit exceeded.")
    
    logger.info("tts_request", text_length=len(body.text))
    
    # Use TTS provider (currently stub - returns 503)
    tts_provider = create_tts_provider()
    audio_bytes = await tts_provider.synthesize(body.text)
    
    # TODO: Store audio and return URL (SPEC-009)
    return TTSResponse(audio_url="https://example.com/audio/placeholder.mp3")
