---
status: done
owner: architect
layer: architecture
type: overview
parent: docs/L2/api-server/requirements.md
caf_version: v0.6.5
---

# Architecture Overview: rag-web-demo

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: overview
parent: "docs/L2/api-server/requirements.md"
items:
  - id: ARCH-OV-001
    statement: "将系统拆分为 api-server/chat-widget/admin-dashboard 三个模块，通过 L2 interfaces 定义契约。"
    sources:
      - id: "IFC-CHAT-API"
        path: "docs/L2/interfaces.md#IFC-CHAT-API"
    rationale: "通过契约降低跨模块耦合，便于并行开发与验证。"
```

## — END REGISTRY —

