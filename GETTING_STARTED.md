# Charter Agent Framework v0.6.3 详细使用指南

本文档提供从零开始使用 Charter Agent Framework 实现软件的完整、详细步骤。

---

## 第一部分：环境准备

### Step 1.1：选择 AI 编辑器

确保你已安装并配置好以下任一 AI 编辑器：
- **Antigravity IDE**（推荐）
- Cursor
- 其他支持 `.agent/` 规则目录的编辑器

### Step 1.2：准备语言工具链

根据你的项目语言，确保已安装对应工具链：

| 语言 | 工具要求 |
|------|----------|
| Python | Python 3.10+, pip, pytest, mypy, ruff |
| Java | JDK 17+, Maven/Gradle, JUnit |
| C++ | GCC/Clang, CMake, GoogleTest |
| Swift | Xcode 15+, Swift Package Manager |

### Step 1.3：获取 Charter Framework

```bash
# 方式 A：克隆仓库
git clone https://github.com/loongtop/charter-agent-framework.git

# 方式 B：下载 zip
# 从 GitHub 下载并解压
```

---

## 第二部分：项目初始化

### Step 2.1：创建新项目目录

```bash
# 创建项目文件夹
mkdir my-awesome-project

# 进入目录
cd my-awesome-project

# （可选）初始化 Git
git init
```

### Step 2.2：复制框架文件到项目

```bash
# 复制 .agent 目录（包含所有规则、模板、工作流）
cp -r /path/to/charter-agent-framework/.agent .

# 复制 charter 模板并重命名
cp /path/to/charter-agent-framework/charter.template.yaml ./charter.yaml

# （可选）复制入门指南
cp /path/to/charter-agent-framework/GETTING_STARTED.md .
```

### Step 2.3：在 AI 编辑器中打开项目

在 Antigravity 或其他 AI 编辑器中：
- 打开 `my-awesome-project` 作为 Workspace
- 确认左侧文件树中能看到 `.agent/` 目录
- AI 会自动加载 `.agent/rules/` 中的 Agent 规则

### Step 2.4：执行 /charter-init 生成目录结构

在 AI 对话框中输入：
```
/charter-init
```

这会创建以下目录结构：
```
my-awesome-project/
├── .agent/           # 框架文件（已复制）
├── docs/
│   ├── L0/           # Phase 1：系统级需求
│   ├── L1/           # Phase 1：Feature 级需求
│   ├── L2/           # Phase 1：模块级需求 + 模块间接口契约
│   └── architecture/ # Phase 1.5：技术架构设计
├── specs/            # Phase 2：Spec 树（leaf 可直接写代码）
├── src/              # Phase 3：源代码
├── tests/            # Phase 3：测试代码
└── charter.yaml      # 项目任务书
```

---

## 第三部分：编写 Charter（任务书）

### Step 3.1：理解 Charter 结构

打开 `charter.yaml`，它包含以下核心部分：

| 部分 | 必填 | 说明 |
|------|------|------|
| `meta` | ✅ | 项目基本信息（名称、负责人、版本） |
| `objective` | ✅ | 核心问题和商业目标 |
| `scope` | ✅ | 必做事项和不做事项 |
| `stakeholders` | ⚠️ 建议 | 干系人和用户画像 |
| `metrics` | ⚠️ 建议 | 性能、安全、稳定性指标（影响测试门禁） |
| `constraints` | ⚠️ 建议 | 预算、时间、技术约束 |
| `dependencies` | ⚠️ 建议 | 外部系统和资源依赖 |
| `risks` | ⚠️ 建议 | 已知风险及应对 |
| `deliverables` | ✅ | 交付物列表 |
| `environments` | ⚠️ 建议 | 开发/测试/生产环境配置 |
| `quality_requirements` | ✅ | 代码质量、性能、安全要求 |
| `language_profile` 或 `components` | ✅ | 编程语言（python/java/cpp/swift） |
| `freeze` | 自动 | 冻结状态（由 /charter-freeze 管理） |

> **说明**：
> - ✅ = 必填，不提供会阻塞后续流程
> - ⚠️ 建议 = 非强制，但缺少会影响质量门禁评估
> - 自动 = 由工作流自动管理，无需手动填写

### Step 3.2：填写 Meta 部分

```yaml
meta:
  id: "PRJ-20260111-001"       # 唯一项目编号
  name: "my-awesome-project"   # 项目英文名（用于 repo）
  owner: "Your Name"           # 项目负责人
  version: "1.0"               # 任务书版本
```

### Step 3.3：填写 Objective 部分

```yaml
objective:
  problems:                    # 要解决的核心痛点（1-3个）
    - "用户无法高效管理日常任务"
    - "现有工具学习成本太高"
  business_goals:              # 对应的商业价值（可量化）
    - "提升用户效率 30%"
    - "获取 1000 名活跃用户"
```

