---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "5fa5705024b8b5e50e22c12cb94632bb58e865c8625eb756864424938bc417df"
profile: "rag-web"
---

# L0 Requirements: RAG Chatbot System

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text (§1-§5) | Generated | 🔒 Readonly |
> | Appendices (A/B/C) | Generated | 🔒 Readonly |
>
> All generated content derives from the Registry block. Use `/requirements-render` to regenerate.

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# Requirements Registry (Single Source of Truth)
# Schema: v1.0 | Template: v2.0 | CAF: v0.5.0
# =============================================================================

schema_version: "v0.5.0"
layer: L0
parent: "charter.yaml"
source_checksum: "5fa5705024b8b5e50e22c12cb94632bb58e865c8625eb756864424938bc417df"
profile: "rag-web"

# -----------------------------------------------------------------------------
# Requirements
# -----------------------------------------------------------------------------
requirements:
  # ===========================================================================
  # Widget (WGT) - 前端交互组件
  # ===========================================================================
  - id: REQ-L0-WGT-001
    priority: P0
    statement: "提供可嵌入的 Chatbot Widget，支持集成到现有产品网站，并提供最小集成示例。"
    sources:
      - id: "SCOPE-MH-001"
        path: "charter.yaml#scope.must_have[0]"
    acceptance:
      - "Widget 可在静态 HTML 页面中通过 script 标签引入并正常渲染"
      - "提供包含初始化参数的集成文档和 Demo 页面"
      - "Widget 支持传入 skuId/productId/url 作为上下文参数"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-WGT-002
    priority: P1
    statement: "Widget 支持语音输入（STT）与语音输出（TTS），STT/TTS Provider 可配置。"
    sources:
      - id: "SCOPE-MH-012"
        path: "charter.yaml#scope.must_have[11]"
    acceptance:
      - "用户可点击语音按钮录音并转换为文字输入"
      - "AI 回复可通过语音播放"
      - "可在配置中切换 STT/TTS Provider"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-007]
    derived: false

  - id: REQ-L0-WGT-003
    priority: P1
    statement: "Widget 与后台 UI 支持中文/英文双语，用户可选择输出语言（默认中文）。"
    sources:
      - id: "SCOPE-MH-013"
        path: "charter.yaml#scope.must_have[12]"
    acceptance:
      - "Widget 界面文案支持中英文切换"
      - "用户可设置首选输出语言"
      - "回答语言与用户选择一致"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-009]
    derived: false

  - id: REQ-L0-WGT-004
    priority: P1
    statement: "Widget 支持用户上传文件或图片作为对话输入，系统提取内容用于回答，并对类型/大小做限制。"
    sources:
      - id: "SCOPE-MH-014"
        path: "charter.yaml#scope.must_have[13]"
    acceptance:
      - "支持常见文件格式（PDF、Word、图片）上传"
      - "系统可解析文件内容并参与 RAG 问答"
      - "超出大小限制时给出明确错误提示"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-008]
    derived: false

  # ===========================================================================
  # Admin Dashboard (ADM) - 后台管理
  # ===========================================================================
  - id: REQ-L0-ADM-001
    priority: P0
    statement: "支持产品数据导入与查询，从 JSON 文件加载约 600 SKU，并支持后台上传、替换与基础检索。"
    sources:
      - id: "SCOPE-MH-002"
        path: "charter.yaml#scope.must_have[1]"
    acceptance:
      - "系统启动时可加载指定 JSON 文件"
      - "后台可上传新 JSON 替换旧数据"
      - "可通过 ID 或名称查询产品详情"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-ADM-002
    priority: P0
    statement: "支持知识库导入与索引：后台上传文档并写入 PostgreSQL + pgvector，支持重建索引与状态查看，支持检索结果排序/重排。"
    sources:
      - id: "SCOPE-MH-003"
        path: "charter.yaml#scope.must_have[2]"
    acceptance:
      - "可通过后台上传文档（PDF/Word/TXT）"
      - "文档内容被拆分、向量化并存入 pgvector"
      - "可查看索引构建状态和进度"
      - "支持手动触发索引重建"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-ADM-003
    priority: P0
    statement: "提供后台管理 UI，包含产品 JSON 管理、文档上传、索引构建/状态、操作日志、人工客服转接处理、寻价/线索管理。"
    sources:
      - id: "SCOPE-MH-009"
        path: "charter.yaml#scope.must_have[8]"
    acceptance:
      - "后台提供统一管理界面"
      - "包含产品数据、知识库、日志等功能模块"
      - "人工客服可查看转接请求并处理"
      - "可查看和管理寻价线索"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-003, TBD-L0-011, TBD-L0-012]
    derived: false

  # ===========================================================================
  # API Server (API) - 后端核心服务
  # ===========================================================================
  - id: REQ-L0-API-001
    priority: P0
    statement: "支持 RAG 问答，回答默认附带来源引用（文档/产品字段），无足够依据时优先澄清或拒答。"
    sources:
      - id: "SCOPE-MH-004"
        path: "charter.yaml#scope.must_have[3]"
    acceptance:
      - "回答包含明确的引用来源标记"
      - "当问题与知识库无关时，模型能够拒绝回答或请求澄清"
      - "引用来源可追溯到具体文档或产品字段"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-API-002
    priority: P0
    statement: "支持产品推荐：基于用户需求输出 Top-N（默认 3）SKU，包含推荐理由与依据来源。"
    sources:
      - id: "SCOPE-MH-005"
        path: "charter.yaml#scope.must_have[4]"
    acceptance:
      - "针对用户需求返回 Top-3 推荐产品"
      - "每个推荐包含推荐理由"
      - "推荐依据可追溯"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]
    derived: false

  - id: REQ-L0-API-003
    priority: P0
    statement: "支持产品比较：支持 2–4 个 SKU，输出结构化对比（表格/卡片），字段可配置。"
    sources:
      - id: "SCOPE-MH-006"
        path: "charter.yaml#scope.must_have[5]"
    acceptance:
      - "可对比 2-4 个产品"
      - "输出结构化表格/卡片形式"
      - "对比字段可配置"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]
    derived: false

  - id: REQ-L0-API-004
    priority: P0
    statement: "支持上下文感知：Widget 可传入当前页面 productId/skuId/url，后端用于检索与排序。"
    sources:
      - id: "SCOPE-MH-007"
        path: "charter.yaml#scope.must_have[6]"
    acceptance:
      - "后端可接收并解析上下文参数"
      - "上下文影响检索结果排序"
      - "当前产品信息优先展示"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  - id: REQ-L0-API-005
    priority: P0
    statement: "支持对话历史管理：多轮对话，记录引用、错误与 token 用量（用于成本与质量分析）。"
    sources:
      - id: "SCOPE-MH-008"
        path: "charter.yaml#scope.must_have[7]"
    acceptance:
      - "支持多轮对话上下文"
      - "对话历史可查询"
      - "记录每次对话的 token 用量"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-004]
    derived: false

  - id: REQ-L0-API-006
    priority: P0
    statement: "LLM Provider 可配置切换：支持在线 OpenAI-Compatible API（如 ChatGPT/DeepSeek）与本地 Ollama 两种模式。"
    sources:
      - id: "SCOPE-MH-010"
        path: "charter.yaml#scope.must_have[9]"
    acceptance:
      - "可通过配置切换 LLM Provider"
      - "在线模式和本地模式均可正常工作"
      - "切换不影响核心功能"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-001]
    derived: false

  - id: REQ-L0-API-007
    priority: P1
    statement: "支持人工/AI 入口切换：用户可在输入界面选择"人工"或"AI"，默认使用 AI；选择"人工"时将对话转接至后台人工队列处理。"
    sources:
      - id: "SCOPE-MH-011"
        path: "charter.yaml#scope.must_have[10]"
    acceptance:
      - "Widget 提供人工/AI 切换按钮"
      - "默认为 AI 模式"
      - "选择人工后，对话进入后台处理队列"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-011]
    derived: false

  # ===========================================================================
  # Shared (SHARED) - 跨组件功能
  # ===========================================================================
  - id: REQ-L0-SHARED-001
    priority: P1
    statement: "支持邮箱登录（验证码）：Widget 支持邮箱验证码登录/验证；登录后可将对话与浏览行为关联到用户；登录后解锁"寻价"与"联系人工客服"功能。"
    sources:
      - id: "SCOPE-MH-015"
        path: "charter.yaml#scope.must_have[14]"
    acceptance:
      - "用户输入邮箱可收到验证码"
      - "验证通过后状态为已登录"
      - "未登录用户点击寻价/人工客服提示登录"
      - "登录后行为可关联到用户"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-010]
    derived: false

  # ===========================================================================
  # Performance (PERF) - 性能需求
  # ===========================================================================
  - id: REQ-L0-PERF-001
    priority: P0
    statement: "端到端首次响应时间（包含 LLM）p95 <= 1.5s（服务端口径）。"
    sources:
      - id: "MET-PERF-001"
        path: "charter.yaml#metrics.performance[0]"
    acceptance:
      - "压测报告显示 p95 响应时间 <= 1.5s"
    status: draft
    section: performance
    tbd_refs: []
    derived: false

  - id: REQ-L0-PERF-002
    priority: P0
    statement: "RAG 检索延迟 p95 <= 500ms（服务端口径）。"
    sources:
      - id: "MET-PERF-002"
        path: "charter.yaml#metrics.performance[1]"
    acceptance:
      - "检索接口单独压测 p95 <= 500ms"
    status: draft
    section: performance
    tbd_refs: []
    derived: false

  - id: REQ-L0-PERF-003
    priority: P0
    statement: "支持并发会话 >= 100（连接保持 5 分钟）。"
    sources:
      - id: "MET-PERF-003"
        path: "charter.yaml#metrics.performance[2]"
    acceptance:
      - "100 并发下系统无报错且响应正常"
    status: draft
    section: performance
    tbd_refs: []
    derived: false

  # ===========================================================================
  # Security (SEC) - 安全需求
  # ===========================================================================
  - id: REQ-L0-SEC-001
    priority: P0
    statement: "所有通信强制使用 HTTPS 加密。"
    sources:
      - id: "MET-SEC-001"
        path: "charter.yaml#metrics.security[0]"
    acceptance:
      - "非 HTTPS 请求被拒绝或重定向"
      - "TLS 版本 >= 1.2"
    status: draft
    section: security
    tbd_refs: []
    derived: false

  - id: REQ-L0-SEC-002
    priority: P0
    statement: "敏感数据（如手机号/邮箱）需脱敏处理。"
    sources:
      - id: "MET-SEC-002"
        path: "charter.yaml#metrics.security[1]"
    acceptance:
      - "日志和 API 返回中无明文敏感信息"
      - "敏感字段使用掩码显示"
    status: draft
    section: security
    tbd_refs: []
    derived: false

  - id: REQ-L0-SEC-003
    priority: P0
    statement: "实施 API 访问频率限制，并记录后台操作审计日志。"
    sources:
      - id: "MET-SEC-003"
        path: "charter.yaml#metrics.security[2]"
    acceptance:
      - "超出频率限制的请求返回 429"
      - "关键操作日志包含操作人、时间、内容"
    status: draft
    section: security
    tbd_refs: []
    derived: false

  - id: REQ-L0-SEC-004
    priority: P0
    statement: "实施 Prompt Injection 基础防护，确保系统提示不被覆盖，引用内容需转义。"
    sources:
      - id: "MET-SEC-004"
        path: "charter.yaml#metrics.security[3]"
    acceptance:
      - "攻击性 Prompt 不会泄露系统设定"
      - "用户输入中的特殊字符被正确转义"
    status: draft
    section: security
    tbd_refs: []
    derived: false

  # ===========================================================================
  # Stability (STAB) - 稳定性需求
  # ===========================================================================
  - id: REQ-L0-STAB-001
    priority: P0
    statement: "系统月可用性 >= 99.5%。"
    sources:
      - id: "MET-STAB-001"
        path: "charter.yaml#metrics.stability[0]"
    acceptance:
      - "监控数据显示月可用性达标"
    status: draft
    section: reliability
    tbd_refs: []
    derived: false

  - id: REQ-L0-STAB-002
    priority: P0
    statement: "LLM/数据库异常时支持自动恢复与优雅降级。"
    sources:
      - id: "MET-STAB-002"
        path: "charter.yaml#metrics.stability[1]"
    acceptance:
      - "模拟数据库断连后能自动恢复"
      - "LLM 不可用时返回友好降级提示"
    status: draft
    section: reliability
    tbd_refs: [TBD-L0-002]
    derived: false

  # ===========================================================================
  # Usability (UX) - 易用性需求
  # ===========================================================================
  - id: REQ-L0-UX-001
    priority: P0
    statement: "Widget 加载时间 <= 1s。"
    sources:
      - id: "MET-UX-001"
        path: "charter.yaml#metrics.usability[0]"
    acceptance:
      - "资源加载时长监控满足指标"
    status: draft
    section: usability
    tbd_refs: [TBD-L0-006]
    derived: false

  - id: REQ-L0-UX-002
    priority: P0
    statement: "支持移动端自适应布局。"
    sources:
      - id: "MET-UX-002"
        path: "charter.yaml#metrics.usability[1]"
    acceptance:
      - "移动端布局显示正常"
      - "触控交互友好"
    status: draft
    section: usability
    tbd_refs: []
    derived: false

  - id: REQ-L0-UX-003
    priority: P0
    statement: "无需用户培训即可使用。"
    sources:
      - id: "MET-UX-003"
        path: "charter.yaml#metrics.usability[2]"
    acceptance:
      - "新用户可直接上手使用"
      - "交互符合常见聊天应用习惯"
    status: draft
    section: usability
    tbd_refs: []
    derived: false

  # ===========================================================================
  # Constraints (CON) - 约束条件
  # ===========================================================================
  - id: REQ-L0-CON-001
    priority: P0
    statement: "云服务月成本 < $5000（含 LLM token、数据库、日志/监控、存储与带宽）。"
    sources:
      - id: "CONSTRAINT-RES-001"
        path: "charter.yaml#constraints.resource.budget"
    acceptance:
      - "成本测算模型显示达标"
    status: draft
    section: constraint
    tbd_refs: []
    derived: false

  - id: REQ-L0-CON-002
    priority: P0
    statement: "交付截止日期: 2026-02-28。"
    sources:
      - id: "CONSTRAINT-RES-002"
        path: "charter.yaml#constraints.resource.timeline"
    acceptance:
      - "按计划交付"
    status: draft
    section: constraint
    tbd_refs: []
    derived: false

  - id: REQ-L0-CON-003
    priority: P0
    statement: "技术栈限制：仅使用 Python(FastAPI), TypeScript/React, PostgreSQL+pgvector, Redis, OpenAI/Ollama。"
    sources:
      - id: "CONSTRAINT-TECH-001"
        path: "charter.yaml#constraints.technology_boundary.allowed"
    acceptance:
      - "代码库依赖检查符合规定"
    status: draft
    section: constraint
    tbd_refs: []
    derived: false

  - id: REQ-L0-CON-004
    priority: P0
    statement: "禁止：自建 LLM 训练、使用 Pinecone、私有化部署专有数据库。"
    sources:
      - id: "CONSTRAINT-TECH-002"
        path: "charter.yaml#constraints.technology_boundary.forbidden"
    acceptance:
      - "代码库依赖检查符合规定"
    status: draft
    section: constraint
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# TBDs (To Be Determined) - 智能判断 target_layer
# -----------------------------------------------------------------------------
tbds:
  - id: TBD-L0-001
    question: "LLM Provider/Model 选择（OpenAI/Claude/兼容方案）与成本上限分配"
    sources:
      - id: "TBD-001"
        path: "charter.yaml#open_questions[0]"
    impact: H
    owner: "Product Owner"
    target_layer: L0
    status: open
    related_reqs: [REQ-L0-API-006]
    rationale: "影响架构设计，必须在 L0 阶段确定"

  - id: TBD-L0-002
    question: "LLM/pgvector 不可用时的降级策略定义"
    sources:
      - id: "TBD-002"
        path: "charter.yaml#open_questions[1]"
    impact: M
    owner: "Architect"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-STAB-002]

  - id: TBD-L0-003
    question: "后台鉴权具体方式（白名单/Basic Auth/SSO）"
    sources:
      - id: "TBD-003"
        path: "charter.yaml#open_questions[2]"
    impact: H
    owner: "Architect"
    target_layer: L0
    status: open
    related_reqs: [REQ-L0-ADM-003]
    rationale: "影响安全架构，必须在 L0 阶段确定"

  - id: TBD-L0-004
    question: "对话与日志留存策略（合规要求）"
    sources:
      - id: "TBD-004"
        path: "charter.yaml#open_questions[3]"
    impact: M
    owner: "Legal/Security"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-API-005]

  - id: TBD-L0-005
    question: "推荐/比较的字段配置来源"
    sources:
      - id: "TBD-005"
        path: "charter.yaml#open_questions[4]"
    impact: L
    owner: "Product Owner"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-API-002, REQ-L0-API-003]

  - id: TBD-L0-006
    question: "Widget 资源体积限制与加载口径"
    sources:
      - id: "TBD-006"
        path: "charter.yaml#open_questions[5]"
    impact: L
    owner: "Frontend Lead"
    target_layer: L2
    status: open
    related_reqs: [REQ-L0-UX-001]
    rationale: "界面相关，影响 Widget 实现"

  - id: TBD-L0-007
    question: "STT/TTS Provider 选择与部署"
    sources:
      - id: "TBD-007"
        path: "charter.yaml#open_questions[6]"
    impact: M
    owner: "Architect"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-WGT-002]

  - id: TBD-L0-008
    question: "文件上传格式、大小、存储与合规"
    sources:
      - id: "TBD-008"
        path: "charter.yaml#open_questions[7]"
    impact: M
    owner: "Security"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-WGT-004]

  - id: TBD-L0-009
    question: "多语言策略细节（自动检测 vs 手动）"
    sources:
      - id: "TBD-009"
        path: "charter.yaml#open_questions[8]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-WGT-003]

  - id: TBD-L0-010
    question: "邮箱登录验证码方案与防刷机制"
    sources:
      - id: "TBD-010"
        path: "charter.yaml#open_questions[9]"
    impact: M
    owner: "Security"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-SHARED-001]

  - id: TBD-L0-011
    question: "人工客服转接方案细节"
    sources:
      - id: "TBD-011"
        path: "charter.yaml#open_questions[10]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-API-007, REQ-L0-ADM-003]

  - id: TBD-L0-012
    question: "寻价功能定义与 CRM 对接"
    sources:
      - id: "TBD-012"
        path: "charter.yaml#open_questions[11]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-SHARED-001, REQ-L0-ADM-003]

