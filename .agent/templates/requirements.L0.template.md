---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "{checksum}"
profile: "{profile}"
---

# L0 Requirements: {system_name}

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text (§1-§5) | Generated | 🔒 Readonly |
> | Appendices (A/B/C) | Generated | 🔒 Readonly |
>
> All generated content derives from the Registry block. Use `/requirements-render` to regenerate.

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# Requirements Registry (Single Source of Truth)
# Schema: v1.0 | Template: v2.0 | CAF: v0.5.0
# =============================================================================

schema_version: "v0.5.0"
layer: L0
parent: "charter.yaml"
source_checksum: "{checksum}"
profile: "{profile}"

# -----------------------------------------------------------------------------
# Requirements
# -----------------------------------------------------------------------------
requirements:
  - id: REQ-L0-001
    priority: P0
    statement: "系统应当..."
    sources:
      - id: "SCOPE-MH-001"
        path: "charter.yaml#scope.must_have[0]"
    acceptance:
      - "验收条件1"
      - "验收条件2"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# TBDs (To Be Determined)
# -----------------------------------------------------------------------------
tbds:
  - id: TBD-L0-001
    question: "待定问题描述"
    sources:
      - id: "TBD-001"
        path: "charter.yaml#open_questions[0]"
    impact: H
    owner: ""
    target_layer: L1
    status: open
    related_reqs:
      - REQ-L0-001

# -----------------------------------------------------------------------------
# Exclusions (N/A with reason)
# -----------------------------------------------------------------------------
exclusions:
  - source:
      path: "charter.yaml#traceability"
    reason: "Process configuration, not a deliverable requirement"
    category: process_config
  - source:
      path: "charter.yaml#freeze"
    reason: "Freeze metadata, not a deliverable requirement"
    category: process_config
```

## — END REGISTRY —

---

<!-- =========================================================================
     GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY
     Regenerate with: /requirements-render L0
     ========================================================================= -->

## 1. 引言

### 1.1 目的

本文档定义了 {system_name} 的 L0（系统级）需求规格说明，是下游 L1/L2/L3 需求分解的唯一事实来源。

本文档的预期读者包括：项目发起人、产品经理、架构师、开发团队、测试团队。

_Source_: `charter.yaml#meta`  
_Covered by_: N/A (document metadata)

### 1.2 范围

{系统边界定义 - 从 Registry 自动生成}

_Source_: `charter.yaml#scope.must_have`, `charter.yaml#scope.out_of_scope`  
_Covered by_: `REQ-L0-9xx` (Constraints)

### 1.3 定义与术语

| 术语 | 定义 |
|------|------|
| RAG | Retrieval-Augmented Generation，检索增强生成 |
| LLM | Large Language Model，大型语言模型 |
| SKU | Stock Keeping Unit，库存单位 |

### 1.4 参考文档

| 文档 | 版本/Checksum | 说明 |
|------|--------------|------|
| `charter.yaml` | `{checksum}` | 项目任务书（已冻结） |
| `docs/L0/split-report.md` | - | Charter → L0 拆分报告 |
| `.agent/docs/srs-template.md` | - | SRS 模板参考 |

### 1.5 文档概述

- §2：总体描述（产品视角、用户、环境、约束、风险）
- §3：具体需求（功能、性能、安全、可靠性、易用性）
- §4：输入/输出
- §5：质量门禁
- 附录A：需求表（从 Registry 渲染）
- 附录B：溯源矩阵（从 Registry 渲染）
- 附录C：TBD/待定项（从 Registry 渲染）

---

## 2. 总体描述

### 2.1 产品视角

{系统在整体架构中的定位 - 从 Registry 自动生成}

_Source_: `charter.yaml#objective.problems`, `charter.yaml#objective.business_goals`  
_Covered by_: `REQ-L0-001`

### 2.2 核心能力

{系统核心能力概述 - 从 Registry 自动生成}

_Source_: `charter.yaml#scope.must_have`  
_Covered by_: `REQ-L0-002` ~ `REQ-L0-0xx`

