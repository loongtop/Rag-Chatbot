---
status: done
owner: requirements_split
layer_from: Charter
layer_to: L0
parent: charter.yaml
target: docs/L0/requirements.md
granularity: medium
decomposition_path: L0→L2→L3
---

# Split Report: Charter → L0

## 1. Summary（结论）

- **Decision**: PASS
- **Why**: Charter 已冻结（frozen=true），所有 15 项 scope.must_have、4 类 metrics、资源/技术约束均可映射为可验证的 L0 需求；12 项 TBD 已识别并分配 target_layer。
- **Granularity Mode**: `medium` (`L0→L2→L3`)
- **Complexity Assessment**: Medium

## 2. Inputs（输入）

| Item | Path | Version/Checksum | Notes |
|------|------|------------------|-------|
| Source | `charter.yaml` | `5fa5705024b8...` | frozen=true, v0.1 |
| Target | `docs/L0/requirements.md` | - | 待生成 |
| Traceability Mode | `charter.yaml#traceability.mode` | `strict` | 必须通过 Gate |
| Components | `charter.yaml#components` | | Count: 3 |

## 3. Split Rules（拆分规则）

- **Granularity**: `medium` (L0→L2→L3)
  - 跳过 L1 层，scope 条目直接按组件分解到 L2

- **REQ-ID 分类规则** (v0.5.0):
  - 组件专属: `REQ-L0-{COMP}-*` (基于 charter.yaml#components)
  - 共享功能: `REQ-L0-SHARED-*` (跨组件功能)
  - 性能: `REQ-L0-PERF-*` (MET-PERF-*)
  - 安全: `REQ-L0-SEC-*` (MET-SEC-*)
  - 稳定: `REQ-L0-STAB-*` (MET-STAB-*)
  - 易用: `REQ-L0-UX-*` (MET-UX-*)
  - 约束: `REQ-L0-CON-*` (constraints)

- **组件前缀映射**:
  - `api-server` → API
  - `chat-widget` → WGT
  - `admin-dashboard` → ADM

## 4. Granularity Decision（粒度决策）

| Dimension | Value | Score |
|-----------|-------|-------|
| Scope items (must_have) | 15 | 2 (>10) |
| Components | 3 | 2 (=3) |
| Cross-module deps | 2 (WGT→API, ADM→API) | 1 |
| **Total Score** | | 5 |
| **Assessment** | | Medium |
| **Recommended Path** | | `medium` (L0→L2→L3) |

> 评判：15 项 scope > 10，组件数 = 3，存在跨模块依赖，选择 `medium` 跳过 L1 直接分解到 L2。

## 5. Source Inventory（上游条目清单）

### 5.1 Scope Must-Have (15 items)

| SRC-ID | Upstream Item | Type | Component |
|--------|---------------|------|-----------|
| SRC-001 | `[SCOPE-MH-001] 嵌入式 Chatbot Widget` | requirement | WGT |
| SRC-002 | `[SCOPE-MH-002] 产品数据导入与查询` | requirement | ADM |
| SRC-003 | `[SCOPE-MH-003] 知识库导入与索引` | requirement | ADM |
| SRC-004 | `[SCOPE-MH-004] RAG 问答` | requirement | API |
| SRC-005 | `[SCOPE-MH-005] 产品推荐` | requirement | API |
| SRC-006 | `[SCOPE-MH-006] 产品比较` | requirement | API |
| SRC-007 | `[SCOPE-MH-007] 上下文感知` | requirement | API |
| SRC-008 | `[SCOPE-MH-008] 对话历史管理` | requirement | API |
| SRC-009 | `[SCOPE-MH-009] 后台管理 UI` | requirement | ADM |
| SRC-010 | `[SCOPE-MH-010] LLM Provider 可配置切换` | requirement | API |
| SRC-011 | `[SCOPE-MH-011] 人工/AI 入口切换` | requirement | API |
| SRC-012 | `[SCOPE-MH-012] 语音交互` | requirement | WGT |
| SRC-013 | `[SCOPE-MH-013] 多语言支持` | requirement | WGT |
| SRC-014 | `[SCOPE-MH-014] 文件/图片输入` | requirement | WGT |
| SRC-015 | `[SCOPE-MH-015] 邮箱登录（验证码）` | requirement | SHARED |

### 5.2 Metrics (12 items)

| SRC-ID | Upstream Item | Type | Category |
|--------|---------------|------|----------|
| SRC-016 | `[MET-PERF-001] 端到端首次响应时间 p95 <= 1.5s` | metric | PERF |
| SRC-017 | `[MET-PERF-002] RAG 检索延迟 p95 <= 500ms` | metric | PERF |
| SRC-018 | `[MET-PERF-003] 并发会话支持 >= 100` | metric | PERF |
| SRC-019 | `[MET-SEC-001] HTTPS 加密通信` | metric | SEC |
| SRC-020 | `[MET-SEC-002] 敏感数据脱敏处理` | metric | SEC |
| SRC-021 | `[MET-SEC-003] API 访问频率限制与审计日志` | metric | SEC |
| SRC-022 | `[MET-SEC-004] Prompt Injection 基础防护` | metric | SEC |
| SRC-023 | `[MET-STAB-001] 系统可用性 >= 99.5%` | metric | STAB |
| SRC-024 | `[MET-STAB-002] LLM/数据库异常自动恢复与降级` | metric | STAB |
| SRC-025 | `[MET-UX-001] Widget 加载时间 <= 1s` | metric | UX |
| SRC-026 | `[MET-UX-002] 移动端自适应支持` | metric | UX |
| SRC-027 | `[MET-UX-003] 无需用户培训即可使用` | metric | UX |

### 5.3 Constraints (4 items)

| SRC-ID | Upstream Item | Type | Category |
|--------|---------------|------|----------|
| SRC-028 | `resource.budget: 云服务月成本 < $5000` | constraint | resource |
| SRC-029 | `resource.timeline: 2026-02-28` | constraint | resource |
| SRC-030 | `technology_boundary.allowed: [Python, TS, PG+pgvector, ...]` | constraint | allowed |
| SRC-031 | `technology_boundary.forbidden: [自建 LLM, Pinecone, ...]` | constraint | forbidden |

### 5.4 Out of Scope (4 items)

| SRC-ID | Upstream Item | Type |
|--------|---------------|------|
| SRC-032 | `[SCOPE-OOS-001] 不做完整认证/账号体系` | exclusion |
| SRC-033 | `[SCOPE-OOS-002] 订单处理和支付功能` | exclusion |
| SRC-034 | `[SCOPE-OOS-005] 知识库自动爬取/同步` | exclusion |
| SRC-035 | `[SCOPE-OOS-006] 自建 LLM 训练` | exclusion |

### 5.5 Open Questions / TBD (12 items)

| SRC-ID | Upstream Item | Type | Impact |
|--------|---------------|------|--------|
| SRC-036 | `[TBD-001] LLM Provider/Model 选择` | tbd | H |
| SRC-037 | `[TBD-002] 降级策略定义` | tbd | M |
| SRC-038 | `[TBD-003] 后台鉴权方式` | tbd | H |
| SRC-039 | `[TBD-004] 对话与日志留存策略` | tbd | M |
| SRC-040 | `[TBD-005] 推荐/比较字段配置来源` | tbd | L |
| SRC-041 | `[TBD-006] Widget 资源体积与加载口径` | tbd | L |
| SRC-042 | `[TBD-007] STT/TTS Provider 选择` | tbd | M |
| SRC-043 | `[TBD-008] 文件/图片上传支持格式` | tbd | M |
| SRC-044 | `[TBD-009] 多语言策略细节` | tbd | M |
| SRC-045 | `[TBD-010] 邮箱登录方案` | tbd | M |
| SRC-046 | `[TBD-011] 人工客服转接方案` | tbd | M |
| SRC-047 | `[TBD-012] 寻价功能定义` | tbd | M |

## 6. Mapping & Split Decisions（映射与拆分决策）

### 6.1 Scope → Requirements

| SRC-ID | Decision | REQ-ID | Source | Notes |
|--------|----------|--------|--------|-------|
| SRC-001 | split | REQ-L0-WGT-001 | `charter.yaml#scope.must_have[0]` | Widget 嵌入 |
| SRC-002 | split | REQ-L0-ADM-001 | `charter.yaml#scope.must_have[1]` | 产品数据管理 |
| SRC-003 | split | REQ-L0-ADM-002 | `charter.yaml#scope.must_have[2]` | 知识库索引 |
| SRC-004 | split | REQ-L0-API-001 | `charter.yaml#scope.must_have[3]` | RAG 问答核心 |
| SRC-005 | split | REQ-L0-API-002 | `charter.yaml#scope.must_have[4]` | 推荐功能 |
| SRC-006 | split | REQ-L0-API-003 | `charter.yaml#scope.must_have[5]` | 比较功能 |
| SRC-007 | split | REQ-L0-API-004 | `charter.yaml#scope.must_have[6]` | 上下文感知 |
| SRC-008 | split | REQ-L0-API-005 | `charter.yaml#scope.must_have[7]` | 对话历史 |
| SRC-009 | split | REQ-L0-ADM-003 | `charter.yaml#scope.must_have[8]` | 后台管理 UI |
| SRC-010 | split | REQ-L0-API-006 | `charter.yaml#scope.must_have[9]` | LLM 切换 |
| SRC-011 | split | REQ-L0-API-007 | `charter.yaml#scope.must_have[10]` | 人工/AI 切换 |
| SRC-012 | split | REQ-L0-WGT-002 | `charter.yaml#scope.must_have[11]` | 语音交互 |
| SRC-013 | split | REQ-L0-WGT-003 | `charter.yaml#scope.must_have[12]` | 多语言支持 |
| SRC-014 | split | REQ-L0-WGT-004 | `charter.yaml#scope.must_have[13]` | 文件/图片输入 |
| SRC-015 | split | REQ-L0-SHARED-001 | `charter.yaml#scope.must_have[14]` | 邮箱登录 |

### 6.2 Metrics → Requirements

| SRC-ID | Decision | REQ-ID | Source |
|--------|----------|--------|--------|
| SRC-016 | split | REQ-L0-PERF-001 | `charter.yaml#metrics.performance[0]` |
| SRC-017 | split | REQ-L0-PERF-002 | `charter.yaml#metrics.performance[1]` |
| SRC-018 | split | REQ-L0-PERF-003 | `charter.yaml#metrics.performance[2]` |
| SRC-019 | split | REQ-L0-SEC-001 | `charter.yaml#metrics.security[0]` |
| SRC-020 | split | REQ-L0-SEC-002 | `charter.yaml#metrics.security[1]` |
| SRC-021 | split | REQ-L0-SEC-003 | `charter.yaml#metrics.security[2]` |
| SRC-022 | split | REQ-L0-SEC-004 | `charter.yaml#metrics.security[3]` |
| SRC-023 | split | REQ-L0-STAB-001 | `charter.yaml#metrics.stability[0]` |
| SRC-024 | split | REQ-L0-STAB-002 | `charter.yaml#metrics.stability[1]` |
| SRC-025 | split | REQ-L0-UX-001 | `charter.yaml#metrics.usability[0]` |
| SRC-026 | split | REQ-L0-UX-002 | `charter.yaml#metrics.usability[1]` |
| SRC-027 | split | REQ-L0-UX-003 | `charter.yaml#metrics.usability[2]` |

### 6.3 Constraints → Requirements

| SRC-ID | Decision | REQ-ID | Source |
|--------|----------|--------|--------|
| SRC-028 | split | REQ-L0-CON-BUDGET | `charter.yaml#constraints.resource.budget` |
| SRC-029 | split | REQ-L0-CON-TIMELINE | `charter.yaml#constraints.resource.timeline` |
| SRC-030 | split | REQ-L0-CON-TECH-ALLOWED | `charter.yaml#constraints.technology_boundary.allowed` |
| SRC-031 | split | REQ-L0-CON-TECH-FORBIDDEN | `charter.yaml#constraints.technology_boundary.forbidden` |

## 7. Cross-Layer Traceability（跨层追溯）

> medium 模式：L0→L2→L3，跳过 L1

**计划追溯路径**：

| L0 Prefix | L2 Target Dir | Notes |
|-----------|---------------|-------|
| REQ-L0-API-* | `docs/L2/api-server/` | 后端 API 模块分解 |
| REQ-L0-WGT-* | `docs/L2/chat-widget/` | Widget 模块分解 |
| REQ-L0-ADM-* | `docs/L2/admin-dashboard/` | 后台管理模块分解 |
| REQ-L0-SHARED-* | 各组件共享 | 邮箱登录等跨组件功能 |
| REQ-L0-PERF/SEC/STAB/UX-* | 各组件验收标准 | 非功能性需求 |
| REQ-L0-CON-* | 全局约束 | 预算/时间/技术栈 |

## 8. Traceability Matrix（覆盖矩阵）

| Upstream | Covered By | Status | Notes |
|----------|------------|--------|-------|
| SCOPE-MH-001 | REQ-L0-WGT-001 | ✅ | |
| SCOPE-MH-002 | REQ-L0-ADM-001 | ✅ | |
| SCOPE-MH-003 | REQ-L0-ADM-002 | ✅ | |
| SCOPE-MH-004 | REQ-L0-API-001 | ✅ | |
| SCOPE-MH-005 | REQ-L0-API-002 | ✅ | |
| SCOPE-MH-006 | REQ-L0-API-003 | ✅ | |
| SCOPE-MH-007 | REQ-L0-API-004 | ✅ | |
| SCOPE-MH-008 | REQ-L0-API-005 | ✅ | |
| SCOPE-MH-009 | REQ-L0-ADM-003 | ✅ | |
| SCOPE-MH-010 | REQ-L0-API-006 | ✅ | |
| SCOPE-MH-011 | REQ-L0-API-007 | ✅ | |
| SCOPE-MH-012 | REQ-L0-WGT-002 | ✅ | |
| SCOPE-MH-013 | REQ-L0-WGT-003 | ✅ | |
| SCOPE-MH-014 | REQ-L0-WGT-004 | ✅ | |
| SCOPE-MH-015 | REQ-L0-SHARED-001 | ✅ | |
| MET-PERF-001 | REQ-L0-PERF-001 | ✅ | |
| MET-PERF-002 | REQ-L0-PERF-002 | ✅ | |
| MET-PERF-003 | REQ-L0-PERF-003 | ✅ | |
| MET-SEC-001 | REQ-L0-SEC-001 | ✅ | |
| MET-SEC-002 | REQ-L0-SEC-002 | ✅ | |
| MET-SEC-003 | REQ-L0-SEC-003 | ✅ | |
| MET-SEC-004 | REQ-L0-SEC-004 | ✅ | |
| MET-STAB-001 | REQ-L0-STAB-001 | ✅ | |
| MET-STAB-002 | REQ-L0-STAB-002 | ✅ | |
| MET-UX-001 | REQ-L0-UX-001 | ✅ | |
| MET-UX-002 | REQ-L0-UX-002 | ✅ | |
| MET-UX-003 | REQ-L0-UX-003 | ✅ | |
| constraints.resource | REQ-L0-CON-BUDGET, REQ-L0-CON-TIMELINE | ✅ | |
| constraints.technology_boundary | REQ-L0-CON-TECH-* | ✅ | |
| scope.out_of_scope | exclusions | ✅ | 见 Section 9 |
| open_questions | TBD-L0-* | ✅ | 见 Section 12 |

## 9. Exclusions（逐条提取）

| source | reason | category |
|--------|--------|----------|
| SCOPE-OOS-001 | 不做完整认证/账号体系：不支持密码登录、第三方 OAuth/SSO、多因素认证、复杂权限管理（仅提供邮箱验证码登录作为最小能力） | scope |
| SCOPE-OOS-002 | 订单处理和支付功能 | scope |
| SCOPE-OOS-005 | 知识库自动爬取/自动同步（V0.1 仅支持手动上传/替换） | deferred |
| SCOPE-OOS-006 | 自建 LLM 训练 | scope |

## 10. Constraints（自动提取）

| ID | Statement | Source | Category |
|----|-----------|--------|----------|
| REQ-L0-CON-BUDGET | 云服务月成本 < $5000（含 LLM token、数据库、日志/监控、存储与带宽） | constraints.resource.budget | resource |
| REQ-L0-CON-TIMELINE | 交付截止日期: 2026-02-28 | constraints.resource.timeline | resource |
| REQ-L0-CON-TECH-ALLOWED | 允许: Python (FastAPI), TypeScript/JavaScript (React), PostgreSQL + pgvector, Redis, OpenAI API / Compatible LLM, Ollama, STT/TTS Provider, OCR/视觉/文档解析, SMTP/Email Provider | constraints.technology_boundary.allowed | allowed |
| REQ-L0-CON-TECH-FORBIDDEN | 禁止: 自建 LLM 训练, Pinecone, 私有化部署专有数据库 | constraints.technology_boundary.forbidden | forbidden |

## 11. 组件接口矩阵

| 组件 | 提供接口 | 依赖接口 | 说明 |
|------|----------|----------|------|
| api-server | REST API, RAG Service, WebSocket | LLM Provider, pgvector, Redis | 后端核心服务 |
| chat-widget | Widget UI, Voice IO | api-server REST API, STT/TTS Provider | 前端交互组件 |
| admin-dashboard | Admin UI, KB Management | api-server REST API | 后台管理界面 |

## 12. TBD & Questions（待定项）

| TBD-ID | Question / Missing Info | Impact | Source | Target Layer |
|--------|--------------------------|--------|--------|--------------|
| TBD-L0-001 | LLM Provider/Model 选择（OpenAI/Claude/兼容方案）与成本上限分配 | H | `charter.yaml#open_questions[0]` | L0 |
| TBD-L0-002 | 降级策略定义：LLM/pgvector 不可用时的用户体验与返回格式 | M | `charter.yaml#open_questions[1]` | L1 |
| TBD-L0-003 | 后台鉴权方式：最小可用方案（账号白名单/Basic Auth/接入现有 SSO） | H | `charter.yaml#open_questions[2]` | L0 |
| TBD-L0-004 | 对话与日志留存策略：数据保留期、脱敏范围、合规要求 | M | `charter.yaml#open_questions[3]` | L1 |
| TBD-L0-005 | 推荐/比较的"字段配置"来源：固定配置/后台可配/按类目不同 | L | `charter.yaml#open_questions[4]` | L2 |
| TBD-L0-006 | Widget 资源体积与加载口径（gzip、缓存策略、CDN） | L | `charter.yaml#open_questions[5]` | L2 |
| TBD-L0-007 | STT/TTS Provider 选择与部署方式（在线/本地）及成本/延迟预算 | M | `charter.yaml#open_questions[6]` | L1 |
| TBD-L0-008 | 文件/图片上传支持格式、大小上限、存储方式与数据保留期（合规） | M | `charter.yaml#open_questions[7]` | L1 |
| TBD-L0-009 | 多语言策略：语言检测/选择规则、知识库中英混合或翻译层、评测口径 | M | `charter.yaml#open_questions[8]` | L1 |
| TBD-L0-010 | 邮箱登录方案：验证码策略、发送渠道（SMTP/第三方）、防刷机制、合规边界 | M | `charter.yaml#open_questions[9]` | L1 |
| TBD-L0-011 | 人工客服转接方案：工作台形态、排队/通知机制、响应 SLA、回退策略 | M | `charter.yaml#open_questions[10]` | L1 |
| TBD-L0-012 | 寻价功能定义：收集字段、触发条件、是否对接 CRM/工单、处理流程与权限 | M | `charter.yaml#open_questions[11]` | L1 |

## 13. Gate Check（门禁检查）

- [x] 上游每个条目：都有映射或 `N/A + 原因`
- [x] 下游每个 `REQ-ID`：都有至少一个 `Source`
- [x] 未出现"无来源的新需求"
- [x] 关键缺失信息已进入 TBD（且带来源）
- [x] **Exclusions 检查**（v0.5.1+）：
  - [x] `scope.out_of_scope` 全部映射到 exclusions (4/4)
  - [x] 每个 exclusion 有明确 reason
- [x] **Constraints 检查**（v0.5.1+）：
  - [x] 资源约束（budget/timeline）已提取 (2/2)
  - [x] 技术约束（allowed/forbidden）已提取 (2/2)

---

**Result**: ✅ **PASS**

**Next Steps**:
1. 运行 `/requirements-render` 生成 `docs/L0/requirements.md`
2. 运行 `/requirements-validate` 验证需求文档
3. 按 `medium` 路径分解到 `docs/L2/{component}/`