# -----------------------------------------------------------------------------
# Exclusions (N/A with reason) - 逐条提取
# -----------------------------------------------------------------------------
exclusions:
  - source:
      id: "SCOPE-OOS-001"
      path: "charter.yaml#scope.out_of_scope[0]"
    reason: "不做完整认证/账号体系：不支持密码登录、第三方 OAuth/SSO、多因素认证、复杂权限管理（仅提供邮箱验证码登录作为最小能力）"
    category: out_of_scope
  - source:
      id: "SCOPE-OOS-002"
      path: "charter.yaml#scope.out_of_scope[1]"
    reason: "订单处理和支付功能不在当前范围内"
    category: out_of_scope
  - source:
      id: "SCOPE-OOS-005"
      path: "charter.yaml#scope.out_of_scope[2]"
    reason: "知识库自动爬取/自动同步（V0.1 仅支持手动上传/替换）"
    category: deferred
  - source:
      id: "SCOPE-OOS-006"
      path: "charter.yaml#scope.out_of_scope[3]"
    reason: "自建 LLM 训练不在范围内"
    category: out_of_scope
  - source:
      path: "charter.yaml#traceability"
    reason: "Process configuration, not a deliverable requirement"
    category: process_config
  - source:
      path: "charter.yaml#freeze"
    reason: "Freeze metadata, not a deliverable requirement"
    category: process_config
