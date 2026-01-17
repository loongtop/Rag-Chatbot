---
id: "SPEC-011"
status: draft
owner: spec
leaf: false
parent: "docs/L2/chat-widget/requirements.md"
source_requirements:
  - "REQ-L2-WGT-001"
  - "REQ-L2-WGT-002"
  - "REQ-L2-WGT-003"
  - "REQ-L2-WGT-004"
  - "REQ-L2-WGT-005"
  - "REQ-L2-WGT-006"
interfaces:
  - "IFC-CHAT-API"
depends_on: []
profile: "typescript"
---

# Spec: Chat Widget Overview

## 0. Summary

- Goal: 将 Widget 的 L2 需求拆解为可实现 leaf Specs（嵌入、i18n、登录、语音、上传、人机切换）。
- Non-goals: UI 视觉精修/品牌定制（可在实现阶段迭代）。
- Leaf: `false`

## 1. Scope

### In Scope
- 产出可通过 `<script>` 集成的 Widget bundle，并与 API Server 的 `IFC-CHAT-API` 对齐。
- 基础交互能力：对话、语言切换、登录、语音、上传、人机切换。

### Out of Scope
- 完整账户体系/复杂权限与后台 SSO。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-001 | SPEC-012 | embed + demo |
| REQ-L2-WGT-003 | SPEC-013 | zh/en i18n |
| REQ-L2-WGT-002 | SPEC-014 | email login UI |
| REQ-L2-WGT-004 | SPEC-015 | voice UI |
| REQ-L2-WGT-005 | SPEC-016 | upload UI |
| REQ-L2-WGT-006 | SPEC-017 | AI/human toggle |

## 3. Design / Decisions

### Proposed Approach
- Widget 作为可嵌入组件：`window.RagChatbotWidget.init({ apiBaseUrl, context, language })`。
- `session_id` 持久化在 localStorage；每次请求携带 `language`（对齐接口契约）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | chat/recommend/compare/auth/handoff/voice/upload |

## 5. Implementation Plan

1. 完成 SPEC-012：最小可用 Widget（对话 UI + /api/chat）。
2. 完成 SPEC-013：多语言 UI 文案与请求 language 参数。
3. 完成 SPEC-014/016/017：登录/上传/人机切换闭环。
4. 完成 SPEC-015：语音交互。

## 6. Acceptance Tests

- 嵌入集成冒烟：静态页面引入脚本后可初始化并完成一次 `/api/chat` 对话。

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-006 | Widget 资源体积与加载口径（CDN/缓存） | M | Product Owner | open |

## 8. Leaf Checklist

N/A（leaf=false）

