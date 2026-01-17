---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "admgmt"
caf_version: v0.6.5
---

# L1 Requirements: 后台管理 (ADMGMT)

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L1
parent: "docs/L0/requirements.md"
feature: "admgmt"

requirements:
  - id: REQ-L1-ADMGMT-001
    priority: P0
    statement: "提供产品数据管理能力：JSON 加载/上传/替换/检索。"
    sources:
      - id: "REQ-L0-ADM-001"
        path: "docs/L0/requirements.md#REQ-L0-ADM-001"
    acceptance:
      - "可加载 JSON"
      - "可上传替换"
    status: draft
    section: functional

  - id: REQ-L1-ADMGMT-002
    priority: P0
    statement: "提供知识库管理能力：文档上传/向量化/索引状态。"
    sources:
      - id: "REQ-L0-ADM-002"
        path: "docs/L0/requirements.md#REQ-L0-ADM-002"
    acceptance:
      - "可上传文档"
      - "可查看索引状态"
    status: draft
    section: functional

  - id: REQ-L1-ADMGMT-003
    priority: P0
    statement: "提供后台管理 UI：产品/知识库/日志/客服/寻价管理。"
    sources:
      - id: "REQ-L0-ADM-003"
        path: "docs/L0/requirements.md#REQ-L0-ADM-003"
    acceptance:
      - "统一管理界面"
      - "包含所有功能模块"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-003, TBD-L0-012]

tbds: []
exclusions: []
```

## — END REGISTRY —

---

## Summary

| Metric | Value |
|--------|-------|
| Total requirements | 3 |
| P0 | 3 |
| P1 | 0 |
| P2 | 0 |
| TBDs | 0 |
| Exclusions | 0 |

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L1-ADMGMT-001 | P0 | 提供产品数据管理能力：JSON 加载/上传/替换/检索。 | REQ-L0-ADM-001 | 2 | draft |
| REQ-L1-ADMGMT-002 | P0 | 提供知识库管理能力：文档上传/向量化/索引状态。 | REQ-L0-ADM-002 | 2 | draft |
| REQ-L1-ADMGMT-003 | P0 | 提供后台管理 UI：产品/知识库/日志/客服/寻价管理。 | REQ-L0-ADM-003 | 2 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L1-ADMGMT-001 | REQ-L0-ADM-001 | docs/L0/requirements.md#REQ-L0-ADM-001 |
| REQ-L1-ADMGMT-002 | REQ-L0-ADM-002 | docs/L0/requirements.md#REQ-L0-ADM-002 |
| REQ-L1-ADMGMT-003 | REQ-L0-ADM-003 | docs/L0/requirements.md#REQ-L0-ADM-003 |

## Gate Check

- [x] All requirements have `sources[]` (3/3)
- [x] All P0/P1 have `acceptance[]`