```

## — END REGISTRY —

---

<!-- =========================================================================
     GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY
     Regenerate with: /requirements-render L0
     ========================================================================= -->

## 1. 引言

### 1.1 目的

本文档定义了 **RAG Chatbot System** 的 L0（系统级）需求规格说明，是下游 L1/L2/L3 需求分解的唯一事实来源。

本文档的预期读者包括：项目发起人、产品经理、架构师、开发团队、测试团队。

_Source_: `charter.yaml#meta`

### 1.2 范围

**系统边界**：嵌入式产品知识库 RAG Chatbot，支持产品推荐、对比、多语言、语音交互、人工客服转接。

**包含**：
- 可嵌入的 Chatbot Widget（含语音、多语言、文件上传）
- RAG 问答核心服务（推荐、对比、上下文感知）
- 后台管理系统（产品/知识库管理、人工客服、寻价线索）
- 邮箱验证码登录

**不包含**：
- 完整认证/账号体系（OAuth/SSO/MFA）
- 订单处理和支付功能
- 知识库自动爬取/同步
- 自建 LLM 训练

_Source_: `charter.yaml#scope.must_have`, `charter.yaml#scope.out_of_scope`

### 1.3 定义与术语

| 术语 | 定义 |
|------|------|
| RAG | Retrieval-Augmented Generation，检索增强生成 |
| LLM | Large Language Model，大型语言模型 |
| SKU | Stock Keeping Unit，库存单位 |
| pgvector | PostgreSQL 向量扩展，用于相似度搜索 |
| STT | Speech-to-Text，语音转文字 |
| TTS | Text-to-Speech，文字转语音 |

