---
id: "SPEC-018"
status: draft
owner: spec
leaf: false
parent: "docs/L2/admin-dashboard/requirements.md"
source_requirements:
  - "REQ-L2-ADM-001"
  - "REQ-L2-ADM-002"
  - "REQ-L2-ADM-003"
  - "REQ-L2-ADM-004"
interfaces:
  - "IFC-ADMIN-API"
depends_on: []
profile: "typescript"
---

# Spec: Admin Dashboard Overview

## 0. Summary

- Goal: 将 Admin Dashboard 的 L2 需求拆解为可落地 leaf Specs（布局、产品管理、知识库管理、客服工作台）。
- Non-goals: 与现有企业 SSO/权限系统深度集成（TBD）。
- Leaf: `false`

## 1. Scope

### In Scope
- React Admin App：统一布局 + 侧边栏导航 + 登录/鉴权入口。
- 功能模块：Products、Knowledge Base、Handoff Console、Logs（最小可用）。

### Out of Scope
- 复杂权限矩阵（RBAC/ABAC）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-ADM-003 | SPEC-019 | app shell + auth entry |
| REQ-L2-ADM-001 | SPEC-020 | products management |
| REQ-L2-ADM-002 | SPEC-021 | docs/index/logs |
| REQ-L2-ADM-004 | SPEC-022 | handoff console |

## 3. Design / Decisions

### Proposed Approach
- SPA：`/products`、`/knowledge-base`、`/handoff`、`/logs`。
- `AdminApiClient` 统一封装 `IFC-ADMIN-API` 调用并携带鉴权信息。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | consume | admin endpoints |

## 5. Implementation Plan

1. 完成 SPEC-019（统一骨架与鉴权入口）。
2. 完成 SPEC-020 与 SPEC-021（核心管理闭环）。
3. 完成 SPEC-022（客服接入与完成闭环）。

## 6. Acceptance Tests

- 手工冒烟：登录后可导航到各页面并调用对应后端接口（leaf Specs 各自定义详细用例）。

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-003 | 后台鉴权方式（Basic Auth/SSO） | M | Product Owner | open |

## 8. Leaf Checklist

N/A（leaf=false）

