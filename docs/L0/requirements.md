---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "from-charter"
profile: "python,typescript"
caf_version: v0.6.5
---

# L0 Requirements: RAG Chatbot System

> ⚠️ **Document Structure (Template v2.0 / CAF v0.6.5)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Body text | Generated | 🔒 Readonly |

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# L0 Requirements Registry - System Level
# Schema: v1.0 | Template: v2.0 | CAF: v0.6.5
# =============================================================================

schema_version: "v0.6.5"
layer: L0
parent: "charter.yaml"
profile: "python,typescript"

# -----------------------------------------------------------------------------
# Functional Requirements
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
    status: draft
    section: functional
    tbd_refs: []

  - id: REQ-L0-WGT-002
    priority: P1
    statement: "Widget 支持语音输入（STT）与语音输出（TTS），STT/TTS Provider 可配置。"
    sources:
      - id: "SCOPE-MH-012"
        path: "charter.yaml#scope.must_have[11]"
    acceptance:
      - "用户可点击语音按钮录音并转换为文字输入"
      - "AI 回复可通过语音播放"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-007]

  - id: REQ-L0-WGT-003
    priority: P1
    statement: "Widget 与后台 UI 支持中文/英文双语，用户可选择输出语言。"
    sources:
      - id: "SCOPE-MH-013"
        path: "charter.yaml#scope.must_have[12]"
    acceptance:
      - "Widget 界面文案支持中英文切换"
      - "用户可设置首选输出语言"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-009]

  - id: REQ-L0-WGT-004
    priority: P1
    statement: "Widget 支持用户上传文件或图片作为对话输入，系统提取内容用于回答。"
    sources:
      - id: "SCOPE-MH-014"
        path: "charter.yaml#scope.must_have[13]"
    acceptance:
      - "支持常见文件格式（PDF、Word、图片）上传"
      - "系统可解析文件内容并参与 RAG 问答"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-008]

  # ===========================================================================
  # Admin Dashboard (ADM) - 后台管理
  # ===========================================================================
  - id: REQ-L0-ADM-001
    priority: P0
    statement: "支持产品数据导入与查询，从 JSON 文件加载约 600 SKU，支持后台上传/替换与基础检索。"
    sources:
      - id: "SCOPE-MH-002"
        path: "charter.yaml#scope.must_have[1]"
    acceptance:
      - "系统启动时可加载指定 JSON 文件"
      - "后台可上传新 JSON 替换旧数据"
    status: draft
    section: functional
    tbd_refs: []

  - id: REQ-L0-ADM-002
    priority: P0
    statement: "支持知识库导入与索引：后台上传文档并写入 PostgreSQL + pgvector，支持重建索引与状态查看。"
    sources:
      - id: "SCOPE-MH-003"
        path: "charter.yaml#scope.must_have[2]"
    acceptance:
      - "可通过后台上传文档（PDF/Word/TXT）"
      - "文档内容被向量化并存入 pgvector"
    status: draft
    section: functional
    tbd_refs: []

  - id: REQ-L0-ADM-003
    priority: P0
    statement: "提供后台管理 UI，包含产品管理、文档上传、索引状态、操作日志、人工客服处理、寻价线索管理。"
    sources:
      - id: "SCOPE-MH-009"
        path: "charter.yaml#scope.must_have[8]"
    acceptance:
      - "后台提供统一管理界面"
      - "人工客服可查看转接请求并处理"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-003, TBD-L0-011, TBD-L0-012]

  # ===========================================================================
  # API Server (API) - 后端核心服务
  # ===========================================================================
  - id: REQ-L0-API-001
    priority: P0
    statement: "支持 RAG 问答，回答默认附带来源引用，无足够依据时优先澄清或拒答。"
    sources:
      - id: "SCOPE-MH-004"
        path: "charter.yaml#scope.must_have[3]"
    acceptance:
      - "回答包含明确的引用来源标记"
      - "当问题与知识库无关时，模型能够拒绝回答"
    status: draft
    section: functional
    tbd_refs: []

  - id: REQ-L0-API-002
    priority: P0
    statement: "支持产品推荐：基于用户需求输出 Top-N（默认 3）SKU，包含推荐理由与依据来源。"
    sources:
      - id: "SCOPE-MH-005"
        path: "charter.yaml#scope.must_have[4]"
    acceptance:
      - "针对用户需求返回 Top-3 推荐产品"
      - "每个推荐包含推荐理由"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]

  - id: REQ-L0-API-003
    priority: P0
    statement: "支持产品比较：支持 2–4 个 SKU，输出结构化对比（表格/卡片）。"
    sources:
      - id: "SCOPE-MH-006"
        path: "charter.yaml#scope.must_have[5]"
    acceptance:
      - "可对比 2-4 个产品"
      - "输出结构化表格/卡片形式"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-005]

  - id: REQ-L0-API-004
    priority: P0
    statement: "支持上下文感知：Widget 可传入当前页面 productId/skuId/url，后端用于检索与排序。"
    sources:
      - id: "SCOPE-MH-007"
        path: "charter.yaml#scope.must_have[6]"
    acceptance:
      - "后端可接收并解析上下文参数"
      - "上下文影响检索结果排序"
    status: draft
    section: functional
    tbd_refs: []

  - id: REQ-L0-API-005
    priority: P0
    statement: "支持对话历史管理：多轮对话，记录引用、错误与 token 用量。"
    sources:
      - id: "SCOPE-MH-008"
        path: "charter.yaml#scope.must_have[7]"
    acceptance:
      - "支持多轮对话上下文"
      - "记录每次对话的 token 用量"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-004]

  - id: REQ-L0-API-006
    priority: P0
    statement: "LLM Provider 可配置切换：支持在线 OpenAI-Compatible API 与本地 Ollama 两种模式。"
    sources:
      - id: "SCOPE-MH-010"
        path: "charter.yaml#scope.must_have[9]"
    acceptance:
      - "可通过配置切换 LLM Provider"
      - "在线和本地模式均可正常工作"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-001]

  - id: REQ-L0-API-007
    priority: P1
    statement: "支持人工/AI 入口切换：用户可选择人工或 AI，选择人工时转接至后台队列。"
    sources:
      - id: "SCOPE-MH-011"
        path: "charter.yaml#scope.must_have[10]"
    acceptance:
      - "Widget 提供人工/AI 切换按钮"
      - "选择人工后，对话进入后台处理队列"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-011]

  # ===========================================================================
  # Shared (SHARED) - 跨组件功能
  # ===========================================================================
  - id: REQ-L0-SHARED-001
    priority: P1
    statement: "支持邮箱登录（验证码）：Widget 支持邮箱验证码登录/验证，登录后解锁寻价与人工客服功能。"
    sources:
      - id: "SCOPE-MH-015"
        path: "charter.yaml#scope.must_have[14]"
    acceptance:
      - "用户输入邮箱可收到验证码"
      - "验证通过后状态为已登录"
    status: draft
    section: functional
    tbd_refs: [TBD-L0-010]

  # ===========================================================================
  # Performance (PERF)
  # ===========================================================================
  - id: REQ-L0-PERF-001
    priority: P0
    statement: "端到端首次响应时间（包含 LLM）p95 <= 1.5s。"
    sources:
      - id: "MET-PERF-001"
        path: "charter.yaml#metrics.performance[0]"
    acceptance:
      - "压测报告显示 p95 响应时间 <= 1.5s"
    status: draft
    section: performance
    tbd_refs: []

  - id: REQ-L0-PERF-002
    priority: P0
    statement: "RAG 检索延迟 p95 <= 500ms。"
    sources:
      - id: "MET-PERF-002"
        path: "charter.yaml#metrics.performance[1]"
    acceptance:
      - "检索接口单独压测 p95 <= 500ms"
    status: draft
    section: performance
    tbd_refs: []

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

  # ===========================================================================
  # Security (SEC)
  # ===========================================================================
  - id: REQ-L0-SEC-001
    priority: P0
    statement: "所有通信强制使用 HTTPS 加密。"
    sources:
      - id: "MET-SEC-001"
        path: "charter.yaml#metrics.security[0]"
    acceptance:
      - "非 HTTPS 请求被拒绝或重定向"
    status: draft
    section: security
    tbd_refs: []

  - id: REQ-L0-SEC-002
    priority: P0
    statement: "敏感数据（如手机号/邮箱）需脱敏处理。"
    sources:
      - id: "MET-SEC-002"
        path: "charter.yaml#metrics.security[1]"
    acceptance:
      - "日志和 API 返回中无明文敏感信息"
    status: draft
    section: security
    tbd_refs: []

  - id: REQ-L0-SEC-003
    priority: P0
    statement: "实施 API 访问频率限制，并记录后台操作审计日志。"
    sources:
      - id: "MET-SEC-003"
        path: "charter.yaml#metrics.security[2]"
    acceptance:
      - "超出频率限制的请求返回 429"
    status: draft
    section: security
    tbd_refs: []

  - id: REQ-L0-SEC-004
    priority: P0
    statement: "实施 Prompt Injection 基础防护，确保系统提示不被覆盖。"
    sources:
      - id: "MET-SEC-004"
        path: "charter.yaml#metrics.security[3]"
    acceptance:
      - "攻击性 Prompt 不会泄露系统设定"
    status: draft
    section: security
    tbd_refs: []

  # ===========================================================================
  # Stability (STAB)
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

  - id: REQ-L0-STAB-002
    priority: P0
    statement: "LLM/数据库异常时支持自动恢复与优雅降级。"
    sources:
      - id: "MET-STAB-002"
        path: "charter.yaml#metrics.stability[1]"
    acceptance:
      - "模拟数据库断连后能自动恢复"
    status: draft
    section: reliability
    tbd_refs: [TBD-L0-002]

  # ===========================================================================
  # Usability (UX)
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

  - id: REQ-L0-UX-002
    priority: P0
    statement: "支持移动端自适应布局。"
    sources:
      - id: "MET-UX-002"
        path: "charter.yaml#metrics.usability[1]"
    acceptance:
      - "移动端布局显示正常"
    status: draft
    section: usability
    tbd_refs: []

  - id: REQ-L0-UX-003
    priority: P0
    statement: "无需用户培训即可使用。"
    sources:
      - id: "MET-UX-003"
        path: "charter.yaml#metrics.usability[2]"
    acceptance:
      - "新用户可直接上手使用"
    status: draft
    section: usability
    tbd_refs: []

  # ===========================================================================
  # Constraints (CON)
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

  # ===========================================================================
  # Risk Mitigation (RISK) - v0.6.2 新增
  # ===========================================================================
  - id: REQ-L0-RISK-001
    priority: P0
    statement: "实施风险缓解: Token 用量监控、缓存与限流策略。"
    sources:
      - id: "RISK-001"
        path: "charter.yaml#risks[0]"
    acceptance:
      - "Token 用量监控面板可用"
      - "缓存命中率 > 30%"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-002
    priority: P1
    statement: "实施风险缓解: 分段/召回/重排策略，支持 Embedding 模型切换。"
    sources:
      - id: "RISK-002"
        path: "charter.yaml#risks[1]"
    acceptance:
      - "Embedding 模型可配置"
      - "检索准确性评测集通过"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-003
    priority: P1
    statement: "实施风险缓解: 知识库版本管理与有效期提示。"
    sources:
      - id: "RISK-003"
        path: "charter.yaml#risks[2]"
    acceptance:
      - "回答附带引用更新时间"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-004
    priority: P0
    statement: "实施风险缓解: 输入输出过滤、引用转义、最小权限、审计日志。"
    sources:
      - id: "RISK-004"
        path: "charter.yaml#risks[3]"
    acceptance:
      - "Prompt Injection 测试用例通过"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-005
    priority: P0
    statement: "实施风险缓解: 缓存策略、异步处理与连接池优化。"
    sources:
      - id: "RISK-005"
        path: "charter.yaml#risks[4]"
    acceptance:
      - "高并发压测通过"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-006
    priority: P1
    statement: "实施风险缓解: 文件类型与大小限制、内容扫描、脱敏与保留期策略。"
    sources:
      - id: "RISK-006"
        path: "charter.yaml#risks[5]"
    acceptance:
      - "恶意文件上传被拒绝"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-007
    priority: P1
    statement: "实施风险缓解: 语音功能提供开关、缓存与降级策略。"
    sources:
      - id: "RISK-007"
        path: "charter.yaml#risks[6]"
    acceptance:
      - "语音功能可通过配置关闭"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-008
    priority: P1
    statement: "实施风险缓解: 选择支持中英的模型/Embedding，建立评测集。"
    sources:
      - id: "RISK-008"
        path: "charter.yaml#risks[7]"
    acceptance:
      - "多语言评测集通过"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-009
    priority: P1
    statement: "实施风险缓解: 邮箱验证码频控、验证策略、审计日志。"
    sources:
      - id: "RISK-009"
        path: "charter.yaml#risks[8]"
    acceptance:
      - "刷码攻击被拦截"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-010
    priority: P1
    statement: "实施风险缓解: 人工客服 SLA、排队策略、离线收集联系方式。"
    sources:
      - id: "RISK-010"
        path: "charter.yaml#risks[9]"
    acceptance:
      - "无人接待时回退到 AI"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  - id: REQ-L0-RISK-011
    priority: P1
    statement: "实施风险缓解: 寻价数据最小化收集、脱敏、访问控制与留存策略。"
    sources:
      - id: "RISK-011"
        path: "charter.yaml#risks[10]"
    acceptance:
      - "敏感数据脱敏存储"
    status: draft
    section: risk_mitigation
    tbd_refs: []

  # ===========================================================================
  # Dependencies (DEP) - v0.6.2 新增
  # ===========================================================================
  - id: REQ-L0-DEP-001
    priority: P0
    statement: "依赖外部系统: 现有产品网站（提供嵌入入口与页面上下文）。"
    sources:
      - id: "DEP-EXT-001"
        path: "charter.yaml#dependencies.external_systems[0]"
    acceptance:
      - "产品网站可嵌入 Widget"
      - "上下文参数传递正常"
    status: draft
    section: dependency
    tbd_refs: []

  - id: REQ-L0-DEP-002
    priority: P2
    statement: "可选依赖: 现有网站登录态/用户标识注入。"
    sources:
      - id: "DEP-EXT-002"
        path: "charter.yaml#dependencies.external_systems[1]"
    acceptance:
      - "可选：识别已登录用户"
    status: draft
    section: dependency
    tbd_refs: []

  - id: REQ-L0-DEP-003
    priority: P0
    statement: "依赖资源: 产品数据 JSON（约 600 SKU）。"
    sources:
      - id: "DEP-RES-001"
        path: "charter.yaml#dependencies.resources[0]"
    acceptance:
      - "产品数据 JSON 可加载"
    status: draft
    section: dependency
    tbd_refs: []

  - id: REQ-L0-DEP-004
    priority: P0
    statement: "依赖资源: 产品文档、FAQ、知识库资料。"
    sources:
      - id: "DEP-RES-002"
        path: "charter.yaml#dependencies.resources[1]"
    acceptance:
      - "知识库资料可上传处理"
    status: draft
    section: dependency
    tbd_refs: []

  - id: REQ-L0-DEP-005
    priority: P0
    statement: "依赖资源: PostgreSQL（启用 pgvector 扩展）。"
    sources:
      - id: "DEP-RES-003"
        path: "charter.yaml#dependencies.resources[2]"
    acceptance:
      - "pgvector 查询正常"
    status: draft
    section: dependency
    tbd_refs: []

  - id: REQ-L0-DEP-006
    priority: P0
    statement: "依赖资源: OpenAI-Compatible API 密钥。"
    sources:
      - id: "DEP-RES-004"
        path: "charter.yaml#dependencies.resources[3]"
    acceptance:
      - "API 调用正常"
    status: draft
    section: dependency
    tbd_refs: [TBD-L0-001]

  - id: REQ-L0-DEP-007
    priority: P1
    statement: "依赖资源: Ollama 服务与模型文件。"
    sources:
      - id: "DEP-RES-005"
        path: "charter.yaml#dependencies.resources[4]"
    acceptance:
      - "本地模型推理正常"
    status: draft
    section: dependency
    tbd_refs: [TBD-L0-001]

  - id: REQ-L0-DEP-008
    priority: P1
    statement: "依赖资源: STT/TTS Provider。"
    sources:
      - id: "DEP-RES-006"
        path: "charter.yaml#dependencies.resources[5]"
    acceptance:
      - "语音转文字和播放正常"
    status: draft
    section: dependency
    tbd_refs: [TBD-L0-007]

  - id: REQ-L0-DEP-009
    priority: P1
    statement: "依赖资源: 文件/图片存储与内容提取能力。"
    sources:
      - id: "DEP-RES-007"
        path: "charter.yaml#dependencies.resources[6]"
    acceptance:
      - "文件可上传并提取内容"
    status: draft
    section: dependency
    tbd_refs: [TBD-L0-008]

  - id: REQ-L0-DEP-010
    priority: P1
    statement: "依赖资源: 邮件发送/验证码服务。"
    sources:
      - id: "DEP-RES-008"
        path: "charter.yaml#dependencies.resources[7]"
    acceptance:
      - "验证码邮件可发送"
    status: draft
    section: dependency
    tbd_refs: [TBD-L0-010]

