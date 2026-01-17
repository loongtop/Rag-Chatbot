---
id: "SPEC-015"
status: draft
owner: spec
leaf: true
parent: "SPEC-011"
source_requirements:
  - "REQ-L2-WGT-004"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-012"
  - "SPEC-009"
profile: "typescript"
---

# Spec: Voice UI (Record + Playback)

## 0. Summary

- Goal: Widget 提供语音交互 UI：录音按钮（STT）与回复语音播放（TTS）。
- Non-goals: 复杂降噪/断句等高级体验。
- Leaf: `true`

## 1. Scope

### In Scope
- 录音：浏览器 `MediaRecorder` 采集音频并上传到 `/api/voice/stt`，将返回 text 填入输入框。
- 播放：对回复 text 调用 `/api/voice/tts` 获取 audio_url 并播放（可选开关）。
- 错误提示：无麦克风权限/接口不可用。

### Out of Scope
- 语音流式识别。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-WGT-004 | record + play controls | |

## 3. Design / Decisions

### Proposed Approach
- 音频格式：优先 `audio/webm`（浏览器支持优先），后端不支持则提示。
- TTS 播放：每条 assistant 消息可显示“播放”按钮。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | consume | voice endpoints |

## 5. Implementation Plan

1. 实现录音组件：start/stop；生成 Blob。
2. 上传到 STT：multipart(audio)；处理返回 text。
3. TTS：按钮触发；缓存 audio_url（同一文本避免重复请求）。
4. 单测（可选）：mock MediaRecorder + API。

### Files / Modules
- `apps/widget/src/components/VoiceControls.tsx`
- `apps/widget/src/api/voice.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| record | 录音 3s | STT 返回 text 并填入输入框 | |
| play | 点击播放 | 音频可播放 | |
| denied | 无权限 | 显示权限提示 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-007 | STT/TTS Provider 选择 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

