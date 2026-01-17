---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "usrmgmt"
caf_version: v0.6.5
---

# L1 Requirements: 用户管理 (USRMGMT)

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L1
parent: "docs/L0/requirements.md"
feature: "usrmgmt"

requirements:
  - id: REQ-L1-USRMGMT-001
    priority: P1
    statement: "提供邮箱验证码登录能力，登录后解锁寻价与人工客服功能。"
    sources:
      - id: "REQ-L0-SHARED-001"
        path: "docs/L0/requirements.md#REQ-L0-SHARED-001"
    acceptance:
      - "邮箱可收到验证码"
      - "验证通过后登录"
      - "登录后解锁功能"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-010]

tbds: []
exclusions: []
```

## — END REGISTRY —

---

## Summary

| Metric | Value |
|--------|-------|
| Total requirements | 1 |
| P0 | 0 |
| P1 | 1 |
| P2 | 0 |
| TBDs | 0 |
| Exclusions | 0 |

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L1-USRMGMT-001 | P1 | 提供邮箱验证码登录能力，登录后解锁寻价与人工客服功能。 | REQ-L0-SHARED-001 | 3 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L1-USRMGMT-001 | REQ-L0-SHARED-001 | docs/L0/requirements.md#REQ-L0-SHARED-001 |

## Gate Check

- [x] All requirements have `sources[]` (1/1)
- [x] All P0/P1 have `acceptance[]`