### 1.4 参考文档

| 文档 | 版本/Checksum | 说明 |
|------|--------------|------|
| `charter.yaml` | `5fa570...` | 项目任务书（已冻结） |
| `docs/L0/split-report.md` | - | Charter → L0 拆分报告 |

### 1.5 文档概述

- §2：总体描述（产品视角、用户、环境、约束、风险）
- §3：具体需求（功能、性能、安全、可靠性、易用性）
- §4：组件架构
- §5：质量门禁
- 附录A：需求表
- 附录B：溯源矩阵
- 附录C：TBD/待定项

---

## 2. 总体描述

### 2.1 产品视角

本系统是一个嵌入式产品知识库 RAG Chatbot，旨在解决以下问题：
- 销售人员难以快速准确回答客户关于产品的复杂问题
- 潜在客户无法高效获取产品对比和推荐信息
- 产品知识分散，客户自助服务体验差

**业务目标**：
- 提升销售效率 30%，减少人工咨询响应时间
- 提高客户自助服务满意度至 85%+
- 增加网站用户停留时间和转化率

_Source_: `charter.yaml#objective.problems`, `charter.yaml#objective.business_goals`

### 2.2 核心能力

| 能力 | 描述 | 优先级 |
|------|------|--------|
| RAG 问答 | 基于知识库的问答，附带来源引用 | P0 |
| 产品推荐 | 基于需求推荐 Top-N 产品 | P0 |
| 产品比较 | 结构化对比 2-4 个产品 | P0 |
| 上下文感知 | 利用页面上下文优化检索 | P0 |
| 语音交互 | STT/TTS 支持 | P1 |
| 多语言 | 中英文双语支持 | P1 |
| 人工转接 | AI/人工切换 | P1 |

