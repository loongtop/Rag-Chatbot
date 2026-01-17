"""
Configuration settings for the API server.

Loads configuration from environment variables with sensible defaults.
Uses pydantic-settings for validation and type coercion.

SPEC Reference: SPEC-003 (Provider Abstraction)
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # ==========================================================================
    # Application
    # ==========================================================================
    app_name: str = "RAG Chatbot API"
    app_version: str = "0.1.0"
    debug: bool = False
    environment: Literal["dev", "staging", "production", "test"] = "dev"

    # ==========================================================================
    # Server
    # ==========================================================================
    host: str = "0.0.0.0"
    port: int = 8000

    # ==========================================================================
    # Database (PostgreSQL + pgvector)
    # ==========================================================================
    database_url: str = "postgresql://postgres:postgres@localhost:5432/ragchat"

    # ==========================================================================
    # LLM Provider Configuration
    # SPEC-003: LLM Provider Abstraction
    # ==========================================================================
    llm_provider: Literal["openai", "ollama"] = "openai"
    
    # OpenAI-compatible settings
    openai_api_key: str = ""  # Required if llm_provider=openai
    openai_api_base: str = "https://api.openai.com/v1"
    openai_model: str = "gpt-4"
    
    # Ollama settings (local mode)
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    # ==========================================================================
    # Embedding Provider Configuration
    # SPEC-003: Embedding Provider Abstraction
    # ==========================================================================
    embedding_provider: Literal["openai", "ollama"] = "openai"
    embedding_model: str = "text-embedding-3-small"
    embedding_dimension: int = 1536

    # ==========================================================================
    # STT/TTS Provider Configuration (Stub for v0.1)
    # SPEC-009: Voice STT/TTS APIs
    # TODO: Implement actual STT/TTS providers
    # ==========================================================================
    stt_provider: Literal["stub", "whisper"] = "stub"
    tts_provider: Literal["stub", "openai"] = "stub"

    # ==========================================================================
    # Admin Authentication
    # TBD-L0-003: Basic Auth for v0.1
    # ==========================================================================
    admin_username: str = "admin"
    admin_password: str = "changeme"  # MUST be changed in production

    # ==========================================================================
    # Rate Limiting
    # REQ-L0-SEC-003: API Rate Limiting
    # ==========================================================================
    rate_limit_chat: int = 30  # per minute
    rate_limit_auth: int = 5   # per 10 minutes
    rate_limit_upload: int = 10  # per 10 minutes
    rate_limit_admin: int = 100  # per minute

    # ==========================================================================
    # Security
    # ==========================================================================
    secret_key: str = "dev-secret-key-change-in-production"
    token_expire_minutes: int = 60 * 24  # 24 hours


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
