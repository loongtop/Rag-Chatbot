---
status: done
owner: requirements-split
layer_from: L0
layer_to: L0
parent: charter.yaml
target: docs/L0
granularity: structured
---

# Split Report: Charter → L0

## 1. Summary（结论）

- **Decision**: PASS
- **Why**: `charter.yaml` 已冻结（`meta.version=v0.1`，`freeze.frozen=true`），关键条目均使用稳定 ID（如 `[SCOPE-MH-001]`），可按结构化粒度拆分为可实现/可测试的 L0 需求；不确定项已在 `open_questions` 与显式 `TBD` 注记中列出，将以 TBD 形式进入 L0 requirements。

## 2. Inputs（输入）

| Item | Path | Version/Checksum | Notes |
|------|------|------------------|-------|
| Source | `charter.yaml` | `v0.1` / `sha256: 9bf2a6cdf4c711958850ff063d4702fdb071581b3bcdbb57e88c43b5413cef97` | `freeze.frozen=true` |
| Target | `docs/L0/` | - | L0: `split-report.md`, `requirements.md`, `subtasks.md` |

## 3. Split Rules（拆分规则）

- **Granularity**: `structured`
- **No invention**: 不得引入无来源的新需求；仅允许将原句重写为可测试表达，并保留来源
- **REQ-ID**: 使用 `REQ-L0-XXX`
- **Source format**: `charter.yaml#<yaml_path>`（允许多来源）

## 4. Source Inventory（上游条目清单）

