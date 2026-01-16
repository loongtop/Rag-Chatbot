---
status: draft
owner: requirements_split
layer_from: L0 | L1 | L2
layer_to: L0 | L1 | L2
parent: {source_path}
target: {target_path}
granularity: auto | full | medium | light | direct
decomposition_path: L0→L1→L2 | L0→L2 | L0→L1 | L0→L2(single)
---

# Split Report: {layer_from} → {layer_to}

## 1. Summary（结论）

- **Decision**: PASS / FAIL
- **Why**: 1–3 句话说明原因（明确性/缺失信息/可验证性/可追溯性）
- **Granularity Mode**: `{granularity}` (`{decomposition_path}`)
- **Complexity Assessment**: High / Medium / Low

## 2. Inputs（输入）

| Item | Path | Version/Checksum | Notes |
|------|------|------------------|-------|
| Source | `{source_path}` | `{sha256_or_version}` | |
| Target | `{target_path}` | - | |
| Traceability Mode | `charter.yaml#traceability.mode` | | |
| Components | `charter.yaml#components` | | Count: {count} |

## 3. Split Rules（拆分规则）

- **Granularity**: `{granularity}` (auto/full/medium/light/direct)
  - `auto`: 自动评估复杂度选择路径
  - `full`: L0→L1→L2（复杂系统）
  - `medium`: L0→L2（中等系统，跳过 L1）
  - `light`: L0→L1（简单系统，先停在 L1）
  - `direct`: L0→L2（单模块/边界极清晰）

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
  - `mobile-app` → MOB

- **No invention**: 不得引入无来源的新需求；只允许"重写为可测试语句"，且必须保留来源
- **Source format**:
  - `charter.yaml#<yaml_path>`（例：`charter.yaml#scope.must_have[0]`）
  - `REQ-L0-001`（引用上游需求 ID）

## 4. Granularity Decision（粒度决策，仅 auto 模式）

| Dimension | Value | Score |
|-----------|-------|-------|
| Scope items (must_have) | {scope_count} | {scope_score} |
| Components | {component_count} | {component_score} |
| Cross-module deps | {dep_count} | {dep_score} |
| **Total Score** | | {total_score} |
| **Assessment** | | {assessment} |
| **Recommended Path** | | {recommended_path} |

## 5. Source Inventory（上游条目清单）

> 逐条列出将被分析的上游条目（可引用原句/原段落或 YAML 路径）

| SRC-ID | Upstream Item | Type | Notes |
|--------|---------------|------|-------|
| SRC-001 | `{quote_or_pointer}` | requirement / metric / constraint / risk / tbd / out_of_scope | |

## 6. Mapping & Split Decisions（映射与拆分决策）

| SRC-ID | Decision | Downstream Output | Source | Notes |
|--------|----------|------------------|--------|-------|
| SRC-001 | split / keep / N/A | `REQ-Lx-000`, `interfaces.md#{name}` | `{source}` | |

## 7. Cross-Layer Traceability（跨层追溯，跳过中间层时）

> 当跳过中间层时，建立 L0→L2（或 L0→SPEC）的直接追溯链

| Source (L0) | Target (L2) | Link Type | Notes |
|-------------|-------------|-----------|-------|
| REQ-L0-001 | REQ-L2-001 | direct | 无中间层分解 |
| REQ-L0-002 | REQ-L2-002 | derived | 需求合并 |

**追溯验证**:
- [ ] 每个目标层需求有且仅有 1 个 L0 来源
- [ ] 追溯链完整，无断裂

## 8. Traceability Matrix（覆盖矩阵）

> 上游每个条目必须映射到下游至少 1 个 REQ/接口，或写 `N/A + 原因`。

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
| MET-PERF-* | REQ-L0-PERF-* | ✅ | |
| MET-SEC-* | REQ-L0-SEC-* | ✅ | |
| MET-STAB-* | REQ-L0-STAB-* | ✅ | |
| MET-UX-* | REQ-L0-UX-* | ✅ | |
| scope.out_of_scope | exclusions | ✅ | 逐条映射 |
| constraints | REQ-L0-CON-* | ✅ | 预算/时间/技术栈 |

