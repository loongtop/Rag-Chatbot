---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: "9bf2a6cdf4c711958850ff063d4702fdb071581b3bcdbb57e88c43b5413cef97"
---

# L0 Requirements: rag-chatbot

> 本文档必须 100% 可追溯到 `charter.yaml`（见 `docs/L0/split-report.md` 覆盖矩阵）。任何不明确/不可验证/不可实现的内容进入 `TBD` 并标注来源。

## 0. Sources（来源）

- `charter.yaml`（`meta.version=v0.1`；checksum: `9bf2a6cdf4c711958850ff063d4702fdb071581b3bcdbb57e88c43b5413cef97`）
- `docs/L0/split-report.md`（Charter → L0 拆分与覆盖矩阵）

## 1. Traceability Matrix（覆盖矩阵：Charter → L0）

| Charter Item | Covered By (REQ-ID / TBD-ID / N/A) | Status | Notes |
|-------------|-------------------------------------|--------|-------|
| `charter.yaml#objective.problems[0]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#objective.problems[1]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#objective.problems[2]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#objective.business_goals[0]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#objective.business_goals[1]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#objective.business_goals[2]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#stakeholders.users[0]` | `REQ-L0-002, REQ-L0-005, REQ-L0-006, REQ-L0-007` | ✅ | |
| `charter.yaml#stakeholders.users[1]` | `REQ-L0-002, REQ-L0-005, REQ-L0-006, REQ-L0-007` | ✅ | |
| `charter.yaml#stakeholders.users[2]` | `REQ-L0-002, REQ-L0-005` | ✅ | |
| `charter.yaml#scope.must_have[0]` | `REQ-L0-002` | ✅ | |
| `charter.yaml#scope.must_have[1]` | `REQ-L0-003, REQ-L0-020` | ✅ | |
| `charter.yaml#scope.must_have[2]` | `REQ-L0-004` | ✅ | |
| `charter.yaml#scope.must_have[3]` | `REQ-L0-005` | ✅ | |
| `charter.yaml#scope.must_have[4]` | `REQ-L0-006` | ✅ | |
| `charter.yaml#scope.must_have[5]` | `REQ-L0-007` | ✅ | |
| `charter.yaml#scope.must_have[6]` | `REQ-L0-008, REQ-L0-021` | ✅ | |
| `charter.yaml#scope.must_have[7]` | `REQ-L0-009` | ✅ | |
| `charter.yaml#scope.must_have[8]` | `REQ-L0-010` | ✅ | |
| `charter.yaml#scope.must_have[9]` | `REQ-L0-011` | ✅ | |
| `charter.yaml#scope.must_have[10]` | `REQ-L0-012` | ✅ | |
| `charter.yaml#scope.must_have[11]` | `REQ-L0-013` | ✅ | |
| `charter.yaml#scope.must_have[12]` | `REQ-L0-014` | ✅ | |
| `charter.yaml#scope.must_have[13]` | `REQ-L0-015` | ✅ | |
| `charter.yaml#scope.must_have[14]` | `REQ-L0-016, REQ-L0-017` | ✅ | |
| `charter.yaml#scope.out_of_scope[0]` | `REQ-L0-950` | ✅ | |
| `charter.yaml#scope.out_of_scope[1]` | `REQ-L0-951` | ✅ | |
| `charter.yaml#scope.out_of_scope[2]` | `REQ-L0-952` | ✅ | |
| `charter.yaml#scope.out_of_scope[3]` | `REQ-L0-953` | ✅ | |
| `charter.yaml#metrics.performance[0]` | `REQ-L0-101` | ✅ | |
| `charter.yaml#metrics.performance[1]` | `REQ-L0-102` | ✅ | |
| `charter.yaml#metrics.performance[2]` | `REQ-L0-103` | ✅ | |
| `charter.yaml#metrics.security[0]` | `REQ-L0-201` | ✅ | |
| `charter.yaml#metrics.security[1]` | `REQ-L0-202` | ✅ | |
| `charter.yaml#metrics.security[2]` | `REQ-L0-203` | ✅ | |
| `charter.yaml#metrics.security[3]` | `REQ-L0-204` | ✅ | |
| `charter.yaml#metrics.stability[0]` | `REQ-L0-301` | ✅ | |
| `charter.yaml#metrics.stability[1]` | `REQ-L0-302` | ✅ | |
| `charter.yaml#metrics.usability[0]` | `REQ-L0-401` | ✅ | |
| `charter.yaml#metrics.usability[1]` | `REQ-L0-402` | ✅ | |
| `charter.yaml#metrics.usability[2]` | `REQ-L0-403` | ✅ | |
| `charter.yaml#constraints.resource.budget` | `REQ-L0-901` | ✅ | |
| `charter.yaml#constraints.resource.timeline` | `REQ-L0-902` | ✅ | |
| `charter.yaml#constraints.technology_boundary.allowed` | `REQ-L0-903` | ✅ | |
| `charter.yaml#constraints.technology_boundary.forbidden` | `REQ-L0-903` | ✅ | |
| `charter.yaml#dependencies.external_systems[0]` | `REQ-L0-801` | ✅ | |
| `charter.yaml#dependencies.external_systems[1]` | `TBD-L0-003` | ✅ | |
| `charter.yaml#dependencies.resources` | `REQ-L0-802` | ✅ | |
| `charter.yaml#product_data_contract` | `REQ-L0-020` | ✅ | |
| `charter.yaml#widget_context_contract` | `REQ-L0-021` | ✅ | |
| `charter.yaml#risks[0]` | `REQ-L0-009, REQ-L0-203, REQ-L0-210, REQ-L0-901` | ✅ | |
| `charter.yaml#risks[1]` | `REQ-L0-004, REQ-L0-211` | ✅ | |
| `charter.yaml#risks[2]` | `REQ-L0-212` | ✅ | |
| `charter.yaml#risks[3]` | `REQ-L0-201, REQ-L0-202, REQ-L0-204` | ✅ | |
| `charter.yaml#risks[4]` | `REQ-L0-101, REQ-L0-102, REQ-L0-103, REQ-L0-210` | ✅ | |
| `charter.yaml#risks[5]` | `REQ-L0-015, REQ-L0-213` | ✅ | |
| `charter.yaml#risks[6]` | `REQ-L0-214, REQ-L0-302` | ✅ | |
| `charter.yaml#risks[7]` | `REQ-L0-214` | ✅ | |
| `charter.yaml#risks[8]` | `REQ-L0-215` | ✅ | |
| `charter.yaml#risks[9]` | `REQ-L0-012, REQ-L0-216` | ✅ | |
| `charter.yaml#risks[10]` | `REQ-L0-017, REQ-L0-217` | ✅ | |
| `charter.yaml#deliverables.mandatory[0]` | `REQ-L0-001` | ✅ | |
| `charter.yaml#deliverables.mandatory[1]` | `REQ-L0-002` | ✅ | |
| `charter.yaml#deliverables.mandatory[2]` | `REQ-L0-010` | ✅ | |
| `charter.yaml#deliverables.mandatory[3]` | `REQ-L0-004` | ✅ | |
| `charter.yaml#deliverables.mandatory[4]` | `REQ-L0-060` | ✅ | |
| `charter.yaml#deliverables.mandatory[5]` | `REQ-L0-061` | ✅ | |
| `charter.yaml#deliverables.mandatory[6]` | `REQ-L0-062` | ✅ | |
| `charter.yaml#quality_requirements` | `REQ-L0-104, REQ-L0-205, REQ-L0-960` | ✅ | |
| `charter.yaml#components` | `REQ-L0-970` | ✅ | |
| `charter.yaml#assumptions[0]` | `REQ-L0-002, REQ-L0-021` | ✅ | |
| `charter.yaml#assumptions[1]` | `REQ-L0-020` | ✅ | |
| `charter.yaml#assumptions[2]` | `TBD-L0-016` | ✅ | |
| `charter.yaml#acceptance_criteria[0]` | `REQ-L0-018` | ✅ | |
| `charter.yaml#acceptance_criteria[1]` | `REQ-L0-005` | ✅ | |
| `charter.yaml#acceptance_criteria[2]` | `REQ-L0-003, REQ-L0-004, REQ-L0-010` | ✅ | |
| `charter.yaml#acceptance_criteria[3]` | `REQ-L0-004` | ✅ | |
| `charter.yaml#acceptance_criteria[4]` | `REQ-L0-002, REQ-L0-021` | ✅ | |
| `charter.yaml#acceptance_criteria[5]` | `REQ-L0-101, REQ-L0-201, REQ-L0-301, REQ-L0-960` | ✅ | |
| `charter.yaml#acceptance_criteria[6]` | `REQ-L0-011` | ✅ | |
| `charter.yaml#acceptance_criteria[7]` | `REQ-L0-012` | ✅ | |
| `charter.yaml#acceptance_criteria[8]` | `REQ-L0-013` | ✅ | |
| `charter.yaml#acceptance_criteria[9]` | `REQ-L0-014` | ✅ | |
| `charter.yaml#acceptance_criteria[10]` | `REQ-L0-015` | ✅ | |
| `charter.yaml#acceptance_criteria[11]` | `REQ-L0-016, REQ-L0-017` | ✅ | |
| `charter.yaml#acceptance_criteria[12]` | `REQ-L0-017` | ✅ | |
| `charter.yaml#open_questions[0]` | `TBD-L0-001` | ✅ | |
| `charter.yaml#open_questions[1]` | `TBD-L0-002` | ✅ | |
| `charter.yaml#open_questions[2]` | `TBD-L0-004` | ✅ | |
| `charter.yaml#open_questions[3]` | `TBD-L0-005` | ✅ | |
| `charter.yaml#open_questions[4]` | `TBD-L0-006` | ✅ | |
| `charter.yaml#open_questions[5]` | `TBD-L0-007` | ✅ | |
| `charter.yaml#open_questions[6]` | `TBD-L0-008` | ✅ | |
| `charter.yaml#open_questions[7]` | `TBD-L0-009` | ✅ | |
| `charter.yaml#open_questions[8]` | `TBD-L0-010` | ✅ | |
| `charter.yaml#open_questions[9]` | `TBD-L0-011` | ✅ | |
| `charter.yaml#open_questions[10]` | `TBD-L0-012` | ✅ | |
| `charter.yaml#open_questions[11]` | `TBD-L0-013` | ✅ | |
| `charter.yaml#traceability` | `N/A` | ✅ | process config |
| `charter.yaml#freeze` | `N/A` | ✅ | freeze metadata |

