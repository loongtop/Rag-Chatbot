---
status: done
owner: architect
layer: L2
type: interfaces
parent: docs/L2/api-server/requirements.md
caf_version: v0.6.5
---

# L2 Interfaces: rag-web-demo

## — BEGIN REGISTRY —

```interfaces-registry
schema_version: "v0.6.5"
layer: L2
parent: "docs/L2/api-server/requirements.md"

interfaces:
  - id: IFC-CHAT-API
    name: "Chat API"
    type: API
    description: "Widget 与 api-server 之间的 RAG 问答接口契约"
    providers: ["api-server"]
    consumers: ["chat-widget"]
    sources:
      - id: "REQ-L2-API-001"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-001"
    contract:
      transport: "HTTP"
      input: |
        { "message": "string", "session_id": "string?" }
      output: |
        { "answer": "string", "references": "Reference[]" }
      errors:
        - code: "ERR_BAD_REQUEST"
          description: "请求参数不合法"
    version: "v1"
    status: done

tbds: []
exclusions: []
```

## — END REGISTRY —

