---
id: "SPEC-009"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-011"
interfaces:
  - "IFC-CHAT-API"
depends_on: []
profile: "python"
---

# Spec: Voice STT/TTS APIs

## 0. Summary

- Goal: 提供 STT/TTS API：语音转文字 + 文字转语音，并可配置 Provider。
- Non-goals: 自研语音模型/训练。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/voice/stt`：上传音频 → `{text}`。
- `POST /api/voice/tts`：`{text}` → `{audio_url}`。
- Provider 抽象：可配置在线/本地；未配置时返回可理解错误。

### Out of Scope
- 多语言语音合成参数细化（后续）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-011 | stt/tts endpoints + provider config | Widget 语音 UI 依赖 |

## 3. Design / Decisions

### Proposed Approach
- SpeechProvider：`stt(audio_bytes, content_type) -> text`；`tts(text, language) -> audio_url`。
- 安全：限制音频大小与时长（基线），避免滥用。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | voice endpoints |

## 5. Implementation Plan

1. 定义上传格式（multipart）与 JSON body（tts）。
2. 实现 provider 工厂（按 env）。
3. 实现端点与错误映射：未配置→503；不支持→400/415。
4. 单测：mock provider + 校验限制逻辑。

### Files / Modules
- `apps/api/api/voice.py`
- `apps/api/voice/base.py`, `apps/api/voice/factory.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| stt ok | audio file | 返回 text 非空 | mock provider |
| tts ok | text | 返回 audio_url | |
| not configured | no provider | 503 + 错误码 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-007 | STT/TTS Provider 选择与成本/延迟预算 | M | Product Owner | open |
| TBD-L1-VOICE-001 | STT/TTS 部署方式（在线/本地） | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