## 2. Functional Requirements

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-001 | P0 | 系统应当提供“嵌入式产品知识库 RAG Chatbot”能力，用于回答产品问题、提供推荐与对比，以解决 Charter 中的问题并支撑业务目标。 | `charter.yaml#objective.problems[0]`, `charter.yaml#objective.problems[1]`, `charter.yaml#objective.problems[2]`, `charter.yaml#objective.business_goals[0]`, `charter.yaml#objective.business_goals[1]`, `charter.yaml#objective.business_goals[2]` | L0 P0 功能需求（REQ-L0-002~017）可实现且可验收；关键指标/门禁在测试报告中给出结果或偏差说明。 |
| REQ-L0-002 | P0 | 系统应当提供可嵌入现有产品网站的 Chatbot Widget，并提供最小集成示例。 | `charter.yaml#scope.must_have[0]`, `charter.yaml#deliverables.mandatory[1]`, `charter.yaml#acceptance_criteria[4]` | 提供最小集成示例；Widget 可在现有网站页面展示并发起对话；可配置挂载点与基础样式。 |
| REQ-L0-003 | P0 | 系统应当支持从 JSON 文件加载约 600 SKU，并提供后台上传/替换与基础检索能力。 | `charter.yaml#scope.must_have[1]`, `charter.yaml#acceptance_criteria[2]` | 后台可上传/替换 `data/products.json`；替换后检索可命中新增/更新 SKU；支持按关键字/类别等基础检索（细节进入 L1/L2）。 |
| REQ-L0-004 | P0 | 系统应当支持知识库导入与索引：后台上传文档并写入 PostgreSQL + pgvector；支持重建索引、状态查看，并支持检索结果排序/重排。 | `charter.yaml#scope.must_have[2]`, `charter.yaml#deliverables.mandatory[3]`, `charter.yaml#acceptance_criteria[3]` | 后台可上传文档并触发索引构建；可查看构建状态/日志/失败原因；可触发重建；检索结果具备可定义的排序/重排能力（算法进入 L1/L2）。 |
| REQ-L0-005 | P0 | 系统应当提供 RAG 问答：回答默认附带来源引用（文档/产品字段）；无足够依据时优先澄清或拒答。 | `charter.yaml#scope.must_have[3]`, `charter.yaml#acceptance_criteria[1]` | 每次回答包含可追溯引用；当检索证据不足时返回澄清问题或拒答，并避免编造。 |
| REQ-L0-006 | P0 | 系统应当提供产品推荐：基于用户需求输出 Top-N（默认 3）SKU，包含推荐理由与依据来源。 | `charter.yaml#scope.must_have[4]` | 默认返回 3 个 SKU（可配置）；每个推荐项包含理由与来源引用（来自文档/产品字段）。 |
| REQ-L0-007 | P0 | 系统应当支持产品比较：支持 2–4 个 SKU，输出结构化对比（表格/卡片），字段可配置。 | `charter.yaml#scope.must_have[5]` | 支持输入 2–4 个 SKU；输出结构化对比；字段配置来源与配置方式见 `TBD-L0-006`。 |
| REQ-L0-008 | P0 | 系统应当支持上下文感知：Widget 可传入当前页面 `productId/skuId/url`，后端用于检索与排序。 | `charter.yaml#scope.must_have[6]`, `charter.yaml#acceptance_criteria[4]` | Widget 请求携带 `skuId/productId/url`（方式见 `TBD-L0-015`）；后端可在检索/排序逻辑中使用上下文。 |
| REQ-L0-009 | P0 | 系统应当支持对话历史管理：支持多轮对话；记录引用、错误与 token 用量，用于成本与质量分析。 | `charter.yaml#scope.must_have[7]` | 支持多轮上下文；每轮记录引用与错误；记录 token 用量并可按会话/用户（登录后）汇总。 |
| REQ-L0-010 | P0 | 系统应当提供后台管理 UI：产品 JSON 管理、文档上传、索引构建/状态、操作日志，并包含人工客服转接处理与寻价/线索管理入口。 | `charter.yaml#scope.must_have[8]`, `charter.yaml#deliverables.mandatory[2]` | 后台 UI 覆盖上述功能入口；关键操作有审计/日志；索引构建状态可观测。 |
| REQ-L0-011 | P0 | 系统应当支持 LLM Provider 可配置切换：在线 OpenAI-Compatible API（如 ChatGPT/DeepSeek）与本地 Ollama 两种模式。 | `charter.yaml#scope.must_have[9]`, `charter.yaml#acceptance_criteria[6]` | 通过配置切换在线/本地；两种模式均可完成基础对话/RAG 流程；Provider/Model 选型见 `TBD-L0-001`。 |
| REQ-L0-012 | P0 | 系统应当支持人工/AI 入口切换：用户可在输入界面选择“人工”或“AI”；默认使用 AI；选择“人工”时将对话转接到后台人工队列/工作台处理。 | `charter.yaml#scope.must_have[10]`, `charter.yaml#acceptance_criteria[7]` | 默认 AI；用户选择人工后，产生可在后台处理的转接任务（工作台形态见 `TBD-L0-012`）；支持回退策略见 `REQ-L0-216`。 |
| REQ-L0-013 | P0 | 系统应当支持语音交互：Widget 支持语音输入（STT）与语音输出（TTS），且 STT/TTS Provider 可配置。 | `charter.yaml#scope.must_have[11]`, `charter.yaml#acceptance_criteria[8]` | 语音输入可驱动同一对话/RAG 流程；语音输出可播放；Provider 选型见 `TBD-L0-008`。 |
| REQ-L0-014 | P0 | 系统应当支持中文/英文：Widget 与后台 UI 支持中文/英文；用户可选择输出语言（默认中文）。 | `charter.yaml#scope.must_have[12]`, `charter.yaml#acceptance_criteria[9]` | UI 与回答可在中文/英文间切换；引用/推荐/对比输出语言与选择一致；多语言策略见 `TBD-L0-010`。 |
| REQ-L0-015 | P0 | 系统应当支持文件/图片输入：Widget 支持用户上传文件或图片作为对话输入；系统提取内容用于回答，并对类型/大小做限制。 | `charter.yaml#scope.must_have[13]`, `charter.yaml#acceptance_criteria[10]` | 支持上传并提取内容参与回答；超限或不支持类型时返回清晰错误；格式/大小/存储与保留期见 `TBD-L0-009`。 |
| REQ-L0-016 | P0 | 系统应当支持邮箱验证码登录/验证；登录后可将对话与浏览行为关联到用户用于后台分析；登录后解锁“寻价”与“联系人工客服”功能。 | `charter.yaml#scope.must_have[14]`, `charter.yaml#acceptance_criteria[11]` | 邮箱验证码登录可用；登录后可触发寻价与联系人工入口；合规边界与防刷机制见 `TBD-L0-011`。 |
| REQ-L0-017 | P0 | 系统应当支持“寻价”请求：登录用户可提交寻价并形成可追踪记录，后台可查看/处理/导出。 | `charter.yaml#acceptance_criteria[12]`, `charter.yaml#risks[10]` | 登录用户可提交寻价请求并生成记录；后台可按用户维度关联查看；字段/流程/权限见 `TBD-L0-013`。 |
| REQ-L0-018 | P0 | 后端应当提供对话/RAG/推荐/对比相关接口，并提供可用的 OpenAPI 文档。 | `charter.yaml#acceptance_criteria[0]` | 可访问 OpenAPI 文档；包含主要接口与请求/响应示例（细节进入 L1/L2）。 |
| REQ-L0-020 | P0 | 系统应当遵循 `product_data_contract`：产品数据来源为 `data/products.json` 且至少包含约定的最小字段集合。 | `charter.yaml#product_data_contract`, `charter.yaml#assumptions[1]` | 校验并拒绝缺失关键字段的输入；字段扩展被保留；版本回滚实现见 `TBD-L0-014`。 |
| REQ-L0-021 | P0 | 系统应当遵循 `widget_context_contract`：Widget 向后端传递 `skuId/productId/url` 上下文字段以支持检索与分析。 | `charter.yaml#widget_context_contract`, `charter.yaml#assumptions[0]` | 至少传 `skuId` 或 `productId`；支持传 `url`；字段命名与传递方式见 `TBD-L0-015`。 |
| REQ-L0-060 | P1 | 项目应当交付部署文档与集成指南。 | `charter.yaml#deliverables.mandatory[4]` | 文档覆盖本地/云端部署与 Widget 集成步骤（细节进入 L1/L2）。 |
| REQ-L0-061 | P1 | 项目应当交付完整源代码。 | `charter.yaml#deliverables.mandatory[5]` | 代码可在约定环境中构建/运行（细节进入 CI/CD 约定）。 |
| REQ-L0-062 | P1 | 项目应当交付测试报告（含关键用例与性能基线）。 | `charter.yaml#deliverables.mandatory[6]` | 报告包含关键用例结果与性能基线数据；偏差需解释。 |
| REQ-L0-801 | P0 | 系统应当可与“现有产品网站”集成：提供嵌入入口并支持页面上下文注入；（可选）识别现有网站登录态/用户标识注入方案。 | `charter.yaml#dependencies.external_systems[0]`, `charter.yaml#dependencies.external_systems[1]` | Widget 可在现有网站嵌入；上下文可传递；登录态注入方案见 `TBD-L0-003`。 |
| REQ-L0-802 | P0 | 系统应当将外部依赖作为可配置资源管理（如 PostgreSQL+pgvector、在线/本地 LLM、STT/TTS、OCR/文档解析、邮件发送等）。 | `charter.yaml#dependencies.resources` | 依赖项可通过配置切换/启停；在缺失依赖时按降级策略处理（见 `TBD-L0-002`）。 |

