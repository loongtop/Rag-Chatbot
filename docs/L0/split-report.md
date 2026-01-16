---
status: done
owner: requirements_split
layer_from: Charter
layer_to: L0
parent: charter.yaml
target: docs/L0/requirements.md
granularity: full
decomposition_path: L0→L1→L2
caf_version: v0.6.2
---

# Split Report: Charter → L0 (v0.6.2)

## 1. Summary（结论）

- **Decision**: PASS
- **Why**: Charter 已冻结（frozen=true），100% 覆盖：scope(15) + metrics(12) + constraints(4) + exclusions(4) + TBD(12) + **risks(11)** + **dependencies(10)** + **contracts(2)**
- **Granularity Mode**: `full` (`L0→L1→L2`)
- **CAF Version**: v0.6.2

## 2. Inputs（输入）

| Item | Path | Version | Notes |
|------|------|---------|-------|
| Source | `charter.yaml` | frozen=true, v0.1 | |
| Target | `docs/L0/requirements.md` | - | 待生成 |
| Traceability Mode | `charter.yaml#traceability.mode` | `strict` | |
| Components | `charter.yaml#components` | 3 | API/WGT/ADM |
| Config | `.agent/config/split-rules.yaml` | v0.6.2 | 多语言关键词 |

## 3. Split Rules（拆分规则）

- **Granularity**: `full` (L0→L1→L2)
- **REQ-ID 分类规则** (v0.6.2):
  - 组件专属: `REQ-L0-{COMP}-*`
  - 共享功能: `REQ-L0-SHARED-*`
  - 性能/安全/稳定/易用: `REQ-L0-{PERF|SEC|STAB|UX}-*`
  - 约束: `REQ-L0-CON-*`
  - **风险缓解**: `REQ-L0-RISK-*` (v0.6.2 新增)
  - **依赖约束**: `REQ-L0-DEP-*` (v0.6.2 新增)

## 4. Granularity Decision（粒度决策）

| Dimension | Value | Score |
|-----------|-------|-------|
| Scope items (must_have) | 15 | 2 (>10) |
| Components | 3 | 2 (>=3) → **full** |
| Cross-module deps | 2 | 1 |
| **Total Score** | | 5 |
| **Recommended Path** | | `full` (L0→L1→L2) |

> v0.6.0 规则：components >= 3 强制使用 full 模式

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
| SRC-016 | `[MET-PERF-001] 端到端首次响应 p95 <= 1.5s` | metric | PERF |
| SRC-017 | `[MET-PERF-002] RAG 检索延迟 p95 <= 500ms` | metric | PERF |
| SRC-018 | `[MET-PERF-003] 并发会话 >= 100` | metric | PERF |
| SRC-019 | `[MET-SEC-001] HTTPS 加密通信` | metric | SEC |
| SRC-020 | `[MET-SEC-002] 敏感数据脱敏` | metric | SEC |
| SRC-021 | `[MET-SEC-003] API 频率限制与审计` | metric | SEC |
| SRC-022 | `[MET-SEC-004] Prompt Injection 防护` | metric | SEC |
| SRC-023 | `[MET-STAB-001] 可用性 >= 99.5%` | metric | STAB |
| SRC-024 | `[MET-STAB-002] 异常恢复与降级` | metric | STAB |
| SRC-025 | `[MET-UX-001] Widget 加载 <= 1s` | metric | UX |
| SRC-026 | `[MET-UX-002] 移动端自适应` | metric | UX |
| SRC-027 | `[MET-UX-003] 无需培训即可使用` | metric | UX |

### 5.3 Constraints (4 items)
| SRC-ID | Upstream Item | Type | Category |
|--------|---------------|------|----------|
| SRC-028 | `resource.budget: < $5000/月` | constraint | resource |
| SRC-029 | `resource.timeline: 2026-02-28` | constraint | resource |
| SRC-030 | `technology.allowed: [Python, TS, PG+pgvector, ...]` | constraint | allowed |
| SRC-031 | `technology.forbidden: [自建 LLM, Pinecone, ...]` | constraint | forbidden |

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

### 5.6 Risks（v0.6.2 新增，11 items）
| SRC-ID | Upstream Item | Type | Mitigation |
|--------|---------------|------|------------|
| SRC-048 | `[RISK-001] LLM API 成本超预算` | risk | Token 监控、缓存、限流 |
| SRC-049 | `[RISK-002] RAG 检索准确性不达预期` | risk | 分段/召回/重排策略 |
| SRC-050 | `[RISK-003] 产品知识过期误导` | risk | 版本管理、有效期提示 |
| SRC-051 | `[RISK-004] Prompt Injection/数据外泄` | risk | 过滤、转义、审计 |
| SRC-052 | `[RISK-005] 高并发性能下降` | risk | 缓存、异步、连接池 |
| SRC-053 | `[RISK-006] 文件上传安全合规` | risk | 类型限制、扫描、脱敏 |
| SRC-054 | `[RISK-007] 语音/多语言延迟成本` | risk | 开关、缓存、降级 |
| SRC-055 | `[RISK-008] 多语言质量不稳定` | risk | 模型评测、回归测试 |
| SRC-056 | `[RISK-009] 邮箱验证码滥用` | risk | 频控、验证策略、审计 |
| SRC-057 | `[RISK-010] 人工客服无人接待` | risk | SLA、排队、回退 AI |
| SRC-058 | `[RISK-011] 寻价数据隐私合规` | risk | 最小化、脱敏、访问控制 |

