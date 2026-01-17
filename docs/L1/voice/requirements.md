---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
feature: "voice"
caf_version: v0.6.5
---

# L1 Requirements: 语音交互 (VOICE)

> v0.6.2 新增：基于 `classify_ui_requirement()` 判定，WGT-002 有 STT/TTS Provider 选择逻辑，提升为独立 Feature

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L1
parent: "docs/L0/requirements.md"
feature: "voice"

requirements:
  - id: REQ-L1-VOICE-001
    priority: P1
    statement: "提供语音交互能力：STT 语音输入 + TTS 语音输出，Provider 可配置。"
    sources:
      - id: "REQ-L0-WGT-002"
        path: "docs/L0/requirements.md#REQ-L0-WGT-002"
    acceptance:
      - "可录音转文字"
      - "可语音播放回复"
      - "Provider 可配置"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-007]

tbds:
  - id: TBD-L1-VOICE-001
    question: "STT/TTS Provider 选择与部署方式（在线/本地）"
    sources:
      - id: "TBD-L0-007"
        path: "docs/L0/requirements.md#TBD-L0-007"
    impact: M
    status: open

exclusions: []
```

## — END REGISTRY —

---

## 说明

此 Feature 从 WGT-002 提升，原因：

| 关键词匹配 | 结果 |
|------------|------|
| "语音" | ❌ 不在 ui_only_keywords |
| "配置" | ✅ 命中 business_keywords |

根据 `.agent/config/split-rules.yaml` 的 `ui_classification.business_keywords`，"配置" 关键词触发 `strategy: feature`。

---

## Summary

| Metric | Value |
|--------|-------|
| Total requirements | 1 |
| P0 | 0 |
| P1 | 1 |
| P2 | 0 |
| TBDs | 1 |
| Exclusions | 0 |

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L1-VOICE-001 | P1 | 提供语音交互能力：STT 语音输入 + TTS 语音输出，Provider 可配置。 | REQ-L0-WGT-002 | 3 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L1-VOICE-001 | REQ-L0-WGT-002 | docs/L0/requirements.md#REQ-L0-WGT-002 |

## TBDs

| TBD ID | Question | Target Layer | Impact | Status |
|--------|----------|--------------|--------|--------|
| TBD-L1-VOICE-001 | STT/TTS Provider 选择与部署方式（在线/本地） |  | M | open |

## Gate Check

- [x] All requirements have `sources[]` (1/1)
- [x] All P0/P1 have `acceptance[]`
