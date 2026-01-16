---
status: done
owner: architect
layer: L2
parent: docs/L1/ragqa/requirements.md
profile: "rag-web"
caf_version: v0.6.5
---

# L2 Requirements: api-server

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L2
parent: "docs/L1/ragqa/requirements.md"
profile: "rag-web"

requirements:
  - id: REQ-L2-API-001
    priority: P0
    statement: "api-server 应当提供 POST /api/chat 接口用于 RAG 问答，并返回 references。"
    sources:
      - id: "REQ-L1-RAGQA-001"
        path: "docs/L1/ragqa/requirements.md#REQ-L1-RAGQA-001"
    acceptance:
      - "返回字段包含 answer + references[]"
    status: done
    section: functional
    tbd_refs: []
    derived: false

tbds: []
exclusions: []
```

## — END REGISTRY —

