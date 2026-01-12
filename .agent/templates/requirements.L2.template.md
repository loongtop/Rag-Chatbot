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
# Schema: v1.0 | Template: v2.0 | CAF: v0.4.0
# =============================================================================

schema_version: "v1.0"
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
# Interfaces (Module-level interface refinement)
# -----------------------------------------------------------------------------
interfaces:
  - name: "{interface_name}"
    type: API  # API | Event | Data | Internal
    description: "模块接口描述（至少10个字符）"
    sources:
      - path: "docs/L1/{feature}/requirements.md#interface_name"
    contract:
      input: |
        {
          "field": "type"
        }
      output: |
        {
          "field": "type"
        }
      errors:
        - code: "ERR_001"
          description: "错误描述"
    consumers:
      - "{consumer_module}"
    providers:
      - "{provider_module}"

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
    target_layer: L3
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

{模块依赖 - 从 Registry interfaces[] 自动生成}

---

## 2. 功能需求

{模块功能需求叙述}

---

## 3. 接口详细设计

{接口详细定义 - 从 Registry interfaces[] 自动生成}

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

### 附录 D：接口表

| Name | Type | Input | Output | Errors | Consumers | Providers |
|------|------|-------|--------|--------|-----------|-----------|
| {从 Registry 渲染} | | | | | | |

---

## 门禁检查

- [ ] Registry 所有条目有非空 `sources[]`
- [ ] L1 需求 100% 覆盖
- [ ] 接口 contract 完整（含 errors）
- [ ] 无交叉引用错位
