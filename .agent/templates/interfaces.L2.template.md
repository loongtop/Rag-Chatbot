---
status: draft
owner: architect
layer: L2
parent: docs/L0/requirements.md
source_checksum: "{checksum}"
profile: "{profile}"
---

# L2 Interfaces: Inter-Module Contracts

> 本文件定义 **L2 模块之间的协作契约**（API / Event / Data）。
>
> 规则：
> - 任何跨模块交互都必须在此登记（模块私有实现不登记）
> - 每个接口条目必须可追溯到 L1/L2 的 `REQ-*`（至少 1 个 Source）
> - 契约一旦被实现依赖，必须遵循版本策略（见 §4）

---

## — BEGIN REGISTRY —

```interfaces-registry
# =============================================================================
# L2 Interfaces Registry - Inter-Module Contracts
# Schema: v1.0 | Template: v1.0 | CAF: v0.6.5
# =============================================================================

schema_version: "v0.6.5"
layer: L2
parent: "docs/L0/requirements.md"
source_checksum: "{checksum}"
profile: "{profile}"

interfaces:
  - id: "IFC-CHAT-API"
    name: "chat_api"
    type: "API" # API | Event | Data
    description: "模块间契约描述（至少10个字符）"
    providers: ["api-server"]
    consumers: ["chat-widget"]
    sources:
      - id: "REQ-L2-API-001"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-001"
    contract:
      transport: "HTTP" # HTTP | gRPC | MQ | File | InProcess
      input: |
        {
          "field": "type"
        }
      output: |
        {
          "field": "type"
        }
      errors:
        - code: "ERR_001"
          description: "错误描述"
    version: "v1"
    status: draft # draft | ready | done

tbds: []
exclusions: []
```

## — END REGISTRY —

---

<!-- GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY -->

## 1. 概览

### 1.1 模块边界

- Modules: `{module_list}`
- 本文件覆盖：跨模块 API / Event / Data 契约

### 1.2 契约清单（摘要）

| IFC-ID | Type | Name | Providers | Consumers | Version | Status |
|--------|------|------|-----------|-----------|---------|--------|
| {从 Registry 渲染} | | | | | | |

---

## 2. API 契约

{从 Registry 渲染 type=API 的 contract（路径/方法/鉴权/分页/幂等等）}

---

## 3. Event / Data 契约

### 3.1 Events

{从 Registry 渲染 type=Event 的 topics / payload / ordering / retry / DLQ 等}

### 3.2 Shared Data

{从 Registry 渲染 type=Data 的 schema / ownership / migrations 等}

---

## 4. 版本与兼容策略

- 版本格式：`v{major}` 或 `v{major}.{minor}`
- Breaking change：必须升 major，并提供迁移窗口
- 向后兼容：默认要求至少 1 个小版本窗口
- 变更记录：在每个 IFC 条目下维护（或在附录维护 changelog）

---

## 附录

### 附录 A：Traceability（L1/L2 → Interfaces）

| IFC-ID | Related REQ-ID(s) | Source Paths | Notes |
|--------|--------------------|--------------|-------|
| {从 Registry 渲染} | | | |

### 附录 B：TBD/待定项

| TBD-ID | Question | Sources | Impact | Owner | Target | Status |
|--------|----------|---------|--------|-------|--------|--------|
| {从 Registry 渲染} | | | | | | |

---

## 门禁检查

- [ ] 所有接口条目均有非空 `sources[]`
- [ ] providers/consumers 均为有效 L2 模块名
- [ ] contract 至少包含 input/output/errors（或明确 N/A）
- [ ] 版本策略已确定且可执行
