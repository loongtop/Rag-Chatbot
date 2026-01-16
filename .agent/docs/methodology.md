# Development Methodology

三阶段开发方法论：从需求到架构到代码的自动化流程。

> 本文侧重“方法论/设计原则”；按步骤操作请阅读仓库根目录的 `GETTING_STARTED.md`。

---

## Three-Phase Model (v0.6.5)

```
Phase 1: Requirements (L0→L2)    Phase 1.5: Architecture    Phase 2: Specs    Phase 3: Code
───────────────────────────    ────────────────────────    ─────────────    ──────────────
Charter.yaml
    ↓ [Freeze]
L0 Requirements
    ↓
L1 Requirements
    ↓
L2 Requirements + interfaces.md
    ↓ /architecture-generate        ← Phase 1.5
docs/architecture/
    ├── overview.md
    ├── database-schema.md
    ├── core-flows.md
    └── api-spec.md
    ↓ /spec (recursive)             ← Phase 2
leaf Specs (SPEC-*)
    ↓ Coder                          ← Phase 3
src/*{{profile.source.extensions}}
    ↓ Tester
tests/*{{profile.test.extensions}}
    ↓ Integrator
integration
```

---

## Phase 0: Charter 定义与冻结

1. 使用 `charter.template.yaml` 与 LLM 多轮讨论
2. 产出 `{project}.charter.yaml`
3. 执行 `/charter-freeze` 锁定（防止需求漂移）

**冻结后规则**：
- 所有 Agent 只能**引用**，不得**修改** Charter
- 如需修改，必须先解冻

---

## Phase 1: Recursive Decomposition

将复杂需求分解为 **L2 模块需求**（需求文档层终点），并在 L2 产出模块间契约。

| Layer | Name | Outputs | Template | Granularity Support |
|-------|------|---------|----------|---------------------|
| L0 | Charter | requirements.md, subtasks.md | `requirements.L0.template.md` | - |
| L1 | Features | requirements.md, subtasks.md | `requirements.L1.template.md` | Optional |
| L2 | Modules | requirements.md, **interfaces.md**, **execution-tracker.md** | `requirements.L2.template.md` + `interfaces.L2.template.md` | Optional |

> 说明：Phase 1 的终点是 L2。实现粒度由 Phase 2 的 Spec 树（`SPEC-*`）承接。

### 自适应分解粒度（v0.6.5）

```yaml
granularity 参数:
  - auto:   自动评估复杂度选择路径（推荐）
  - full:   强制 L0→L1→L2
  - medium: L0→L2（跳过 L1）
  - light:  L0→L1（模块边界不明显时先停在 L1）
  - direct: L0→L2（单模块）
```

### 复杂度评估

```python
评估维度 = {
    "scope_items": len(charter.scope.must_have),
    "components": len(charter.components),
    "cross_deps": count_cross_module_dependencies(),
}

if scope_items > 20 OR components >= 3 OR cross_deps > 2:  # v0.6.5
    granularity = "full"
elif scope_items > 10 OR components > 1:
    granularity = "medium"
else:
    granularity = "light"
```

### 产物路径对比

```
# full (L0→L1→L2)
docs/
├── L0/requirements.md
├── L1/feature-a/requirements.md
└── L2/module-x/requirements.md
└── L2/interfaces.md
specs/
└── SPEC-001.md

# medium (L0→L2)
docs/
├── L0/requirements.md
└── L2/module-x/requirements.md
└── L2/interfaces.md
specs/
└── SPEC-001.md

# light (L0→L1)
docs/
├── L0/requirements.md
└── L1/feature-a/requirements.md
specs/
└── SPEC-001.md
```

> 必须：生成 requirements.md 后执行 `/requirements-render` + `/requirements-validate`

### Traceability Gate（可配置）

Traceability Gate 的行为由 `charter.yaml` 中的 `traceability.mode` 控制：

| mode | 行为 |
|------|------|
| `strict` | **必须**：生成下一层文档前必须先生成 `split-report.md` 且 Gate PASS |
| `assist` | **推荐**：建议使用，但 Gate FAIL 不阻塞（仅警告） |
| `off` | **跳过**：不执行溯源门禁 |

**默认行为**：使用 `strict` 模式以确保需求可追溯。

在每次层级迁移（Charter→L0、L0→L1、L1→L2）前，根据 `traceability.mode` 决定是否生成 `split-report.md`：
- 目的：验证"可拆分性"并形成**覆盖矩阵**（上游条目 → 下游 REQ/接口）
- 约束（strict 模式）：下游每条需求/接口必须带 `Source`，不得凭空新增
- 模板：`split-report.template.md`
- 工作流：`/requirements-split`

**示例**:
```
E-commerce Platform (L0)
├── User Management (L1)
│   ├── Authentication (L2)
│   │   ├── SPEC-001 (leaf=false)
│   │   │   ├── SPEC-001-A (leaf=true)
│   │   │   └── SPEC-001-B (leaf=true)
│   │   └── SPEC-002 (leaf=true)
│   └── Profile (L2)
└── Order Processing (L1)
```

