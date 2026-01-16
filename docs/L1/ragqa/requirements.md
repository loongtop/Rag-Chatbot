---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "ragqa"
---

# L1 Requirements: RAG 问答服务 (RAGQA)

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.2"
layer: L1
feature: "ragqa"

requirements:
  - id: REQ-L1-RAGQA-001
    priority: P0
    statement: "提供 RAG 问答核心能力，回答附带来源引用，无足够依据时拒答。"
    sources:
      - id: "REQ-L0-API-001"
        path: "docs/L0/requirements.md#REQ-L0-API-001"
    acceptance:
      - "回答包含引用来源标记"
      - "无关问题拒绝回答"
    status: draft
    section: functional

  - id: REQ-L1-RAGQA-002
    priority: P0
    statement: "支持上下文感知检索：接收 productId/skuId/url，优化检索排序。"
    sources:
      - id: "REQ-L0-API-004"
        path: "docs/L0/requirements.md#REQ-L0-API-004"
    acceptance:
      - "上下文影响检索结果排序"
    status: draft
    section: functional

  - id: REQ-L1-RAGQA-003
    priority: P0
    statement: "提供对话历史管理能力：多轮对话，记录 token 用量。"
    sources:
      - id: "REQ-L0-API-005"
        path: "docs/L0/requirements.md#REQ-L0-API-005"
    acceptance:
      - "支持多轮对话"
      - "记录 token 用量"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-004]

  - id: REQ-L1-RAGQA-004
    priority: P0
    statement: "LLM Provider 可配置切换：在线 API 与本地 Ollama。"
    sources:
      - id: "REQ-L0-API-006"
        path: "docs/L0/requirements.md#REQ-L0-API-006"
    acceptance:
      - "可切换 LLM Provider"
      - "两种模式均正常工作"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-001]

tbds: []
exclusions: []
```

## — END REGISTRY —
