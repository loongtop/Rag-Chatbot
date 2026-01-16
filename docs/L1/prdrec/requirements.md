---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "prdrec"
caf_version: v0.6.5
---

# L1 Requirements: 产品推荐对比 (PRDREC)

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
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

---

## Summary

| Metric | Value |
|--------|-------|
| Total requirements | 2 |
| P0 | 2 |
| P1 | 0 |
| P2 | 0 |
| TBDs | 0 |
| Exclusions | 0 |

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L1-PRDREC-001 | P0 | 提供产品推荐能力：输出 Top-N SKU，包含推荐理由。 | REQ-L0-API-002 | 2 | draft |
| REQ-L1-PRDREC-002 | P0 | 提供产品比较能力：2–4 个 SKU 结构化对比。 | REQ-L0-API-003 | 2 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L1-PRDREC-001 | REQ-L0-API-002 | docs/L0/requirements.md#REQ-L0-API-002 |
| REQ-L1-PRDREC-002 | REQ-L0-API-003 | docs/L0/requirements.md#REQ-L0-API-003 |

## Gate Check

- [x] All requirements have `sources[]` (2/2)
- [x] All P0/P1 have `acceptance[]`