### Step 3.4：填写 Scope 部分

```yaml
scope:
  must_have:                   # 本版本必须做
    - "用户注册和登录"
    - "创建、编辑、删除任务"
    - "任务列表展示"
    - "任务搜索功能"
  out_of_scope:                # 本版本明确不做
    - "多用户协作"
    - "移动端 App"
    - "第三方日历同步"
```

### Step 3.5：填写 Quality Requirements 部分

```yaml
quality_requirements:
  code:
    test_coverage: "95%"       # 测试覆盖率要求
    type_coverage: "100%"      # 类型注解覆盖率
    complexity_limit: 10       # 圈复杂度上限
    documentation: "required"  # 文档要求
  
  performance:
    response_time_p95: "200ms" # 95分位响应时间
    throughput: "1000rps"      # 吞吐量要求
    memory_limit: "512MB"      # 内存限制
  
  security:
    vulnerability_scan: "required"
    dependency_audit: "required"
    secrets_detection: "required"
```

### Step 3.6：设置 Language Profile

```yaml
# 单语言项目
language_profile: python       # python | java | cpp | swift

# 或多语言/混合项目（取消注释）
# components:
#   - name: "backend-api"
#     language_profile: python
#     path: "services/api"
#   - name: "core-engine"
#     language_profile: cpp
#     path: "libs/core"
```

### Step 3.7：验证 Charter

在 AI 对话框中输入：
```
/charter-validate
```

**如果验证失败**：
- 阅读错误信息
- 修正 charter.yaml 中的问题
- 重新运行 `/charter-validate`

**如果验证通过**：继续下一步

---

## 第四部分：冻结 Charter

### Step 4.1：理解为什么要冻结

**问题**：LLM 在后续步骤中可能"重新理解"charter，导致需求漂移

**解决**：冻结 charter，使所有 Agent 只能引用、不能修改

### Step 4.2：执行冻结

在 AI 对话框中输入：
```
/charter-freeze
```

### Step 4.3：验证冻结状态

检查 `charter.yaml` 底部的 `freeze` 部分：

```yaml
freeze:
  frozen: true                 # ← 应该是 true
  checksum: "abc123..."        # ← 应该有值
  frozen_at: "2026-01-11T..."  # ← 应该有时间戳
  frozen_by: "Your Name"       # ← 应该有操作人
```

### Step 4.4：如果需要修改 Charter

```
# 1. 解冻
/charter-unfreeze

# 2. 编辑 charter.yaml

# 3. 重新验证
/charter-validate

# 4. 重新冻结
/charter-freeze
```

---

## 第五部分：Phase 1 - 递归分解

### Step 5.1：理解分解层级

| 层级 | 名称 | 粒度 | 模板 |
|------|------|------|------|
| L0 | Charter | 整个项目 | `requirements.L0.template.md` |
| L1 | Features | 功能模块 | `requirements.L1.template.md` |
| L2 | Modules | 子模块 | `requirements.L2.template.md` |
| SPEC | Specs | 可实现规格（可递归） | `spec.template.md` |

> **v0.6.0**: L0-L2 是需求文档层（L2 为终点）；实现粒度通过 `/spec` 递归分解到 leaf Spec。所有 requirements 模板使用 Registry 块作为唯一事实源。生成后必须执行 `/requirements-render` + `/requirements-validate`。

### Step 5.2：L0 分解（Charter → Features）

告诉 AI：
```
请先运行 /requirements-split：
/requirements-split source_path=charter.yaml target_dir=docs/L0

请按 architect-agent 角色分析 charter.yaml。
1. 在 docs/L0/ 创建 requirements.md（使用 requirements.L0.template.md）
   - 每条需求必须有 REQ-ID + Source（可追溯到 charter.yaml）
2. 在 docs/L0/ 创建 subtasks.md，列出 L1 功能模块
3. 执行 /requirements-render L0 和 /requirements-validate L0
```

**检查产出**：
- `docs/L0/requirements.md` - 系统级需求
- `docs/L0/subtasks.md` - L1 子任务列表
- `docs/L0/split-report.md` - 拆分报告（覆盖矩阵、TBD）

### Step 5.3：L1 分解（Features）

对于 L0 subtasks.md 中列出的每个功能，告诉 AI：
```
请先运行 /requirements-split：
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L1/{功能名}

请分解 L1 功能 "{功能名}"。
1. 在 docs/L1/{功能名}/ 创建 requirements.md（使用 requirements.L1.template.md）
   - L0→L1 必须逐条映射（每条需求必须有 Source=REQ-L0-xxx）
2. 创建 subtasks.md 列出 L2 子模块
   - v0.6.0：L1 不产出模块间接口契约；接口在 L2 的 `docs/L2/interfaces.md` 统一定义
```

