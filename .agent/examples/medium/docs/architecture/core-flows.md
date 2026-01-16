---
status: done
owner: architect
layer: architecture
type: flows
parent: docs/L2/api-server/requirements.md
caf_version: v0.6.5
---

# Architecture: Core Flows (rag-web-demo)

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: flows
parent: "docs/L2/api-server/requirements.md"
items:
  - id: ARCH-FL-001
    statement: "RAG 问答流程：query → retrieve(top_k) → (optional rerank) → generate(answer+refs)。"
    sources:
      - id: "REQ-L2-API-001"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-001"
    rationale: "明确关键链路有助于 leaf Spec 拆分与测试点设计。"
```

## — END REGISTRY —