_Source_: `charter.yaml#scope.must_have`

### 2.3 用户与特征

| 用户角色 | 特征 | 主要需求 |
|----------|------|----------|
| 产品销售团队 | 需要快速获取产品知识 | 准确回答客户问题 |
| 潜在客户 | 了解产品功能 | 获取推荐和对比 |
| 现有客户 | 产品使用指导 | 问题解答 |
| 后台管理员 | 维护知识库 | 管理产品和文档 |

_Source_: `charter.yaml#stakeholders.users`

### 2.4 操作环境

**组件架构**：

| 组件 | 语言 | 路径 | 说明 |
|------|------|------|------|
| api-server | Python | apps/api | RAG Chatbot 后端 API 服务 |
| chat-widget | TypeScript | apps/widget | 可嵌入的 Chatbot 前端组件 |
| admin-dashboard | TypeScript | apps/admin | 知识库/产品数据管理后台 |

**环境配置**：

| 环境 | 数据库 | API | 缓存 |
|------|--------|-----|------|
| dev | PostgreSQL | localhost:8000 | 关闭 |
| staging | PostgreSQL | staging-chat.example.com | 开启 |
| production | PostgreSQL-HA | chat.example.com | 开启 |

_Source_: `charter.yaml#environments`, `charter.yaml#components`

