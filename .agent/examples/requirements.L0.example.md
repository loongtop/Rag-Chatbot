---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "9bf2a6cdf4c711958850ff063d4702fdb071581b3bcdbb57e88c43b5413cef97"
profile: "rag-web"
---

# L0 Requirements: rag-chatbot (v2 Example)

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text (§1-§5) | Generated | 🔒 Readonly |
> | Appendices (A/B/C) | Generated | 🔒 Readonly |
>
> All generated content derives from the Registry block. Use `/requirements-render L0` to regenerate.

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# Requirements Registry (Single Source of Truth)
# Schema: v1.0 | Template: v2.0 | CAF: v0.4.0
# =============================================================================

schema_version: "v0.4.0"
layer: L0
parent: "charter.yaml"
source_checksum: "9bf2a6cdf4c711958850ff063d4702fdb071581b3bcdbb57e88c43b5413cef97"
profile: "rag-web"

# -----------------------------------------------------------------------------
# Requirements (Minimal Example)
# -----------------------------------------------------------------------------
requirements:
  - id: REQ-L0-001
    priority: P0
    statement: "系统应当提供嵌入式产品知识库 RAG Chatbot，用于回答产品问题、提供推荐与对比。"
    sources:
      - id: "PROB-001"
        path: "charter.yaml#objective.problems[0]"
      - id: "GOAL-001"
        path: "charter.yaml#objective.business_goals[0]"
    acceptance:
      - "后端提供对话/RAG/推荐/对比接口"
      - "提供可用的 OpenAPI 文档"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-002
    priority: P0
    statement: "系统应当提供可嵌入现有产品网站的 Chatbot Widget，并提供最小集成示例。"
    sources:
      - id: "SCOPE-MH-001"
        path: "charter.yaml#scope.must_have[0]"
    acceptance:
      - "Widget 可在现有网站页面展示并发起对话"
      - "可配置挂载点与基础样式"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-101
    priority: P0
    statement: "端到端首次响应时间 p95 应当 <= 1.5s（包含 LLM；口径以服务端为准）。"
    sources:
      - id: "MET-PERF-001"
        path: "charter.yaml#metrics.performance[0]"
    acceptance:
      - "测试报告给出 p95 结果（服务端口径）"
    status: draft
    section: performance
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# TBDs (To Be Determined)
# -----------------------------------------------------------------------------
tbds:
  - id: TBD-L0-001
    question: "LLM Provider/Model 选择与成本上限分配"
    sources:
      - id: "TBD-001"
        path: "charter.yaml#open_questions[0]"
    impact: H
    owner: "Product Team"
    target_layer: L1
    status: open
    related_reqs:
      - REQ-L0-001

  - id: TBD-L0-002
    question: "降级策略定义：LLM/pgvector 不可用时的用户体验与返回格式"
    sources:
      - id: "TBD-002"
        path: "charter.yaml#open_questions[1]"
    impact: M
    owner: ""
    target_layer: L1
    status: open
    related_reqs: []

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

本文档定义了 rag-chatbot 的 L0（系统级）需求规格说明，是下游 L1/L2/L3 需求分解的唯一事实来源。

本文档的预期读者包括：项目发起人、产品经理、架构师、开发团队、测试团队。

_Source_: `charter.yaml#meta`  
_Covered by_: N/A (document metadata)

### 1.2 范围

本系统为"嵌入式产品知识库 RAG Chatbot"，支持产品推荐与对比功能，可集成到现有产品网站。

_Source_: `charter.yaml#scope.must_have`, `charter.yaml#scope.out_of_scope`  
_Covered by_: `REQ-L0-002`

### 1.3 定义与术语

| 术语 | 定义 |
|------|------|
| RAG | Retrieval-Augmented Generation，检索增强生成 |
| LLM | Large Language Model，大型语言模型 |
| SKU | Stock Keeping Unit，库存单位 |

### 1.4 参考文档

| 文档 | 版本/Checksum | 说明 |
|------|--------------|------|
| `charter.yaml` | `9bf2a6c...` | 项目任务书（已冻结） |
| `docs/L0/split-report.md` | - | Charter → L0 拆分报告 |

---

## 2. 总体描述

### 2.1 产品视角

本系统旨在解决销售人员难以快速回答客户复杂问题、潜在客户无法高效获取产品对比推荐、产品知识分散导致自助服务体验差的问题。

_Source_: `charter.yaml#objective.problems[0..2]`, `charter.yaml#objective.business_goals[0..2]`  
_Covered by_: `REQ-L0-001`

### 2.2 核心能力

系统核心能力包括：嵌入式 Widget、RAG 问答、产品推荐、产品对比、多语言支持。

_Source_: `charter.yaml#scope.must_have`  
_Covered by_: `REQ-L0-001`, `REQ-L0-002`

---

## 3. 具体需求

### 3.1 功能需求

详见附录 A 的 `section: functional` 条目。

_Source_: `charter.yaml#scope.must_have`  
_Covered by_: `REQ-L0-001`, `REQ-L0-002`

### 3.2 性能需求

详见附录 A 的 `section: performance` 条目。

_Source_: `charter.yaml#metrics.performance`  
_Covered by_: `REQ-L0-101`

---

## 附录

### 附录 A：需求表

| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| REQ-L0-001 | P0 | 系统应当提供嵌入式产品知识库 RAG Chatbot | PROB-001, GOAL-001 | 后端提供接口; OpenAPI 文档 | draft |
| REQ-L0-002 | P0 | 系统应当提供可嵌入的 Chatbot Widget | SCOPE-MH-001 | Widget 可展示; 可配置 | draft |
| REQ-L0-101 | P0 | 端到端响应时间 p95 <= 1.5s | MET-PERF-001 | 测试报告给出结果 | draft |

### 附录 B：溯源矩阵（Charter → L0）

| Charter Item | Covered By | Status | Notes |
|--------------|------------|--------|-------|
| `charter.yaml#objective.problems[0]` | REQ-L0-001 | ✅ | |
| `charter.yaml#objective.business_goals[0]` | REQ-L0-001 | ✅ | |
| `charter.yaml#scope.must_have[0]` | REQ-L0-002 | ✅ | |
| `charter.yaml#metrics.performance[0]` | REQ-L0-101 | ✅ | |
| `charter.yaml#open_questions[0]` | TBD-L0-001 | ✅ | |
| `charter.yaml#open_questions[1]` | TBD-L0-002 | ✅ | |
| `charter.yaml#traceability` | N/A | ✅ | process_config |
| `charter.yaml#freeze` | N/A | ✅ | process_config |

### 附录 C：TBD/待定项

| TBD-ID | Question | Sources | Impact | Owner | Target Layer | Status |
|--------|----------|---------|--------|-------|--------------|--------|
| TBD-L0-001 | LLM Provider/Model 选择 | TBD-001 | H | Product Team | L1 | open |
| TBD-L0-002 | 降级策略定义 | TBD-002 | M | - | L1 | open |

---

## 门禁检查

> 由 `/requirements-validate L0` 自动校验。

- [x] Registry 所有 `requirements[]` 有非空 `sources[]`
- [x] P0/P1 需求有非空 `acceptance[]`
- [x] Charter 关键条目已覆盖（REQ / TBD / Exclusion）
- [x] 无交叉引用错位
- [x] `derived: true` 的需求有 `rationale`

---

## 变更记录

| 版本 | 日期 | 作者 | 变更说明 |
|------|------|------|----------|
| v0.1 | 2026-01-12 | Architect Agent | v2 示例版本 |
