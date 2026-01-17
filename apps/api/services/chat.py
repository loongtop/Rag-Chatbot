"""
Chat service - RAG pipeline implementation.

Provides the core RAG functionality for chat, including:
- Query embedding
- Vector search (pgvector)
- Prompt assembly with references
- LLM completion
- Token usage tracking

SPEC Reference: SPEC-002 (Chat RAG Endpoint)
"""

import uuid
from dataclasses import dataclass

from apps.api.api.schemas import (
    ChatContext,
    ChatRequest,
    ChatResponse,
    Reference,
    TokenUsage,
)
from apps.api.core.logging import get_logger
from apps.api.providers.base import BaseLLMProvider, BaseEmbeddingProvider, Message
from apps.api.providers.llm import create_llm_provider
from apps.api.providers.embedding import create_embedding_provider

logger = get_logger(__name__)


@dataclass
class RetrievedChunk:
    """Retrieved document chunk from vector search."""
    document_id: str
    chunk_id: str
    content: str
    title: str
    url: str | None
    score: float
    metadata: dict


class ChatService:
    """RAG Chat service.
    
    SPEC-002: Implements the RAG pipeline for grounded answers.
    
    TODO:
    - Implement actual vector search (SPEC-006)
    - Implement session persistence (SPEC-002)
    - Implement reranking (optional)
    """
    
    def __init__(
        self,
        llm_provider: BaseLLMProvider | None = None,
        embedding_provider: BaseEmbeddingProvider | None = None,
    ) -> None:
        self._llm = llm_provider or create_llm_provider()
        self._embedding = embedding_provider or create_embedding_provider()
        logger.info(
            "chat_service_initialized",
            llm_provider=self._llm.provider_name,
            embedding_provider=self._embedding.provider_name,
        )
    
    async def chat(self, request: ChatRequest) -> ChatResponse:
        """Process a chat request through the RAG pipeline.
        
        SPEC-002 Pipeline:
        1. Generate session_id if not provided
        2. Embed query
        3. Vector search with context filtering
        4. Assemble prompt with references
        5. LLM completion
        6. Parse and return response with references
        """
        # 1. Session management
        session_id = request.session_id or f"sess_{uuid.uuid4().hex[:12]}"
        
        logger.info(
            "chat_request_started",
            session_id=session_id,
            message_length=len(request.message),
            has_context=request.context is not None,
        )
        
        try:
            # 2. Retrieve relevant chunks
            chunks = await self._retrieve_chunks(
                query=request.message,
                context=request.context,
                top_k=5,
            )
            
            # 3. Build prompt with references
            messages = self._build_prompt(
                query=request.message,
                chunks=chunks,
                language=request.language,
            )
            
            # 4. LLM completion
            llm_response = await self._llm.chat(messages, temperature=0.3)
            
            # 5. Build references
            references = self._build_references(chunks)
            
            # 6. Build response
            response = ChatResponse(
                answer=llm_response.content,
                references=references,
                session_id=session_id,
                token_usage=TokenUsage(
                    prompt=llm_response.token_usage.get("prompt", 0),
                    completion=llm_response.token_usage.get("completion", 0),
                    model=llm_response.model,
                ),
            )
            
            # TODO: Persist message to session (SPEC-002)
            # await self._persist_message(session_id, request, response)
            
            logger.info(
                "chat_request_completed",
                session_id=session_id,
                references_count=len(references),
                tokens_used=llm_response.token_usage,
            )
            
            return response
            
        except Exception as e:
            logger.exception("chat_request_failed", session_id=session_id)
            raise
    
    async def _retrieve_chunks(
        self,
        query: str,
        context: ChatContext | None,
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        """Retrieve relevant document chunks via vector search.
        
        TODO: Implement actual pgvector search (SPEC-006)
        Currently returns mock data for skeleton.
        """
        # Embed query
        # embedding_response = await self._embedding.embed([query])
        # query_embedding = embedding_response.embeddings[0]
        
        # TODO: Vector search with pgvector
        # SELECT * FROM document_chunks
        # WHERE embedding <-> $1 < threshold
        # ORDER BY embedding <-> $1
        # LIMIT $2
        
        # TODO: Context filtering
        # if context and context.product_id:
        #     filter by product relevance
        
        # Mock data for skeleton
        logger.warning("retrieve_chunks_mock", message="Using mock data - implement SPEC-006")
        return [
            RetrievedChunk(
                document_id="doc-001",
                chunk_id="chunk-001",
                content="[Mock] 这是一段来自产品手册的内容，描述了产品的主要功能。",
                title="产品手册 - 功能说明",
                url="https://example.com/docs/manual",
                score=0.95,
                metadata={"source": "manual"},
            ),
        ]
    
    def _build_prompt(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        language: str,
    ) -> list[Message]:
        """Build prompt with system instructions and retrieved context.
        
        SPEC-002:
        - Include reference numbers for traceability
        - Language-specific instructions
        - Refusal instruction when evidence is insufficient
        """
        # System prompt
        if language == "zh":
            system_content = """你是一个产品知识库助手。请根据提供的参考资料回答用户问题。

规则：
1. 仅基于参考资料回答，不要编造信息
2. 引用时使用 [1], [2] 等编号标注来源
3. 如果参考资料不足以回答问题，请明确说明"根据现有资料无法回答"
4. 保持回答简洁、专业"""
        else:
            system_content = """You are a product knowledge assistant. Answer questions based on the provided references.

Rules:
1. Only answer based on the references provided, do not make up information
2. Use [1], [2] etc. to cite sources
3. If references are insufficient, clearly state "Unable to answer based on available information"
4. Keep answers concise and professional"""
        
        # Build context with references
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            context_parts.append(f"[{i}] {chunk.title}\n{chunk.content}")
        
        context_content = "\n\n".join(context_parts) if context_parts else "(No references available)"
        
        return [
            Message(role="system", content=system_content),
            Message(role="user", content=f"参考资料:\n{context_content}\n\n用户问题: {query}"),
        ]
    
    def _build_references(self, chunks: list[RetrievedChunk]) -> list[Reference]:
        """Build reference list from retrieved chunks."""
        return [
            Reference(
                type="document_chunk",
                title=chunk.title,
                snippet=chunk.content[:200] + "..." if len(chunk.content) > 200 else chunk.content,
                source={
                    "documentId": chunk.document_id,
                    "chunkId": chunk.chunk_id,
                },
                url=chunk.url,
            )
            for chunk in chunks
        ]


# Global service instance (lazy initialization)
_chat_service: ChatService | None = None


def get_chat_service() -> ChatService:
    """Get or create chat service instance."""
    global _chat_service
    if _chat_service is None:
        _chat_service = ChatService()
    return _chat_service
