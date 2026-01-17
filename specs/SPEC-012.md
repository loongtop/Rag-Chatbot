---
id: "SPEC-012"
status: draft
owner: spec
leaf: true
parent: "SPEC-011"
source_requirements:
  - "REQ-L2-WGT-001"
interfaces:
  - "IFC-CHAT-API"
depends_on: []
profile: "typescript"
---

# Spec: Embed + Core Chat UI

## 0. Summary

- Goal: 提供可嵌入的 Widget：script 标签引入、可初始化、可对话（调用 `/api/chat`）。
- Non-goals: 完整设计系统/主题定制。
- Leaf: `true`

## 1. Scope

### In Scope
- `window.RagChatbotWidget.init(options)` 初始化 API（options 包含 apiBaseUrl、context、language）。
- UI：消息列表、输入框、发送按钮、加载态、错误提示。
- 会话：自动生成/缓存 `session_id`，每次调用带上。

### Out of Scope
- SSR/复杂路由（Widget 单组件）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-001 | script embed + demo + init | 最小集成示例 |

## 3. Design / Decisions

### Proposed Approach
- Build 产物：单 JS bundle + 可选 CSS；暴露全局 init；渲染到指定 container 或 body。
- 网络：封装 `ChatApiClient` 调用 `/api/chat`，带 `session_id`/`language`/`context`。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | `POST /api/chat` |

## 5. Implementation Plan

1. 建立目录：`apps/widget/src`（React 组件）+ `apps/widget/demo/index.html`。
2. 实现 init：
   - 创建/选择容器；
   - 渲染 `WidgetApp`；
   - 注入配置（apiBaseUrl/context/language）。
3. 实现会话管理：localStorage `rag_chat_session_id`。
4. 实现基础对话：发送 message → 渲染 answer + references（基础列表即可）。
5. 单测（可选）：组件渲染、API client mock。

### Files / Modules
- `apps/widget/src/index.ts`
- `apps/widget/src/WidgetApp.tsx`
- `apps/widget/src/api/client.ts`
- `apps/widget/demo/index.html`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| embed | `<script>` + init | Widget 可显示 | |
| chat | 输入 message | 渲染 answer 与 references | mock server |
| session | 刷新页面 | session_id 复用 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-006 | bundle 输出形态与 CDN 策略 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

