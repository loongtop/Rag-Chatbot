---
id: "SPEC-019"
status: draft
owner: spec
leaf: true
parent: "SPEC-018"
source_requirements:
  - "REQ-L2-ADM-003"
interfaces:
  - "IFC-ADMIN-API"
depends_on: []
profile: "typescript"
---

# Spec: App Shell + Nav + Auth Entry

## 0. Summary

- Goal: 提供后台统一管理界面：统一布局框架、侧边栏导航、登录/鉴权入口。
- Non-goals: 完整权限体系（先提供最小鉴权形态）。
- Leaf: `true`

## 1. Scope

### In Scope
- Layout：Header + Sidebar + Content。
- Routes：Products / Knowledge Base / Handoff / Logs。
- Auth Entry：最小登录页（基于 token/Basic 占位），并在 API client 中统一注入。

### Out of Scope
- 细粒度权限控制 UI。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-ADM-003 | app shell + sidebar + auth entry | |

## 3. Design / Decisions

### Proposed Approach
- Token 存储：localStorage（v0.1）；后端鉴权方式由 TBD-L0-003 定。
- 未登录访问受保护路由：重定向到 `/login`。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | consume | 所有 admin endpoints |

## 5. Implementation Plan

1. 初始化 `apps/admin`（React + Router）。
2. Layout + Sidebar：定义导航项与路由。
3. Login Page：输入 token 或 Basic（占位），保存到 localStorage。
4. AdminApiClient：统一设置 Authorization header。
5. 单测（可选）：路由守卫与导航渲染。

### Files / Modules
- `apps/admin/src/App.tsx`
- `apps/admin/src/routes.tsx`
- `apps/admin/src/components/Layout.tsx`
- `apps/admin/src/auth/storage.ts`
- `apps/admin/src/api/client.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| nav | 登录后点击侧边栏 | 路由切换正确 | |
| guard | 未登录访问 /products | 重定向到 /login | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-003 | 后台鉴权最小方案 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