### 5.7 Dependencies（v0.6.2 新增，10 items）
| SRC-ID | Upstream Item | Type | Category |
|--------|---------------|------|----------|
| SRC-059 | 现有产品网站（提供嵌入入口） | dependency | external_system |
| SRC-060 | 现有网站登录态/用户标识注入（可选） | dependency | external_system |
| SRC-061 | 产品数据 JSON（约 600 SKU） | dependency | resource |
| SRC-062 | 产品文档/FAQ/知识库资料 | dependency | resource |
| SRC-063 | PostgreSQL + pgvector | dependency | resource |
| SRC-064 | OpenAI-Compatible API 密钥 | dependency | resource |
| SRC-065 | Ollama 服务与模型文件 | dependency | resource |
| SRC-066 | STT/TTS Provider | dependency | resource |
| SRC-067 | 文件/图片存储与提取能力 | dependency | resource |
| SRC-068 | 邮件发送/验证码服务 | dependency | resource |

### 5.8 Contracts（v0.6.2 新增，2 items）
| SRC-ID | Upstream Item | Type | Status |
|--------|---------------|------|--------|
| SRC-069 | `product_data_contract` | contract | defined |
| SRC-070 | `widget_context_contract` | contract | defined |

## 6. Mapping & Split Decisions（映射与拆分决策）

### 6.1 Scope → Requirements
| SRC-ID | Decision | REQ-ID | Source |
|--------|----------|--------|--------|
| SRC-001 | split | REQ-L0-WGT-001 | `charter.yaml#scope.must_have[0]` |
| SRC-002 | split | REQ-L0-ADM-001 | `charter.yaml#scope.must_have[1]` |
| SRC-003 | split | REQ-L0-ADM-002 | `charter.yaml#scope.must_have[2]` |
| SRC-004 | split | REQ-L0-API-001 | `charter.yaml#scope.must_have[3]` |
| SRC-005 | split | REQ-L0-API-002 | `charter.yaml#scope.must_have[4]` |
| SRC-006 | split | REQ-L0-API-003 | `charter.yaml#scope.must_have[5]` |
| SRC-007 | split | REQ-L0-API-004 | `charter.yaml#scope.must_have[6]` |
| SRC-008 | split | REQ-L0-API-005 | `charter.yaml#scope.must_have[7]` |
| SRC-009 | split | REQ-L0-ADM-003 | `charter.yaml#scope.must_have[8]` |
| SRC-010 | split | REQ-L0-API-006 | `charter.yaml#scope.must_have[9]` |
| SRC-011 | split | REQ-L0-API-007 | `charter.yaml#scope.must_have[10]` |
| SRC-012 | split | REQ-L0-WGT-002 | `charter.yaml#scope.must_have[11]` |
| SRC-013 | split | REQ-L0-WGT-003 | `charter.yaml#scope.must_have[12]` |
| SRC-014 | split | REQ-L0-WGT-004 | `charter.yaml#scope.must_have[13]` |
| SRC-015 | split | REQ-L0-SHARED-001 | `charter.yaml#scope.must_have[14]` |

### 6.2 Metrics → Requirements
| SRC-ID | Decision | REQ-ID | Source |
|--------|----------|--------|--------|
| SRC-016~018 | split | REQ-L0-PERF-001~003 | `charter.yaml#metrics.performance[*]` |
| SRC-019~022 | split | REQ-L0-SEC-001~004 | `charter.yaml#metrics.security[*]` |
| SRC-023~024 | split | REQ-L0-STAB-001~002 | `charter.yaml#metrics.stability[*]` |
| SRC-025~027 | split | REQ-L0-UX-001~003 | `charter.yaml#metrics.usability[*]` |

### 6.3 Constraints → Requirements
| SRC-ID | Decision | REQ-ID | Source |
|--------|----------|--------|--------|
| SRC-028 | split | REQ-L0-CON-001 | `charter.yaml#constraints.resource.budget` |
| SRC-029 | split | REQ-L0-CON-002 | `charter.yaml#constraints.resource.timeline` |
| SRC-030 | split | REQ-L0-CON-003 | `charter.yaml#constraints.technology_boundary.allowed` |
| SRC-031 | split | REQ-L0-CON-004 | `charter.yaml#constraints.technology_boundary.forbidden` |

