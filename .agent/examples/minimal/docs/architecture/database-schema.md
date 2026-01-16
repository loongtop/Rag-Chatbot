---
status: done
owner: architect
layer: architecture
type: database
parent: docs/L2/notes-store/requirements.md
caf_version: v0.6.5
---

# Architecture: Data Model (notes-cli)

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: database
parent: "docs/L2/notes-store/requirements.md"
items:
  - id: ARCH-DB-001
    statement: "笔记以 JSON 数组形式存储，每条记录包含 id/content/created_at 字段。"
    sources:
      - id: "REQ-L2-NS-001"
        path: "docs/L2/notes-store/requirements.md#REQ-L2-NS-001"
    rationale: "结构简单、易于序列化与测试；无需引入数据库。"
```

## — END REGISTRY —

