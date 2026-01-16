---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "prdrec"
---

# L1 Requirements: 产品推荐对比 (PRDREC)

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.2"
layer: L1
feature: "prdrec"

requirements:
  - id: REQ-L1-PRDREC-001
    priority: P0
    statement: "提供产品推荐能力：输出 Top-N SKU，包含推荐理由。"
    sources:
      - id: "REQ-L0-API-002"
        path: "docs/L0/requirements.md#REQ-L0-API-002"
    acceptance:
      - "返回 Top-3 推荐"
      - "包含推荐理由"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]

  - id: REQ-L1-PRDREC-002
    priority: P0
    statement: "提供产品比较能力：2–4 个 SKU 结构化对比。"
    sources:
      - id: "REQ-L0-API-003"
        path: "docs/L0/requirements.md#REQ-L0-API-003"
    acceptance:
      - "可对比 2-4 个产品"
      - "输出表格/卡片"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]

tbds: []
exclusions: []
```

## — END REGISTRY —
