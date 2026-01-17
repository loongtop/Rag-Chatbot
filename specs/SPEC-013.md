---
id: "SPEC-013"
status: draft
owner: spec
leaf: true
parent: "SPEC-011"
source_requirements:
  - "REQ-L2-WGT-003"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-012"
profile: "typescript"
---

# Spec: i18n + Language Toggle

## 0. Summary

- Goal: Widget 支持中英文 UI 文案切换，并将 `language` 参数传给后端以保证回答语言一致。
- Non-goals: 自动语言检测（可后续加）。
- Leaf: `true`

## 1. Scope

### In Scope
- UI 文案 i18n：按钮/提示/错误信息。
- 语言选择：默认 `zh`，可切换 `en`；持久化到 localStorage。
- API 调用：对 `/api/chat`、`/api/recommend`、`/api/compare` 传 `language`（见 `docs/L2/interfaces.md`）。

### Out of Scope
- 全量多语言（仅 zh/en）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-003 | i18n 字典 + toggle + 持久化 | |

## 3. Design / Decisions

### Proposed Approach
- `i18n.ts` 提供 `t(key, language)`。
- Widget 顶层状态维护 `language`，并注入 API client。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | `language?: 'zh'|'en'` |

## 5. Implementation Plan

1. 增加语言状态与切换 UI（下拉/按钮）。
2. 封装 i18n 字典与 `t()` 方法。
3. localStorage 存 `rag_chat_language`。
4. API client 默认带 language。
5. 单测（可选）：t() 覆盖 key。

### Files / Modules
- `apps/widget/src/i18n.ts`
- `apps/widget/src/state/settings.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| toggle | 切换到 en | UI 文案变为英文 | |
| persist | 刷新页面 | 保持上次语言 | |
| backend param | 发起 chat | request 带 language | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-009 | 语言选择规则与知识库中英策略 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