### 2.3 用户与特征

{用户角色与特征 - 从 Registry 自动生成}

_Source_: `charter.yaml#stakeholders.users`  
_Covered by_: `REQ-L0-0xx`

### 2.4 操作环境

{运行环境说明 - 从 Registry 自动生成}

_Source_: `charter.yaml#environments`, `charter.yaml#components`  
_Covered by_: `REQ-L0-9xx`

### 2.5 约束与依赖

{技术、资源、时间约束 - 从 Registry 自动生成}

_Source_: `charter.yaml#constraints`, `charter.yaml#dependencies`  
_Covered by_: `REQ-L0-9xx`

### 2.6 风险分析

{风险识别与应对 - 从 Registry 自动生成}

_Source_: `charter.yaml#risks`  
_Covered by_: `REQ-L0-2xx` (Security), `REQ-L0-3xx` (Reliability)

---

## 3. 具体需求

### 3.1 功能需求

{功能需求叙述概述 - 不重复 Registry 原文，提供上下文}

详见附录 A 的 `section: functional` 条目。

_Source_: `charter.yaml#scope.must_have`  
_Covered by_: `REQ-L0-001` ~ `REQ-L0-0xx`

### 3.2 性能需求

{性能需求叙述概述}

详见附录 A 的 `section: performance` 条目。

_Source_: `charter.yaml#metrics.performance`, `charter.yaml#quality_requirements.performance`  
_Covered by_: `REQ-L0-1xx`

### 3.3 安全需求

{安全需求叙述概述}

详见附录 A 的 `section: security` 条目。

_Source_: `charter.yaml#metrics.security`, `charter.yaml#quality_requirements.security`  
_Covered by_: `REQ-L0-2xx`

### 3.4 可靠性需求

{可靠性需求叙述概述}

详见附录 A 的 `section: reliability` 条目。

_Source_: `charter.yaml#metrics.stability`  
_Covered by_: `REQ-L0-3xx`

### 3.5 易用性需求

{易用性需求叙述概述}

详见附录 A 的 `section: usability` 条目。

_Source_: `charter.yaml#metrics.usability`  
_Covered by_: `REQ-L0-4xx`

---

## 4. 输入/输出

### 4.1 输入

{系统输入定义 - 从 Registry 自动生成}

### 4.2 输出

{系统输出定义 - 从 Registry 自动生成}

---

## 5. 质量门禁

{质量门禁要求 - 从 Registry 自动生成}

_Source_: `charter.yaml#quality_requirements`  
_Covered by_: `REQ-L0-9xx`

---

## 附录

### 附录 A：需求表

> 从 Registry `requirements[]` 自动渲染。

| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| {从 Registry 渲染} | | | | | |

### 附录 B：溯源矩阵（Charter → L0）

> 从 Registry `requirements[].sources[]` + `exclusions[]` 反向汇聚。
> 每条 Charter 关键条目必须出现在 REQ、TBD 或 Exclusion 中。

| Charter Item | Covered By | Status | Notes |
|--------------|------------|--------|-------|
| {从 Registry 渲染} | | | |

### 附录 C：TBD/待定项

> 从 Registry `tbds[]` 自动渲染。

| TBD-ID | Question | Sources | Impact | Owner | Target Layer | Status |
|--------|----------|---------|--------|-------|--------------|--------|
| {从 Registry 渲染} | | | | | | |

---

## 门禁检查

> 由 `/requirements-validate L0` 自动校验。

- [ ] Registry 所有 `requirements[]` 有非空 `sources[]`
- [ ] P0/P1 需求有非空 `acceptance[]`
- [ ] Charter 关键条目 100% 覆盖（REQ / TBD / Exclusion）
- [ ] 无交叉引用错位（`tbd_refs[]` 指向存在的 TBD）
- [ ] `derived: true` 的需求有 `rationale`

---

## 变更记录

| 版本 | 日期 | 作者 | 变更说明 |
|------|------|------|----------|
| v0.1 | {date} | {author} | 初始版本 |
