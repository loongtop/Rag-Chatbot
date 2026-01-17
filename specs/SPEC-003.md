---
id: "SPEC-003"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-004"
interfaces: []
depends_on: []
profile: "python"
---

# Spec: LLM Provider Abstraction (OpenAI-Compatible + Ollama)

## 0. Summary

- Goal: 提供统一的 LLM/Embedding 调用抽象，可通过配置在 OpenAI-Compatible API 与 Ollama 间切换。
- Non-goals: 固定某个具体模型/厂商（由配置决定）。
- Leaf: `true`

## 1. Scope

### In Scope
- `LLMProvider` 接口：`chat_completion()`、`embed_texts()`。
- OpenAI-Compatible Provider（base_url/api_key/model/embedding_model）。
- Ollama Provider（host/model/embedding_model）。
- 超时/重试/错误分类，返回 token usage（若上游支持）。

### Out of Scope
- 模型评测与自动选择策略（后续）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-004 | 抽象层 + 两种实现 + 配置切换 | 供 `/api/chat`、索引构建复用 |

## 3. Design / Decisions

### Proposed Approach
- 统一内部异常：`ProviderConfigError`、`ProviderTimeout`、`ProviderUnavailable`。
- 通过 env 选择 Provider：`LLM_PROVIDER=openai|ollama`，其余参数按 provider 前缀读取。

### Key Decisions
- Decision: Embedding 与 Chat 走同一 Provider 抽象
  - Rationale: 简化配置与依赖，满足 RAG 所需的 embedding 与生成。
  - Alternatives: 单独 embedding provider（配置更复杂）。

## 4. Interfaces Impact

N/A（内部模块，被 IFC-CHAT-API/ADMIN-API 的实现间接使用）

## 5. Implementation Plan

1. 定义 `LLMProvider` 协议与 `ProviderResponse`（text + usage）。
2. 实现 OpenAI-Compatible：
   - chat completions（兼容 `/v1/chat/completions`）
   - embeddings（兼容 `/v1/embeddings`）
3. 实现 Ollama：
   - chat（`/api/chat`）
   - embeddings（`/api/embeddings`）
4. 实现 Provider 工厂：`get_llm_provider(config) -> LLMProvider`。
5. 单测：mock HTTP；覆盖配置校验、错误映射与超时。

### Files / Modules
- `apps/api/llm/base.py`
- `apps/api/llm/openai_compat.py`
- `apps/api/llm/ollama.py`
- `apps/api/llm/factory.py`

### Risks & Mitigations
- Risk: Provider 兼容性差异导致行为不一致
  - Mitigation: 对外只暴露最小共同语义；差异通过适配层吸收。

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| switch provider | `LLM_PROVIDER=openai/ollama` | 工厂返回对应实现 | |
| invalid config | 缺少 key/base_url | 抛 ProviderConfigError | |
| timeout | 超时 | 映射为 ProviderTimeout | |
| embedding | texts[] | 返回向量维度一致 | 维度可配置/记录 |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-001 | Provider/Model 选择与成本约束 | H | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

