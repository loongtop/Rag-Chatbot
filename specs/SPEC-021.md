---
id: "SPEC-021"
status: draft
owner: spec
leaf: true
parent: "SPEC-018"
source_requirements:
  - "REQ-L2-ADM-002"
interfaces:
  - "IFC-ADMIN-API"
depends_on:
  - "SPEC-019"
  - "SPEC-006"
profile: "typescript"
---

# Spec: Knowledge Base Management UI

## 0. Summary

- Goal: 提供知识库管理 UI：文档上传/列表/索引状态/日志。
- Non-goals: 自动爬取/同步与复杂权限审批流。
- Leaf: `true`

## 1. Scope

### In Scope
- 页面：Knowledge Base
  - 上传文档
  - 文档列表（filename/status/created_at）
  - 索引状态（idle/building/error + progress）
  - 操作日志（最小：审计日志分页）
- API：
  - `POST /api/admin/docs`、`GET /api/admin/docs`
  - `POST /api/admin/index/rebuild`、`GET /api/admin/index/status`
  - `GET /api/admin/logs`

### Out of Scope
- 文档全文预览/编辑。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-ADM-002 | docs page + index status + logs | |

## 3. Design / Decisions

### Proposed Approach
- 索引重建按钮：点击触发 rebuild，并轮询 status。
- 日志：按 scope 过滤（如 `index`/`handoff`/`products`），v0.1 可先只展示最近 N 条。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | consume | docs/index/logs endpoints |

## 5. Implementation Plan

1. DocsUpload：文件选择→POST→toast。
2. DocsList：GET 列表 + pagination/search。
3. IndexStatus：轮询 GET status；Rebuild 按钮触发 POST rebuild。
4. LogsView：GET logs（分页），展示 action/actor/time/metadata。

### Files / Modules
- `apps/admin/src/pages/KnowledgeBasePage.tsx`
- `apps/admin/src/api/docs.ts`
- `apps/admin/src/api/index.ts`
- `apps/admin/src/api/logs.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| upload | 文档文件 | 文档出现在列表中 | mock |
| rebuild | 点击重建 | status 变为 building | |
| logs | 打开日志区 | 显示最近日志 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-008 | 文档格式/大小/留存与合规 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

