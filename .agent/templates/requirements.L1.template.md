---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
source_checksum: "{checksum}"
profile: "{profile}"
feature: "{feature_name}"
---

# L1 Requirements: {feature_name}

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
# L1 Requirements Registry - Feature Level
# Schema: v1.0 | Template: v2.0 | CAF: v0.4.0
# =============================================================================

schema_version: "v1.0"
layer: L1
parent: "docs/L0/requirements.md"
source_checksum: "{checksum}"
profile: "{profile}"

# -----------------------------------------------------------------------------
# Requirements (Feature-level decomposition of L0)
# -----------------------------------------------------------------------------
requirements:
  - id: REQ-L1-001
    priority: P0
    statement: "Feature 应当..."
    sources:
      - id: "REQ-L0-001"
        path: "docs/L0/requirements.md#REQ-L0-001"
    acceptance:
      - "验收条件1"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# Interfaces (L1 introduces interface definitions)
# -----------------------------------------------------------------------------
interfaces:
  - name: "{interface_name}"
    type: API  # API | Event | Data | Internal
    description: "接口描述（至少10个字符）"
    sources:
      - path: "docs/L0/requirements.md#REQ-L0-0xx"
    contract:
      input: "{input_schema}"
      output: "{output_schema}"
    consumers:
      - "{module_name}"
    providers:
      - "{module_name}"

# -----------------------------------------------------------------------------
# TBDs
# -----------------------------------------------------------------------------
tbds:
  - id: TBD-L1-001
    question: "待定问题"
    sources:
      - path: "docs/L0/requirements.md#TBD-L0-001"
    impact: M
    owner: ""
    target_layer: L2
    status: open
    related_reqs:
      - REQ-L1-001

# -----------------------------------------------------------------------------
# Exclusions
# -----------------------------------------------------------------------------
exclusions: []
```

## — END REGISTRY —

---

<!-- GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY -->

## 1. Feature 概述

### 1.1 功能定位

{Feature 在系统中的定位 - 从 Registry 自动生成}

_Source_: `docs/L0/requirements.md#REQ-L0-0xx`  
_Covered by_: `REQ-L1-001`

### 1.2 范围边界

{Feature 的范围边界 - 从 Registry 自动生成}

---

## 2. 功能需求

{Feature 功能需求叙述}

详见附录 A。

---

## 3. 接口定义

{接口概述 - 从 Registry interfaces[] 自动生成}

详见附录 D（接口表）。

---

## 4. 非功能需求

### 4.1 性能
{性能约束}

### 4.2 安全
{安全约束}

---

## 附录

### 附录 A：需求表

| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| {从 Registry 渲染} | | | | | |

### 附录 B：溯源矩阵（L0 → L1）

| L0 Item | Covered By | Status | Notes |
|---------|------------|--------|-------|
| {从 Registry 渲染} | | | |

### 附录 C：TBD/待定项

| TBD-ID | Question | Sources | Impact | Owner | Target | Status |
|--------|----------|---------|--------|-------|--------|--------|
| {从 Registry 渲染} | | | | | | |

### 附录 D：接口表

| Name | Type | Description | Input | Output | Consumers | Providers |
|------|------|-------------|-------|--------|-----------|-----------|
| {从 Registry 渲染} | | | | | | |

---

## 门禁检查

- [ ] Registry 所有条目有非空 `sources[]`
- [ ] L0 需求 100% 覆盖（REQ / TBD / Exclusion）
- [ ] 接口定义完整（有 contract）
- [ ] 无交叉引用错位