### 6.4 Risks → Requirements（v0.6.2 新增）
| SRC-ID | Decision | REQ-ID | Mitigation |
|--------|----------|--------|------------|
| SRC-048 | split | REQ-L0-RISK-001 | Token 用量监控、缓存与限流策略 |
| SRC-049 | split | REQ-L0-RISK-002 | 分段/召回/重排策略，Embedding 模型切换 |
| SRC-050 | split | REQ-L0-RISK-003 | 知识库版本管理与有效期提示 |
| SRC-051 | split | REQ-L0-RISK-004 | 输入输出过滤、引用转义、最小权限、审计日志 |
| SRC-052 | split | REQ-L0-RISK-005 | 缓存策略、异步处理与连接池优化 |
| SRC-053 | split | REQ-L0-RISK-006 | 类型与大小限制、内容扫描、脱敏与保留期策略 |
| SRC-054 | split | REQ-L0-RISK-007 | 提供开关、缓存与降级策略 |
| SRC-055 | split | REQ-L0-RISK-008 | 支持中英的模型/Embedding，评测集与回归测试 |
| SRC-056 | split | REQ-L0-RISK-009 | 频控、验证码策略、审计日志、保留期与告知机制 |
| SRC-057 | split | REQ-L0-RISK-010 | SLA、排队策略、离线收集联系方式与回退 AI |
| SRC-058 | split | REQ-L0-RISK-011 | 最小化收集、脱敏、访问控制与留存策略 |

### 6.5 Dependencies → Requirements（v0.6.2 新增）
| SRC-ID | Decision | REQ-ID | Statement |
|--------|----------|--------|-----------|
| SRC-059 | split | REQ-L0-DEP-001 | 依赖外部系统: 现有产品网站 |
| SRC-060 | split | REQ-L0-DEP-002 | 可选依赖: 现有网站登录态注入 |
| SRC-061 | split | REQ-L0-DEP-003 | 依赖资源: 产品数据 JSON |
| SRC-062 | split | REQ-L0-DEP-004 | 依赖资源: 知识库原始资料 |
| SRC-063 | split | REQ-L0-DEP-005 | 依赖资源: PostgreSQL + pgvector |
| SRC-064 | split | REQ-L0-DEP-006 | 依赖资源: OpenAI-Compatible API |
| SRC-065 | split | REQ-L0-DEP-007 | 依赖资源: Ollama 服务 |
| SRC-066 | split | REQ-L0-DEP-008 | 依赖资源: STT/TTS Provider |
| SRC-067 | split | REQ-L0-DEP-009 | 依赖资源: 文件存储与提取能力 |
| SRC-068 | split | REQ-L0-DEP-010 | 依赖资源: 邮件发送服务 |

### 6.6 Contracts → IFC（v0.6.2 新增）
| SRC-ID | Decision | IFC-ID | Description |
|--------|----------|--------|-------------|
| SRC-069 | → L2 | IFC-PRODUCT-DATA | 产品数据契约 (minimum_fields 已定义) |
| SRC-070 | → L2 | IFC-WIDGET-CONTEXT | Widget 上下文契约 |

## 7. Traceability Matrix（覆盖矩阵）

| Category | Total | Covered | Coverage |
|----------|-------|---------|----------|
| Scope (must_have) | 15 | 15 | 100% |
| Metrics | 12 | 12 | 100% |
| Constraints | 4 | 4 | 100% |
| Exclusions | 4 | 4 | 100% |
| TBDs | 12 | 12 | 100% |
| **Risks** | 11 | 11 | 100% ✅ |
| **Dependencies** | 10 | 10 | 100% ✅ |
| **Contracts** | 2 | 2 | 100% ✅ |
| **Total** | **70** | **70** | **100%** |

## 8. Gate Check（门禁检查）

- [x] Scope 覆盖: 15/15 (100%)
- [x] Metrics 覆盖: 12/12 (100%)
- [x] Constraints 覆盖: 4/4 (100%)
- [x] Exclusions 覆盖: 4/4 (100%)
- [x] TBD 覆盖: 12/12 (100%)
- [x] **Risks 覆盖**: 11/11 (100%) ✅ v0.6.2
- [x] **Dependencies 覆盖**: 10/10 (100%) ✅ v0.6.2
- [x] **Contracts 覆盖**: 2/2 (100%) ✅ v0.6.2

---

**Result**: ✅ **PASS**

**Total**: 70 items → 70 covered (100%)

**Next Steps**:
1. 运行 `/requirements-render` 生成 `docs/L0/requirements.md`
2. 运行 `/requirements-validate` 验证
3. 按 `full` 路径执行 L0 → L1 → L2