## 3. Non-Functional Requirements

### Performance

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-101 | P0 | 端到端首次响应时间 p95 应当 <= 1.5s（包含 LLM；口径以服务端为准）。 | `charter.yaml#metrics.performance[0]`, `charter.yaml#quality_requirements.performance.response_time_p95` | 测试报告给出 p95 结果（服务端口径）；若不达标需列出原因与改进计划。 |
| REQ-L0-102 | P0 | RAG 检索延迟 p95 应当 <= 500ms（pgvector 查询；口径以服务端为准）。 | `charter.yaml#metrics.performance[1]` | 测试报告给出 pgvector 查询 p95 延迟。 |
| REQ-L0-103 | P1 | 系统应当支持并发会话 >= 100（连接保持 5 分钟；压测脚本与环境 TBD）。 | `charter.yaml#metrics.performance[2]` | 压测方案与环境在 `TBD-L0-015` 定义；报告给出并发结果或偏差说明。 |
| REQ-L0-104 | P1 | 系统应当满足吞吐 >= 100rps 且单实例内存上限 <= 1GB（口径以服务端为准）。 | `charter.yaml#quality_requirements.performance.throughput`, `charter.yaml#quality_requirements.performance.memory_limit` | 测试报告给出吞吐与内存基线；若需按组件拆分口径，在 L1/L2 定义。 |
| REQ-L0-210 | P1 | 系统应当具备成本与性能优化手段：记录 token 用量、支持缓存（可使用 Redis）与限流，以控制成本并改善高并发性能。 | `charter.yaml#scope.must_have[7]`, `charter.yaml#constraints.technology_boundary.allowed`, `charter.yaml#risks[0]`, `charter.yaml#risks[4]` | 能按会话统计 token；可配置缓存开关；存在基础限流策略（具体阈值进入 L1/L2）。 |
| REQ-L0-211 | P1 | 系统应当支持 RAG 检索质量持续改进：支持分段/召回/重排策略调整与评测回归（Embedding 模型切换等细节 TBD）。 | `charter.yaml#risks[1]`, `charter.yaml#scope.must_have[2]` | 至少支持检索结果重排；评测集与回归口径在 L1/L2 明确（部分见 `TBD-L0-010`）。 |

