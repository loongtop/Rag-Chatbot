---
id: "SPEC-017"
status: draft
owner: spec
leaf: true
parent: "SPEC-011"
source_requirements:
  - "REQ-L2-WGT-006"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-012"
  - "SPEC-008"
profile: "typescript"
---

# Spec: AI/Human Toggle UI (Queue Status)

## 0. Summary

- Goal: Widget 提供人工/AI 切换 UI；人工模式下展示队列等待与状态。
- Non-goals: 多客服并发转接/复杂 SLA 规则。
- Leaf: `true`

## 1. Scope

### In Scope
- UI：AI/Human toggle；human 选中后调用 `/api/handoff`，显示 queue_position。
- 轮询：`GET /api/handoff/queue` 查询状态（pending/active/resolved...）。
- 降级：接口不可用/超时提示并允许回退 AI。

### Out of Scope
- “联系人工客服”以外的工单系统联动。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-006 | toggle + queue UI | |

## 3. Design / Decisions

### Proposed Approach
- human 模式下：
  - 输入框禁用或提示“等待客服接入”；
  - status=active 后允许与客服消息交互（形态 TBD，先占位）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | handoff endpoints |

## 5. Implementation Plan

1. toggle 状态管理（AI/Human）。
2. human→发起 `/api/handoff`（需要 session_id）。
3. 轮询 `/api/handoff/queue`，更新 UI。
4. 失败/超时：提示并允许回退 AI。

### Files / Modules
- `apps/widget/src/components/HandoffToggle.tsx`
- `apps/widget/src/api/handoff.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| toggle on | 选择 human | 调用 /api/handoff 并显示 queue_position | |
| poll | pending→active | UI 状态变化 | mock |
| fallback | 503 | 提示并可切回 AI | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-011 | 人工客服工作台形态与 SLA | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

