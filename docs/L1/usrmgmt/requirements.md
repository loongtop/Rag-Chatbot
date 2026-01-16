---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
profile: "python"
feature: "usrmgmt"
---

# L1 Requirements: 用户管理 (USRMGMT)

---

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.0"
layer: L1
parent: "docs/L0/requirements.md"
profile: "python"
feature: "usrmgmt"

requirements:
  - id: REQ-L1-USRMGMT-001
    priority: P1
    statement: "提供邮箱验证码登录能力：Widget 支持邮箱验证码登录/验证；登录后可将对话与浏览行为关联到用户；登录后解锁寻价与联系人工客服功能。"
    sources:
      - id: "REQ-L0-SHARED-001"
        path: "docs/L0/requirements.md#REQ-L0-SHARED-001"
    acceptance:
      - "用户输入邮箱可收到验证码"
      - "验证通过后状态为已登录"
      - "未登录用户点击寻价/人工客服提示登录"
      - "登录后行为可关联到用户"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-010]
    derived: false

tbds:
  - id: TBD-L1-USRMGMT-001
    question: "邮箱验证码方案与防刷机制"
    sources:
      - id: "TBD-L0-010"
        path: "docs/L0/requirements.md#TBD-L0-010"
    impact: M
    owner: "Security"
    target_layer: L2
    status: open
    related_reqs: [REQ-L1-USRMGMT-001]

exclusions: []
```

## — END REGISTRY —

---

## 1. Feature 概述

### 1.1 定位

**用户管理** 提供轻量级的邮箱验证码登录能力，用于关联用户行为和解锁高级功能。

> 注意：本系统不做完整认证/账号体系（如 OAuth/SSO/MFA），仅提供邮箱验证码作为最小能力。

### 1.2 核心能力

| 能力 | 描述 | Priority |
|------|------|----------|
| 邮箱登录 | 验证码登录/验证 | P1 |
| 行为关联 | 登录后关联对话与浏览 | P1 |
| 功能解锁 | 登录后解锁寻价/人工客服 | P1 |

---

## 附录 A：溯源矩阵

| L0 Item | L1 Coverage | Status |
|---------|-------------|--------|
| REQ-L0-SHARED-001 | REQ-L1-USRMGMT-001 | ✅ |
