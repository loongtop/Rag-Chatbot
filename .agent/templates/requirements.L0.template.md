---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "{checksum}"
profile: "{profile}"
---

# L0 Requirements: {system_name}

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
source_checksum: "{checksum}"
profile: "{profile}"

# -----------------------------------------------------------------------------
# Requirements
# -----------------------------------------------------------------------------
requirements:
  # --- Widget (WGT) ---
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
    derived: false

  # --- Admin & Data (ADM) ---
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

  # --- API & Core (API) ---
  - id: REQ-L0-API-001
    priority: P0
    statement: "支持 RAG 问答，回答默认附带来源引用（文档/产品字段），无足够依据时优先澄清或拒答。"
    sources:
      - id: "SCOPE-MH-004"
        path: "charter.yaml#scope.must_have[3]"
    acceptance:
      - "回答包含明确的引用来源标记"
      - "当问题与知识库无关时，模型能够拒绝回答"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  # --- Shared (SHARED) ---
  - id: REQ-L0-SHARED-001
    priority: P1
    statement: "支持邮箱登录（验证码），登录后关联用户行为，解锁寻价与人工客服功能。"
    sources:
      - id: "SCOPE-MH-015"
        path: "charter.yaml#scope.must_have[14]"
    acceptance:
      - "用户输入邮箱可收到验证码"
      - "验证通过后状态为已登录"
      - "未登录用户点击寻价提示登录"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

  # --- Performance ---
  - id: REQ-L0-PERF-001
    priority: P0
    statement: "端到端首次响应时间（包含 LLM）p95 <= 1.5s。"
    sources:
      - id: "MET-PERF-001"
        path: "charter.yaml#metrics.performance[0]"
    acceptance:
      - "压测报告显示 p95 响应时间满足指标"
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
      - "检索接口单独压测满足指标"
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

  # --- Security ---
  - id: REQ-L0-SEC-001
    priority: P0
    statement: "所有通信强制使用 HTTPS 加密，且敏感数据（手机/邮箱）需脱敏处理。"
    sources:
      - id: "MET-SEC-001"
        path: "charter.yaml#metrics.security[0]"
      - id: "MET-SEC-002"
        path: "charter.yaml#metrics.security[1]"
    acceptance:
      - "非 HTTPS 请求被拒绝或重定向"
      - "日志和 API 返回中无明文敏感信息"
    status: draft
    section: security
    tbd_refs: []
    derived: false

  - id: REQ-L0-SEC-002
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

  - id: REQ-L0-SEC-003
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
    derived: false

  # --- Reliability ---
  - id: REQ-L0-STAB-001
    priority: P0
    statement: "系统月可用性 >= 99.5%，具备 LLM/数据库异常自动恢复与降级能力。"
    sources:
      - id: "MET-STAB-001"
        path: "charter.yaml#metrics.stability[0]"
      - id: "MET-STAB-002"
        path: "charter.yaml#metrics.stability[1]"
    acceptance:
      - "模拟数据库断连后能自动恢复"
      - "LLM 不可用时返回友好降级提示"
    status: draft
    section: reliability
    tbd_refs: []
    derived: false

  # --- Usability ---
  - id: REQ-L0-UX-001
    priority: P0
    statement: "Widget 加载时间 <= 1s，支持移动端自适应，且无需培训即可使用。"
    sources:
      - id: "MET-UX-001"
        path: "charter.yaml#metrics.usability[0]"
      - id: "MET-UX-002"
        path: "charter.yaml#metrics.usability[1]"
      - id: "MET-UX-003"
        path: "charter.yaml#metrics.usability[2]"
    acceptance:
      - "移动端布局显示正常"
      - "资源加载时长监控满足指标"
    status: draft
    section: usability
    tbd_refs: []
    derived: false

  # --- Constraints (v0.5.1 自动提取) ---
  - id: REQ-L0-CON-BUDGET
    priority: P0
    statement: "云服务月成本 < $5000。"
    sources:
      - id: "CONSTRAINT-RES-001"
        path: "charter.yaml#constraints.resource.budget"
    acceptance:
      - "成本测算模型显示达标"
    status: draft
    section: constraint
    tbd_refs: []
    derived: false

  - id: REQ-L0-CON-TIMELINE
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

  - id: REQ-L0-CON-TECH-ALLOWED
    priority: P0
    statement: "技术栈限制：Python(FastAPI), TypeScript/React, PostgreSQL+pgvector, Redis, OpenAI/Ollama。"
    sources:
      - id: "CONSTRAINT-TECH-001"
        path: "charter.yaml#constraints.technology_boundary.allowed"
    acceptance:
      - "代码库依赖检查符合规定"
    status: draft
    section: constraint
    tbd_refs: []
    derived: false

  - id: REQ-L0-CON-TECH-FORBIDDEN
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
    question: "LLM Provider/Model 选择与成本分配"
    sources:
      - id: "TBD-001"
        path: "charter.yaml#open_questions[0]"
    impact: H
    owner: "Product Owner"
    target_layer: L0
    status: open
    related_reqs: []
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
    related_reqs: [REQ-L0-STAB-001]

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
    related_reqs: [REQ-L0-API-007]

  - id: TBD-L0-012
    question: "寻价功能定义与 CRM 对接"
    sources:
      - id: "TBD-012"
        path: "charter.yaml#open_questions[11]"
    impact: M
    owner: "Product Owner"
    target_layer: L1
    status: open
    related_reqs: [REQ-L0-SHARED-001]

