---
id: "SPEC-001"
status: draft
owner: spec
leaf: false
parent: "docs/L2/api-server/requirements.md"
source_requirements:
  - "REQ-L2-API-001"
  - "REQ-L2-API-002"
  - "REQ-L2-API-003"
  - "REQ-L2-API-004"
  - "REQ-L2-API-005"
  - "REQ-L2-API-006"
  - "REQ-L2-API-007"
  - "REQ-L2-API-008"
  - "REQ-L2-API-009"
  - "REQ-L2-API-010"
  - "REQ-L2-API-011"
  - "REQ-L2-API-012"
interfaces:
  - "IFC-CHAT-API"
  - "IFC-ADMIN-API"
depends_on: []
profile: "python"
---

# Spec: API Server Overview

## 0. Summary

- Goal: 将 `docs/L2/api-server/requirements.md` 的能力拆解为可落地的 leaf Specs，并与 `docs/architecture/*` 对齐。
- Non-goals: 生产级部署/监控体系、第三方 SSO/复杂权限、跨 Region 容灾。
- Leaf: `false`

## 1. Scope

### In Scope
- 按 `docs/L2/interfaces.md` 提供 `IFC-CHAT-API` 与 `IFC-ADMIN-API` 的端点与契约。
- PostgreSQL + pgvector 数据模型（按 `docs/architecture/database-schema.md`）。
- 基础安全/限流/审计钩子（满足 L0 安全指标的最小实现）。

### Out of Scope
- 引入额外基础设施（如 Kafka/Celery/ES）作为强依赖（可在后续版本评估）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-001 | SPEC-002 | `/api/chat` + references |
| REQ-L2-API-002 | SPEC-002 | context-aware retrieval |
| REQ-L2-API-003 | SPEC-002 | session/messages + token usage |
| REQ-L2-API-004 | SPEC-003 | OpenAI-compatible + Ollama provider |
| REQ-L2-API-005 | SPEC-005 | `/api/recommend` |
| REQ-L2-API-006 | SPEC-005 | `/api/compare` |
| REQ-L2-API-007 | SPEC-007 | email OTP auth |
| REQ-L2-API-008 | SPEC-004 | products import/query |
| REQ-L2-API-009 | SPEC-006 | docs upload + index jobs |
| REQ-L2-API-010 | SPEC-008 | handoff state machine + APIs |
| REQ-L2-API-011 | SPEC-009 | STT/TTS |
| REQ-L2-API-012 | SPEC-010 | upload parse |

## 3. Design / Decisions

### Proposed Approach
- FastAPI + Pydantic 定义接口模型；SQLAlchemy/SQLModel 管理 DB；pgvector 承载向量检索。
- 统一错误响应、request_id、限流/审计中间件；Provider 抽象覆盖 LLM/Embedding/STT/TTS/Extractor。

### Key Decisions
- Decision: 单体 API Server 作为统一入口（公开/用户/后台）
  - Rationale: v0.1 降低运维复杂度，满足技术边界并便于迭代。
  - Alternatives: 拆分多服务（不利于快速落地）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | 面向 Widget 的公开接口 |
| IFC-ADMIN-API | provide | 面向后台管理的接口 |

## 5. Implementation Plan

1. 完成 SPEC-003（Provider 抽象）与基础配置结构。
2. 完成 SPEC-004 / SPEC-006（数据与索引入口）。
3. 完成 SPEC-002（核心 `/api/chat`），并接入检索与引用。
4. 完成 SPEC-005/007/008/009/010（增量能力）。

## 6. Acceptance Tests

- 集成冒烟：按 `docs/L2/interfaces.md` 对所有端点做 200/4xx/5xx 基础断言（leaf Specs 各自定义详细用例）。

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-001 | LLM Provider/Model 选择与成本上限 | H | Product Owner | open |
| TBD-L0-002 | 降级策略定义 | M | Product Owner | open |
| TBD-L0-003 | 后台鉴权方式（Basic/SSO） | M | Product Owner | open |

## 8. Leaf Checklist

N/A（leaf=false）

