---
id: "SPEC-016"
status: draft
owner: spec
leaf: true
parent: "SPEC-011"
source_requirements:
  - "REQ-L2-WGT-005"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-012"
  - "SPEC-010"
profile: "typescript"
---

# Spec: Upload UI (Progress + Limits)

## 0. Summary

- Goal: Widget 支持文件上传：拖拽/点击上传、进度显示、格式/大小提示。
- Non-goals: 复杂文件管理（历史列表/多文件批处理）。
- Leaf: `true`

## 1. Scope

### In Scope
- UI：上传按钮 + dropzone；展示上传中/成功/失败状态。
- 调用 `/api/upload` 获取 `extracted_content`：
  - 成功后将 extracted_content 注入下一次 `/api/chat` 的 message（以固定模板拼接）。
- 限制提示：前端先做扩展名/大小预校验（后端仍需强校验）。

### Out of Scope
- 上传文件长期存储与回溯（TBD）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-005 | upload UI + progress + limits | |

## 3. Design / Decisions

### Proposed Approach
- 注入模板（示例）：
  - `【附件内容】\n{extracted}\n【用户问题】\n{message}`

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | upload endpoint |

## 5. Implementation Plan

1. 实现 dropzone + file picker。
2. 上传：XHR/fetch + `onprogress`（或简化为 spinner）。
3. 成功后缓存 extracted_content（一次对话周期内）。
4. 发送 chat 时拼接注入模板。

### Files / Modules
- `apps/widget/src/components/UploadPanel.tsx`
- `apps/widget/src/api/upload.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| drag upload | 拖拽文件 | 显示进度/成功 | |
| inject | 上传后发送问题 | message 包含附件内容 | |
| invalid | 超大/不支持 | UI 提示原因 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-008 | 上传格式/大小/留存策略 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