### Security

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-201 | P0 | 所有对外通信应当使用 HTTPS。 | `charter.yaml#metrics.security[0]` | 生产/测试环境仅暴露 HTTPS；HTTP 请求被拒绝或重定向（策略在 L1/L2 定义）。 |
| REQ-L0-202 | P0 | 系统应当对敏感数据做脱敏处理（如手机号/邮箱等）。 | `charter.yaml#metrics.security[1]` | 日志/审计/可观测数据中不出现明文敏感字段；脱敏规则在 `TBD-L0-005` 细化。 |
| REQ-L0-203 | P0 | 系统应当实施 API 访问频率限制与后台操作审计日志。 | `charter.yaml#metrics.security[2]`, `charter.yaml#risks[0]` | 存在基础限流；后台关键操作可追溯（操作者/时间/动作）；阈值与策略进入 L1/L2。 |
| REQ-L0-204 | P0 | 系统应当具备 Prompt Injection 基础防护（引用内容转义、系统提示不可被覆盖）。 | `charter.yaml#metrics.security[3]`, `charter.yaml#risks[3]` | 引用内容被安全处理；系统提示与工具调用边界在 L1/L2 规范化。 |
| REQ-L0-205 | P1 | 项目应当对依赖与代码安全进行门禁：漏洞扫描、依赖审计、敏感信息检测。 | `charter.yaml#quality_requirements.security` | CI 或交付检查中包含上述扫描；结果在测试/交付物中可审计。 |
| REQ-L0-213 | P0 | 文件/图片上传应当具备安全与合规控制：类型/大小限制、恶意内容/隐私风险控制与保留期策略。 | `charter.yaml#scope.must_have[13]`, `charter.yaml#risks[5]` | 拒绝不支持格式/超限；对上传内容执行基础安全处理；保留期与扫描策略见 `TBD-L0-009`、`TBD-L0-005`。 |
| REQ-L0-215 | P0 | 邮箱验证码登录应当具备防滥用机制与审计能力（频控、验证码策略、告知与合规边界）。 | `charter.yaml#scope.must_have[14]`, `charter.yaml#risks[8]`, `charter.yaml#open_questions[9]` | 存在频控与验证码策略；关键操作可审计；合规边界在 `TBD-L0-011` 明确。 |
| REQ-L0-217 | P0 | 寻价/线索数据应当遵循最小化收集与访问控制原则，并定义留存/脱敏/导出策略。 | `charter.yaml#risks[10]`, `charter.yaml#open_questions[11]` | 后台访问受控且可审计；留存策略在 `TBD-L0-005` 与 `TBD-L0-013` 中明确。 |

