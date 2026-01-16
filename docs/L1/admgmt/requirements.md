---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
profile: "typescript"
feature: "admgmt"
---

# L1 Requirements: 后台管理 (ADMGMT)

---

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.0"
layer: L1
parent: "docs/L0/requirements.md"
profile: "typescript"
feature: "admgmt"

requirements:
  - id: REQ-L1-ADMGMT-001
    priority: P0
    statement: "提供产品数据管理能力：从 JSON 文件加载约 600 SKU，支持后台上传、替换与基础检索。"
    sources:
      - id: "REQ-L0-ADM-001"
        path: "docs/L0/requirements.md#REQ-L0-ADM-001"
    acceptance:
      - "系统启动时可加载指定 JSON 文件"
      - "后台可上传新 JSON 替换旧数据"
      - "可通过 ID 或名称查询产品详情"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L1-ADMGMT-002
    priority: P0
    statement: "提供知识库管理能力：后台上传文档并写入 PostgreSQL + pgvector，支持重建索引与状态查看。"
    sources:
      - id: "REQ-L0-ADM-002"
        path: "docs/L0/requirements.md#REQ-L0-ADM-002"
    acceptance:
      - "可通过后台上传文档（PDF/Word/TXT）"
      - "文档内容被拆分、向量化并存入 pgvector"
      - "可查看索引构建状态和进度"
      - "支持手动触发索引重建"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L1-ADMGMT-003
    priority: P0
    statement: "提供后台管理 UI：包含产品 JSON 管理、文档上传、索引状态、操作日志、人工客服处理、寻价线索管理。"
    sources:
      - id: "REQ-L0-ADM-003"
        path: "docs/L0/requirements.md#REQ-L0-ADM-003"
    acceptance:
      - "后台提供统一管理界面"
      - "包含产品数据、知识库、日志等功能模块"
      - "人工客服可查看转接请求并处理"
      - "可查看和管理寻价线索"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-003, TBD-L0-012]
    derived: false

tbds:
  - id: TBD-L1-ADMGMT-001
    question: "后台鉴权具体方式（白名单/Basic Auth/SSO）"
    sources:
      - id: "TBD-L0-003"
        path: "docs/L0/requirements.md#TBD-L0-003"
    impact: H
    owner: "Architect"
    target_layer: L1
    status: open
    related_reqs: [REQ-L1-ADMGMT-003]

  - id: TBD-L1-ADMGMT-002
    question: "寻价功能定义与 CRM 对接"
    sources:
      - id: "TBD-L0-012"
        path: "docs/L0/requirements.md#TBD-L0-012"
    impact: M
    owner: "Product Owner"
    target_layer: L2
    status: open
    related_reqs: [REQ-L1-ADMGMT-003]

exclusions: []
```

## — END REGISTRY —

---

## 1. Feature 概述

### 1.1 定位

**后台管理** 为管理员提供产品数据、知识库、操作日志、人工客服、寻价线索等统一管理能力。

### 1.2 核心能力

| 能力 | 描述 | Priority |
|------|------|----------|
| 产品数据 | JSON 上传/替换/查询 | P0 |
| 知识库 | 文档上传/向量化/索引 | P0 |
| 管理 UI | 统一后台界面 | P0 |

---

## 附录 A：溯源矩阵

| L0 Item | L1 Coverage | Status |
|---------|-------------|--------|
| REQ-L0-ADM-001 | REQ-L1-ADMGMT-001 | ✅ |
| REQ-L0-ADM-002 | REQ-L1-ADMGMT-002 | ✅ |
| REQ-L0-ADM-003 | REQ-L1-ADMGMT-003 | ✅ |
