---
status: done
owner: architect
layer: architecture
type: api
parent: docs/L2/api-server/requirements.md
caf_version: v0.6.5
---

# Architecture: API Spec (rag-web-demo)

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: api
parent: "docs/L2/api-server/requirements.md"
items:
  - id: ARCH-API-001
    statement: "公开接口 /api/chat 的 request/response 必须与 IFC-CHAT-API 契约一致。"
    sources:
      - id: "IFC-CHAT-API"
        path: "docs/L2/interfaces.md#IFC-CHAT-API"
    rationale: "接口契约作为单一事实源，避免实现与 Widget/前端对接偏差。"
```

## — END REGISTRY —

