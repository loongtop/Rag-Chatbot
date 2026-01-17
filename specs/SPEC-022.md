---
id: "SPEC-022"
status: draft
owner: spec
leaf: true
parent: "SPEC-018"
source_requirements:
  - "REQ-L2-ADM-004"
interfaces:
  - "IFC-ADMIN-API"
depends_on:
  - "SPEC-019"
  - "SPEC-008"
profile: "typescript"
---

# Spec: Handoff Console UI

## 0. Summary

- Goal: 提供客服工作台 UI：转接队列、对话接入、处理完成。
- Non-goals: 全渠道客服与工单系统集成。
- Leaf: `true`

## 1. Scope

### In Scope
- 页面：Handoff Console
  - 队列列表（pending）
  - 选择一条请求并 accept
  - 标记完成 complete
- API：
  - `GET /api/admin/handoff/queue`
  - `POST /api/admin/handoff/{id}/accept`
  - `POST /api/admin/handoff/{id}/complete`

### Out of Scope
- 客服与用户实时消息通道（v0.1 先实现状态闭环；消息形态 TBD）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-ADM-004 | queue list + accept + complete | |

## 3. Design / Decisions

### Proposed Approach
- 队列 polling：每 3-5 秒刷新（或手动刷新）。
- 接入后显示会话摘要（占位）：session_id、创建时间、状态。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | consume | handoff admin endpoints |

## 5. Implementation Plan

1. QueueList：轮询 GET queue；渲染表格/列表。
2. Accept：选中条目→POST accept→状态更新。
3. Complete：POST complete→从队列移除并显示完成提示。
4. 错误处理：显示失败原因；提供重试。

### Files / Modules
- `apps/admin/src/pages/HandoffPage.tsx`
- `apps/admin/src/api/handoff.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| list | 打开页面 | 显示 pending 队列 | mock |
| accept | 点击接入 | status 变为 active | |
| complete | 点击完成 | status 变为 resolved | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-011 | 客服工作台形态/消息通道/SLA | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