# -----------------------------------------------------------------------------
# TBDs
# -----------------------------------------------------------------------------
tbds:
  - id: TBD-L0-001
    question: "LLM Provider/Model 选择与成本上限分配"
    sources:
      - id: "TBD-001"
        path: "charter.yaml#open_questions[0]"
    impact: H
    owner: "Product Owner"
    target_layer: L0
    status: open

  - id: TBD-L0-002
    question: "降级策略定义：LLM/pgvector 不可用时的用户体验"
    sources:
      - id: "TBD-002"
        path: "charter.yaml#open_questions[1]"
    impact: M
    owner: "Architect"
    target_layer: L1
    status: open

  - id: TBD-L0-003
    question: "后台鉴权具体方式（白名单/Basic Auth/SSO）"
    sources:
      - id: "TBD-003"
        path: "charter.yaml#open_questions[2]"
    impact: H
    owner: "Architect"
    target_layer: L0
    status: open

  - id: TBD-L0-004
    question: "对话与日志留存策略：保留期、脱敏范围"
    sources:
      - id: "TBD-004"
        path: "charter.yaml#open_questions[3]"
    impact: M
    owner: "Legal"
    target_layer: L1
    status: open

  - id: TBD-L0-005
    question: "推荐/比较的字段配置来源"
    sources:
      - id: "TBD-005"
        path: "charter.yaml#open_questions[4]"
    impact: L
    owner: "Product Owner"
    target_layer: L2
    status: open

  - id: TBD-L0-006
    question: "Widget 资源体积与加载口径"
    sources:
      - id: "TBD-006"
        path: "charter.yaml#open_questions[5]"
    impact: L
    owner: "Frontend Lead"
    target_layer: L2
    status: open

  - id: TBD-L0-007
    question: "STT/TTS Provider 选择与部署方式"
    sources:
      - id: "TBD-007"
        path: "charter.yaml#open_questions[6]"
    impact: M
    owner: "Backend Lead"
    target_layer: L1
    status: open

  - id: TBD-L0-008
    question: "文件/图片上传支持格式与大小限制"
    sources:
      - id: "TBD-008"
        path: "charter.yaml#open_questions[7]"
    impact: M
    owner: "Backend Lead"
    target_layer: L1
    status: open

  - id: TBD-L0-009
    question: "多语言策略：语言检测/选择规则"
    sources:
      - id: "TBD-009"
        path: "charter.yaml#open_questions[8]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open

  - id: TBD-L0-010
    question: "邮箱登录方案：验证码策略、发送渠道"
    sources:
      - id: "TBD-010"
        path: "charter.yaml#open_questions[9]"
    impact: M
    owner: "Security"
    target_layer: L1
    status: open

  - id: TBD-L0-011
    question: "人工客服转接方案：工作台形态、排队机制"
    sources:
      - id: "TBD-011"
        path: "charter.yaml#open_questions[10]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open

  - id: TBD-L0-012
    question: "寻价功能定义：收集字段、触发条件"
    sources:
      - id: "TBD-012"
        path: "charter.yaml#open_questions[11]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open