**递归粒度规则**：
- 单个 Agent 实例**每次只推进一个 Feature/Module**
- 多人/多实例可并行处理不同模块（需独立 execution-tracker）
- L2 层的 execution-tracker 汇总 leaf Spec 完成状态
- L1 集成门禁统一验证所有模块

---

## Phase 1.5: Architecture (v0.6.5)

Phase 1.5 的目标是将 “L2 需求 + 接口契约” 变成 **可追溯、可验证、可落地的架构设计**，以避免从需求直接跳到实现的断层。

**输入**：
- `docs/L2/*/requirements.md`
- `docs/L2/interfaces.md`
- `charter.yaml`（技术边界与约束）

**输出**（建议固定在 `docs/architecture/`）：
- `overview.md`：组件边界、部署、信任边界、关键约束落地
- `database-schema.md`：数据模型、索引/约束、迁移策略
- `core-flows.md`：关键链路（如 RAG pipeline）、异常与降级
- `api-spec.md`：鉴权、错误码、端点与契约摘要

**溯源门禁（核心规则）**：
- 每个 `ARCH-*` 必须包含 `sources[]`，指向 `REQ-L2-*` 或 `IFC-*`
- 架构不得引入“无来源的新需求”；新增内容必须以 “设计决策/权衡” 形式表达，并绑定来源

**工作流**：
- 生成：`/architecture-generate`
- 验证：`/architecture-validate`
- 渲染（可选）：`/architecture-render`
- A/B 对比（可选）：`/architecture-compare`

---

## Phase 2: Specs (Recursive)

Phase 2 将 L2（以及架构）进一步分解为 **可直接实现的 leaf Spec**，并用 Spec 树把实现单元组织起来。

**输入**：
- L2 模块需求：`docs/L2/{module}/requirements.md`
- 架构设计：`docs/architecture/*.md`
- 或非 leaf Spec：`specs/SPEC-*.md`（继续递归）

**输出**：
- `specs/SPEC-*.md`：递归 Spec（含 leaf=true/false）
- `specs/spec-tree.md`：树视图 + 覆盖矩阵（REQ-L2-* → SPEC-*）

**leaf Spec 的定义（必须满足才可进入 Phase 3）**：
- 接口/输入输出/错误语义明确（或明确 N/A）
- 依赖与契约明确（引用 `docs/L2/interfaces.md`）
- 可验收：包含可执行的验收标准/测试点
- 可实现：范围可在一次小迭代/PR 内完成
- 无阻塞性 TBD（impact=H），或给出明确 fallback

**工作流**：
- `/spec`（从 L2 或非 leaf Spec 递归分解）

---

## Phase 3: Code Implementation

从 leaf Spec 到代码与测试的实现流程。

```
leaf Spec (`specs/SPEC-*.md`, leaf=true)
    ↓ (optional) Designer
design.md (可选)
    ↓ Coder
src/*{{profile.source.extensions}}
    ↓ Tester
tests/*{{profile.test.extensions}}
    ↓ Reviewer
review_report.md
    ↓ Integrator
integration_report.md (YAML 结构化)
```

---

## Legacy: TDD 模式（L3）

如需 Function-level 的 TDD，可使用 legacy 的 L3 模板与流程；推荐优先使用 leaf Spec 替代。

详情见：`.agent/docs/legacy/L3-tdd.md`（含模板与触发规则）。

---

## Artifact-Driven Communication

Agent 之间不直接调用，通过**产物状态**驱动：

```yaml
# 产物头部元数据
---
status: draft | ready | in_progress | done
owner: architect | designer | coder | tester | reviewer | integrator
layer: L0 | L1 | L2 | SPEC | L3(legacy)
parent: {parent_path}
---
```

**触发规则**:
| 产物 | 状态 | 触发 |
|------|------|------|
| specs/SPEC-*.md (leaf=true) | ready | Coder（或 Designer 可选） |
| design.md (可选) | done | Coder → src/*{{profile.source.extensions}} |
| src/*{{profile.source.extensions}} | exists | Tester → tests/*{{profile.test.extensions}} |
| tests/*{{profile.test.extensions}} | passed | Reviewer → review_report.md |
| review_report.md | approved | Integrator |

---

## Gate 检查

每个模块完成后自动进行 Gate 检查：

```yaml
Gate_Check:
  tests_passed: true
  coverage: ">= 95%"
  deviations_from_spec: []  # 必须为空
```

- ✅ **PASS**: 所有条件满足 → 更新 execution-tracker
- ❌ **FAIL**: 任一不满足 → 回退到对应 Agent

---

## Execution Loop

```python
while not project_complete:
    1. Select next Feature/Module from execution-tracker
    2. Execute /spec until leaf
    3. Implement leaf Specs
    4. Run Gate Check
    5. Update execution-tracker
    6. If FAIL, rollback; else continue
```

---

## Integration Strategy

自底向上集成：

```
leaf Specs → L2 Module Tests
L2 Modules   → L1 Feature Tests
L1 Features  → L0 System Tests
```
