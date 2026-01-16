---
status: done
owner: architect
layer: architecture
type: api
parent: docs/L2/notes-store/requirements.md
caf_version: v0.6.5
---

# Architecture: Public API (notes-cli)

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: api
parent: "docs/L2/notes-store/requirements.md"
items:
  - id: ARCH-API-001
    statement: "提供两个稳定的模块 API：add_note(store_path, content) 与 list_notes(store_path)。"
    sources:
      - id: "REQ-L2-NS-001"
        path: "docs/L2/notes-store/requirements.md#REQ-L2-NS-001"
      - id: "REQ-L2-NS-002"
        path: "docs/L2/notes-store/requirements.md#REQ-L2-NS-002"
    rationale: "以纯函数 API 便于单元测试与复用；CLI/UI 可在其上构建。"
```

## — END REGISTRY —

