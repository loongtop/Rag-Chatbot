---
status: done
owner: architect
layer: architecture
type: flows
parent: docs/L2/notes-store/requirements.md
caf_version: v0.6.5
---

# Architecture: Core Flows (notes-cli)

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: flows
parent: "docs/L2/notes-store/requirements.md"
items:
  - id: ARCH-FL-001
    statement: "新增笔记流程：load → append → sort → persist，任一步骤失败应返回可诊断错误信息。"
    sources:
      - id: "REQ-L2-NS-001"
        path: "docs/L2/notes-store/requirements.md#REQ-L2-NS-001"
    rationale: "把 I/O 与排序定义为显式步骤，便于 Spec 与测试用例覆盖。"
  - id: ARCH-FL-002
    statement: "列出笔记流程：load → sort(desc) → return，文件缺失视为无数据而非错误。"
    sources:
      - id: "REQ-L2-NS-002"
        path: "docs/L2/notes-store/requirements.md#REQ-L2-NS-002"
    rationale: "保证 CLI 可重复运行，且首次运行体验一致。"
```

## — END REGISTRY —

