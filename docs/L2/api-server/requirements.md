---
status: draft
owner: architect
layer: L2
parent: docs/L1/
component: "api-server"
profile: "python"
caf_version: v0.6.5
---

# L2 Requirements: API Server

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L2
parent: "docs/L1/split-report.md"
component: "api-server"
profile: "python"

requirements:
  # ===========================================================================
  # From RAGQA Feature
  # ===========================================================================
  - id: REQ-L2-API-001
    priority: P0
    statement: "提供 RAG 问答 API：接收用户问题，返回带引用来源的回答。"
    sources:
      - id: "REQ-L1-RAGQA-001"
        path: "docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-001"
    acceptance:
      - "POST /api/chat 接口可用"
      - "回答包含 references 字段"
    status: draft
    section: functional

  - id: REQ-L2-API-002
    priority: P0
    statement: "支持上下文感知检索：接收 productId/skuId/url 参数，优化检索排序。"
    sources:
      - id: "REQ-L1-RAGQA-002"
        path: "docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-002"
    acceptance:
      - "接口支持 context 参数"
      - "上下文影响检索结果"
    status: draft
    section: functional

  - id: REQ-L2-API-003
    priority: P0
    statement: "提供对话历史管理 API：存储/检索对话，记录 token 用量。"
    sources:
      - id: "REQ-L1-RAGQA-003"
        path: "docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-003"
    acceptance:
      - "支持 session_id 参数"
      - "记录 token_usage"
    status: draft
    section: functional

  - id: REQ-L2-API-004
    priority: P0
    statement: "实现 LLM Provider 抽象层：支持 OpenAI-Compatible API 和 Ollama 切换。"
    sources:
      - id: "REQ-L1-RAGQA-004"
        path: "docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-004"
    acceptance:
      - "配置 LLM_PROVIDER 可切换"
      - "两种模式均可工作"
    status: draft
    section: functional

  # ===========================================================================
  # From PRDREC Feature
  # ===========================================================================
  - id: REQ-L2-API-005
    priority: P0
    statement: "提供产品推荐 API：基于用户需求返回 Top-N SKU + 推荐理由。"
    sources:
      - id: "REQ-L1-PRDREC-001"
        path: "docs/L1/prdrec/requirements.md#REQ-L1-PRDREC-001"
    acceptance:
      - "POST /api/recommend 接口可用"
      - "返回 products[] + reasons[]"
    status: draft
    section: functional

  - id: REQ-L2-API-006
    priority: P0
    statement: "提供产品比较 API：接收 2-4 个 SKU ID，返回结构化对比。"
    sources:
      - id: "REQ-L1-PRDREC-002"
        path: "docs/L1/prdrec/requirements.md#REQ-L1-PRDREC-002"
    acceptance:
      - "POST /api/compare 接口可用"
      - "返回对比表格数据"
    status: draft
    section: functional

  # ===========================================================================
  # From USRMGMT Feature
  # ===========================================================================
  - id: REQ-L2-API-007
    priority: P1
    statement: "提供邮箱验证 API：发送验证码 + 验证接口。"
    sources:
      - id: "REQ-L1-USRMGMT-001"
        path: "docs/L1/usrmgmt/requirements.md#REQ-L1-USRMGMT-001"
    acceptance:
      - "POST /api/auth/send-code 接口可用"
      - "POST /api/auth/verify 接口可用"
    status: draft
    section: functional

  # ===========================================================================
  # From ADMGMT Feature
  # ===========================================================================
  - id: REQ-L2-API-008
    priority: P0
    statement: "提供产品数据管理 API：JSON 上传/替换/查询。"
    sources:
      - id: "REQ-L1-ADMGMT-001"
        path: "docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-001"
    acceptance:
      - "POST /api/admin/products 上传"
      - "GET /api/admin/products 查询"
    status: draft
    section: functional

  - id: REQ-L2-API-009
    priority: P0
    statement: "提供知识库索引 API：文档上传/向量化/状态查询。"
    sources:
      - id: "REQ-L1-ADMGMT-002"
        path: "docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-002"
    acceptance:
      - "POST /api/admin/docs 上传"
      - "POST /api/admin/index/rebuild 重建"
      - "GET /api/admin/index/status 状态"
    status: draft
    section: functional

  # ===========================================================================
  # From HANDOFF Feature
  # ===========================================================================
  - id: REQ-L2-API-010
    priority: P1
    statement: "提供人工转接 API：创建转接请求，查询队列状态。"
    sources:
      - id: "REQ-L1-HANDOFF-001"
        path: "docs/L1/handoff/requirements.md#REQ-L1-HANDOFF-001"
    acceptance:
      - "POST /api/handoff 创建转接"
      - "GET /api/handoff/queue 队列状态"
    status: draft
    section: functional

  # ===========================================================================
  # From VOICE Feature
  # ===========================================================================
  - id: REQ-L2-API-011
    priority: P1
    statement: "提供 STT/TTS API：语音转文字 + 文字转语音。"
    sources:
      - id: "REQ-L1-VOICE-001"
        path: "docs/L1/voice/requirements.md#REQ-L1-VOICE-001"
    acceptance:
      - "POST /api/voice/stt 语音转文字"
      - "POST /api/voice/tts 文字转语音"
    status: draft
    section: functional

  # ===========================================================================
  # From UPLOAD Feature
  # ===========================================================================
  - id: REQ-L2-API-012
    priority: P1
    statement: "提供文件解析 API：上传文件并提取内容。"
    sources:
      - id: "REQ-L1-UPLOAD-001"
        path: "docs/L1/upload/requirements.md#REQ-L1-UPLOAD-001"
    acceptance:
      - "POST /api/upload 上传文件"
      - "返回 extracted_content"
    status: draft
    section: functional