### 2.5 约束与依赖

**资源约束**：
- 云服务月成本 < $5000
- 交付截止日期: 2026-02-28

**技术约束**：
- 允许：Python(FastAPI), TypeScript/React, PostgreSQL+pgvector, Redis, OpenAI/Ollama
- 禁止：自建 LLM 训练, Pinecone, 私有化数据库

**外部依赖**：
- 现有产品网站（提供嵌入入口）
- 产品数据 JSON（约 600 SKU）
- LLM API（OpenAI/Ollama）

_Source_: `charter.yaml#constraints`, `charter.yaml#dependencies`

### 2.6 风险分析

| 风险 | 影响 | 应对措施 |
|------|------|----------|
| LLM API 成本超支 | 高 | Token 用量监控、缓存与限流 |
| RAG 检索准确性不足 | 高 | 评估分段/召回/重排策略 |
| 产品知识过期 | 中 | 版本管理与有效期提示 |
| Prompt Injection | 高 | 输入输出过滤、审计日志 |
| 高并发性能下降 | 中 | 缓存策略、异步处理 |

_Source_: `charter.yaml#risks`

---

## 3. 具体需求

### 3.1 功能需求

本系统包含 15 项功能需求，按组件分类：

**Widget (WGT)**：4 项 - 嵌入式组件、语音交互、多语言、文件上传

**Admin (ADM)**：3 项 - 产品数据管理、知识库索引、后台 UI

**API (API)**：7 项 - RAG 问答、推荐、对比、上下文、历史、LLM 切换、人工转接

**Shared (SHARED)**：1 项 - 邮箱登录

详见附录 A 的 `section: functional` 条目。

_Source_: `charter.yaml#scope.must_have`

### 3.2 性能需求

| 指标 | 目标 | 验收标准 |
|------|------|----------|
| 端到端响应 p95 | <= 1.5s | 压测报告 |
| 检索延迟 p95 | <= 500ms | 接口压测 |
| 并发会话 | >= 100 | 无错误响应 |

详见附录 A 的 `section: performance` 条目。

_Source_: `charter.yaml#metrics.performance`

### 3.3 安全需求

- HTTPS 强制加密
- 敏感数据脱敏
- API 频率限制
- Prompt Injection 防护

详见附录 A 的 `section: security` 条目。

_Source_: `charter.yaml#metrics.security`

### 3.4 可靠性需求

- 月可用性 >= 99.5%
- LLM/数据库异常自动恢复
- 优雅降级

详见附录 A 的 `section: reliability` 条目。

_Source_: `charter.yaml#metrics.stability`

### 3.5 易用性需求

- Widget 加载 <= 1s
- 移动端自适应
- 无需培训

详见附录 A 的 `section: usability` 条目。

_Source_: `charter.yaml#metrics.usability`

---

## 4. 组件架构

