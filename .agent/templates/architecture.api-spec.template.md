---
template_name: architecture.api-spec
version: v0.6.3
description: API 详细规范模板：从 IFC-* 扩展生成
---

# API Specification

> API 详细规范，扩展自 `docs/L2/interfaces.md`，包含鉴权、错误码、分页、流式、幂等。

## — BEGIN REGISTRY —

```architecture-registry
schema_version: "v0.6.3"
type: "api"
parent: "docs/L2/interfaces.md"

items:
  - id: ARCH-API-001
    statement: "{API 设计决策}"
    sources:
      - id: "{IFC-ID}"
        path: "docs/L2/interfaces.md#{IFC-ID}"
    rationale: "{决策理由}"
```

## — END REGISTRY —

---

## 1. 通用规范

### 1.1 Base URL

| 环境 | URL |
|------|-----|
| dev | `http://localhost:8000/api` |
| staging | `https://staging.example.com/api` |
| prod | `https://api.example.com/api` |

### 1.2 鉴权方案

| 接口类型 | 鉴权方式 | 说明 |
|----------|----------|------|
| 公开接口 | 无 / Rate Limit | `/api/chat` (基础) |
| 用户接口 | Bearer Token | 登录后获取 |
| 管理接口 | Basic Auth / SSO | 后台管理 |

```http
Authorization: Bearer <jwt_token>
```

### 1.3 错误码规范

| HTTP Status | Code | 说明 |
|-------------|------|------|
| 400 | BAD_REQUEST | 请求参数错误 |
| 401 | UNAUTHORIZED | 未认证 |
| 403 | FORBIDDEN | 无权限 |
| 404 | NOT_FOUND | 资源不存在 |
| 422 | VALIDATION_ERROR | 参数校验失败 |
| 429 | RATE_LIMITED | 频率限制 |
| 500 | INTERNAL_ERROR | 服务器错误 |
| 503 | SERVICE_UNAVAILABLE | LLM/DB 不可用 |

**错误响应格式**:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "email 格式不正确",
    "details": [
      {"field": "email", "reason": "invalid format"}
    ]
  }
}
```

### 1.4 分页规范

```http
GET /api/admin/products?page=1&page_size=20
```

**响应**:

```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total": 600,
    "total_pages": 30
  }
}
```

### 1.5 Rate Limiting

| 接口 | 限制 | 窗口 | REQ 来源 |
|------|------|------|----------|
| /api/chat | 30 | 1 分钟 | REQ-L0-SEC-003 |
| /api/auth/send-code | 5 | 1 分钟 | REQ-L0-RISK-009 |
| /api/admin/* | 100 | 1 分钟 | |

**响应头**:

```http
X-RateLimit-Limit: 30
X-RateLimit-Remaining: 28
X-RateLimit-Reset: 1610000000
```

---

## 2. Chat API (IFC-CHAT-API)

### POST /api/chat

**描述**: RAG 问答

**请求**:

```json
{
  "message": "这款激光切割机的最大切割厚度是多少？",
  "session_id": "uuid-optional",
  "context": {
    "product_id": "SKU-001",
    "url": "https://example.com/products/sku-001"
  },
  "stream": false
}
```

**响应**:

```json
{
  "answer": "根据产品规格，SF3015H 最大切割厚度为 20mm（碳钢）[1]。",
  "references": [
    {
      "id": 1,
      "source": "SF3015H 产品规格",
      "content": "最大切割厚度: 碳钢 20mm, 不锈钢 12mm"
    }
  ],
  "session_id": "uuid",
  "token_usage": {
    "prompt": 150,
    "completion": 50
  }
}
```

**流式响应** (stream=true):

```
data: {"delta": "根据产品规格", "done": false}
data: {"delta": "，SF3015H 最大", "done": false}
...
data: {"answer": "...", "references": [...], "done": true}
```

---

### POST /api/recommend

**描述**: 产品推荐

**请求**:

```json
{
  "query": "需要切割 15mm 碳钢的设备",
  "top_n": 3
}
```

**响应**:

```json
{
  "products": [
    {
      "id": "SKU-001",
      "name": "SF3015H",
      "category": "fiber-laser",
      "match_score": 0.95
    }
  ],
  "reasons": [
    "SF3015H 支持 20mm 碳钢切割，满足您的需求"
  ]
}
```

---

### POST /api/compare

**描述**: 产品比较

**请求**:

```json
{
  "product_ids": ["SKU-001", "SKU-002", "SKU-003"]
}
```

**响应**:

```json
{
  "comparison": {
    "columns": ["SKU-001", "SKU-002", "SKU-003"],
    "rows": [
      {"field": "最大切割厚度", "values": ["20mm", "16mm", "25mm"]},
      {"field": "激光功率", "values": ["3000W", "2000W", "6000W"]},
      {"field": "价格", "values": ["$15,000", "$12,000", "$25,000"]}
    ]
  }
}
```

---

## 3. Auth API

### POST /api/auth/send-code

**描述**: 发送邮箱验证码

**请求**:

```json
{
  "email": "user@example.com"
}
```

**响应**:

```json
{
  "success": true,
  "message": "验证码已发送"
}
```

**错误**:

| Code | 说明 |
|------|------|
| RATE_LIMITED | 发送过于频繁 |
| INVALID_EMAIL | 邮箱格式错误 |

---

### POST /api/auth/verify

**描述**: 验证邮箱

**请求**:

```json
{
  "email": "user@example.com",
  "code": "123456"
}
```

**响应**:

```json
{
  "token": "jwt-token",
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

---

## 4. Admin API (IFC-ADMIN-API)

### POST /api/admin/products

**描述**: 上传产品 JSON

**Content-Type**: `multipart/form-data`

**请求**:

```
file: products.json
```

**响应**:

```json
{
  "count": 600,
  "version": "v1.2",
  "created_at": "2026-01-16T10:00:00Z"
}
```

---

### POST /api/admin/index/rebuild

**描述**: 重建向量索引

**响应**:

```json
{
  "job_id": "uuid",
  "status": "started",
  "estimated_time": "5 minutes"
}
```

**幂等性**: 如果已有任务运行中，返回现有 job_id。

---

## 5. OpenAPI 生成

此文档可用于生成 OpenAPI 3.0 规范：

```yaml
openapi: 3.0.3
info:
  title: RAG Chatbot API
  version: 1.0.0
paths:
  /api/chat:
    post:
      summary: RAG 问答
      ...
```

**生成命令**:

```bash
/architecture-render output_type=openapi
```
