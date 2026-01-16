---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
profile: "python"
feature: "handoff"
---

# L1 Requirements: 人机转接 (HANDOFF)

---

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.0"
layer: L1
parent: "docs/L0/requirements.md"
profile: "python"
feature: "handoff"

requirements:
  - id: REQ-L1-HANDOFF-001
    priority: P1
    statement: "提供人工/AI 切换能力：用户可在输入界面选择人工或 AI，默认 AI；选择人工时将对话转接至后台人工队列处理。"
    sources:
      - id: "REQ-L0-API-007"
        path: "docs/L0/requirements.md#REQ-L0-API-007"
    acceptance:
      - "Widget 提供人工/AI 切换按钮"
      - "默认为 AI 模式"
      - "选择人工后，对话进入后台处理队列"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-011]
    derived: false

tbds:
  - id: TBD-L1-HANDOFF-001
    question: "人工客服转接方案细节"
    sources:
      - id: "TBD-L0-011"
        path: "docs/L0/requirements.md#TBD-L0-011"
    impact: M
    owner: "Product Owner"
    target_layer: L2
    status: open
    related_reqs: [REQ-L1-HANDOFF-001]

exclusions: []
```

## — END REGISTRY —

---

## 1. Feature 概述

### 1.1 定位

**人机转接** 提供从 AI 对话无缝切换到人工客服的能力。

### 1.2 核心能力

| 能力 | 描述 | Priority |
|------|------|----------|
| 模式切换 | AI/人工切换按钮 | P1 |
| 队列管理 | 对话转接至后台队列 | P1 |

---

## 附录 A：溯源矩阵

| L0 Item | L1 Coverage | Status |
|---------|-------------|--------|
| REQ-L0-API-007 | REQ-L1-HANDOFF-001 | ✅ |
