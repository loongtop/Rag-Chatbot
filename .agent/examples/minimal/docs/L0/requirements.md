---
status: done
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "0000000000000000000000000000000000000000000000000000000000000000"
profile: "python-web-api"
caf_version: v0.6.5
---

# L0 Requirements: notes-cli

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L0
parent: "charter.yaml"
source_checksum: "0000000000000000000000000000000000000000000000000000000000000000"
profile: "python-web-api"

requirements:
  - id: REQ-L0-APP-001
    priority: P0
    statement: "系统应当支持新增笔记并将数据持久化到本地 JSON 文件。"
    sources:
      - id: "SCOPE-MH-001"
        path: "charter.yaml#scope.must_have[0]"
    acceptance:
      - "新增笔记后文件中出现对应记录（包含 created_at）"
      - "重复运行程序后仍可读取已保存笔记"
    status: done
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-APP-002
    priority: P0
    statement: "系统应当支持列出全部笔记，按 created_at 倒序输出。"
    sources:
      - id: "SCOPE-MH-002"
        path: "charter.yaml#scope.must_have[1]"
    acceptance:
      - "列表输出按 created_at 倒序"
    status: done
    section: functional
    tbd_refs: []
    derived: false

tbds: []
exclusions:
  - source:
      id: "SCOPE-OOS-001"
      path: "charter.yaml#scope.out_of_scope[0]"
    reason: "最小示例聚焦本地持久化，不包含云同步与登录体系。"
    category: out_of_scope
    approved_by: "Example"
```

## — END REGISTRY —

## Summary

- Layer: L0
- Project: notes-cli

## Traceability

L0 条目以 `sources[]` 追溯到 `charter.yaml` 的稳定 ID 前缀（如 `SCOPE-MH-001`）。

## Gate Check

- [x] P0 需求包含 `sources[]`
- [x] P0 需求包含 `acceptance[]`
- [x] 关键 out_of_scope 有显式 exclusion

