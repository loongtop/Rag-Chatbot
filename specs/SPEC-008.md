---
id: "SPEC-008"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-010"
  - "REQ-L2-WGT-006"
  - "REQ-L2-ADM-004"
interfaces:
  - "IFC-CHAT-API"
  - "IFC-ADMIN-API"
depends_on:
  - "SPEC-002"
profile: "python"
---

# Spec: Handoff State Machine + APIs (User + Admin)

## 0. Summary

- Goal: 完成人工转接闭环：用户发起转接、查询队列状态；客服工作台拉取队列并 accept/complete。
- Non-goals: 多渠道客服系统对接、SLA 自动派单算法。
- Leaf: `true`

## 1. Scope

### In Scope
- User:
  - `POST /api/handoff`：创建转接请求，返回 queue_position。
  - `GET /api/handoff/queue`：按 session_id 查询状态与队列位置。
- Admin:
  - `GET /api/admin/handoff/queue`：拉取 pending 队列。
  - `POST /api/admin/handoff/{id}/accept`：接入对话。
  - `POST /api/admin/handoff/{id}/complete`：完成对话。
- DB：`handoff_requests` 状态机（pending/active/resolved/cancelled/timeout）。

### Out of Scope
- 复杂客服权限/路由（与后台鉴权 TBD 绑定）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-010 | user handoff APIs + status | |
| REQ-L2-WGT-006 | queue/status 所需数据返回 | |
| REQ-L2-ADM-004 | admin handoff queue + actions | |

## 3. Design / Decisions

### Proposed Approach
- `POST /api/handoff` 以 `session_id` 为幂等键：同一 session 重复发起返回同一 pending 请求。
- queue_position：按 `created_at` 对 pending 请求排序计算（可在 DB 中窗口函数或应用侧计算）。

### Key Decisions
- Decision: 状态机以 DB 为单一真源
  - Rationale: 前后端一致、可追踪、可审计。
  - Alternatives: 仅内存队列（不可靠）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | handoff user endpoints |
| IFC-ADMIN-API | provide | admin handoff endpoints |

## 5. Implementation Plan

1. 定义 DB 模型：handoff_requests（含 session_id/user_id/status/assigned_agent_id/timestamps）。
2. 实现 user endpoints：
   - 创建/复用 pending 请求；
   - 查询状态与队列位置。
3. 实现 admin endpoints：
   - 队列分页/过滤；
   - accept：置 active + assigned_agent_id；
   - complete：置 resolved + resolved_at。
4. 写入 audit_logs（关键写操作）。
5. 单测：幂等、状态迁移、队列位置、并发创建。

### Files / Modules
- `apps/api/api/handoff_user.py`
- `apps/api/api/admin_handoff.py`
- `apps/api/models/handoff.py`
- `apps/api/services/handoff.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| create | session_id | 返回 queue_position>=1 | |
| idempotent | same session_id twice | 返回同一 handoff 状态 | |
| queue status | GET queue | 返回 status + queue_position | |
| admin accept | accept id | status=active | |
| admin complete | complete id | status=resolved | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-011 | 人工客服转接方案（工作台/通知/SLA） | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

