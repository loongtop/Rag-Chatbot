---
status: done
owner: requirements_split
layer_from: L1
layer_to: L2
parent: docs/L1/
target: docs/L2/
granularity: full
caf_version: v0.6.2
---

# Split Report: L1 → L2 (v0.6.2)

## 1. Summary

- **Decision**: PASS
- **Why**: 13 L1 Requirements (7 Features) → 3 L2 Components + interfaces.md
- **Traceability**: 严格逐级，所有 L2 REQ 来源于 L1 REQ

## 2. Inputs

| Item | Path | Count |
|------|------|-------|
| RAGQA | docs/L1/ragqa/requirements.md | 4 REQs |
| PRDREC | docs/L1/prdrec/requirements.md | 2 REQs |
| USRMGMT | docs/L1/usrmgmt/requirements.md | 1 REQ |
| ADMGMT | docs/L1/admgmt/requirements.md | 3 REQs |
| HANDOFF | docs/L1/handoff/requirements.md | 1 REQ |
| VOICE | docs/L1/voice/requirements.md | 1 REQ |
| UPLOAD | docs/L1/upload/requirements.md | 1 REQ |
| **Total L1 REQs** | | **13** |

## 3. L2 Components (from charter.yaml#components)

| Component | 技术栈 | 说明 |
|-----------|--------|------|
| `api-server` | Python/FastAPI | 后端 API 服务 |
| `chat-widget` | TypeScript/React | 前端嵌入式组件 |
| `admin-dashboard` | TypeScript/React | 后台管理 UI |

## 4. L1 Feature → L2 Component Mapping

| L1 Feature | L1 REQs | L2 Components | 说明 |
|------------|---------|---------------|------|
| RAGQA | 4 | api-server | RAG 核心在后端 |
| PRDREC | 2 | api-server | 推荐/比较算法在后端 |
| USRMGMT | 1 | api-server + chat-widget | 后端验证 + 前端界面 |
| ADMGMT | 3 | api-server + admin-dashboard | 后端 API + 前端 UI |
| HANDOFF | 1 | api-server + admin-dashboard | 队列 + 客服工作台 |
| VOICE | 1 | api-server + chat-widget | 后端 STT/TTS + 前端录音 |
| UPLOAD | 1 | api-server + chat-widget | 后端解析 + 前端上传 |

## 5. L1 → L2 Detailed Mapping

### 5.1 api-server

| L2 REQ-ID | L1 Source | Statement |
|-----------|-----------|-----------|
| REQ-L2-API-001 | REQ-L1-RAGQA-001 | RAG 问答 API |
| REQ-L2-API-002 | REQ-L1-RAGQA-002 | 上下文感知检索 API |
| REQ-L2-API-003 | REQ-L1-RAGQA-003 | 对话历史管理 API |
| REQ-L2-API-004 | REQ-L1-RAGQA-004 | LLM Provider 切换 |
| REQ-L2-API-005 | REQ-L1-PRDREC-001 | 产品推荐 API |
| REQ-L2-API-006 | REQ-L1-PRDREC-002 | 产品比较 API |
| REQ-L2-API-007 | REQ-L1-USRMGMT-001 | 邮箱验证 API |
| REQ-L2-API-008 | REQ-L1-ADMGMT-001 | 产品数据管理 API |
| REQ-L2-API-009 | REQ-L1-ADMGMT-002 | 知识库索引 API |
| REQ-L2-API-010 | REQ-L1-HANDOFF-001 | 人工转接 API |
| REQ-L2-API-011 | REQ-L1-VOICE-001 | STT/TTS API |
| REQ-L2-API-012 | REQ-L1-UPLOAD-001 | 文件解析 API |

### 5.2 chat-widget

