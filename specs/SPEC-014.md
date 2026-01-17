---
id: "SPEC-014"
status: draft
owner: spec
leaf: true
parent: "SPEC-011"
source_requirements:
  - "REQ-L2-WGT-002"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-012"
  - "SPEC-007"
profile: "typescript"
---

# Spec: Email Login UI

## 0. Summary

- Goal: Widget 提供邮箱验证码登录 UI：输入邮箱、验证码、显示登录状态。
- Non-goals: 密码登录、注册流程。
- Leaf: `true`

## 1. Scope

### In Scope
- UI：email 输入、发送验证码按钮、code 输入、验证按钮、登录态展示/退出。
- API：调用 `/api/auth/send-code` 与 `/api/auth/verify`；保存 token。
- 将 token 以 `Authorization: Bearer <token>` 附加到需要用户态的请求（如后续寻价/转接扩展）。

### Out of Scope
- 寻价字段收集（TBD）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-002 | login form + auth calls + status | |

## 3. Design / Decisions

### Proposed Approach
- token 存储：localStorage（v0.1 最小实现），并提供 logout 清除。
- 错误处理：统一显示可读错误（invalid/expired/rate limited）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | auth endpoints |

## 5. Implementation Plan

1. 增加 LoginModal 或独立面板。
2. send-code：禁用按钮 + 倒计时；处理 429。
3. verify：成功后保存 token 与 user.email；UI 展示已登录。
4. API client 支持可选 Authorization header。
5. 单测（可选）：状态机（logged_out → pending → logged_in）。

### Files / Modules
- `apps/widget/src/components/LoginPanel.tsx`
- `apps/widget/src/auth/storage.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| send code | email | 显示“已发送”与倒计时 | |
| verify ok | email+code | 状态=已登录，token 被保存 | |
| verify fail | wrong code | 显示错误，不进入登录态 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-010 | 邮箱登录方案与合规边界 | M | Product Owner | open |
| TBD-L0-012 | 寻价功能字段与触发条件 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

