---
status: draft
owner: architect
layer: L2
parent: docs/L1/
component: "chat-widget"
profile: "typescript"
---

# L2 Requirements: Chat Widget

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.2"
layer: L2
component: "chat-widget"
profile: "typescript"

requirements:
  # ===========================================================================
  # Direct from L0 (strategy: direct_l2)
  # ===========================================================================
  - id: REQ-L2-WGT-001
    priority: P0
    statement: "提供可嵌入的 Widget 组件：支持 script 标签引入，提供集成示例。"
    sources:
      - id: "REQ-L0-WGT-001"
        path: "docs/L0/requirements.md#REQ-L0-WGT-001"
        strategy: "direct_l2"
    acceptance:
      - "Widget 可通过 script 标签引入"
      - "提供集成文档和 Demo"
    status: draft
    section: functional

  - id: REQ-L2-WGT-003
    priority: P1
    statement: "Widget 界面支持中英文切换。"
    sources:
      - id: "REQ-L0-WGT-003"
        path: "docs/L0/requirements.md#REQ-L0-WGT-003"
        strategy: "direct_l2"
    acceptance:
      - "界面文案可切换语言"
      - "用户可选择首选语言"
    status: draft
    section: functional

  # ===========================================================================
  # From USRMGMT Feature
  # ===========================================================================
  - id: REQ-L2-WGT-002
    priority: P1
    statement: "提供邮箱登录 UI：输入邮箱、输入验证码、显示登录状态。"
    sources:
      - id: "REQ-L1-USRMGMT-001"
        path: "docs/L1/usrmgmt/requirements.md#REQ-L1-USRMGMT-001"
    acceptance:
      - "邮箱输入框"
      - "验证码输入框"
      - "登录状态显示"
    status: draft
    section: functional

  # ===========================================================================
  # From VOICE Feature
  # ===========================================================================
  - id: REQ-L2-WGT-004
    priority: P1
    statement: "提供语音交互 UI：录音按钮、语音播放控件。"
    sources:
      - id: "REQ-L1-VOICE-001"
        path: "docs/L1/voice/requirements.md#REQ-L1-VOICE-001"
    acceptance:
      - "录音按钮可用"
      - "回复可语音播放"
    status: draft
    section: functional

  # ===========================================================================
  # From UPLOAD Feature
  # ===========================================================================
  - id: REQ-L2-WGT-005
    priority: P1
    statement: "提供文件上传 UI：拖拽/点击上传、进度显示、格式/大小提示。"
    sources:
      - id: "REQ-L1-UPLOAD-001"
        path: "docs/L1/upload/requirements.md#REQ-L1-UPLOAD-001"
    acceptance:
      - "支持拖拽上传"
      - "显示上传进度"
      - "格式/大小限制提示"
    status: draft
    section: functional

  # ===========================================================================
  # From HANDOFF Feature
  # ===========================================================================
  - id: REQ-L2-WGT-006
    priority: P1
    statement: "提供人工/AI 切换 UI：切换按钮、队列等待提示。"
    sources:
      - id: "REQ-L1-HANDOFF-001"
        path: "docs/L1/handoff/requirements.md#REQ-L1-HANDOFF-001"
    acceptance:
      - "人工/AI 切换按钮"
      - "队列等待状态显示"
    status: draft
    section: functional

tbds: []
exclusions: []
```

## — END REGISTRY —

---

## Summary

| Source | REQ Count | L2 REQ-IDs |
|--------|-----------|------------|
| L0 Direct (WGT-001) | 1 | REQ-L2-WGT-001 |
| L0 Direct (WGT-003) | 1 | REQ-L2-WGT-003 |
| USRMGMT | 1 | REQ-L2-WGT-002 |
| VOICE | 1 | REQ-L2-WGT-004 |
| UPLOAD | 1 | REQ-L2-WGT-005 |
| HANDOFF | 1 | REQ-L2-WGT-006 |
| **Total** | **6** | |