### Reliability

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-301 | P0 | 系统可用性应当 >= 99.5%（月）。 | `charter.yaml#metrics.stability[0]` | 可用性口径在 L1/L2 明确，并在测试报告或上线监控中可验证。 |
| REQ-L0-302 | P0 | 当 LLM/数据库异常时系统应当自动恢复并优雅降级（降级策略 TBD）。 | `charter.yaml#metrics.stability[1]`, `charter.yaml#open_questions[1]` | 降级策略在 `TBD-L0-002` 明确；演练用例在测试报告中体现。 |
| REQ-L0-216 | P0 | 人工客服转接应当具备排队/通知/响应 SLA 与离线处理能力，并提供回退 AI 策略。 | `charter.yaml#risks[9]`, `charter.yaml#open_questions[10]`, `charter.yaml#scope.must_have[10]` | 人工入口不可用或超时可回退到 AI 或离线收集信息；SLA 与工作台形态在 `TBD-L0-012` 明确。 |

### Usability

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-401 | P1 | Widget 加载时间应当 <= 1s（口径 TBD）。 | `charter.yaml#metrics.usability[0]` | 口径与测量方法在 `TBD-L0-007` 明确并给出基线。 |
| REQ-L0-402 | P0 | Widget 应当支持移动端自适应。 | `charter.yaml#metrics.usability[1]` | 在主流移动端分辨率下可正常使用（具体范围在 L1/L2 定义）。 |
| REQ-L0-403 | P1 | Widget 应当做到无需用户培训即可使用（信息架构与引导明确）。 | `charter.yaml#metrics.usability[2]` | 可用性验收口径在 L1/L2 明确（如任务完成率/可用性测试）。 |
| REQ-L0-214 | P1 | 语音/多语言/上传等高成本能力应当支持开关与降级策略，以控制延迟与成本，并支持质量评测回归。 | `charter.yaml#risks[6]`, `charter.yaml#risks[7]` | 支持按配置启停能力；降级策略与评测口径在 `TBD-L0-002`、`TBD-L0-010` 中明确。 |

