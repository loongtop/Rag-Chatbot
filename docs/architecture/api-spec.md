---
status: draft
owner: architect
layer: architecture
type: api
parent: docs/L2/interfaces.md
caf_version: v0.6.5
---

# API Specification

> API 详细规范：扩展自 `docs/L2/interfaces.md`，补充鉴权、错误码、分页与上传约定。

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.5"
type: "api"
parent: "docs/L2/interfaces.md"

items:
  - id: ARCH-API-001
    statement: "所有 REST API 以 `/api` 为前缀，默认使用 JSON（UTF-8），并统一错误响应格式与可追踪 request_id。"
    sources:
      - id: "IFC-CHAT-API"
        path: "docs/L2/interfaces.md#IFC-CHAT-API"
    rationale: "统一前后端契约与可观测性，降低联调与排障成本。"

  - id: ARCH-API-002
    statement: "会话相关接口以 `sessionId` 贯穿；若客户端未提供则服务端生成并在响应中返回，便于多轮对话与状态关联。"
    sources:
      - id: "REQ-L2-API-003"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-003"
      - id: "IFC-CHAT-API"
        path: "docs/L2/interfaces.md#IFC-CHAT-API"
    rationale: "让 Widget 可无状态接入，同时在后端保留完整链路数据。"

  - id: ARCH-API-003
    statement: "后台管理接口（`/api/admin/*`）必须鉴权并对关键写操作写入审计日志，满足后台操作审计与安全指标。"
    sources:
      - id: "IFC-ADMIN-API"
        path: "docs/L2/interfaces.md#IFC-ADMIN-API"
      - id: "REQ-L0-SEC-003"
        path: "docs/L0/requirements.md#REQ-L0-SEC-003"
    rationale: "限制后台权限面并保留可追溯操作记录。"

  - id: ARCH-API-004
    statement: "文件/图片上传采用 `multipart/form-data`，服务端执行类型/大小校验并返回 `extractedContent`（必要时返回可追溯的 documentId）。"
    sources:
      - id: "REQ-L2-API-012"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-012"
      - id: "IFC-CHAT-API"
        path: "docs/L2/interfaces.md#IFC-CHAT-API"
    rationale: "兼容浏览器上传能力并确保解析结果可被问答引用与追踪。"

  - id: ARCH-API-005
    statement: "邮箱验证码接口实施频控与过期策略，避免刷码滥用；验证码仅通过安全通道返回（不在响应体回显）。"
    sources:
      - id: "REQ-L2-API-007"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-007"
      - id: "REQ-L0-SEC-003"
        path: "docs/L0/requirements.md#REQ-L0-SEC-003"
    rationale: "控制风险与成本，并满足安全指标。"

  - id: ARCH-API-006
    statement: "人工转接提供用户侧创建与队列查询接口，同时为客服工作台提供队列读取与 accept/complete 管理接口。"
    sources:
      - id: "REQ-L2-API-010"
        path: "docs/L2/api-server/requirements.md#REQ-L2-API-010"
      - id: "IFC-ADMIN-API"
        path: "docs/L2/interfaces.md#IFC-ADMIN-API"
    rationale: "以最小接口闭环实现“排队-接入-完成”的端到端流程。"
```

## — END REGISTRY —

---

## 1. 通用规范

### 1.1 Base URL

| 环境 | URL |
|------|-----|
| dev | `http://localhost:8000/api` |
| staging | `https://staging-chat.example.com/api` |
| prod | `https://chat.example.com/api` |

### 1.2 Content Types

- JSON：`Content-Type: application/json`
- 上传：`Content-Type: multipart/form-data`

### 1.3 鉴权（最小可用方案）

| 接口类型 | 鉴权方式 | 备注 |
|----------|----------|------|
| 公共接口 | 无（仅限流） | `/api/chat`、`/api/recommend`、`/api/compare` |
| 用户接口 | Bearer Token | `/api/auth/verify` 返回 token；后续可用于“寻价/人工”等需要用户态的能力 |
| 管理接口 | Admin Auth（TBD） | `TBD-003`：Basic Auth / 白名单 / SSO |

```http
Authorization: Bearer <token>
```

