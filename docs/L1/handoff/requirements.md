---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "handoff"
---

# L1 Requirements: 人机转接 (HANDOFF)

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.2"
layer: L1
feature: "handoff"

requirements:
  - id: REQ-L1-HANDOFF-001
    priority: P1
    statement: "提供人工/AI 切换能力：默认 AI，选择人工时转接后台队列。"
    sources:
      - id: "REQ-L0-API-007"
        path: "docs/L0/requirements.md#REQ-L0-API-007"
    acceptance:
      - "提供切换按钮"
      - "人工时进入队列"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-011]

tbds: []
exclusions: []
```

## — END REGISTRY —