# -----------------------------------------------------------------------------
# Exclusions
# -----------------------------------------------------------------------------
exclusions:
  - source: "SCOPE-OOS-001"
    reason: "不做完整认证/账号体系（仅提供邮箱验证码登录）"
    category: scope
  - source: "SCOPE-OOS-002"
    reason: "订单处理和支付功能"
    category: scope
  - source: "SCOPE-OOS-005"
    reason: "知识库自动爬取/同步（V0.1 仅手动上传）"
    category: deferred
  - source: "SCOPE-OOS-006"
    reason: "自建 LLM 训练"
    category: scope
```

## — END REGISTRY —

---

## Summary

| Category | Count |
|----------|-------|
| Functional (WGT/ADM/API/SHARED) | 15 |
| Performance (PERF) | 3 |
| Security (SEC) | 4 |
| Stability (STAB) | 2 |
| Usability (UX) | 3 |
| Constraints (CON) | 4 |
| **Risk Mitigation (RISK)** | 11 |
| **Dependencies (DEP)** | 10 |
| TBDs | 12 |
| Exclusions | 4 |
| **Total Requirements** | **52** |

---

## Gate Check

- [x] All requirements have `sources[]`
- [x] All P0/P1 have `acceptance[]`
- [x] Risks covered: 11/11
- [x] Dependencies covered: 10/10
- [x] TBDs have `target_layer`

---

## Requirements

| ID | Priority | Statement | Sources | Acceptance | Status |
|----|----------|-----------|---------|------------|--------|
| REQ-L0-WGT-001 | P0 | 提供可嵌入的 Chatbot Widget，支持集成到现有产品网站，并提供最小集成示例。 | SCOPE-MH-001 | 2 | draft |
| REQ-L0-WGT-002 | P1 | Widget 支持语音输入（STT）与语音输出（TTS），STT/TTS Provider 可配置。 | SCOPE-MH-012 | 2 | draft |
| REQ-L0-WGT-003 | P1 | Widget 与后台 UI 支持中文/英文双语，用户可选择输出语言。 | SCOPE-MH-013 | 2 | draft |
| REQ-L0-WGT-004 | P1 | Widget 支持用户上传文件或图片作为对话输入，系统提取内容用于回答。 | SCOPE-MH-014 | 2 | draft |
| REQ-L0-ADM-001 | P0 | 支持产品数据导入与查询，从 JSON 文件加载约 600 SKU，支持后台上传/替换与基础检索。 | SCOPE-MH-002 | 2 | draft |
| REQ-L0-ADM-002 | P0 | 支持知识库导入与索引：后台上传文档并写入 PostgreSQL + pgvector，支持重建索引与状态查看。 | SCOPE-MH-003 | 2 | draft |
| REQ-L0-ADM-003 | P0 | 提供后台管理 UI，包含产品管理、文档上传、索引状态、操作日志、人工客服处理、寻价线索管理。 | SCOPE-MH-009 | 2 | draft |
| REQ-L0-API-001 | P0 | 支持 RAG 问答，回答默认附带来源引用，无足够依据时优先澄清或拒答。 | SCOPE-MH-004 | 2 | draft |
| REQ-L0-API-002 | P0 | 支持产品推荐：基于用户需求输出 Top-N（默认 3）SKU，包含推荐理由与依据来源。 | SCOPE-MH-005 | 2 | draft |
| REQ-L0-API-003 | P0 | 支持产品比较：支持 2–4 个 SKU，输出结构化对比（表格/卡片）。 | SCOPE-MH-006 | 2 | draft |
| REQ-L0-API-004 | P0 | 支持上下文感知：Widget 可传入当前页面 productId/skuId/url，后端用于检索与排序。 | SCOPE-MH-007 | 2 | draft |
| REQ-L0-API-005 | P0 | 支持对话历史管理：多轮对话，记录引用、错误与 token 用量。 | SCOPE-MH-008 | 2 | draft |
| REQ-L0-API-006 | P0 | LLM Provider 可配置切换：支持在线 OpenAI-Compatible API 与本地 Ollama 两种模式。 | SCOPE-MH-010 | 2 | draft |
| REQ-L0-API-007 | P1 | 支持人工/AI 入口切换：用户可选择人工或 AI，选择人工时转接至后台队列。 | SCOPE-MH-011 | 2 | draft |
| REQ-L0-SHARED-001 | P1 | 支持邮箱登录（验证码）：Widget 支持邮箱验证码登录/验证，登录后解锁寻价与人工客服功能。 | SCOPE-MH-015 | 2 | draft |
| REQ-L0-PERF-001 | P0 | 端到端首次响应时间（包含 LLM）p95 <= 1.5s。 | MET-PERF-001 | 1 | draft |
| REQ-L0-PERF-002 | P0 | RAG 检索延迟 p95 <= 500ms。 | MET-PERF-002 | 1 | draft |
| REQ-L0-PERF-003 | P0 | 支持并发会话 >= 100（连接保持 5 分钟）。 | MET-PERF-003 | 1 | draft |
| REQ-L0-SEC-001 | P0 | 所有通信强制使用 HTTPS 加密。 | MET-SEC-001 | 1 | draft |
| REQ-L0-SEC-002 | P0 | 敏感数据（如手机号/邮箱）需脱敏处理。 | MET-SEC-002 | 1 | draft |
| REQ-L0-SEC-003 | P0 | 实施 API 访问频率限制，并记录后台操作审计日志。 | MET-SEC-003 | 1 | draft |
| REQ-L0-SEC-004 | P0 | 实施 Prompt Injection 基础防护，确保系统提示不被覆盖。 | MET-SEC-004 | 1 | draft |
| REQ-L0-STAB-001 | P0 | 系统月可用性 >= 99.5%。 | MET-STAB-001 | 1 | draft |
| REQ-L0-STAB-002 | P0 | LLM/数据库异常时支持自动恢复与优雅降级。 | MET-STAB-002 | 1 | draft |
| REQ-L0-UX-001 | P0 | Widget 加载时间 <= 1s。 | MET-UX-001 | 1 | draft |
| REQ-L0-UX-002 | P0 | 支持移动端自适应布局。 | MET-UX-002 | 1 | draft |
| REQ-L0-UX-003 | P0 | 无需用户培训即可使用。 | MET-UX-003 | 1 | draft |
| REQ-L0-CON-001 | P0 | 云服务月成本 < $5000（含 LLM token、数据库、日志/监控、存储与带宽）。 | CONSTRAINT-RES-001 | 1 | draft |
| REQ-L0-CON-002 | P0 | 交付截止日期: 2026-02-28。 | CONSTRAINT-RES-002 | 1 | draft |
| REQ-L0-CON-003 | P0 | 技术栈限制：仅使用 Python(FastAPI), TypeScript/React, PostgreSQL+pgvector, Redis, OpenAI/Ollama。 | CONSTRAINT-TECH-001 | 1 | draft |
| REQ-L0-CON-004 | P0 | 禁止：自建 LLM 训练、使用 Pinecone、私有化部署专有数据库。 | CONSTRAINT-TECH-002 | 1 | draft |
| REQ-L0-RISK-001 | P0 | 实施风险缓解: Token 用量监控、缓存与限流策略。 | RISK-001 | 2 | draft |
| REQ-L0-RISK-002 | P1 | 实施风险缓解: 分段/召回/重排策略，支持 Embedding 模型切换。 | RISK-002 | 2 | draft |
| REQ-L0-RISK-003 | P1 | 实施风险缓解: 知识库版本管理与有效期提示。 | RISK-003 | 1 | draft |
| REQ-L0-RISK-004 | P0 | 实施风险缓解: 输入输出过滤、引用转义、最小权限、审计日志。 | RISK-004 | 1 | draft |
| REQ-L0-RISK-005 | P0 | 实施风险缓解: 缓存策略、异步处理与连接池优化。 | RISK-005 | 1 | draft |
| REQ-L0-RISK-006 | P1 | 实施风险缓解: 文件类型与大小限制、内容扫描、脱敏与保留期策略。 | RISK-006 | 1 | draft |
| REQ-L0-RISK-007 | P1 | 实施风险缓解: 语音功能提供开关、缓存与降级策略。 | RISK-007 | 1 | draft |
| REQ-L0-RISK-008 | P1 | 实施风险缓解: 选择支持中英的模型/Embedding，建立评测集。 | RISK-008 | 1 | draft |
| REQ-L0-RISK-009 | P1 | 实施风险缓解: 邮箱验证码频控、验证策略、审计日志。 | RISK-009 | 1 | draft |
| REQ-L0-RISK-010 | P1 | 实施风险缓解: 人工客服 SLA、排队策略、离线收集联系方式。 | RISK-010 | 1 | draft |
| REQ-L0-RISK-011 | P1 | 实施风险缓解: 寻价数据最小化收集、脱敏、访问控制与留存策略。 | RISK-011 | 1 | draft |
| REQ-L0-DEP-001 | P0 | 依赖外部系统: 现有产品网站（提供嵌入入口与页面上下文）。 | DEP-EXT-001 | 2 | draft |
| REQ-L0-DEP-002 | P2 | 可选依赖: 现有网站登录态/用户标识注入。 | DEP-EXT-002 | 1 | draft |
| REQ-L0-DEP-003 | P0 | 依赖资源: 产品数据 JSON（约 600 SKU）。 | DEP-RES-001 | 1 | draft |
| REQ-L0-DEP-004 | P0 | 依赖资源: 产品文档、FAQ、知识库资料。 | DEP-RES-002 | 1 | draft |
| REQ-L0-DEP-005 | P0 | 依赖资源: PostgreSQL（启用 pgvector 扩展）。 | DEP-RES-003 | 1 | draft |
| REQ-L0-DEP-006 | P0 | 依赖资源: OpenAI-Compatible API 密钥。 | DEP-RES-004 | 1 | draft |
| REQ-L0-DEP-007 | P1 | 依赖资源: Ollama 服务与模型文件。 | DEP-RES-005 | 1 | draft |
| REQ-L0-DEP-008 | P1 | 依赖资源: STT/TTS Provider。 | DEP-RES-006 | 1 | draft |
| REQ-L0-DEP-009 | P1 | 依赖资源: 文件/图片存储与内容提取能力。 | DEP-RES-007 | 1 | draft |
| REQ-L0-DEP-010 | P1 | 依赖资源: 邮件发送/验证码服务。 | DEP-RES-008 | 1 | draft |

## Traceability

| Requirement | Source ID | Source Path |
|------------|-----------|-------------|
| REQ-L0-WGT-001 | SCOPE-MH-001 | charter.yaml#scope.must_have[0] |
| REQ-L0-WGT-002 | SCOPE-MH-012 | charter.yaml#scope.must_have[11] |
| REQ-L0-WGT-003 | SCOPE-MH-013 | charter.yaml#scope.must_have[12] |
| REQ-L0-WGT-004 | SCOPE-MH-014 | charter.yaml#scope.must_have[13] |
| REQ-L0-ADM-001 | SCOPE-MH-002 | charter.yaml#scope.must_have[1] |
| REQ-L0-ADM-002 | SCOPE-MH-003 | charter.yaml#scope.must_have[2] |
| REQ-L0-ADM-003 | SCOPE-MH-009 | charter.yaml#scope.must_have[8] |
| REQ-L0-API-001 | SCOPE-MH-004 | charter.yaml#scope.must_have[3] |
| REQ-L0-API-002 | SCOPE-MH-005 | charter.yaml#scope.must_have[4] |
| REQ-L0-API-003 | SCOPE-MH-006 | charter.yaml#scope.must_have[5] |
| REQ-L0-API-004 | SCOPE-MH-007 | charter.yaml#scope.must_have[6] |
| REQ-L0-API-005 | SCOPE-MH-008 | charter.yaml#scope.must_have[7] |
| REQ-L0-API-006 | SCOPE-MH-010 | charter.yaml#scope.must_have[9] |
| REQ-L0-API-007 | SCOPE-MH-011 | charter.yaml#scope.must_have[10] |
| REQ-L0-SHARED-001 | SCOPE-MH-015 | charter.yaml#scope.must_have[14] |
| REQ-L0-PERF-001 | MET-PERF-001 | charter.yaml#metrics.performance[0] |
| REQ-L0-PERF-002 | MET-PERF-002 | charter.yaml#metrics.performance[1] |
| REQ-L0-PERF-003 | MET-PERF-003 | charter.yaml#metrics.performance[2] |
| REQ-L0-SEC-001 | MET-SEC-001 | charter.yaml#metrics.security[0] |
| REQ-L0-SEC-002 | MET-SEC-002 | charter.yaml#metrics.security[1] |
| REQ-L0-SEC-003 | MET-SEC-003 | charter.yaml#metrics.security[2] |
| REQ-L0-SEC-004 | MET-SEC-004 | charter.yaml#metrics.security[3] |
| REQ-L0-STAB-001 | MET-STAB-001 | charter.yaml#metrics.stability[0] |
| REQ-L0-STAB-002 | MET-STAB-002 | charter.yaml#metrics.stability[1] |
| REQ-L0-UX-001 | MET-UX-001 | charter.yaml#metrics.usability[0] |
| REQ-L0-UX-002 | MET-UX-002 | charter.yaml#metrics.usability[1] |
| REQ-L0-UX-003 | MET-UX-003 | charter.yaml#metrics.usability[2] |
| REQ-L0-CON-001 | CONSTRAINT-RES-001 | charter.yaml#constraints.resource.budget |
| REQ-L0-CON-002 | CONSTRAINT-RES-002 | charter.yaml#constraints.resource.timeline |
| REQ-L0-CON-003 | CONSTRAINT-TECH-001 | charter.yaml#constraints.technology_boundary.allowed |
| REQ-L0-CON-004 | CONSTRAINT-TECH-002 | charter.yaml#constraints.technology_boundary.forbidden |
| REQ-L0-RISK-001 | RISK-001 | charter.yaml#risks[0] |
| REQ-L0-RISK-002 | RISK-002 | charter.yaml#risks[1] |
| REQ-L0-RISK-003 | RISK-003 | charter.yaml#risks[2] |
| REQ-L0-RISK-004 | RISK-004 | charter.yaml#risks[3] |
| REQ-L0-RISK-005 | RISK-005 | charter.yaml#risks[4] |
| REQ-L0-RISK-006 | RISK-006 | charter.yaml#risks[5] |
| REQ-L0-RISK-007 | RISK-007 | charter.yaml#risks[6] |
| REQ-L0-RISK-008 | RISK-008 | charter.yaml#risks[7] |
| REQ-L0-RISK-009 | RISK-009 | charter.yaml#risks[8] |
| REQ-L0-RISK-010 | RISK-010 | charter.yaml#risks[9] |
| REQ-L0-RISK-011 | RISK-011 | charter.yaml#risks[10] |
| REQ-L0-DEP-001 | DEP-EXT-001 | charter.yaml#dependencies.external_systems[0] |
| REQ-L0-DEP-002 | DEP-EXT-002 | charter.yaml#dependencies.external_systems[1] |
| REQ-L0-DEP-003 | DEP-RES-001 | charter.yaml#dependencies.resources[0] |
| REQ-L0-DEP-004 | DEP-RES-002 | charter.yaml#dependencies.resources[1] |
| REQ-L0-DEP-005 | DEP-RES-003 | charter.yaml#dependencies.resources[2] |
| REQ-L0-DEP-006 | DEP-RES-004 | charter.yaml#dependencies.resources[3] |
| REQ-L0-DEP-007 | DEP-RES-005 | charter.yaml#dependencies.resources[4] |
| REQ-L0-DEP-008 | DEP-RES-006 | charter.yaml#dependencies.resources[5] |
| REQ-L0-DEP-009 | DEP-RES-007 | charter.yaml#dependencies.resources[6] |
| REQ-L0-DEP-010 | DEP-RES-008 | charter.yaml#dependencies.resources[7] |

## TBDs

| TBD ID | Question | Target Layer | Impact | Status |
|--------|----------|--------------|--------|--------|
| TBD-L0-001 | LLM Provider/Model 选择与成本上限分配 | L0 | H | open |
| TBD-L0-002 | 降级策略定义：LLM/pgvector 不可用时的用户体验 | L1 | M | open |
| TBD-L0-003 | 后台鉴权具体方式（白名单/Basic Auth/SSO） | L0 | H | open |
| TBD-L0-004 | 对话与日志留存策略：保留期、脱敏范围 | L1 | M | open |
| TBD-L0-005 | 推荐/比较的字段配置来源 | L2 | L | open |
| TBD-L0-006 | Widget 资源体积与加载口径 | L2 | L | open |
| TBD-L0-007 | STT/TTS Provider 选择与部署方式 | L1 | M | open |
| TBD-L0-008 | 文件/图片上传支持格式与大小限制 | L1 | M | open |
| TBD-L0-009 | 多语言策略：语言检测/选择规则 | L1 | M | open |
| TBD-L0-010 | 邮箱登录方案：验证码策略、发送渠道 | L1 | M | open |
| TBD-L0-011 | 人工客服转接方案：工作台形态、排队机制 | L1 | M | open |
| TBD-L0-012 | 寻价功能定义：收集字段、触发条件 | L1 | M | open |

## Exclusions

- SCOPE-OOS-001: 不做完整认证/账号体系（仅提供邮箱验证码登录）
- SCOPE-OOS-002: 订单处理和支付功能
- SCOPE-OOS-005: 知识库自动爬取/同步（V0.1 仅手动上传）
- SCOPE-OOS-006: 自建 LLM 训练