### 1.4 错误响应格式

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "email 格式不正确",
    "details": [
      {"field": "email", "reason": "invalid format"}
    ],
    "request_id": "req_01H..."
  }
}
```

### 1.5 分页规范（后台列表）

请求：
`GET /api/admin/products?page=1&pageSize=20&query=laser`

响应：
```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 600,
    "totalPages": 30
  }
}
```

### 1.6 Rate Limiting（建议默认值）

| 接口 | 建议限制 | 窗口 |
|------|----------|------|
| `/api/chat` | 30 | 1 分钟 |
| `/api/auth/send-code` | 5 | 10 分钟 |
| `/api/upload` | 10 | 10 分钟 |
| `/api/admin/*` | 100 | 1 分钟 |

---

## 2. 数据结构（简化）

### 2.1 Reference

```json
{
  "type": "document_chunk",
  "title": "SKU-001 产品手册",
  "snippet": "关键规格：最大承载 20kg...",
  "source": {"documentId": "uuid", "chunkId": "uuid"},
  "url": "https://example.com/docs/..."
}
```

### 2.2 Product

```json
{
  "id": "SKU-001",
  "name": "Product A",
  "category": "category-a",
  "shortDescription": "高性价比机型",
  "specs": {"power": "3000W"},
  "price": "15000",
  "url": "https://example.com/products/SKU-001"
}
```

---

## 3. Chat API（IFC-CHAT-API）

### 3.1 POST `/api/chat`

请求：
```json
{
  "message": "该产品的关键规格是什么？",
  "sessionId": "uuid-optional",
  "context": {"productId": "SKU-001", "skuId": "SKU-001", "url": "https://..."}
}
```

响应：
```json
{
  "answer": "根据产品规格，SKU-001 的关键规格为最大承载 20kg [1]。",
  "references": [{"type": "document_chunk", "title": "SKU-001 产品手册", "snippet": "...", "source": {"documentId": "uuid", "chunkId": "uuid"}}],
  "sessionId": "uuid",
  "tokenUsage": {"prompt": 150, "completion": 50, "model": "tbd"}
}
```

### 3.2 POST `/api/recommend`

请求：
```json
{"query": "需要切割 15mm 碳钢的设备", "topN": 3}
```

响应：
```json
{"products": [{"id": "SKU-001", "name": "Product A", "category": "category-a"}], "reasons": ["..."]}
```

### 3.3 POST `/api/compare`

请求：
```json
{"productIds": ["SKU-001", "SKU-002"]}
```

响应：
```json
{"comparison": {"columns": ["SKU-001", "SKU-002"], "rows": [{"field": "最大切割厚度", "values": ["20mm", "16mm"]}]}}
```

### 3.4 POST `/api/upload`

`multipart/form-data`：
- `file`: File

响应：
```json
{"extractedContent": "…", "documentId": "uuid-optional"}
```

### 3.5 POST `/api/voice/stt` / `/api/voice/tts`

- `/api/voice/stt`：上传音频 → `{text}`
- `/api/voice/tts`：`{text}` → `{audioUrl}`（或 bytes，TBD）

---

## 4. Auth API

### 4.1 POST `/api/auth/send-code`

请求：
```json
{"email": "user@example.com"}
```

响应：
```json
{"success": true}
```

### 4.2 POST `/api/auth/verify`

请求：
```json
{"email": "user@example.com", "code": "123456"}
```

响应：
```json
{"token": "jwt-or-opaque", "user": {"email": "user@example.com"}}
```

---

## 5. Handoff API

### 5.1 POST `/api/handoff`

请求：
```json
{"sessionId": "uuid"}
```

响应：
```json
{"queuePosition": 3}
```

---

## 6. Admin API（IFC-ADMIN-API）

> 均需 Admin Auth（TBD）。

### 6.1 POST `/api/admin/products`

上传产品 JSON（建议 `multipart/form-data`）：
- `file`: JSON

响应：
```json
{"count": 600, "version": "2026-01-16T12:00:00Z"}
```

### 6.2 GET `/api/admin/products`

查询产品列表（分页）。

### 6.3 POST `/api/admin/docs`

上传知识库文档：
- `file`: File

响应：
```json
{"docId": "uuid"}
```

### 6.4 POST `/api/admin/index/rebuild` / GET `/api/admin/index/status`

- rebuild 响应：`{"jobId":"uuid"}`
- status 响应：`{"status":"idle|building|error","progress":0.0}`

### 6.5 GET `/api/admin/handoff/queue`

响应：
```json
{"queue": [{"handoffId": "uuid", "sessionId": "uuid", "status": "pending"}]}
```

### 6.6 POST `/api/admin/handoff/{handoffId}/accept` / `/complete`

- accept：将请求置为 `active` 并分配客服标识
- complete：将请求置为 `resolved` 并记录处理结果（TBD）
