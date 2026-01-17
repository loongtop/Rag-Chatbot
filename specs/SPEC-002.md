---
id: "SPEC-002"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-001"
  - "REQ-L2-API-002"
  - "REQ-L2-API-003"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-003"
  - "SPEC-006"
profile: "python"
---

# Spec: Chat RAG Endpoint (Session + Context + References)

## 0. Summary

- Goal: 实现 `POST /api/chat`，支持会话、多轮、上下文感知检索、引用回填与 token 用量记录。
- Non-goals: 实现完整评测体系/精细化 rerank（可后续迭代）。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/chat`：`message` + `session_id?` + `language?` + `context?` → `answer` + `references[]` + `token_usage`。
- Session/Messages 持久化：记录用户输入、回答、引用、错误与 token_usage。
- 上下文感知检索：`context.productId/skuId/url` 作为过滤/加权信号。

### Out of Scope
- SSE/流式输出（可在后续扩展）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-001 | 端点返回 grounded answer + references | 引用包含可追溯来源 |
| REQ-L2-API-002 | `context` 参与召回/排序 | 优先与当前页面相关证据 |
| REQ-L2-API-003 | `session_id` + token_usage 持久化 | 追加写 messages |

## 3. Design / Decisions

### Proposed Approach
- RAG：query embedding → pgvector Top-K →（可选）重排 → prompt 组装（引用编号）→ LLM → 回填 references。
- 证据不足：优先澄清，否则拒答（明确“缺少可靠依据”）。
- 多语言：`language` 影响系统提示与输出语言（默认 zh）。

### Key Decisions
- Decision: `session_id` 由客户端可选传入，不传则服务端生成并返回
  - Rationale: 便于 Widget 无状态接入，同时支持多轮。
  - Alternatives: 强制客户端生成（易出错）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | `POST /api/chat`（含 `language` 与 `context`） |

## 5. Implementation Plan

1. 定义 Pydantic 模型：ChatRequest/ChatResponse/Reference/TokenUsage（对齐 `docs/architecture/api-spec.md`）。
2. 建表与访问层：`sessions`、`messages`（按 `docs/architecture/database-schema.md`），写入 token_usage 与 references。
3. 实现 RetrievalService：
   - 从 `chunks` 向量检索 Top-K（按 `docs/architecture/core-flows.md`）。
   - 根据 `context` 做过滤/加权（如 metadata.product_id、url 域名）。
4. 实现 PromptBuilder：
   - 引用内容转义；限制引用长度；分配 `[1]..[n]` 编号。
   - `language` 决定输出语言。
5. 实现 `/api/chat`：
   - 生成/恢复 session；持久化 user message；
   - 组装上下文并调用 `LLMProvider.chat_completion`；
   - 写入 assistant message（含 references/token_usage）并返回。
6. 测试（pytest）：
   - mock Provider；构造检索结果；断言引用编号与结构。

### Files / Modules
- `apps/api/app.py`（FastAPI app）
- `apps/api/api/chat.py`
- `apps/api/models/session.py`, `apps/api/models/message.py`
- `apps/api/services/retrieval.py`, `apps/api/services/prompting.py`

### Risks & Mitigations
- Risk: 证据不足导致幻觉
  - Mitigation: 设定 evidence 阈值 + 必须返回 references，否则澄清/拒答。

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| new session | message only | response 包含 `session_id` | session_id 可复用 |
| with context | context.productId present | references 优先包含该产品相关证据 | |
| no evidence | 检索为空/低分 | 返回澄清或拒答 + references 为空 | |
| token usage | provider returns usage | messages/token_usage 被持久化 | |
| provider down | provider 503 | 返回 503 + 友好错误码 | 见 TBD-L0-002 |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-002 | LLM/DB 异常时的降级返回格式 | M | Product Owner | open |
| TBD-L0-004 | 对话与日志留存策略 | M | Product Owner | open |
| TBD-L0-009 | 多语言策略（选择/检测） | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

