---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
source_checksum: "{checksum}"
profile: "{profile}"
feature: "{feature_name}"              # v0.6.0：L1 按业务 Feature 分组
component: "{component_name}"          # legacy：若仍按组件拆分可填写
language_profile: "{python|typescript}" # 可选：语言配置
decomposition_strategy: "full"         # 可选：分解策略
---

# L1 Requirements: {feature_name}

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text | Generated | 🔒 Readonly |
> | Appendices | Generated | 🔒 Readonly |
>
> **组件信息** (v0.5.2):
> - 组件名: `{component_name}`（可选）
> - 语言配置: `{language_profile}`
> - 分解策略: `{decomposition_strategy}`
>
> v0.6.0 约定：L1 不产出接口契约；模块间契约统一在 `docs/L2/interfaces.md` 定义。

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# L1 Requirements Registry - Feature Level (v0.6.0)
# Schema: v1.0 | Template: v2.0 | CAF: v0.6.0
# =============================================================================

schema_version: "v0.6.0"
layer: L1
parent: "docs/L0/requirements.md"
source_checksum: "{checksum}"
profile: "{profile}"
feature: "{feature_name}"
language_profile: "{language_profile}"

# -----------------------------------------------------------------------------
# Requirements (Component-level decomposition of L0)
# -----------------------------------------------------------------------------
requirements:
  # --- 模块 1 ---
  - id: REQ-L1-{FEAT}-001
    priority: P0
    statement: "Feature 应当提供 XXX 功能..."
    sources:
      - id: "REQ-L0-{XXX}-001"
        path: "docs/L0/requirements.md#REQ-L0-{XXX}-001"
    acceptance:
      - "验收条件1"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  # --- 模块 2 ---
  - id: REQ-L1-{FEAT}-002
    priority: P1
    statement: "Feature 应当提供 YYY 功能..."
    sources:
      - id: "REQ-L0-{YYY}-001"
        path: "docs/L0/requirements.md#REQ-L0-{YYY}-001"
    acceptance:
      - "验收条件1"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# TBDs
# -----------------------------------------------------------------------------
tbds: []

# -----------------------------------------------------------------------------
# Exclusions
# -----------------------------------------------------------------------------
exclusions: []
```

## — END REGISTRY —

---

## 1. 组件概述

### 1.1 组件定位

**组件名**: `{component_name}`  
**语言配置**: `{language_profile}`  
**上游来源**: `docs/L0/requirements.md`

{组件在系统中的定位描述}

**所属 L0 需求**:
- REQ-L0-{XXX}-*（来源）
- REQ-L0-{YYY}-*（来源）

### 1.2 范围边界

**包含**:
- 功能模块 1
- 功能模块 2

**不包含**:
- 其他组件的功能（通过接口调用）

### 1.3 接口依赖

| 接口类型 | 提供/依赖 | 说明 |
|----------|----------|------|
| REST API | 提供 | 对外暴露的服务接口 |
| LLM Provider | 依赖 | 大模型调用 |
| pgvector | 依赖 | 向量检索 |

---

## 2. 功能需求

详见附录 A（需求表）。

---

## 3. 模块间接口契约（L2）

模块间 API/Event/Data 契约统一在 `docs/L2/interfaces.md` 定义；本 Feature 在 L2 分解时补齐相关条目。

---

## 4. 非功能需求

### 4.1 性能约束
- 继承自 L0-PERF-*

### 4.2 安全约束
- 继承自 L0-SEC-*

---

## 附录

### 附录 A：需求表

| REQ-ID | Priority | Statement | Sources | Status |
|--------|----------|-----------|---------|--------|
| REQ-L1-{COMP}-001 | P0 | ... | REQ-L0-* | draft |
| REQ-L1-{COMP}-002 | P1 | ... | REQ-L0-* | draft |

### 附录 B：溯源矩阵（L0 → L1）

| L0 Item | Covered By | Status |
|---------|------------|--------|
| REQ-L0-{XXX}-001 | REQ-L1-{COMP}-001 | ✅ |
| REQ-L0-{YYY}-001 | REQ-L1-{COMP}-002 | ✅ |

### 附录 C：TBD/待定项

无

---

## 门禁检查

- [ ] Registry 所有条目有非空 `sources[]`
- [ ] L0 需求 100% 覆盖
- [ ] 不在 L1 引入模块间接口契约（接口统一在 L2/interfaces.md）
- [ ] 无交叉引用错位