| SRC-ID | Upstream Item | Type | Notes |
|--------|---------------|------|-------|
| SRC-001 | `charter.yaml#objective.problems[0]` | problem | `[PROB-001]` |
| SRC-002 | `charter.yaml#objective.problems[1]` | problem | `[PROB-002]` |
| SRC-003 | `charter.yaml#objective.problems[2]` | problem | `[PROB-003]` |
| SRC-004 | `charter.yaml#objective.business_goals[0]` | business_goal | `[GOAL-001]` |
| SRC-005 | `charter.yaml#objective.business_goals[1]` | business_goal | `[GOAL-002]` |
| SRC-006 | `charter.yaml#objective.business_goals[2]` | business_goal | `[GOAL-003]` |
| SRC-007 | `charter.yaml#stakeholders.users[0]` | stakeholder | `[USER-001]` |
| SRC-008 | `charter.yaml#stakeholders.users[1]` | stakeholder | `[USER-002]` |
| SRC-009 | `charter.yaml#stakeholders.users[2]` | stakeholder | `[USER-003]` |
| SRC-010 | `charter.yaml#scope.must_have[0]` | requirement | `[SCOPE-MH-001]` |
| SRC-011 | `charter.yaml#scope.must_have[1]` | requirement | `[SCOPE-MH-002]` |
| SRC-012 | `charter.yaml#scope.must_have[2]` | requirement | `[SCOPE-MH-003]` |
| SRC-013 | `charter.yaml#scope.must_have[3]` | requirement | `[SCOPE-MH-004]` |
| SRC-014 | `charter.yaml#scope.must_have[4]` | requirement | `[SCOPE-MH-005]` |
| SRC-015 | `charter.yaml#scope.must_have[5]` | requirement | `[SCOPE-MH-006]` |
| SRC-016 | `charter.yaml#scope.must_have[6]` | requirement | `[SCOPE-MH-007]` |
| SRC-017 | `charter.yaml#scope.must_have[7]` | requirement | `[SCOPE-MH-008]` |
| SRC-018 | `charter.yaml#scope.must_have[8]` | requirement | `[SCOPE-MH-009]` |
| SRC-019 | `charter.yaml#scope.must_have[9]` | requirement | `[SCOPE-MH-010]` |
| SRC-020 | `charter.yaml#scope.must_have[10]` | requirement | `[SCOPE-MH-011]` |
| SRC-021 | `charter.yaml#scope.must_have[11]` | requirement | `[SCOPE-MH-012]` |
| SRC-022 | `charter.yaml#scope.must_have[12]` | requirement | `[SCOPE-MH-013]` |
| SRC-023 | `charter.yaml#scope.must_have[13]` | requirement | `[SCOPE-MH-014]` |
| SRC-024 | `charter.yaml#scope.must_have[14]` | requirement | `[SCOPE-MH-015]` |
| SRC-025 | `charter.yaml#scope.out_of_scope[0]` | out_of_scope | `[SCOPE-OOS-001]` |
| SRC-026 | `charter.yaml#scope.out_of_scope[1]` | out_of_scope | `[SCOPE-OOS-002]` |
| SRC-027 | `charter.yaml#scope.out_of_scope[2]` | out_of_scope | `[SCOPE-OOS-005]` |
| SRC-028 | `charter.yaml#scope.out_of_scope[3]` | out_of_scope | `[SCOPE-OOS-006]` |
| SRC-029 | `charter.yaml#metrics.performance[0]` | metric | `[MET-PERF-001]` |
| SRC-030 | `charter.yaml#metrics.performance[1]` | metric | `[MET-PERF-002]` |
| SRC-031 | `charter.yaml#metrics.performance[2]` | metric | `[MET-PERF-003]` |
| SRC-032 | `charter.yaml#metrics.security[0]` | metric | `[MET-SEC-001]` |
| SRC-033 | `charter.yaml#metrics.security[1]` | metric | `[MET-SEC-002]` |
| SRC-034 | `charter.yaml#metrics.security[2]` | metric | `[MET-SEC-003]` |
| SRC-035 | `charter.yaml#metrics.security[3]` | metric | `[MET-SEC-004]` |
| SRC-036 | `charter.yaml#metrics.stability[0]` | metric | `[MET-STAB-001]` |
| SRC-037 | `charter.yaml#metrics.stability[1]` | metric | `[MET-STAB-002]` |
| SRC-038 | `charter.yaml#metrics.usability[0]` | metric | `[MET-UX-001]` |
| SRC-039 | `charter.yaml#metrics.usability[1]` | metric | `[MET-UX-002]` |
| SRC-040 | `charter.yaml#metrics.usability[2]` | metric | `[MET-UX-003]` |
| SRC-041 | `charter.yaml#constraints.resource.budget` | constraint | budget |
| SRC-042 | `charter.yaml#constraints.resource.timeline` | constraint | timeline |
| SRC-043 | `charter.yaml#constraints.technology_boundary.allowed` | constraint | allowed stack |
| SRC-044 | `charter.yaml#constraints.technology_boundary.forbidden` | constraint | forbidden stack |
| SRC-045 | `charter.yaml#dependencies.external_systems[0]` | dependency | website embed + context |
| SRC-046 | `charter.yaml#dependencies.external_systems[1]` | dependency | optional login injection (TBD) |
| SRC-047 | `charter.yaml#dependencies.resources` | dependency | required resources |
| SRC-048 | `charter.yaml#product_data_contract` | contract | products.json minimum fields |
| SRC-049 | `charter.yaml#widget_context_contract` | contract | skuId/productId/url |
| SRC-050 | `charter.yaml#risks[0]` | risk | `[RISK-001]` |
| SRC-051 | `charter.yaml#risks[1]` | risk | `[RISK-002]` |
| SRC-052 | `charter.yaml#risks[2]` | risk | `[RISK-003]` |
| SRC-053 | `charter.yaml#risks[3]` | risk | `[RISK-004]` |
| SRC-054 | `charter.yaml#risks[4]` | risk | `[RISK-005]` |
| SRC-055 | `charter.yaml#risks[5]` | risk | `[RISK-006]` |
| SRC-056 | `charter.yaml#risks[6]` | risk | `[RISK-007]` |
| SRC-057 | `charter.yaml#risks[7]` | risk | `[RISK-008]` |
| SRC-058 | `charter.yaml#risks[8]` | risk | `[RISK-009]` |
| SRC-059 | `charter.yaml#risks[9]` | risk | `[RISK-010]` |
| SRC-060 | `charter.yaml#risks[10]` | risk | `[RISK-011]` |
| SRC-061 | `charter.yaml#deliverables.mandatory[0]` | deliverable | `[DELIV-001]` |
| SRC-062 | `charter.yaml#deliverables.mandatory[1]` | deliverable | `[DELIV-002]` |
| SRC-063 | `charter.yaml#deliverables.mandatory[2]` | deliverable | `[DELIV-003]` |
| SRC-064 | `charter.yaml#deliverables.mandatory[3]` | deliverable | `[DELIV-004]` |
| SRC-065 | `charter.yaml#deliverables.mandatory[4]` | deliverable | `[DELIV-005]` |
| SRC-066 | `charter.yaml#deliverables.mandatory[5]` | deliverable | `[DELIV-006]` |
| SRC-067 | `charter.yaml#deliverables.mandatory[6]` | deliverable | `[DELIV-007]` |
| SRC-068 | `charter.yaml#quality_requirements` | constraint | quality gates |
| SRC-069 | `charter.yaml#components` | constraint | component boundary |
| SRC-070 | `charter.yaml#assumptions[0]` | assumption | `[ASM-001]` |
| SRC-071 | `charter.yaml#assumptions[1]` | assumption | `[ASM-002]` |
| SRC-072 | `charter.yaml#assumptions[2]` | assumption | `[ASM-003]` |
| SRC-073 | `charter.yaml#acceptance_criteria[0]` | acceptance | `[ACC-001]` |
| SRC-074 | `charter.yaml#acceptance_criteria[1]` | acceptance | `[ACC-002]` |
| SRC-075 | `charter.yaml#acceptance_criteria[2]` | acceptance | `[ACC-003]` |
| SRC-076 | `charter.yaml#acceptance_criteria[3]` | acceptance | `[ACC-004]` |
| SRC-077 | `charter.yaml#acceptance_criteria[4]` | acceptance | `[ACC-005]` |
| SRC-078 | `charter.yaml#acceptance_criteria[5]` | acceptance | `[ACC-006]` |
| SRC-079 | `charter.yaml#acceptance_criteria[6]` | acceptance | `[ACC-007]` |
| SRC-080 | `charter.yaml#acceptance_criteria[7]` | acceptance | `[ACC-008]` |
| SRC-081 | `charter.yaml#acceptance_criteria[8]` | acceptance | `[ACC-009]` |
| SRC-082 | `charter.yaml#acceptance_criteria[9]` | acceptance | `[ACC-010]` |
| SRC-083 | `charter.yaml#acceptance_criteria[10]` | acceptance | `[ACC-011]` |
| SRC-084 | `charter.yaml#acceptance_criteria[11]` | acceptance | `[ACC-012]` |
| SRC-085 | `charter.yaml#acceptance_criteria[12]` | acceptance | `[ACC-013]` |
| SRC-086 | `charter.yaml#open_questions[0]` | tbd | `[TBD-001]` |
| SRC-087 | `charter.yaml#open_questions[1]` | tbd | `[TBD-002]` |
| SRC-088 | `charter.yaml#open_questions[2]` | tbd | `[TBD-003]` |
| SRC-089 | `charter.yaml#open_questions[3]` | tbd | `[TBD-004]` |
| SRC-090 | `charter.yaml#open_questions[4]` | tbd | `[TBD-005]` |
| SRC-091 | `charter.yaml#open_questions[5]` | tbd | `[TBD-006]` |
| SRC-092 | `charter.yaml#open_questions[6]` | tbd | `[TBD-007]` |
| SRC-093 | `charter.yaml#open_questions[7]` | tbd | `[TBD-008]` |
| SRC-094 | `charter.yaml#open_questions[8]` | tbd | `[TBD-009]` |
| SRC-095 | `charter.yaml#open_questions[9]` | tbd | `[TBD-010]` |
| SRC-096 | `charter.yaml#open_questions[10]` | tbd | `[TBD-011]` |
| SRC-097 | `charter.yaml#open_questions[11]` | tbd | `[TBD-012]` |
| SRC-098 | `charter.yaml#traceability` | process | traceability mode |
| SRC-099 | `charter.yaml#freeze` | process | freeze block |

