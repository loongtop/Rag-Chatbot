---
status: done
owner: architect
layer: L2
parent: docs/L0/requirements.md
source_checksum: "0000000000000000000000000000000000000000000000000000000000000000"
profile: "python-web-api"
caf_version: v0.6.5
---

# L2 Requirements: notes-store

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L2
parent: "docs/L0/requirements.md"
source_checksum: "0000000000000000000000000000000000000000000000000000000000000000"
profile: "python-web-api"

requirements:
  - id: REQ-L2-NS-001
    priority: P0
    statement: "notes-store 应当将笔记持久化到本地 JSON 文件，并在文件不存在时自动初始化空集合。"
    sources:
      - id: "REQ-L0-APP-001"
        path: "docs/L0/requirements.md#REQ-L0-APP-001"
    acceptance:
      - "写入后文件存在且为合法 JSON"
      - "文件缺失时，读取返回空列表而不是抛异常"
    status: done
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L2-NS-002
    priority: P0
    statement: "notes-store 应当返回按 created_at 倒序排列的笔记列表。"
    sources:
      - id: "REQ-L0-APP-002"
        path: "docs/L0/requirements.md#REQ-L0-APP-002"
    acceptance:
      - "新增两条不同时间的笔记后，list 返回顺序为最近在前"
    status: done
    section: functional
    tbd_refs: []
    derived: false

tbds: []
exclusions: []
```

## — END REGISTRY —

## Summary

- Module: notes-store
- Layer: L2

## Traceability

`REQ-L2-NS-*` 仅承接 `REQ-L0-APP-*`，不新增无来源需求。

## Gate Check

- [x] P0 需求包含 `sources[]`
- [x] P0 需求包含 `acceptance[]`

