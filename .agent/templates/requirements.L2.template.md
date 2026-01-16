---
status: draft
owner: architect
layer: L2
parent: docs/L1/{feature}/requirements.md
source_checksum: "{checksum}"
profile: "{profile}"
feature: "{feature_name}"
module: "{module_name}"
---

# L2 Requirements: {module_name}

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text | Generated | 🔒 Readonly |
> | Appendices | Generated | 🔒 Readonly |

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# L2 Requirements Registry - Module Level
# Schema: v1.0 | Template: v2.0 | CAF: v0.6.5
# =============================================================================

schema_version: "v0.6.5"
layer: L2
parent: "docs/L1/{feature}/requirements.md"
source_checksum: "{checksum}"
profile: "{profile}"

# -----------------------------------------------------------------------------
# Requirements (Module-level decomposition of L1)
# -----------------------------------------------------------------------------
requirements:
  - id: REQ-L2-001
    priority: P0
    statement: "模块应当..."
    sources:
      - id: "REQ-L1-001"
        path: "docs/L1/{feature}/requirements.md#REQ-L1-001"
    acceptance:
      - "验收条件1"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# TBDs
# -----------------------------------------------------------------------------
tbds:
  - id: TBD-L2-001
    question: "待定问题"
    sources:
      - path: "docs/L1/{feature}/requirements.md#TBD-L1-001"
    impact: L
    owner: ""
    target_layer: SPEC
    status: open
    related_reqs:
      - REQ-L2-001

# -----------------------------------------------------------------------------
# Exclusions
# -----------------------------------------------------------------------------
exclusions: []
```

## — END REGISTRY —

---

<!-- GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY -->

## 1. 模块概述

### 1.1 模块职责

{模块在 Feature 中的职责 - 从 Registry 自动生成}

_Source_: `docs/L1/{feature}/requirements.md#REQ-L1-0xx`  
_Covered by_: `REQ-L2-001`

### 1.2 依赖关系

{模块依赖 - 可在本节描述，并引用 docs/L2/interfaces.md 中的接口契约条目}

---

## 2. 功能需求

{模块功能需求叙述}

---

## 3. 模块间接口契约（引用）

本模块与其它模块的交互契约统一在 `docs/L2/interfaces.md` 定义：
- 本模块提供的接口：{IFC-...}
- 本模块消费的接口：{IFC-...}

> 规则：任何跨模块调用/API/Event/Data 共享都必须在 `docs/L2/interfaces.md` 中有条目，并带可追溯 Source。

---

## 4. 数据模型

{数据结构定义}

---

## 附录

### 附录 A：需求表

| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| {从 Registry 渲染} | | | | | |

### 附录 B：溯源矩阵（L1 → L2）

| L1 Item | Covered By | Status | Notes |
|---------|------------|--------|-------|
| {从 Registry 渲染} | | | |

### 附录 C：TBD/待定项

| TBD-ID | Question | Sources | Impact | Owner | Target | Status |
|--------|----------|---------|--------|-------|--------|--------|
| {从 Registry 渲染} | | | | | | |

### 附录 D：接口引用表（L2/interfaces.md）

| Interface ID | Role (provide/consume) | Notes |
|--------------|-------------------------|-------|
| {IFC-...} | provide | |
| {IFC-...} | consume | |

---

## 门禁检查

- [ ] Registry 所有条目有非空 `sources[]`
- [ ] L1 需求 100% 覆盖
- [ ] 相关模块间交互已在 `docs/L2/interfaces.md` 定义并可追溯
- [ ] 无交叉引用错位