## 5. Mapping & Split Decisions（映射与拆分决策）

| SRC-ID | Decision | Downstream Output | Source | Notes |
|--------|----------|------------------|--------|-------|
| SRC-001 | keep | `REQ-L0-001` | `charter.yaml#objective.problems[0]` | 目标/问题聚合为系统级需求 |
| SRC-002 | keep | `REQ-L0-001` | `charter.yaml#objective.problems[1]` | 同上 |
| SRC-003 | keep | `REQ-L0-001` | `charter.yaml#objective.problems[2]` | 同上 |
| SRC-004 | keep | `REQ-L0-001` | `charter.yaml#objective.business_goals[0]` | 系统级业务目标 |
| SRC-005 | keep | `REQ-L0-001` | `charter.yaml#objective.business_goals[1]` | 同上 |
| SRC-006 | keep | `REQ-L0-001` | `charter.yaml#objective.business_goals[2]` | 同上 |
| SRC-007 | keep | `REQ-L0-002, REQ-L0-005, REQ-L0-006, REQ-L0-007` | `charter.yaml#stakeholders.users[0]` | 影响 Widget/问答/推荐/对比体验 |
| SRC-008 | keep | `REQ-L0-002, REQ-L0-005, REQ-L0-006, REQ-L0-007` | `charter.yaml#stakeholders.users[1]` | 同上 |
| SRC-009 | keep | `REQ-L0-002, REQ-L0-005` | `charter.yaml#stakeholders.users[2]` | 偏问答与使用指导 |
| SRC-010 | split | `REQ-L0-002` | `charter.yaml#scope.must_have[0]` | Widget 集成与最小示例 |
| SRC-011 | split | `REQ-L0-003, REQ-L0-020` | `charter.yaml#scope.must_have[1]` | 产品 JSON 导入 + 数据契约 |
| SRC-012 | split | `REQ-L0-004` | `charter.yaml#scope.must_have[2]` | 文档上传、索引、重建、状态、重排 |
| SRC-013 | split | `REQ-L0-005` | `charter.yaml#scope.must_have[3]` | RAG + 引用 + 澄清/拒答 |
| SRC-014 | split | `REQ-L0-006` | `charter.yaml#scope.must_have[4]` | 推荐 Top-N 与依据 |
| SRC-015 | split | `REQ-L0-007` | `charter.yaml#scope.must_have[5]` | 对比 2–4 SKU + 字段可配（TBD） |
| SRC-016 | split | `REQ-L0-008, REQ-L0-021` | `charter.yaml#scope.must_have[6]` | 上下文契约 + 检索/排序 |
| SRC-017 | split | `REQ-L0-009` | `charter.yaml#scope.must_have[7]` | 多轮、引用、错误、token 用量 |
| SRC-018 | split | `REQ-L0-010` | `charter.yaml#scope.must_have[8]` | 后台 UI 能力集合 |
| SRC-019 | split | `REQ-L0-011` | `charter.yaml#scope.must_have[9]` | 在线/本地 LLM 切换 |
| SRC-020 | split | `REQ-L0-012` | `charter.yaml#scope.must_have[10]` | 人工/AI 切换与转接 |
| SRC-021 | split | `REQ-L0-013` | `charter.yaml#scope.must_have[11]` | 语音 STT/TTS（可配） |
| SRC-022 | split | `REQ-L0-014` | `charter.yaml#scope.must_have[12]` | 中英双语（可配） |
| SRC-023 | split | `REQ-L0-015` | `charter.yaml#scope.must_have[13]` | 文件/图片输入与内容提取 |
| SRC-024 | split | `REQ-L0-016, REQ-L0-017` | `charter.yaml#scope.must_have[14]` | 邮箱验证码登录 + 寻价/联系人工解锁 |
| SRC-025 | keep | `REQ-L0-950` | `charter.yaml#scope.out_of_scope[0]` | 负向范围约束 |
| SRC-026 | keep | `REQ-L0-951` | `charter.yaml#scope.out_of_scope[1]` | 负向范围约束 |
| SRC-027 | keep | `REQ-L0-952` | `charter.yaml#scope.out_of_scope[2]` | 负向范围约束 |
| SRC-028 | keep | `REQ-L0-953` | `charter.yaml#scope.out_of_scope[3]` | 负向范围约束 |
| SRC-029 | keep | `REQ-L0-101` | `charter.yaml#metrics.performance[0]` | 性能指标转为 NFR |
| SRC-030 | keep | `REQ-L0-102` | `charter.yaml#metrics.performance[1]` | 同上 |
| SRC-031 | keep | `REQ-L0-103` | `charter.yaml#metrics.performance[2]` | 同上（压测口径 TBD） |
| SRC-032 | keep | `REQ-L0-201` | `charter.yaml#metrics.security[0]` | 安全指标转为 NFR |
| SRC-033 | keep | `REQ-L0-202` | `charter.yaml#metrics.security[1]` | 同上 |
| SRC-034 | keep | `REQ-L0-203` | `charter.yaml#metrics.security[2]` | 同上 |
| SRC-035 | keep | `REQ-L0-204` | `charter.yaml#metrics.security[3]` | 同上 |
| SRC-036 | keep | `REQ-L0-301` | `charter.yaml#metrics.stability[0]` | 稳定性指标转为 NFR |
| SRC-037 | keep | `REQ-L0-302` | `charter.yaml#metrics.stability[1]` | 降级策略 TBD |
| SRC-038 | keep | `REQ-L0-401` | `charter.yaml#metrics.usability[0]` | Widget 加载口径 TBD |
| SRC-039 | keep | `REQ-L0-402` | `charter.yaml#metrics.usability[1]` | 可用性指标 |
| SRC-040 | keep | `REQ-L0-403` | `charter.yaml#metrics.usability[2]` | 可用性指标 |
| SRC-041 | keep | `REQ-L0-901` | `charter.yaml#constraints.resource.budget` | 预算约束 |
| SRC-042 | keep | `REQ-L0-902` | `charter.yaml#constraints.resource.timeline` | 里程碑约束 |
| SRC-043 | keep | `REQ-L0-903` | `charter.yaml#constraints.technology_boundary.allowed` | 技术边界（允许） |
| SRC-044 | keep | `REQ-L0-903` | `charter.yaml#constraints.technology_boundary.forbidden` | 技术边界（禁止） |
| SRC-045 | keep | `REQ-L0-801` | `charter.yaml#dependencies.external_systems[0]` | 依赖现有网站嵌入与上下文 |
| SRC-046 | keep | `TBD-L0-003` | `charter.yaml#dependencies.external_systems[1]` | 可选登录态注入方案 TBD |
| SRC-047 | keep | `REQ-L0-802` | `charter.yaml#dependencies.resources` | 外部资源依赖汇总 |
| SRC-048 | split | `REQ-L0-020` | `charter.yaml#product_data_contract` | 产品数据契约细化为输入约束 |
| SRC-049 | split | `REQ-L0-021` | `charter.yaml#widget_context_contract` | 上下文契约细化为输入约束 |
| SRC-050 | keep | `REQ-L0-009, REQ-L0-203, REQ-L0-210, REQ-L0-901` | `charter.yaml#risks[0]` | 成本风险 → 监控/缓存/限流/预算 |
| SRC-051 | keep | `REQ-L0-004, REQ-L0-211` | `charter.yaml#risks[1]` | 检索质量风险 → 重排/评测/可调参 |
| SRC-052 | keep | `REQ-L0-212` | `charter.yaml#risks[2]` | 知识过期 → 版本/更新时间提示（TBD） |
| SRC-053 | keep | `REQ-L0-201, REQ-L0-202, REQ-L0-204` | `charter.yaml#risks[3]` | 注入/外泄风险 → 安全基线 |
| SRC-054 | keep | `REQ-L0-101, REQ-L0-102, REQ-L0-103, REQ-L0-210` | `charter.yaml#risks[4]` | 性能风险 → 指标 + 缓存/连接池（实现细节 TBD） |
| SRC-055 | keep | `REQ-L0-015, REQ-L0-213` | `charter.yaml#risks[5]` | 上传安全/合规 → 限制/扫描/留存策略（TBD） |
| SRC-056 | keep | `REQ-L0-214, REQ-L0-302` | `charter.yaml#risks[6]` | 语音/多语言成本延迟 → 开关/降级（TBD） |
| SRC-057 | keep | `REQ-L0-214` | `charter.yaml#risks[7]` | 多语言质量 → 评测与回归（TBD） |
| SRC-058 | keep | `REQ-L0-215` | `charter.yaml#risks[8]` | 邮箱验证码滥用/合规 → 频控/审计（TBD） |
| SRC-059 | keep | `REQ-L0-012, REQ-L0-216` | `charter.yaml#risks[9]` | 人工转接无人接待 → SLA/回退（TBD） |
| SRC-060 | keep | `REQ-L0-017, REQ-L0-217` | `charter.yaml#risks[10]` | 寻价/线索隐私合规 → 最小化/访问控制（TBD） |
| SRC-061 | keep | `REQ-L0-001` | `charter.yaml#deliverables.mandatory[0]` | 交付物覆盖到系统级需求 |
| SRC-062 | keep | `REQ-L0-002` | `charter.yaml#deliverables.mandatory[1]` | Widget 交付 |
| SRC-063 | keep | `REQ-L0-010` | `charter.yaml#deliverables.mandatory[2]` | 后台交付 |
| SRC-064 | keep | `REQ-L0-004` | `charter.yaml#deliverables.mandatory[3]` | 索引构建能力 |
| SRC-065 | keep | `REQ-L0-060` | `charter.yaml#deliverables.mandatory[4]` | 文档交付 |
| SRC-066 | keep | `REQ-L0-061` | `charter.yaml#deliverables.mandatory[5]` | 源代码交付 |
| SRC-067 | keep | `REQ-L0-062` | `charter.yaml#deliverables.mandatory[6]` | 测试报告交付 |
| SRC-068 | split | `REQ-L0-104, REQ-L0-205, REQ-L0-960` | `charter.yaml#quality_requirements` | 质量门禁落地为 NFR |
| SRC-069 | keep | `REQ-L0-970` | `charter.yaml#components` | 组件边界与技术栈 |
| SRC-070 | keep | `REQ-L0-002, REQ-L0-021` | `charter.yaml#assumptions[0]` | 嵌入与上下文依赖 |
| SRC-071 | keep | `REQ-L0-020` | `charter.yaml#assumptions[1]` | 产品数据契约 |
| SRC-072 | keep | `TBD-L0-016` | `charter.yaml#assumptions[2]` | pgvector 运维与性能细节 TBD |
| SRC-073 | keep | `REQ-L0-018` | `charter.yaml#acceptance_criteria[0]` | OpenAPI/接口验收 |
| SRC-074 | keep | `REQ-L0-005` | `charter.yaml#acceptance_criteria[1]` | 引用与拒答验收 |
| SRC-075 | keep | `REQ-L0-003, REQ-L0-004, REQ-L0-010` | `charter.yaml#acceptance_criteria[2]` | 产品/文档/索引后台验收 |
| SRC-076 | keep | `REQ-L0-004` | `charter.yaml#acceptance_criteria[3]` | 索引可观测性验收 |
| SRC-077 | keep | `REQ-L0-002, REQ-L0-021` | `charter.yaml#acceptance_criteria[4]` | Widget 集成验收 |
| SRC-078 | keep | `REQ-L0-101, REQ-L0-201, REQ-L0-301, REQ-L0-960` | `charter.yaml#acceptance_criteria[5]` | 指标与门禁验收 |
| SRC-079 | keep | `REQ-L0-011` | `charter.yaml#acceptance_criteria[6]` | LLM 切换验收 |
| SRC-080 | keep | `REQ-L0-012` | `charter.yaml#acceptance_criteria[7]` | 人工转接验收（形态 TBD） |
| SRC-081 | keep | `REQ-L0-013` | `charter.yaml#acceptance_criteria[8]` | 语音能力验收 |
| SRC-082 | keep | `REQ-L0-014` | `charter.yaml#acceptance_criteria[9]` | 多语言验收 |
| SRC-083 | keep | `REQ-L0-015` | `charter.yaml#acceptance_criteria[10]` | 上传与错误提示验收 |
| SRC-084 | keep | `REQ-L0-016, REQ-L0-017` | `charter.yaml#acceptance_criteria[11]` | 登录与解锁能力验收（合规 TBD） |
| SRC-085 | keep | `REQ-L0-017` | `charter.yaml#acceptance_criteria[12]` | 寻价验收（字段/流程 TBD） |
| SRC-086 | keep | `TBD-L0-001` | `charter.yaml#open_questions[0]` | TBD 入表 |
| SRC-087 | keep | `TBD-L0-002` | `charter.yaml#open_questions[1]` | TBD 入表 |
| SRC-088 | keep | `TBD-L0-004` | `charter.yaml#open_questions[2]` | TBD 入表 |
| SRC-089 | keep | `TBD-L0-005` | `charter.yaml#open_questions[3]` | TBD 入表 |
| SRC-090 | keep | `TBD-L0-006` | `charter.yaml#open_questions[4]` | TBD 入表 |
| SRC-091 | keep | `TBD-L0-007` | `charter.yaml#open_questions[5]` | TBD 入表 |
| SRC-092 | keep | `TBD-L0-008` | `charter.yaml#open_questions[6]` | TBD 入表 |
| SRC-093 | keep | `TBD-L0-009` | `charter.yaml#open_questions[7]` | TBD 入表 |
| SRC-094 | keep | `TBD-L0-010` | `charter.yaml#open_questions[8]` | TBD 入表 |
| SRC-095 | keep | `TBD-L0-011` | `charter.yaml#open_questions[9]` | TBD 入表 |
| SRC-096 | keep | `TBD-L0-012` | `charter.yaml#open_questions[10]` | TBD 入表 |
| SRC-097 | keep | `TBD-L0-013` | `charter.yaml#open_questions[11]` | TBD 入表 |
| SRC-098 | N/A | N/A | `charter.yaml#traceability` | 流程配置项，不进入产品需求 |
| SRC-099 | N/A | N/A | `charter.yaml#freeze` | 冻结状态，不进入产品需求 |

