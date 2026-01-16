---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
profile: "python"
feature: "prdrec"
---

# L1 Requirements: 产品推荐对比 (PRDREC)

---

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.0"
layer: L1
parent: "docs/L0/requirements.md"
profile: "python"
feature: "prdrec"

requirements:
  - id: REQ-L1-PRDREC-001
    priority: P0
    statement: "提供产品推荐能力：基于用户需求输出 Top-N（默认 3）SKU，包含推荐理由与依据来源。"
    sources:
      - id: "REQ-L0-API-002"
        path: "docs/L0/requirements.md#REQ-L0-API-002"
    acceptance:
      - "针对用户需求返回 Top-3 推荐产品"
      - "每个推荐包含推荐理由"
      - "推荐依据可追溯"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]
    derived: false

  - id: REQ-L1-PRDREC-002
    priority: P0
    statement: "提供产品比较能力：支持 2–4 个 SKU，输出结构化对比（表格/卡片），字段可配置。"
    sources:
      - id: "REQ-L0-API-003"
        path: "docs/L0/requirements.md#REQ-L0-API-003"
    acceptance:
      - "可对比 2-4 个产品"
      - "输出结构化表格/卡片形式"
      - "对比字段可配置"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]
    derived: false

tbds:
  - id: TBD-L1-PRDREC-001
    question: "推荐/比较的字段配置来源"
    sources:
      - id: "TBD-L0-005"
        path: "docs/L0/requirements.md#TBD-L0-005"
    impact: L
    owner: "Product Owner"
    target_layer: L2
    status: open
    related_reqs: [REQ-L1-PRDREC-001, REQ-L1-PRDREC-002]

exclusions: []
```

## — END REGISTRY —

---

## 1. Feature 概述

### 1.1 定位

**产品推荐对比** 提供基于用户需求的智能产品推荐和多产品对比功能。

### 1.2 核心能力

| 能力 | 描述 | Priority |
|------|------|----------|
| 产品推荐 | 基于需求推荐 Top-N 产品 | P0 |
| 产品比较 | 结构化对比 2-4 个产品 | P0 |

---

## 附录 A：溯源矩阵

| L0 Item | L1 Coverage | Status |
|---------|-------------|--------|
| REQ-L0-API-002 | REQ-L1-PRDREC-001 | ✅ |
| REQ-L0-API-003 | REQ-L1-PRDREC-002 | ✅ |
