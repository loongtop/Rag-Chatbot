---
status: draft
owner: architect
layer: L2
type: interfaces
caf_version: v0.6.2
---

# L2 Interfaces Definition

> 定义 L2 组件间的接口契约，确保模块解耦与可测试性

## — BEGIN REGISTRY —

```interfaces-registry
schema_version: "v0.6.2"
layer: L2

interfaces:
  # ===========================================================================
  # IFC-CHAT-API: Widget ↔ API Server
  # ===========================================================================
  - id: IFC-CHAT-API
    name: "Chat API"
    type: REST
    provider: api-server
    consumers: [chat-widget]
    description: "Widget 前端与后端 API 的通信接口"
    sources:
      - id: "IFC-PRODUCT-DATA"
        path: "charter.yaml#product_data_contract"
      - id: "IFC-WIDGET-CTX"
        path: "charter.yaml#widget_context_contract"
    endpoints:
      - method: POST
        path: "/api/chat"
        description: "RAG 问答"
        request:
          - "message: string"
          - "session_id?: string"
          - "context?: { productId?, skuId?, url? }"
        response:
          - "answer: string"
          - "references: Reference[]"
          - "token_usage: { prompt, completion }"
        
      - method: POST
        path: "/api/recommend"
        description: "产品推荐"
        request:
          - "query: string"
          - "top_n?: number (default: 3)"
        response:
          - "products: Product[]"
          - "reasons: string[]"
        
      - method: POST
        path: "/api/compare"
        description: "产品比较"
        request:
          - "product_ids: string[] (2-4)"
        response:
          - "comparison: ComparisonTable"
        
      - method: POST
        path: "/api/auth/send-code"
        description: "发送验证码"
        request:
          - "email: string"
        response:
          - "success: boolean"
        
      - method: POST
        path: "/api/auth/verify"
        description: "验证邮箱"
        request:
          - "email: string"
          - "code: string"
        response:
          - "token: string"
          - "user: User"
        
      - method: POST
        path: "/api/handoff"
        description: "人工转接"
        request:
          - "session_id: string"
        response:
          - "queue_position: number"
        
      - method: POST
        path: "/api/voice/stt"
        description: "语音转文字"
        request:
          - "audio: Blob"
        response:
          - "text: string"
        
      - method: POST
        path: "/api/voice/tts"
        description: "文字转语音"
        request:
          - "text: string"
        response:
          - "audio_url: string"
        
      - method: POST
        path: "/api/upload"
        description: "文件上传"
        request:
          - "file: File"
        response:
          - "extracted_content: string"

  # ===========================================================================
  # IFC-ADMIN-API: Admin Dashboard ↔ API Server
  # ===========================================================================
  - id: IFC-ADMIN-API
    name: "Admin API"
    type: REST
    provider: api-server
    consumers: [admin-dashboard]
    description: "后台管理 UI 与后端 API 的通信接口"
    endpoints:
      - method: POST
        path: "/api/admin/products"
        description: "上传产品 JSON"
        request:
          - "file: JSON"
        response:
          - "count: number"
          - "version: string"
        
      - method: GET
        path: "/api/admin/products"
        description: "查询产品列表"
        request:
          - "query?: string"
          - "page?: number"
        response:
          - "products: Product[]"
          - "total: number"
        
      - method: POST
        path: "/api/admin/docs"
        description: "上传知识库文档"
        request:
          - "file: File"
        response:
          - "doc_id: string"
        
      - method: POST
        path: "/api/admin/index/rebuild"
        description: "重建向量索引"
        response:
          - "job_id: string"
        
      - method: GET
        path: "/api/admin/index/status"
        description: "索引状态"
        response:
          - "status: 'idle' | 'building' | 'error'"
          - "progress: number"
        
      - method: GET
        path: "/api/admin/handoff/queue"
        description: "客服队列"
        response:
          - "queue: HandoffRequest[]"
        
      - method: POST
        path: "/api/admin/handoff/:id/accept"
        description: "接入对话"
        
      - method: POST
        path: "/api/admin/handoff/:id/complete"
        description: "完成对话"

  # ===========================================================================
  # IFC-PRODUCT-DATA: 产品数据契约
  # ===========================================================================
  - id: IFC-PRODUCT-DATA
    name: "Product Data Contract"
    type: Data
    provider: external
    consumers: [api-server]
    description: "产品数据 JSON 格式契约"
    sources:
      - path: "charter.yaml#product_data_contract"
    schema:
      required:
        - "id: string (唯一)"
        - "name: string"
        - "category: string"
        - "url: string"
      optional:
        - "short_description: string"
        - "specs: object"
        - "price: number | string"
    notes:
      - "允许扩展字段"
      - "后台应保留原始 JSON 并提供版本回滚"

  # ===========================================================================
  # IFC-WIDGET-CTX: Widget 上下文契约
  # ===========================================================================
  - id: IFC-WIDGET-CTX
    name: "Widget Context Contract"
    type: Data
    provider: host-page
    consumers: [chat-widget]
    description: "宿主页面传递给 Widget 的上下文"
    sources:
      - path: "charter.yaml#widget_context_contract"
    schema:
      required:
        - "skuId | productId (至少其一)"
      optional:
        - "url: string (当前页面 URL)"
    notes:
      - "传递方式（query/header/body）由前后端联调确定"
```

## — END REGISTRY —

---

## Summary

| IFC-ID | Type | Provider | Consumer |
|--------|------|----------|----------|
| IFC-CHAT-API | REST | api-server | chat-widget |
| IFC-ADMIN-API | REST | api-server | admin-dashboard |
| IFC-PRODUCT-DATA | Data | external | api-server |
| IFC-WIDGET-CTX | Data | host-page | chat-widget |

---

## Traceability

| Interface | Charter Source |
|-----------|----------------|
| IFC-PRODUCT-DATA | `charter.yaml#product_data_contract` |
| IFC-WIDGET-CTX | `charter.yaml#widget_context_contract` |
