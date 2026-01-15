---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
source_checksum: "{checksum}"
profile: "{profile}"
component: "{component_name}"           # v0.5.2 新增：组件名
language_profile: "{python|typescript}" # v0.5.2 新增：语言配置
decomposition_strategy: "full"          # v0.5.2 新增：分解策略
---

# L1 Requirements: {component_name}

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text | Generated | 🔒 Readonly |
> | Appendices | Generated | 🔒 Readonly |
>
> **组件信息** (v0.5.2):
> - 组件名: `{component_name}`
> - 语言配置: `{language_profile}`
> - 分解策略: `{decomposition_strategy}`

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# L1 Requirements Registry - Component Level (v0.5.2)
# Schema: v1.0 | Template: v2.0 | CAF: v0.5.2
# =============================================================================

schema_version: "v0.5.2"
layer: L1
parent: "docs/L0/requirements.md"
source_checksum: "{checksum}"
profile: "{profile}"
component: "{component_name}"
language_profile: "{language_profile}"

# -----------------------------------------------------------------------------
# Requirements (Component-level decomposition of L0)
# -----------------------------------------------------------------------------
requirements:
  # --- 模块 1 ---
  - id: REQ-L1-{COMP}-001
    priority: P0
    statement: "Component 应当提供 XXX 功能..."
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
  - id: REQ-L1-{COMP}-002
    priority: P1
    statement: "Component 应当提供 YYY 功能..."
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
# Interfaces (L1 defines component interfaces)
# -----------------------------------------------------------------------------
interfaces:
  - name: "{interface_name}"
    type: API  # API | Event | Data | Internal
    description: "接口描述"
    sources:
      - path: "docs/L0/requirements.md#REQ-L0-0xx"
    contract:
      input: "{input_schema}"
      output: "{output_schema}"
    consumers: ["{other_component}"]
    providers: ["{component_name}"]

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

## 3. 接口定义

详见附录 D（接口表）。

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

### 附录 D：接口表

| Name | Type | Description | Consumers | Providers |
|------|------|-------------|-----------|-----------|
| {interface_name} | API | ... | {other} | {component} |

---

## 门禁检查

- [ ] Registry 所有条目有非空 `sources[]`
- [ ] L0 需求 100% 覆盖
- [ ] 接口定义完整
- [ ] 无交叉引用错位