### Quality Gates

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-960 | P1 | 项目应当满足代码质量门禁：测试覆盖率 95%、类型覆盖 100%、复杂度上限 10、文档要求为 required。 | `charter.yaml#quality_requirements.code` | CI 或交付检查可输出覆盖率/类型覆盖/复杂度与文档检查结果。 |

## 4. Inputs/Outputs

**Inputs**:
- End-user: `message: string`, `mode: ai|human`, `language: zh|en`, `context: {skuId?, productId?, url?}`, `attachments?: file[]`, `session_id`
- Auth: `email` + `otp`（登录后获得 `user_id`/token）
- Admin: 产品 JSON 上传、文档上传、索引构建操作、人工客服处理、寻价处理

**Outputs**:
- Chat response: `answer`, `citations[]`, `recommended_skus[]`, `comparison`（可选）, `actions`（如 login/quote/contact-human）
- Observability: 对话历史、引用记录、错误记录、token 用量、操作审计日志

## 5. Constraints

- `REQ-L0-901`：云服务月成本 `< $5000`（含 LLM token、数据库、日志/监控、存储与带宽）。`Source: charter.yaml#constraints.resource.budget`
- `REQ-L0-902`：V0.1 目标时间 `2026-02-28`。`Source: charter.yaml#constraints.resource.timeline`
- `REQ-L0-903`：技术边界必须符合 allowed/forbidden 列表（V0.1 统一使用 pgvector；禁止 Pinecone；不做自建 LLM 训练等）。`Source: charter.yaml#constraints.technology_boundary.allowed, charter.yaml#constraints.technology_boundary.forbidden`
- `REQ-L0-950`：不做完整认证/账号体系（仅邮箱验证码登录；不支持密码/OAuth/SSO/MFA/复杂权限）。`Source: charter.yaml#scope.out_of_scope[0]`
- `REQ-L0-951`：不做订单处理和支付功能。`Source: charter.yaml#scope.out_of_scope[1]`
- `REQ-L0-952`：不做知识库自动爬取/自动同步（V0.1 仅手动上传/替换）。`Source: charter.yaml#scope.out_of_scope[2]`
- `REQ-L0-953`：不做自建 LLM 训练。`Source: charter.yaml#scope.out_of_scope[3]`
- `REQ-L0-970`：系统组件边界为 `api-server`（Python/FastAPI）、`chat-widget`（TS/React）、`admin-dashboard`（TS/React）。`Source: charter.yaml#components`