```
┌─────────────────────────────────────────────────────────────┐
│                    External Website                          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                  chat-widget (TS)                    │    │
│  │  - 嵌入式界面                                        │    │
│  │  - 语音交互 (STT/TTS)                                │    │
│  │  - 多语言 UI                                         │    │
│  │  - 文件/图片上传                                     │    │
│  └──────────────────────┬──────────────────────────────┘    │
└─────────────────────────│───────────────────────────────────┘
                          │ REST API / WebSocket
┌─────────────────────────▼───────────────────────────────────┐
│                    api-server (Python)                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ RAG 问答 │ │ 推荐引擎 │ │ 对比引擎 │ │ 历史管理 │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│  ┌──────────────────────────────────────────────────┐       │
│  │              LLM Adapter (OpenAI/Ollama)          │       │
│  └──────────────────────────────────────────────────┘       │
└──────────────────────────┬──────────────────────────────────┘
                           │
    ┌──────────────────────┼──────────────────────┐
    │                      │                      │
┌───▼───┐            ┌─────▼─────┐          ┌─────▼─────┐
│ Redis │            │ PostgreSQL│          │   LLM     │
│       │            │ + pgvector│          │  Provider │
└───────┘            └───────────┘          └───────────┘

┌─────────────────────────────────────────────────────────────┐
│                  admin-dashboard (TS)                        │
│  - 产品 JSON 管理                                            │
│  - 文档上传 / 索引构建                                       │
│  - 人工客服工作台                                            │
│  - 寻价线索管理                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. 质量门禁

| 维度 | 指标 | 目标 |
|------|------|------|
| 测试覆盖率 | 代码覆盖 | 95% |
| 类型覆盖率 | TypeScript/Python | 100% |
| 复杂度 | McCabe | <= 10 |
| 响应时间 | p95 | <= 1500ms |
| 吞吐量 | RPS | >= 100 |
| 漏洞扫描 | 依赖审计 | 必须通过 |

_Source_: `charter.yaml#quality_requirements`

---

## 附录

### 附录 A：需求表

| REQ-ID | Priority | Statement | Section | Status |
|--------|----------|-----------|---------|--------|
| REQ-L0-WGT-001 | P0 | 提供可嵌入的 Chatbot Widget | functional | draft |
| REQ-L0-WGT-002 | P1 | Widget 支持语音输入/输出 | functional | draft |
| REQ-L0-WGT-003 | P1 | 中文/英文双语支持 | functional | draft |
| REQ-L0-WGT-004 | P1 | 文件/图片上传输入 | functional | draft |
| REQ-L0-ADM-001 | P0 | 产品数据导入与查询 | functional | draft |
| REQ-L0-ADM-002 | P0 | 知识库导入与索引 | functional | draft |
| REQ-L0-ADM-003 | P0 | 后台管理 UI | functional | draft |
| REQ-L0-API-001 | P0 | RAG 问答（附带引用） | functional | draft |
| REQ-L0-API-002 | P0 | 产品推荐 Top-N | functional | draft |
| REQ-L0-API-003 | P0 | 产品比较 2-4 SKU | functional | draft |
| REQ-L0-API-004 | P0 | 上下文感知 | functional | draft |
| REQ-L0-API-005 | P0 | 对话历史管理 | functional | draft |
| REQ-L0-API-006 | P0 | LLM Provider 可配置切换 | functional | draft |
| REQ-L0-API-007 | P1 | 人工/AI 入口切换 | functional | draft |
| REQ-L0-SHARED-001 | P1 | 邮箱登录（验证码） | functional | draft |
| REQ-L0-PERF-001 | P0 | 响应时间 p95 <= 1.5s | performance | draft |
| REQ-L0-PERF-002 | P0 | 检索延迟 p95 <= 500ms | performance | draft |
| REQ-L0-PERF-003 | P0 | 并发会话 >= 100 | performance | draft |
| REQ-L0-SEC-001 | P0 | HTTPS 加密通信 | security | draft |
| REQ-L0-SEC-002 | P0 | 敏感数据脱敏 | security | draft |
| REQ-L0-SEC-003 | P0 | API 频率限制 + 审计日志 | security | draft |
| REQ-L0-SEC-004 | P0 | Prompt Injection 防护 | security | draft |
| REQ-L0-STAB-001 | P0 | 月可用性 >= 99.5% | reliability | draft |
| REQ-L0-STAB-002 | P0 | 自动恢复与降级 | reliability | draft |
| REQ-L0-UX-001 | P0 | Widget 加载 <= 1s | usability | draft |
| REQ-L0-UX-002 | P0 | 移动端自适应 | usability | draft |
| REQ-L0-UX-003 | P0 | 无需培训 | usability | draft |
| REQ-L0-CON-001 | P0 | 月成本 < $5000 | constraint | draft |
| REQ-L0-CON-002 | P0 | 交付截止 2026-02-28 | constraint | draft |
| REQ-L0-CON-003 | P0 | 允许技术栈 | constraint | draft |
| REQ-L0-CON-004 | P0 | 禁止技术栈 | constraint | draft |

### 附录 B：溯源矩阵（Charter → L0）