**检查产出**：
- `docs/L1/{功能名}/requirements.md` - 包含 goals, non_goals, constraints, risks
- `docs/L1/{功能名}/subtasks.md` - L2 子任务列表
- `docs/L1/{功能名}/split-report.md` - 拆分报告（覆盖矩阵、TBD）

### Step 5.4：L2 分解（Modules）

对于 L1 subtasks.md 中列出的每个模块，告诉 AI：
```
请先运行 /requirements-split：
/requirements-split source_path=docs/L1/{功能名}/requirements.md target_dir=docs/L2/{模块名}

请分解 L2 模块 "{模块名}"。
1. 在 docs/L2/{模块名}/ 创建 requirements.md（使用 requirements.L2.template.md）
   - L1→L2 可按段落/句子映射，但每条必须有 Source=REQ-L1-xxx
2. 在 docs/L2/ 创建（或更新）interfaces.md（使用 interfaces.L2.template.md）
   - 定义模块间 API/Event/Data 契约（providers/consumers）
   - 每个接口条目必须有 Source（REQ-L1/REQ-L2）
3. 在 docs/L2/ 创建 execution-tracker.md 追踪进度
```

**检查产出**：
- `docs/L2/{模块名}/requirements.md` - 包含 features, data_models
- `docs/L2/interfaces.md` - 模块间接口契约
- `docs/L2/execution-tracker.md` - 进度追踪表
- `docs/L2/{模块名}/split-report.md` - 拆分报告（覆盖矩阵、TBD）

### Step 5.5：架构设计（L2 → Architecture）

L2 完成后，先生成架构设计文档：
```
请运行 /architecture-generate：
/architecture-generate

这将生成：
- docs/architecture/overview.md (系统概览)
- docs/architecture/database-schema.md (数据库设计)
- docs/architecture/core-flows.md (RAG Pipeline)
- docs/architecture/api-spec.md (API 规范)
```

**检查产出**：
- `docs/architecture/*.md` - 架构设计文档
- 运行 `/architecture-validate` 验证追溯性

### Step 5.6：/spec 递归分解（Architecture → Spec Tree）

**前置条件**：`docs/architecture/*.md` 已生成

**重要规则**：每次只推进一个 L2 模块（或一个非 leaf Spec）！

对于每个 L2 模块，告诉 AI：
```
请运行 /spec：
/spec source_path=docs/L2/{模块名}/requirements.md target_dir=specs

要求：
1. 从该模块的 REQ-L2-* 分解出若干 SPEC（如 SPEC-001, SPEC-002...）
2. 对每个 Spec 判断是否 leaf（可直接写代码）
   - 是：标记 leaf=true，并补齐 Implementation Plan + Acceptance Tests + Interfaces Impact
   - 否：生成子 Spec（如 SPEC-001-A, SPEC-001-B...），并继续递归
3. 生成/更新 specs/spec-tree.md（包含树视图 + 覆盖矩阵）
```

**检查产出**：
- `specs/SPEC-*.md`（leaf Spec 可直接进入实现）
- `specs/spec-tree.md`（树视图 + 覆盖矩阵）

---

## 第六部分：Phase 3 - 实现 leaf Specs

### Step 6.1：实现 leaf Spec（Coder）

对于每个 `leaf: true` 且 `status: ready/done` 的 `specs/SPEC-*.md`，告诉 AI：
```
请按 coder-agent 角色，根据 specs/SPEC-xxx.md 实现代码。
遵循 .agent/config/quality.{language_profile}.yaml 中的规范。
代码放入 src/ 目录（或对应 component.path）。
```

**检查产出**：
- `src/{模块}/{文件}.{扩展名}` - 源代码
- 包含类型注解和文档字符串
- 代码复杂度 ≤ 10

### Step 6.2：实现测试并运行（Tester）

对于每个新生成的源代码，告诉 AI：
```
请按 tester-agent 角色：
1. 根据 leaf Spec 的 Acceptance Tests 实现测试代码
2. 测试代码放入 tests/ 目录
3. 运行测试并确保通过
4. 测试覆盖率 ≥ 95%
```

**检查产出**：
- `tests/{测试文件}.{扩展名}` - 测试代码
- 测试运行通过
- 覆盖率达标

### Step 6.3：Gate 检查

在 AI 对话框中输入：
```
/charter-quality
```

**Gate 检查项**：
- ✅ 所有测试通过
- ✅ 覆盖率 ≥ 95%
- ✅ Linting 通过
- ✅ 类型检查通过
- ✅ 安全扫描通过

**如果 Gate 失败**：
- 阅读错误信息
- 修复问题
- 重新运行 `/charter-quality`

### Step 6.6：更新进度

1. 运行 `/charter-status` 查看整体进度
2. 更新 `docs/L2/execution-tracker.md`，标记当前模块为完成
3. 选择下一个 L2 模块
4. 重复 Step 5.5 - Step 6.5

