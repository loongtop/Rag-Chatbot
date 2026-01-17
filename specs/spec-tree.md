---
status: draft
owner: spec
layer: SPEC
parent: docs/L2
profile: "python,typescript"
caf_version: v0.6.5
---

# Spec Tree

> 目的：把 L2 Requirements 映射到可实现的 leaf Specs，并提供进度与覆盖视图。

## 1. Tree View

```
docs/L2/api-server/requirements.md
  └─ SPEC-001 (leaf=false) API Server Overview
       ├─ SPEC-002 (leaf=true)  Chat RAG Endpoint (session/context/references)
       ├─ SPEC-003 (leaf=true)  LLM Provider Abstraction (OpenAI-compatible + Ollama)
       ├─ SPEC-004 (leaf=true)  Product Data Admin APIs (import/version/query)
       ├─ SPEC-005 (leaf=true)  Recommend & Compare APIs
       ├─ SPEC-006 (leaf=true)  Knowledge Base Docs + Index Jobs APIs
       ├─ SPEC-007 (leaf=true)  Email OTP Auth APIs
       ├─ SPEC-008 (leaf=true)  Handoff State Machine + APIs (user + admin)
       ├─ SPEC-009 (leaf=true)  Voice STT/TTS APIs
       └─ SPEC-010 (leaf=true)  Upload Parsing API (file/image → extractedContent)

docs/L2/chat-widget/requirements.md
  └─ SPEC-011 (leaf=false) Chat Widget Overview
       ├─ SPEC-012 (leaf=true)  Embed + Core Chat UI
       ├─ SPEC-013 (leaf=true)  i18n + Language Toggle
       ├─ SPEC-014 (leaf=true)  Email Login UI
       ├─ SPEC-015 (leaf=true)  Voice UI (record + playback)
       ├─ SPEC-016 (leaf=true)  Upload UI (progress + limits)
       └─ SPEC-017 (leaf=true)  AI/Human Toggle UI (queue status)

docs/L2/admin-dashboard/requirements.md
  └─ SPEC-018 (leaf=false) Admin Dashboard Overview
       ├─ SPEC-019 (leaf=true)  App Shell + Nav + Auth Entry
       ├─ SPEC-020 (leaf=true)  Products Management UI
       ├─ SPEC-021 (leaf=true)  Knowledge Base Management UI
       └─ SPEC-022 (leaf=true)  Handoff Console UI
```

## 2. Coverage Matrix (L2 → Spec)

| REQ-L2 | SPEC | Leaf | Status | Notes |
|--------|------|------|--------|------|
| REQ-L2-API-001 | SPEC-002 | true | draft | `/api/chat` grounded answer + references |
| REQ-L2-API-002 | SPEC-002 | true | draft | context-aware retrieval |
| REQ-L2-API-003 | SPEC-002 | true | draft | sessions/messages + token usage |
| REQ-L2-API-004 | SPEC-003 | true | draft | provider abstraction + config |
| REQ-L2-API-005 | SPEC-005 | true | draft | `/api/recommend` |
| REQ-L2-API-006 | SPEC-005 | true | draft | `/api/compare` |
| REQ-L2-API-007 | SPEC-007 | true | draft | `/api/auth/send-code` + `/verify` |
| REQ-L2-API-008 | SPEC-004 | true | draft | `/api/admin/products` |
| REQ-L2-API-009 | SPEC-006 | true | draft | docs upload + index rebuild/status |
| REQ-L2-API-010 | SPEC-008 | true | draft | `/api/handoff` + queue/admin actions |
| REQ-L2-API-011 | SPEC-009 | true | draft | `/api/voice/stt` + `/tts` |
| REQ-L2-API-012 | SPEC-010 | true | draft | `/api/upload` |
| REQ-L2-WGT-001 | SPEC-012 | true | draft | script embed + demo |
| REQ-L2-WGT-002 | SPEC-014 | true | draft | email login UI |
| REQ-L2-WGT-003 | SPEC-013 | true | draft | zh/en toggle |
| REQ-L2-WGT-004 | SPEC-015 | true | draft | voice UI |
| REQ-L2-WGT-005 | SPEC-016 | true | draft | upload UI |
| REQ-L2-WGT-006 | SPEC-017 | true | draft | AI/human toggle |
| REQ-L2-ADM-001 | SPEC-020 | true | draft | products UI |
| REQ-L2-ADM-002 | SPEC-021 | true | draft | docs/index/logs UI |
| REQ-L2-ADM-003 | SPEC-019 | true | draft | layout + auth entry |
| REQ-L2-ADM-004 | SPEC-022 | true | draft | handoff console |

