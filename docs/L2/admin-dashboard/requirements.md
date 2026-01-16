---
status: draft
owner: architect
layer: L2
parent: docs/L1/
component: "admin-dashboard"
profile: "typescript"
---

# L2 Requirements: Admin Dashboard

## — BEGIN REGISTRY —

```requirements-registry
schema_version: "v0.6.2"
layer: L2
component: "admin-dashboard"
profile: "typescript"

requirements:
  # ===========================================================================
  # From ADMGMT Feature
  # ===========================================================================
  - id: REQ-L2-ADM-001
    priority: P0
    statement: "提供产品数据管理 UI：JSON 上传/替换/查看/搜索。"
    sources:
      - id: "REQ-L1-ADMGMT-001"
        path: "docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-001"
    acceptance:
      - "产品列表页面"
      - "JSON 上传功能"
      - "搜索/筛选功能"
    status: draft
    section: functional

  - id: REQ-L2-ADM-002
    priority: P0
    statement: "提供知识库管理 UI：文档上传/列表/索引状态/日志。"
    sources:
      - id: "REQ-L1-ADMGMT-002"
        path: "docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-002"
    acceptance:
      - "文档上传功能"
      - "索引状态显示"
      - "操作日志查看"
    status: draft
    section: functional

  - id: REQ-L2-ADM-003
    priority: P0
    statement: "提供后台统一管理界面：侧边栏导航、权限控制入口。"
    sources:
      - id: "REQ-L1-ADMGMT-003"
        path: "docs/L1/admgmt/requirements.md#REQ-L1-ADMGMT-003"
    acceptance:
      - "统一布局框架"
      - "侧边栏导航"
      - "登录/鉴权入口"
    status: draft
    section: functional

  # ===========================================================================
  # From HANDOFF Feature
  # ===========================================================================
  - id: REQ-L2-ADM-004
    priority: P1
    statement: "提供客服工作台 UI：转接队列、对话接入、处理完成。"
    sources:
      - id: "REQ-L1-HANDOFF-001"
        path: "docs/L1/handoff/requirements.md#REQ-L1-HANDOFF-001"
    acceptance:
      - "队列列表"
      - "接入对话功能"
      - "对话完成标记"
    status: draft
    section: functional

tbds: []
exclusions: []
```

## — END REGISTRY —

---

## Summary

| Source Feature | REQ Count | L2 REQ-IDs |
|----------------|-----------|------------|
| ADMGMT | 3 | REQ-L2-ADM-001 ~ 003 |
| HANDOFF | 1 | REQ-L2-ADM-004 |
| **Total** | **4** | |
