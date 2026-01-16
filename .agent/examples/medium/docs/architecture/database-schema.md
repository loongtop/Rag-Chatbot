---
status: done
owner: architect
layer: architecture
type: database
parent: docs/L2/api-server/requirements.md
caf_version: v0.6.5
---

# Architecture: Database Schema (rag-web-demo)

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: database
parent: "docs/L2/api-server/requirements.md"
items:
  - id: ARCH-DB-001
    statement: "向量与元数据存储采用 PostgreSQL + pgvector，便于统一事务与检索。"
    sources:
      - id: "REQ-L2-API-001"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-001"
    rationale: "RAG 需要向量检索能力；示例仅展示决策与溯源结构。"
```

## — END REGISTRY —