## 6. TBD / Open Questions（待定项）

| TBD-ID | Question | Source | Notes |
|--------|----------|--------|-------|
| TBD-L0-001 | `[TBD-001] LLM Provider/Model 选择与成本上限分配` | `charter.yaml#open_questions[0]` | |
| TBD-L0-002 | `[TBD-002] 降级策略定义：LLM/pgvector 不可用时的用户体验与返回格式` | `charter.yaml#open_questions[1]` | |
| TBD-L0-003 | `（可选）现有网站登录态/用户标识注入方案` | `charter.yaml#dependencies.external_systems[1]` | |
| TBD-L0-004 | `[TBD-003] 后台鉴权方式：最小可用方案（账号白名单/Basic Auth/接入现有 SSO）` | `charter.yaml#open_questions[2]` | |
| TBD-L0-005 | `[TBD-004] 对话与日志留存策略：数据保留期、脱敏范围、合规要求` | `charter.yaml#open_questions[3]` | |
| TBD-L0-006 | `[TBD-005] 推荐/比较字段配置来源：固定配置/后台可配/按类目不同` | `charter.yaml#open_questions[4]` | |
| TBD-L0-007 | `[TBD-006] Widget 资源体积与加载口径（gzip、缓存策略、CDN）` | `charter.yaml#open_questions[5]` | |
| TBD-L0-008 | `[TBD-007] STT/TTS Provider 选择与部署方式（在线/本地）及成本/延迟预算` | `charter.yaml#open_questions[6]` | |
| TBD-L0-009 | `[TBD-008] 文件/图片上传支持格式、大小上限、存储方式与数据保留期（合规）` | `charter.yaml#open_questions[7]` | |
| TBD-L0-010 | `[TBD-009] 多语言策略：语言检测/选择规则、知识库中英混合或翻译层、评测口径` | `charter.yaml#open_questions[8]` | |
| TBD-L0-011 | `[TBD-010] 邮箱登录方案：验证码策略、发送渠道、防刷机制、用户数据与行为分析的合规边界` | `charter.yaml#open_questions[9]` | |
| TBD-L0-012 | `[TBD-011] 人工客服转接方案：工作台形态、排队/通知机制、响应 SLA、离线处理与回退策略` | `charter.yaml#open_questions[10]` | |
| TBD-L0-013 | `[TBD-012] 寻价功能定义：收集字段、触发条件、是否对接 CRM/工单、处理流程与权限` | `charter.yaml#open_questions[11]` | |
| TBD-L0-014 | `产品 JSON 版本回滚（保留原始 JSON 并提供版本回滚）的实现与数据模型` | `charter.yaml#product_data_contract.notes[0]` | |
| TBD-L0-015 | `Widget 上下文传递字段命名与传递方式（query/header/body）` | `charter.yaml#widget_context_contract.notes[0]` | |
| TBD-L0-016 | `pgvector 运维与性能保障细节（容量/索引/备份/监控等）` | `charter.yaml#assumptions[2]` | |

## 7. Gate Check（门禁）

- [ ] 100% L0 需求条目包含 `Source`
- [ ] `charter.yaml` 关键条目已覆盖（或 N/A + 原因）
- [ ] 未引入“无来源的新需求”
