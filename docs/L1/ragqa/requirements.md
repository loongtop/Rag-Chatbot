---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
source_checksum: "from-L0"
profile: "python"
feature: "ragqa"
---

# L1 Requirements: RAG 问答服务 (RAGQA)

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text | Generated | 🔒 Readonly |

---

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.0"
layer: L1
parent: "docs/L0/requirements.md"
profile: "python"
feature: "ragqa"

requirements:
  - id: REQ-L1-RAGQA-001
    priority: P0
    statement: "提供 RAG 问答核心能力，回答附带来源引用（文档/产品字段），无足够依据时优先澄清或拒答。"
    sources:
      - id: "REQ-L0-API-001"
        path: "docs/L0/requirements.md#REQ-L0-API-001"
    acceptance:
      - "回答包含明确的引用来源标记"
      - "引用来源可追溯到具体文档或产品字段"
      - "当问题与知识库无关时，模型能够拒绝回答或请求澄清"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L1-RAGQA-002
    priority: P0
    statement: "支持上下文感知检索：接收 Widget 传入的 productId/skuId/url，用于检索排序优化。"
    sources:
      - id: "REQ-L0-API-004"
        path: "docs/L0/requirements.md#REQ-L0-API-004"
    acceptance:
      - "后端可接收并解析上下文参数"
      - "上下文影响检索结果排序"
      - "当前产品信息优先展示"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L1-RAGQA-003
    priority: P0
    statement: "提供对话历史管理能力：支持多轮对话，记录引用、错误与 token 用量。"
    sources:
      - id: "REQ-L0-API-005"
        path: "docs/L0/requirements.md#REQ-L0-API-005"
    acceptance:
      - "支持多轮对话上下文"
      - "对话历史可查询"
      - "记录每次对话的 token 用量"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-004]
    derived: false

  - id: REQ-L1-RAGQA-004
    priority: P0
    statement: "LLM Provider 可配置切换：支持 OpenAI-Compatible API（ChatGPT/DeepSeek）与本地 Ollama 两种模式。"
    sources:
      - id: "REQ-L0-API-006"
        path: "docs/L0/requirements.md#REQ-L0-API-006"
    acceptance:
      - "可通过配置切换 LLM Provider"
      - "在线模式和本地模式均可正常工作"
      - "切换不影响核心功能"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-001, TBD-L0-002]
    derived: false

tbds:
  - id: TBD-L1-RAGQA-001
    question: "LLM Provider/Model 选择与成本分配"
    sources:
      - id: "TBD-L0-001"
        path: "docs/L0/requirements.md#TBD-L0-001"
    impact: H
    owner: "Product Owner"
    target_layer: L1
    status: open
    related_reqs: [REQ-L1-RAGQA-004]

  - id: TBD-L1-RAGQA-002
    question: "LLM/pgvector 不可用时的降级策略"
    sources:
      - id: "TBD-L0-002"
        path: "docs/L0/requirements.md#TBD-L0-002"
    impact: M
    owner: "Architect"
    target_layer: L2
    status: open
    related_reqs: [REQ-L1-RAGQA-004]

exclusions: []
```

## — END REGISTRY —

---

## 1. Feature 概述

### 1.1 定位

**RAG 问答服务** 是系统的核心能力，提供基于检索增强生成的智能问答功能。

**上游来源**: REQ-L0-API-001, API-004, API-005, API-006

### 1.2 核心能力

| 能力 | 描述 | Priority |
|------|------|----------|
| RAG 问答 | 基于知识库的问答，附带来源引用 | P0 |
| 上下文感知 | 利用页面上下文优化检索排序 | P0 |
| 对话历史 | 多轮对话与 token 记录 | P0 |
| LLM 切换 | Provider 可配置（在线/本地） | P0 |

### 1.3 范围边界

**包含**:
- RAG 检索与生成 Pipeline
- 上下文解析与排序优化
- 对话历史存储与查询
- LLM Provider 抽象与切换

**不包含**:
- Widget UI（chat-widget 组件）
- 产品推荐/比较逻辑（PRDREC Feature）
- 用户认证（USRMGMT Feature）

---

## 附录 A：需求表

| REQ-ID | Priority | Statement | Sources | Status |
|--------|----------|-----------|---------|--------|
| REQ-L1-RAGQA-001 | P0 | RAG 问答核心 | REQ-L0-API-001 | draft |
| REQ-L1-RAGQA-002 | P0 | 上下文感知 | REQ-L0-API-004 | draft |
| REQ-L1-RAGQA-003 | P0 | 对话历史 | REQ-L0-API-005 | draft |
| REQ-L1-RAGQA-004 | P0 | LLM 切换 | REQ-L0-API-006 | draft |

## 附录 B：溯源矩阵

| L0 Item | L1 Coverage | Status |
|---------|-------------|--------|
| REQ-L0-API-001 | REQ-L1-RAGQA-001 | ✅ |
| REQ-L0-API-004 | REQ-L1-RAGQA-002 | ✅ |
| REQ-L0-API-005 | REQ-L1-RAGQA-003 | ✅ |
| REQ-L0-API-006 | REQ-L1-RAGQA-004 | ✅ |