## 3. Leaf Queue

| SPEC | Priority | Owner | Ready For Code | Notes |
|------|----------|-------|----------------|------|
| SPEC-003 | P0 | | yes | Provider abstraction unblocks chat/indexing |
| SPEC-002 | P0 | | yes | Core user path |
| SPEC-004 | P0 | | yes | Product import for recommend/compare |
| SPEC-006 | P0 | | yes | Indexing loop for RAG |
| SPEC-012 | P0 | | yes | Widget baseline |
| SPEC-019 | P0 | | yes | Admin baseline |
| SPEC-020 | P0 | | yes | Admin products |
| SPEC-021 | P0 | | yes | Admin docs/index |
| SPEC-005 | P1 | | yes | Depends on SPEC-004 |
| SPEC-007 | P1 | | yes | Unlocks login gating |
| SPEC-008 | P1 | | yes | Handoff loop |
| SPEC-010 | P1 | | yes | Extraction provider can be stubbed |
| SPEC-009 | P1 | | yes | Provider TBD |
| SPEC-013 | P1 | | yes | UI-only |
| SPEC-014 | P1 | | yes | UI + auth API |
| SPEC-015 | P1 | | yes | UI + voice API |
| SPEC-016 | P1 | | yes | UI + upload API |
| SPEC-017 | P1 | | yes | UI + handoff API |
| SPEC-022 | P1 | | yes | Depends on SPEC-008 |

## 4. Interface Touchpoints

| SPEC | IFC | Role | Notes |
|------|-----|------|------|
| SPEC-002 | IFC-CHAT-API | provide | `/api/chat` contract |
| SPEC-003 | IFC-CHAT-API | provide | indirectly supports chat outputs |
| SPEC-004 | IFC-ADMIN-API | provide | products admin endpoints |
| SPEC-005 | IFC-CHAT-API | provide | recommend/compare |
| SPEC-006 | IFC-ADMIN-API | provide | docs + index endpoints |
| SPEC-007 | IFC-CHAT-API | provide | auth endpoints |
| SPEC-008 | IFC-CHAT-API | provide | user handoff |
| SPEC-008 | IFC-ADMIN-API | provide | admin handoff |
| SPEC-009 | IFC-CHAT-API | provide | voice endpoints |
| SPEC-010 | IFC-CHAT-API | provide | upload endpoint |
| SPEC-012 | IFC-CHAT-API | consume | widget calls backend |
| SPEC-014 | IFC-CHAT-API | consume | auth calls |
| SPEC-015 | IFC-CHAT-API | consume | voice calls |
| SPEC-016 | IFC-CHAT-API | consume | upload calls |
| SPEC-017 | IFC-CHAT-API | consume | handoff calls |
| SPEC-019 | IFC-ADMIN-API | consume | admin calls backend |
| SPEC-020 | IFC-ADMIN-API | consume | products admin |
| SPEC-021 | IFC-ADMIN-API | consume | docs/index admin |
| SPEC-022 | IFC-ADMIN-API | consume | handoff admin |

## 5. Gate Check

- [ ] 每个 Spec 都有 `source_requirements`
- [ ] 每个 REQ-L2 至少映射到 1 个 Spec（或标注 N/A + reason）
- [ ] leaf Spec 的 Leaf Checklist 全部满足