# -----------------------------------------------------------------------------
# Exclusions (N/A with reason) - 逐条提取
# -----------------------------------------------------------------------------
exclusions:
  - source:
      id: "SCOPE-OOS-001"
      path: "charter.yaml#scope.out_of_scope[0]"
    reason: "不做完整认证/账号体系：不支持密码登录、第三方 OAuth/SSO、多因素认证、复杂权限管理（仅提供邮箱验证码登录作为最小能力）"
    category: scope
  - source:
      id: "SCOPE-OOS-002"
      path: "charter.yaml#scope.out_of_scope[1]"
    reason: "订单处理和支付功能不在当前范围内"
    category: scope
  - source:
      id: "SCOPE-OOS-005"
      path: "charter.yaml#scope.out_of_scope[4]"
    reason: "知识库自动爬取/自动同步（V0.1 仅支持手动上传/替换）"
    category: deferred
  - source:
      id: "SCOPE-OOS-006"
      path: "charter.yaml#scope.out_of_scope[5]"
    reason: "自建 LLM 训练不在范围内"
    category: scope
  - source:
      path: "charter.yaml#traceability"
    reason: "Process configuration, not a deliverable requirement"
    category: process_config
  - source:
      path: "charter.yaml#freeze"
    reason: "Freeze metadata, not a deliverable requirement"
    category: meta
```

## — END REGISTRY —

---

<!-- =========================================================================
     GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY
     Regenerate with: /requirements-render L0
     ========================================================================= -->

## 1. 引言

### 1.1 目的

本文档定义了 {system_name} 的 L0（系统级）需求规格说明，是下游 L1/L2/L3 需求分解的唯一事实来源。

本文档的预期读者包括：项目发起人、产品经理、架构师、开发团队、测试团队。

_Source_: `charter.yaml#meta`  
_Covered by_: N/A (document metadata)

### 1.2 范围

{系统边界定义 - 从 Registry 自动生成}

_Source_: `charter.yaml#scope.must_have`, `charter.yaml#scope.out_of_scope`  
_Covered by_: `REQ-L0-9xx` (Constraints)

### 1.3 定义与术语

| 术语 | 定义 |
|------|------|
| RAG | Retrieval-Augmented Generation，检索增强生成 |
| LLM | Large Language Model，大型语言模型 |
| SKU | Stock Keeping Unit，库存单位 |

### 1.4 参考文档

| 文档 | 版本/Checksum | 说明 |
|------|--------------|------|
| `charter.yaml` | `{checksum}` | 项目任务书（已冻结） |
| `docs/L0/split-report.md` | - | Charter → L0 拆分报告 |
| `.agent/docs/srs-template.md` | - | SRS 模板参考 |

### 1.5 文档概述

- §2：总体描述（产品视角、用户、环境、约束、风险）
- §3：具体需求（功能、性能、安全、可靠性、易用性）
- §4：输入/输出
- §5：质量门禁
- 附录A：需求表（从 Registry 渲染）
- 附录B：溯源矩阵（从 Registry 渲染）
- 附录C：TBD/待定项（从 Registry 渲染）

---

## 2. 总体描述

### 2.1 产品视角

{系统在整体架构中的定位 - 从 Registry 自动生成}