tbds: []
exclusions: []
```

## — END REGISTRY —

---

## Summary

| Source Feature | REQ Count | L2 REQ-IDs |
|----------------|-----------|------------|
| RAGQA | 4 | REQ-L2-API-001 ~ 004 |
| PRDREC | 2 | REQ-L2-API-005 ~ 006 |
| USRMGMT | 1 | REQ-L2-API-007 |
| ADMGMT | 2 | REQ-L2-API-008 ~ 009 |
| HANDOFF | 1 | REQ-L2-API-010 |
| VOICE | 1 | REQ-L2-API-011 |
| UPLOAD | 1 | REQ-L2-API-012 |
| **Total** | **12** | |

---

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L2-API-001 | P0 | 提供 RAG 问答 API：接收用户问题，返回带引用来源的回答。 | REQ-L1-RAGQA-001 | 2 | draft |
| REQ-L2-API-002 | P0 | 支持上下文感知检索：接收 productId/skuId/url 参数，优化检索排序。 | REQ-L1-RAGQA-002 | 2 | draft |
| REQ-L2-API-003 | P0 | 提供对话历史管理 API：存储/检索对话，记录 token 用量。 | REQ-L1-RAGQA-003 | 2 | draft |
| REQ-L2-API-004 | P0 | 实现 LLM Provider 抽象层：支持 OpenAI-Compatible API 和 Ollama 切换。 | REQ-L1-RAGQA-004 | 2 | draft |
| REQ-L2-API-005 | P0 | 提供产品推荐 API：基于用户需求返回 Top-N SKU + 推荐理由。 | REQ-L1-PRDREC-001 | 2 | draft |
| REQ-L2-API-006 | P0 | 提供产品比较 API：接收 2-4 个 SKU ID，返回结构化对比。 | REQ-L1-PRDREC-002 | 2 | draft |
| REQ-L2-API-007 | P1 | 提供邮箱验证 API：发送验证码 + 验证接口。 | REQ-L1-USRMGMT-001 | 2 | draft |
| REQ-L2-API-008 | P0 | 提供产品数据管理 API：JSON 上传/替换/查询。 | REQ-L1-ADMGMT-001 | 2 | draft |
| REQ-L2-API-009 | P0 | 提供知识库索引 API：文档上传/向量化/状态查询。 | REQ-L1-ADMGMT-002 | 3 | draft |
| REQ-L2-API-010 | P1 | 提供人工转接 API：创建转接请求，查询队列状态。 | REQ-L1-HANDOFF-001 | 2 | draft |
| REQ-L2-API-011 | P1 | 提供 STT/TTS API：语音转文字 + 文字转语音。 | REQ-L1-VOICE-001 | 2 | draft |
| REQ-L2-API-012 | P1 | 提供文件解析 API：上传文件并提取内容。 | REQ-L1-UPLOAD-001 | 2 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L2-API-001 | REQ-L1-RAGQA-001 | docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-001 |
| REQ-L2-API-002 | REQ-L1-RAGQA-002 | docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-002 |
| REQ-L2-API-003 | REQ-L1-RAGQA-003 | docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-003 |
| REQ-L2-API-004 | REQ-L1-RAGQA-004 | docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-004 |
| REQ-L2-API-005 | REQ-L1-PRDREC-001 | docs/L1/prdrec/requirements.md#REQ-L1-PRDREC-001 |
| REQ-L2-API-006 | REQ-L1-PRDREC-002 | docs/L1/prdrec/requirements.md#REQ-L1-PRDREC-002 |
| REQ-L2-API-007 | REQ-L1-USRMGMT-001 | docs/L1/usrmgmt/requirements.md#REQ-L1-USRMGMT-001 |
| REQ-L2-API-008 | REQ-L1-ADMGMT-001 | docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-001 |
| REQ-L2-API-009 | REQ-L1-ADMGMT-002 | docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-002 |
| REQ-L2-API-010 | REQ-L1-HANDOFF-001 | docs/L1/handoff/requirements.md#REQ-L1-HANDOFF-001 |
| REQ-L2-API-011 | REQ-L1-VOICE-001 | docs/L1/voice/requirements.md#REQ-L1-VOICE-001 |
| REQ-L2-API-012 | REQ-L1-UPLOAD-001 | docs/L1/upload/requirements.md#REQ-L1-UPLOAD-001 |

## Gate Check

- [x] All requirements have `sources[]` (12/12)
- [x] All P0/P1 have `acceptance[]`