| L2 REQ-ID | L1 Source | Statement |
|-----------|-----------|-----------|
| REQ-L2-WGT-001 | REQ-L0-WGT-001 (direct) | Widget 嵌入能力 |
| REQ-L2-WGT-002 | REQ-L1-USRMGMT-001 | 邮箱登录 UI |
| REQ-L2-WGT-003 | REQ-L0-WGT-003 (direct) | 多语言切换 UI |
| REQ-L2-WGT-004 | REQ-L1-VOICE-001 | 语音录入/播放 UI |
| REQ-L2-WGT-005 | REQ-L1-UPLOAD-001 | 文件上传 UI |
| REQ-L2-WGT-006 | REQ-L1-HANDOFF-001 | 人工/AI 切换 UI |

### 5.3 admin-dashboard

| L2 REQ-ID | L1 Source | Statement |
|-----------|-----------|-----------|
| REQ-L2-ADM-001 | REQ-L1-ADMGMT-001 | 产品数据管理 UI |
| REQ-L2-ADM-002 | REQ-L1-ADMGMT-002 | 知识库管理 UI |
| REQ-L2-ADM-003 | REQ-L1-ADMGMT-003 | 后台统一界面 |
| REQ-L2-ADM-004 | REQ-L1-HANDOFF-001 | 客服工作台 UI |

## 6. Interfaces (IFC)

| IFC-ID | Type | Provider | Consumer | Description |
|--------|------|----------|----------|-------------|
| IFC-CHAT-API | REST | api-server | chat-widget | 对话/RAG/推荐接口 |
| IFC-ADMIN-API | REST | api-server | admin-dashboard | 管理接口 |
| IFC-PRODUCT-DATA | Data | external | api-server | 产品数据契约 |
| IFC-WIDGET-CTX | Data | host page | chat-widget | Widget 上下文 |

## 7. Traceability Matrix

| L1 REQ-ID | L2 REQ-IDs | Coverage |
|-----------|------------|----------|
| REQ-L1-RAGQA-001 | REQ-L2-API-001 | ✅ |
| REQ-L1-RAGQA-002 | REQ-L2-API-002 | ✅ |
| REQ-L1-RAGQA-003 | REQ-L2-API-003 | ✅ |
| REQ-L1-RAGQA-004 | REQ-L2-API-004 | ✅ |
| REQ-L1-PRDREC-001 | REQ-L2-API-005 | ✅ |
| REQ-L1-PRDREC-002 | REQ-L2-API-006 | ✅ |
| REQ-L1-USRMGMT-001 | REQ-L2-API-007, REQ-L2-WGT-002 | ✅ |
| REQ-L1-ADMGMT-001 | REQ-L2-API-008, REQ-L2-ADM-001 | ✅ |
| REQ-L1-ADMGMT-002 | REQ-L2-API-009, REQ-L2-ADM-002 | ✅ |
| REQ-L1-ADMGMT-003 | REQ-L2-ADM-003 | ✅ |
| REQ-L1-HANDOFF-001 | REQ-L2-API-010, REQ-L2-WGT-006, REQ-L2-ADM-004 | ✅ |
| REQ-L1-VOICE-001 | REQ-L2-API-011, REQ-L2-WGT-004 | ✅ |
| REQ-L1-UPLOAD-001 | REQ-L2-API-012, REQ-L2-WGT-005 | ✅ |
| (direct) REQ-L0-WGT-001 | REQ-L2-WGT-001 | ✅ |
| (direct) REQ-L0-WGT-003 | REQ-L2-WGT-003 | ✅ |

**L1 Coverage**: 13/13 (100%)
**L0 Direct Coverage**: 2/2 (100%)

## 8. Gate Check

- [x] All L2 REQs have sources from L1 or L0-direct
- [x] No orphan L1 REQs
- [x] Interfaces defined for cross-component communication
- [x] Traceability matrix complete

---

**Result**: ✅ **PASS**

**Output Structure**:
```
docs/L2/
├── split-report.md
├── api-server/requirements.md      (12 REQs)
├── chat-widget/requirements.md     (6 REQs)
├── admin-dashboard/requirements.md (4 REQs)
└── interfaces.md                   (4 IFCs)
```