_Source_: `charter.yaml#objective.problems`, `charter.yaml#objective.business_goals`  
_Covered by_: `REQ-L0-001`

### 2.2 核心能力

{系统核心能力概述 - 从 Registry 自动生成}

_Source_: `charter.yaml#scope.must_have`  
_Covered by_: `REQ-L0-002` ~ `REQ-L0-0xx`

### 2.3 用户与特征

{用户角色与特征 - 从 Registry 自动生成}

_Source_: `charter.yaml#stakeholders.users`  
_Covered by_: `REQ-L0-0xx`

### 2.4 操作环境

{运行环境说明 - 从 Registry 自动生成}

_Source_: `charter.yaml#environments`, `charter.yaml#components`  
_Covered by_: `REQ-L0-9xx`

### 2.5 约束与依赖

{技术、资源、时间约束 - 从 Registry 自动生成}

_Source_: `charter.yaml#constraints`, `charter.yaml#dependencies`  
_Covered by_: `REQ-L0-9xx`

### 2.6 风险分析

{风险识别与应对 - 从 Registry 自动生成}

_Source_: `charter.yaml#risks`  
_Covered by_: `REQ-L0-2xx` (Security), `REQ-L0-3xx` (Reliability)

---

## 3. 具体需求

### 3.1 功能需求

{功能需求叙述概述 - 不重复 Registry 原文，提供上下文}

详见附录 A 的 `section: functional` 条目。

_Source_: `charter.yaml#scope.must_have`  
_Covered by_: `REQ-L0-001` ~ `REQ-L0-0xx`

### 3.2 性能需求

{性能需求叙述概述}

详见附录 A 的 `section: performance` 条目。

_Source_: `charter.yaml#metrics.performance`, `charter.yaml#quality_requirements.performance`  
_Covered by_: `REQ-L0-1xx`

### 3.3 安全需求

{安全需求叙述概述}

详见附录 A 的 `section: security` 条目。

_Source_: `charter.yaml#metrics.security`, `charter.yaml#quality_requirements.security`  
_Covered by_: `REQ-L0-2xx`

### 3.4 可靠性需求

{可靠性需求叙述概述}

详见附录 A 的 `section: reliability` 条目。

_Source_: `charter.yaml#metrics.stability`  
_Covered by_: `REQ-L0-3xx`

### 3.5 易用性需求

{易用性需求叙述概述}

详见附录 A 的 `section: usability` 条目。

_Source_: `charter.yaml#metrics.usability`  
_Covered by_: `REQ-L0-4xx`

---

## 4. 输入/输出

### 4.1 输入

{系统输入定义 - 从 Registry 自动生成}

### 4.2 输出

{系统输出定义 - 从 Registry 自动生成}

---

## 5. 质量门禁

{质量门禁要求 - 从 Registry 自动生成}

_Source_: `charter.yaml#quality_requirements`  
_Covered by_: `REQ-L0-9xx`

---

## 附录

### 附录 A：需求表

> 从 Registry `requirements[]` 自动渲染。

| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| {从 Registry 渲染} | | | | | |

### 附录 B：溯源矩阵（Charter → L0）

> 从 Registry `requirements[].sources[]` + `exclusions[]` 反向汇聚。
> 每条 Charter 关键条目必须出现在 REQ、TBD 或 Exclusion 中。

| Charter Item | Covered By | Status | Notes |
|--------------|------------|--------|-------|
| {从 Registry 渲染} | | | |

### 附录 C：TBD/待定项

> 从 Registry `tbds[]` 自动渲染。

| TBD-ID | Question | Sources | Impact | Owner | Target Layer | Status |
|--------|----------|---------|--------|-------|--------------|--------|
| {从 Registry 渲染} | | | | | | |

---

## 门禁检查

> 由 `/requirements-validate L0` 自动校验。

- [ ] Registry 所有 `requirements[]` 有非空 `sources[]`
- [ ] P0/P1 需求有非空 `acceptance[]`
- [ ] Charter 关键条目 100% 覆盖（REQ / TBD / Exclusion）
- [ ] 无交叉引用错位（`tbd_refs[]` 指向存在的 TBD）
- [ ] `derived: true` 的需求有 `rationale`

---

## 变更记录

| 版本 | 日期 | 作者 | 变更说明 |
|------|------|------|----------|
| v0.1 | {date} | {author} | 初始版本 |