## 9. Exclusions（逐条提取）

> 从 `charter.yaml#scope.out_of_scope` 逐条提取

| source | reason | category |
|--------|--------|----------|
| SCOPE-OOS-001 | 不做完整认证/账号体系 | scope |
| SCOPE-OOS-002 | 订单处理和支付功能 | scope |
| SCOPE-OOS-005 | 知识库自动爬取/同步 | deferred |
| SCOPE-OOS-006 | 自建 LLM 训练 | scope |

## 10. Constraints（自动提取）

> 从 `charter.yaml#constraints` 自动提取

| ID | Statement | Source | Category |
|----|-----------|--------|----------|
| REQ-L0-CON-BUDGET | 云服务月成本 < $5000 | resource.budget | resource |
| REQ-L0-CON-TIMELINE | 交付截止日期: 2026-02-28 | resource.timeline | resource |
| REQ-L0-CON-TECH-ALLOWED | 允许: Python, TypeScript, PostgreSQL+pgvector | technology_boundary.allowed | allowed |
| REQ-L0-CON-TECH-FORBIDDEN | 禁止: 自建 LLM 训练, Pinecone, 私有化数据库 | technology_boundary.forbidden | forbidden |

## 11. 模块接口矩阵（L2）

> L2 层级分解时，定义模块间的接口依赖关系（最终落地到 `docs/L2/interfaces.md`）

| 组件 | 提供接口 | 依赖接口 | 说明 |
|------|----------|----------|------|
| api-server | REST API, RAG Service | LLM Provider, pgvector | 后端核心服务 |
| chat-widget | Widget UI, Voice IO | api-server REST API | 前端交互组件 |
| admin-dashboard | Admin UI, KB Management | api-server REST API | 后台管理界面 |

**接口类型说明**：
- `REST API`: HTTP JSON 接口
- `RAG Service`: 内部检索增强生成服务
- `Widget UI`: 前端组件接口
- `Voice IO`: 语音输入输出接口
- `LLM Provider`: 大模型调用接口
- `pgvector`: 向量数据库接口

## 12. TBD & Questions（待定项）

> 任何不明确/不可验证/不可实现的内容必须进入 TBD，并带来源。

| TBD-ID | Question / Missing Info | Impact | Source | Target Layer |
|--------|--------------------------|--------|--------|--------------|
| TBD-001 | LLM Provider/Model 选择 | H | `charter.yaml#[TBD-001]` | L0 |
| TBD-002 | 降级策略定义 | M | `charter.yaml#[TBD-002]` | L1 |
| TBD-003 | 后台鉴权方式 | H | `charter.yaml#[TBD-003]` | L0 |
| TBD-006 | Widget 资源体积与加载口径 | L | `charter.yaml#[TBD-006]` | L2 |
| TBD-010 | 邮箱登录验证码方案 | M | `charter.yaml#[TBD-010]` | L1 |

## 13. Gate Check（门禁检查）

- [ ] 上游每个条目：都有映射或 `N/A + 原因`
- [ ] 下游每个 `REQ-ID`：都有至少一个 `Source`
- [ ] 未出现"无来源的新需求"
- [ ] 关键缺失信息已进入 TBD（且带来源）
- [ ] **跨层追溯验证**（仅 medium/light/direct 模式）：
  - [ ] 每个目标层需求有唯一来源
  - [ ] 追溯链清晰可查
- [ ] **Exclusions 检查**（v0.5.1+）：
  - [ ] `scope.out_of_scope` 全部映射到 exclusions
  - [ ] 每个 exclusion 有明确 reason
- [ ] **Constraints 检查**（v0.5.1+）：
  - [ ] 资源约束（budget/timeline）已提取
  - [ ] 技术约束（allowed/forbidden）已提取
