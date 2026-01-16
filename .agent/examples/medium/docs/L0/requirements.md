---
status: done
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "0000000000000000000000000000000000000000000000000000000000000000"
profile: "rag-web"
caf_version: v0.6.5
---

# L0 Requirements: rag-web-demo

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.5"
layer: L0
parent: "charter.yaml"
source_checksum: "0000000000000000000000000000000000000000000000000000000000000000"
profile: "rag-web"

requirements:
  - id: REQ-L0-API-001
    priority: P0
    statement: "系统应当提供 RAG 问答能力，回答应包含可追溯的来源引用。"
    sources:
      - id: "SCOPE-MH-001"
        path: "charter.yaml#scope.must_have[0]"
    acceptance:
      - "API 返回 answer + references"
    status: done
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-WGT-001
    priority: P0
    statement: "系统应当提供可嵌入网站的 Chatbot Widget，可配置挂载点与基础样式。"
    sources:
      - id: "SCOPE-MH-002"
        path: "charter.yaml#scope.must_have[1]"
    acceptance:
      - "提供最小集成示例（script 引入 + init 参数）"
    status: done
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-ADM-001
    priority: P0
    statement: "系统应当提供后台上传产品资料，并触发索引更新。"
    sources:
      - id: "SCOPE-MH-003"
        path: "charter.yaml#scope.must_have[2]"
    acceptance:
      - "上传后可查询到新资料的索引状态"
    status: done
    section: functional
    tbd_refs: []
    derived: false

tbds: []
exclusions: []
```

## — END REGISTRY —