---

## 第七部分：集成与完成

### Step 7.1：Reviewer 代码审查

当一个 L2 模块的所有函数都通过 Gate 后，告诉 AI：
```
请按 reviewer-agent 角色审查 {模块名} 的代码。
检查：代码质量、安全漏洞、性能问题、最佳实践。
生成 review_report.md。
```

### Step 7.2：Integrator 集成测试

当所有 L2 模块都审查通过后，告诉 AI：
```
请按 integrator-agent 角色：
1. 集成所有模块
2. 执行集成测试
3. 生成 integration_report.md
```

**检查 Integration Report**：
```yaml
Implementation_Report:
  tests_passed: true
  coverage: "95%"
  deviations_from_spec: []    # 应该为空
  gate_check: PASS
```

### Step 7.3：最终验证

```
/charter-status
```

确认输出类似：
```
Charter: frozen ✅
Phase 1: L0 ✅ → L1 ✅ → L2 ✅ → SPEC ✅
Phase 2: Code ✅ → Tests ✅
```

---

## 附录 A：命令速查

| 命令 | 时机 | 说明 |
|------|------|------|
| `/charter-init` | 项目开始 | 创建目录结构 |
| `/charter-validate` | 编辑 charter 后 | 验证格式 |
| `/charter-freeze` | L1 分析前 | 锁定 charter |
| `/charter-unfreeze` | 需要改 charter 时 | 解锁 charter |
| `/charter-status` | 随时 | 查看进度 |
| `/charter-quality` | 每个模块完成后 | Gate 检查 |
| `/requirements-split` | 每次层级迁移前 | 生成 split-report.md（溯源覆盖矩阵） |
| `/requirements-render` | 生成 requirements.md 后 | 从 Registry 渲染正文+附录 |
| `/requirements-validate` | 生成 requirements.md 后 | 覆盖率/溯源/可验收检查 |
| `/architecture-generate` | L2 完成后 | 生成 docs/architecture/*.md (v0.6.3) |
| `/architecture-validate` | 架构生成后 | 验证架构追溯性 (v0.6.3) |
| `/architecture-render` | 架构更新后 | 渲染 OpenAPI/ADR (v0.6.3) |
| `/spec` | 架构完成后 | 生成 specs/SPEC-*.md + specs/spec-tree.md |

---

## 附录 B：产物状态流转

```
specs/SPEC-xxx.md
├── status: draft    (Spec Agent 创建中)
├── status: ready    (leaf=true 且 checklist 通过，可触发实现)
└── status: done     (实现与测试完成，Gate PASS)

design.md
├── status: draft    (Designer 创建中)
└── status: done     (可触发 Coder)
```

---

## 附录 C：目录结构示例

```
my-awesome-project/
├── .agent/
│   ├── rules/           # Agent 规则
│   ├── workflows/       # 工作流命令
│   ├── templates/       # 文档模板
│   ├── config/          # 语言配置
│   └── docs/            # 方法论文档
├── docs/
│   ├── L0/
│   │   ├── requirements.md
│   │   ├── split-report.md
│   │   └── subtasks.md
│   ├── L1/
│   │   ├── UserAuth/
│   │   │   ├── requirements.md
│   │   │   ├── split-report.md
│   │   │   └── subtasks.md
│   │   └── TaskManagement/
│   │       └── ...
│   ├── L2/
│   │   ├── execution-tracker.md
│   │   ├── interfaces.md
│   │   ├── Login/
│   │   │   ├── requirements.md
│   │   │   ├── split-report.md
│   │   │   └── subtasks.md
│   │   └── Register/
│   │       └── ...
├── specs/
│   ├── spec-tree.md
│   ├── SPEC-001.md
│   ├── SPEC-001-A.md
│   └── ...
├── src/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── login.py
│   │   └── register.py
│   └── tasks/
│       └── ...
├── tests/
│   ├── test_login.py
│   ├── test_register.py
│   └── ...
└── charter.yaml
```

---

## 附录 D：常见问题

### Q1: AI 没有按预期工作怎么办？

明确告诉 AI 使用哪个 Agent 角色：
```
请按 {agent-name} 角色执行...
```

### Q2: 忘记冻结 charter 就开始分解了？

1. 停止当前工作
2. 执行 `/charter-freeze`
3. 继续分解

### Q3: 需求变更怎么办？

1. `/charter-unfreeze`
2. 修改 charter.yaml
3. `/charter-validate`
4. `/charter-freeze`
5. 评估对已完成工作的影响
6. 必要时重新分解受影响的模块

### Q4: Gate 检查总是失败？

检查具体失败项：
- 测试失败 → 修复代码或测试
- 覆盖率不足 → 添加更多测试
- Linting 失败 → 按规范修正代码
- 类型检查失败 → 补充类型注解