## 6. Traceability Matrix（覆盖矩阵）

| Upstream | Covered By | Status | Notes |
|----------|------------|--------|-------|
| SRC-001 | `REQ-L0-001` | ✅ | |
| SRC-002 | `REQ-L0-001` | ✅ | |
| SRC-003 | `REQ-L0-001` | ✅ | |
| SRC-004 | `REQ-L0-001` | ✅ | |
| SRC-005 | `REQ-L0-001` | ✅ | |
| SRC-006 | `REQ-L0-001` | ✅ | |
| SRC-007 | `REQ-L0-002, REQ-L0-005, REQ-L0-006, REQ-L0-007` | ✅ | |
| SRC-008 | `REQ-L0-002, REQ-L0-005, REQ-L0-006, REQ-L0-007` | ✅ | |
| SRC-009 | `REQ-L0-002, REQ-L0-005` | ✅ | |
| SRC-010 | `REQ-L0-002` | ✅ | |
| SRC-011 | `REQ-L0-003, REQ-L0-020` | ✅ | |
| SRC-012 | `REQ-L0-004` | ✅ | |
| SRC-013 | `REQ-L0-005` | ✅ | |
| SRC-014 | `REQ-L0-006` | ✅ | |
| SRC-015 | `REQ-L0-007` | ✅ | |
| SRC-016 | `REQ-L0-008, REQ-L0-021` | ✅ | |
| SRC-017 | `REQ-L0-009` | ✅ | |
| SRC-018 | `REQ-L0-010` | ✅ | |
| SRC-019 | `REQ-L0-011` | ✅ | |
| SRC-020 | `REQ-L0-012` | ✅ | |
| SRC-021 | `REQ-L0-013` | ✅ | |
| SRC-022 | `REQ-L0-014` | ✅ | |
| SRC-023 | `REQ-L0-015` | ✅ | |
| SRC-024 | `REQ-L0-016, REQ-L0-017` | ✅ | |
| SRC-025 | `REQ-L0-950` | ✅ | |
| SRC-026 | `REQ-L0-951` | ✅ | |
| SRC-027 | `REQ-L0-952` | ✅ | |
| SRC-028 | `REQ-L0-953` | ✅ | |
| SRC-029 | `REQ-L0-101` | ✅ | |
| SRC-030 | `REQ-L0-102` | ✅ | |
| SRC-031 | `REQ-L0-103` | ✅ | |
| SRC-032 | `REQ-L0-201` | ✅ | |
| SRC-033 | `REQ-L0-202` | ✅ | |
| SRC-034 | `REQ-L0-203` | ✅ | |
| SRC-035 | `REQ-L0-204` | ✅ | |
| SRC-036 | `REQ-L0-301` | ✅ | |
| SRC-037 | `REQ-L0-302` | ✅ | |
| SRC-038 | `REQ-L0-401` | ✅ | |
| SRC-039 | `REQ-L0-402` | ✅ | |
| SRC-040 | `REQ-L0-403` | ✅ | |
| SRC-041 | `REQ-L0-901` | ✅ | |
| SRC-042 | `REQ-L0-902` | ✅ | |
| SRC-043 | `REQ-L0-903` | ✅ | |
| SRC-044 | `REQ-L0-903` | ✅ | |
| SRC-045 | `REQ-L0-801` | ✅ | |
| SRC-046 | `TBD-L0-003` | ✅ | |
| SRC-047 | `REQ-L0-802` | ✅ | |
| SRC-048 | `REQ-L0-020` | ✅ | |
| SRC-049 | `REQ-L0-021` | ✅ | |
| SRC-050 | `REQ-L0-009, REQ-L0-203, REQ-L0-210, REQ-L0-901` | ✅ | |
| SRC-051 | `REQ-L0-004, REQ-L0-211` | ✅ | |
| SRC-052 | `REQ-L0-212` | ✅ | |
| SRC-053 | `REQ-L0-201, REQ-L0-202, REQ-L0-204` | ✅ | |
| SRC-054 | `REQ-L0-101, REQ-L0-102, REQ-L0-103, REQ-L0-210` | ✅ | |
| SRC-055 | `REQ-L0-015, REQ-L0-213` | ✅ | |
| SRC-056 | `REQ-L0-214, REQ-L0-302` | ✅ | |
| SRC-057 | `REQ-L0-214` | ✅ | |
| SRC-058 | `REQ-L0-215` | ✅ | |
| SRC-059 | `REQ-L0-012, REQ-L0-216` | ✅ | |
| SRC-060 | `REQ-L0-017, REQ-L0-217` | ✅ | |
| SRC-061 | `REQ-L0-001` | ✅ | |
| SRC-062 | `REQ-L0-002` | ✅ | |
| SRC-063 | `REQ-L0-010` | ✅ | |
| SRC-064 | `REQ-L0-004` | ✅ | |
| SRC-065 | `REQ-L0-060` | ✅ | |
| SRC-066 | `REQ-L0-061` | ✅ | |
| SRC-067 | `REQ-L0-062` | ✅ | |
| SRC-068 | `REQ-L0-104, REQ-L0-205, REQ-L0-960` | ✅ | |
| SRC-069 | `REQ-L0-970` | ✅ | |
| SRC-070 | `REQ-L0-002, REQ-L0-021` | ✅ | |
| SRC-071 | `REQ-L0-020` | ✅ | |
| SRC-072 | `TBD-L0-016` | ✅ | |
| SRC-073 | `REQ-L0-018` | ✅ | |
| SRC-074 | `REQ-L0-005` | ✅ | |
| SRC-075 | `REQ-L0-003, REQ-L0-004, REQ-L0-010` | ✅ | |
| SRC-076 | `REQ-L0-004` | ✅ | |
| SRC-077 | `REQ-L0-002, REQ-L0-021` | ✅ | |
| SRC-078 | `REQ-L0-101, REQ-L0-201, REQ-L0-301, REQ-L0-960` | ✅ | |
| SRC-079 | `REQ-L0-011` | ✅ | |
| SRC-080 | `REQ-L0-012` | ✅ | |
| SRC-081 | `REQ-L0-013` | ✅ | |
| SRC-082 | `REQ-L0-014` | ✅ | |
| SRC-083 | `REQ-L0-015` | ✅ | |
| SRC-084 | `REQ-L0-016, REQ-L0-017` | ✅ | |
| SRC-085 | `REQ-L0-017` | ✅ | |
| SRC-086 | `TBD-L0-001` | ✅ | |
| SRC-087 | `TBD-L0-002` | ✅ | |
| SRC-088 | `TBD-L0-004` | ✅ | |
| SRC-089 | `TBD-L0-005` | ✅ | |
| SRC-090 | `TBD-L0-006` | ✅ | |
| SRC-091 | `TBD-L0-007` | ✅ | |
| SRC-092 | `TBD-L0-008` | ✅ | |
| SRC-093 | `TBD-L0-009` | ✅ | |
| SRC-094 | `TBD-L0-010` | ✅ | |
| SRC-095 | `TBD-L0-011` | ✅ | |
| SRC-096 | `TBD-L0-012` | ✅ | |
| SRC-097 | `TBD-L0-013` | ✅ | |
| SRC-098 | `N/A` | ✅ | process |
| SRC-099 | `N/A` | ✅ | process |

