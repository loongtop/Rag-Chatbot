---
status: done
owner: architect
layer: L1
parent: docs/L0/requirements.md
profile: "rag-web"
caf_version: v0.6.5
---

# L1 Requirements: RAG QA

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L1
parent: "docs/L0/requirements.md"
profile: "rag-web"

requirements:
  - id: REQ-L1-RAGQA-001
    priority: P0
    statement: "RAG QA 功能应当支持基于检索结果生成回答，并返回引用列表。"
    sources:
      - id: "REQ-L0-API-001"
        path: "docs/L0/requirements.md#REQ-L0-API-001"
    acceptance:
      - "至少包含引用的 doc_id + snippet"
    status: done
    section: functional
    tbd_refs: []
    derived: false

tbds: []
exclusions: []
```

## — END REGISTRY —

