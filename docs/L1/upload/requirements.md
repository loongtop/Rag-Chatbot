---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "upload"
caf_version: v0.6.5
---

# L1 Requirements: 文件上传 (UPLOAD)

> v0.6.2 新增：基于 `classify_ui_requirement()` 判定，WGT-004 有格式/大小/解析逻辑，提升为独立 Feature

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L1
feature: "upload"

requirements:
  - id: REQ-L1-UPLOAD-001
    priority: P1
    statement: "提供文件/图片上传能力：支持常见格式，内容提取用于问答。"
    sources:
      - id: "REQ-L0-WGT-004"
        path: "docs/L0/requirements.md#REQ-L0-WGT-004"
    acceptance:
      - "支持 PDF/Word/图片上传"
      - "可解析内容参与 RAG"
      - "类型/大小有限制"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-008]

tbds:
  - id: TBD-L1-UPLOAD-001
    question: "文件/图片上传支持格式与大小限制"
    sources:
      - id: "TBD-L0-008"
        path: "docs/L0/requirements.md#TBD-L0-008"
    impact: M
    status: open

exclusions: []
```

## — END REGISTRY —

---

## 说明

此 Feature 从 WGT-004 提升，原因：

| 关键词匹配 | 结果 |
|------------|------|
| "上传" | ✅ 命中 business_keywords |
| "处理" | ✅ 命中 business_keywords |

根据 `.agent/config/split-rules.yaml` 的 `ui_classification.business_keywords`，"上传" 和 "处理" 关键词触发 `strategy: feature`。

---

## Summary

| Metric | Value |
|--------|-------|
| Total requirements | 1 |
| P0 | 0 |
| P1 | 1 |
| P2 | 0 |
| TBDs | 1 |
| Exclusions | 0 |

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L1-UPLOAD-001 | P1 | 提供文件/图片上传能力：支持常见格式，内容提取用于问答。 | REQ-L0-WGT-004 | 3 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L1-UPLOAD-001 | REQ-L0-WGT-004 | docs/L0/requirements.md#REQ-L0-WGT-004 |

## TBDs

| TBD ID | Question | Target Layer | Impact | Status |
|--------|----------|--------------|--------|--------|
| TBD-L1-UPLOAD-001 | 文件/图片上传支持格式与大小限制 |  | M | open |

## Gate Check

- [x] All requirements have `sources[]` (1/1)
- [x] All P0/P1 have `acceptance[]`