## 7. TBD & Questions（待定项）

| TBD-ID | Question / Missing Info | Impact | Source |
|--------|--------------------------|--------|--------|
| TBD-L0-001 | `[TBD-001] LLM Provider/Model 选择与成本上限分配` | H | `charter.yaml#open_questions[0]` |
| TBD-L0-002 | `[TBD-002] 降级策略定义：LLM/pgvector 不可用时的用户体验与返回格式` | H | `charter.yaml#open_questions[1]` |
| TBD-L0-003 | `（可选）现有网站登录态/用户标识注入方案` | M | `charter.yaml#dependencies.external_systems[1]` |
| TBD-L0-004 | `[TBD-003] 后台鉴权方式：最小可用方案（账号白名单/Basic Auth/接入现有 SSO）` | M | `charter.yaml#open_questions[2]` |
| TBD-L0-005 | `[TBD-004] 对话与日志留存策略：保留期、脱敏范围、合规要求` | H | `charter.yaml#open_questions[3]` |
| TBD-L0-006 | `[TBD-005] 推荐/比较字段配置来源：固定/后台可配/按类目不同` | M | `charter.yaml#open_questions[4]` |
| TBD-L0-007 | `[TBD-006] Widget 资源体积与加载口径（gzip、缓存策略、CDN）` | M | `charter.yaml#open_questions[5]` |
| TBD-L0-008 | `[TBD-007] STT/TTS Provider 选择与部署方式（在线/本地）及成本/延迟预算` | M | `charter.yaml#open_questions[6]` |
| TBD-L0-009 | `[TBD-008] 文件/图片上传支持格式、大小上限、存储方式与数据保留期（合规）` | H | `charter.yaml#open_questions[7]` |
| TBD-L0-010 | `[TBD-009] 多语言策略：语言检测/选择规则、知识库中英混合或翻译层、评测口径` | H | `charter.yaml#open_questions[8]` |
| TBD-L0-011 | `[TBD-010] 邮箱登录方案：验证码策略、发送渠道、防刷机制、合规边界` | H | `charter.yaml#open_questions[9]` |
| TBD-L0-012 | `[TBD-011] 人工客服转接方案：工作台形态、排队/通知、响应 SLA、离线与回退策略` | H | `charter.yaml#open_questions[10]` |
| TBD-L0-013 | `[TBD-012] 寻价功能定义：收集字段、触发条件、是否对接 CRM/工单、处理流程与权限` | H | `charter.yaml#open_questions[11]` |
| TBD-L0-014 | `产品 JSON 版本回滚的实现与数据模型（“保留原始 JSON 并提供版本回滚”）` | M | `charter.yaml#product_data_contract.notes[0]` |
| TBD-L0-015 | `Widget 上下文传递字段命名与传递方式（query/header/body）` | M | `charter.yaml#widget_context_contract.notes[0]` |
| TBD-L0-016 | `pgvector 性能与运维保障细节（容量/索引/备份/迁移/监控）` | M | `charter.yaml#assumptions[2]` |

## 8. Gate Check（门禁检查）

- [x] 上游每个条目：都有映射或 `N/A + 原因`
- [x] 下游每个 `REQ-ID`：都有至少一个 `Source`
- [x] 未出现“无来源的新需求”
- [x] 关键缺失信息已进入 TBD（且带来源）