| Charter Item | Type | Covered By | Status |
|--------------|------|------------|--------|
| SCOPE-MH-001 | scope | REQ-L0-WGT-001 | ✅ |
| SCOPE-MH-002 | scope | REQ-L0-ADM-001 | ✅ |
| SCOPE-MH-003 | scope | REQ-L0-ADM-002 | ✅ |
| SCOPE-MH-004 | scope | REQ-L0-API-001 | ✅ |
| SCOPE-MH-005 | scope | REQ-L0-API-002 | ✅ |
| SCOPE-MH-006 | scope | REQ-L0-API-003 | ✅ |
| SCOPE-MH-007 | scope | REQ-L0-API-004 | ✅ |
| SCOPE-MH-008 | scope | REQ-L0-API-005 | ✅ |
| SCOPE-MH-009 | scope | REQ-L0-ADM-003 | ✅ |
| SCOPE-MH-010 | scope | REQ-L0-API-006 | ✅ |
| SCOPE-MH-011 | scope | REQ-L0-API-007 | ✅ |
| SCOPE-MH-012 | scope | REQ-L0-WGT-002 | ✅ |
| SCOPE-MH-013 | scope | REQ-L0-WGT-003 | ✅ |
| SCOPE-MH-014 | scope | REQ-L0-WGT-004 | ✅ |
| SCOPE-MH-015 | scope | REQ-L0-SHARED-001 | ✅ |
| MET-PERF-001 | metric | REQ-L0-PERF-001 | ✅ |
| MET-PERF-002 | metric | REQ-L0-PERF-002 | ✅ |
| MET-PERF-003 | metric | REQ-L0-PERF-003 | ✅ |
| MET-SEC-001 | metric | REQ-L0-SEC-001 | ✅ |
| MET-SEC-002 | metric | REQ-L0-SEC-002 | ✅ |
| MET-SEC-003 | metric | REQ-L0-SEC-003 | ✅ |
| MET-SEC-004 | metric | REQ-L0-SEC-004 | ✅ |
| MET-STAB-001 | metric | REQ-L0-STAB-001 | ✅ |
| MET-STAB-002 | metric | REQ-L0-STAB-002 | ✅ |
| MET-UX-001 | metric | REQ-L0-UX-001 | ✅ |
| MET-UX-002 | metric | REQ-L0-UX-002 | ✅ |
| MET-UX-003 | metric | REQ-L0-UX-003 | ✅ |
| CONSTRAINT-RES | constraint | REQ-L0-CON-001/002 | ✅ |
| CONSTRAINT-TECH | constraint | REQ-L0-CON-003/004 | ✅ |
| SCOPE-OOS-001 | exclusion | Exclusion | ✅ |
| SCOPE-OOS-002 | exclusion | Exclusion | ✅ |
| SCOPE-OOS-005 | exclusion | Exclusion | ✅ |
| SCOPE-OOS-006 | exclusion | Exclusion | ✅ |
| TBD-001~012 | tbd | TBD-L0-001~012 | ✅ |

**Coverage**: 100% (15 scope + 12 metrics + 4 constraints + 4 exclusions + 12 TBDs)

### 附录 C：TBD/待定项

| TBD-ID | Question | Impact | Owner | Target Layer | Status |
|--------|----------|--------|-------|--------------|--------|
| TBD-L0-001 | LLM Provider/Model 选择 | H | Product Owner | L0 | open |
| TBD-L0-002 | 降级策略定义 | M | Architect | L1 | open |
| TBD-L0-003 | 后台鉴权方式 | H | Architect | L0 | open |
| TBD-L0-004 | 日志留存策略 | M | Legal/Security | L1 | open |
| TBD-L0-005 | 推荐/比较字段配置 | L | Product Owner | L1 | open |
| TBD-L0-006 | Widget 资源体积 | L | Frontend Lead | L2 | open |
| TBD-L0-007 | STT/TTS Provider | M | Architect | L1 | open |
| TBD-L0-008 | 文件上传规格 | M | Security | L1 | open |
| TBD-L0-009 | 多语言策略 | M | Product Owner | L1 | open |
| TBD-L0-010 | 邮箱验证码方案 | M | Security | L1 | open |
| TBD-L0-011 | 人工客服转接 | M | Product Owner | L1 | open |
| TBD-L0-012 | 寻价功能定义 | M | Product Owner | L1 | open |

> ⚠️ **High Impact TBDs**: TBD-L0-001（LLM 选择）和 TBD-L0-003（后台鉴权）需在 L0 阶段解决。

---

## 门禁检查

> 由 `/requirements-validate L0` 自动校验。

- [x] Registry 所有 `requirements[]` 有非空 `sources[]`
- [x] P0/P1 需求有非空 `acceptance[]`
- [x] Charter 关键条目 100% 覆盖（REQ / TBD / Exclusion）
- [x] 无交叉引用错位（`tbd_refs[]` 指向存在的 TBD）
- [x] `derived: true` 的需求有 `rationale`（无 derived 需求）
- [x] Traceability: strict 模式已满足

---

## 变更记录

| 版本 | 日期 | 作者 | 变更说明 |
|------|------|------|----------|
| v0.1 | 2026-01-15 | architect-agent | 初始版本，从 charter.yaml 生成 |
