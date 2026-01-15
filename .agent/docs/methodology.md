# Development Methodology

两阶段开发方法论：从需求到代码的自动化流程。

---

## Two-Phase Model

```
Phase 1: Decomposition          Phase 2: Implementation
────────────────────────        ────────────────────────
Charter (L0)                    design.md
    ↓ [Freeze]                      ↓
Features (L1)                   src/*{{profile.source.extensions}}
    ↓                               ↓
Modules (L2)                    tests/*{{profile.test.extensions}}
    ↓                               ↓
Functions (L3)                  integration
    ↓
Test Spec (TDD)
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

将复杂需求逐层分解为可实现的函数规格。

| Layer | Name | Outputs | Template | Granularity Support |
|-------|------|---------|----------|---------------------|
| L0 | Charter | requirements.md, subtasks.md | `requirements.L0.template.md` | - |
| L1 | Features | requirements.md, interfaces.md, subtasks.md | `requirements.L1.template.md` | Optional |
| L2 | Modules | requirements.md, interfaces.md, **execution-tracker.md** | `requirements.L2.template.md` | Optional |
| L3 | Functions | requirements.md (含 Function Spec + Test Spec) | `requirements.L3.template.md` | Required |

> **v0.5.0 特性**：L1/L2 层可根据复杂度跳过，使用 `granularity=medium/light/direct` 参数。

### 自适应分解粒度（v0.5.0 新增）

```yaml
granularity 参数:
  - auto:   自动评估复杂度选择路径（推荐）
  - full:   强制 L0→L1→L2→L3
  - medium: L0→L2→L3（跳过 L1）
  - light:  L0→L3（跳过 L1/L2）
  - direct: L0→代码（仅配置/胶水代码）
```

### 复杂度评估

```python
评估维度 = {
    "scope_items": len(charter.scope.must_have),
    "components": len(charter.components),
    "cross_deps": count_cross_module_dependencies(),
}

if scope_items > 20 OR components > 3 OR cross_deps > 2:
    granularity = "full"
elif scope_items > 10 OR components > 1:
    granularity = "medium"
else:
    granularity = "light"
```

### 产物路径对比

```
# full (L0→L1→L2→L3)
docs/
├── L0/requirements.md
├── L1/feature-a/requirements.md
├── L2/feature-a/module-x/requirements.md
└── L3/feature-a/module-x/func-y/requirements.md

# medium (L0→L2→L3)
docs/
├── L0/requirements.md
└── L2/feature-a/module-x/requirements.md
    └── L3/ (嵌套)

# light (L0→L3)
docs/
├── L0/requirements.md
└── L3/feature-a/func-x/requirements.md
```

> **v0.5.0 必须**: 生成 requirements.md 后执行 `/requirements-render` + `/requirements-validate`

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
│   │   ├── validate_credentials() (L3)
│   │   ├── create_session() (L3)
│   │   └── logout_user() (L3)
│   └── Profile (L2)
└── Order Processing (L1)
```

**递归粒度规则**：
- 单个 Agent 实例**每次只推进一个 Feature/Module**
- 多人/多实例可并行处理不同模块（需独立 execution-tracker）
- L2 层的 execution-tracker 汇总所有 L3 完成状态
- L1 集成门禁统一验证所有模块

---

## Phase 2: Automatic Implementation

从设计到代码的自动生成流程。

```
L3 requirements.md (含 Function Spec + Test Spec)
    ↓ Designer
design.md
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

## TDD 模式

L3 阶段采用**测试先行**策略：

1. **Architect**: 定义 Function Spec（签名、职责、前置/后置条件）
2. **Tester Phase 1**: 编写 Test Spec（测试用例表格，不含实现）
3. **Designer**: 整合为 design.md
4. **Coder**: 实现代码（不改接口）
5. **Tester Phase 2**: 实现测试代码 + 执行

---

## Artifact-Driven Communication

Agent 之间不直接调用，通过**产物状态**驱动：

```yaml
# 产物头部元数据
---
status: draft | ready | in_progress | done
owner: architect | designer | coder | tester | reviewer | integrator
layer: L0 | L1 | L2 | L3
parent: {parent_path}
---
```

**触发规则**:
| 产物 | 状态 | 触发 |
|------|------|------|
| requirements.md (L3) + Test Spec | done | Designer → design.md |
| design.md | done | Coder → src/*{{profile.source.extensions}} |
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
    2. Execute Phase 1 (L3 decomposition)
    3. Execute Phase 2 (Implementation)
    4. Run Gate Check
    5. Update execution-tracker
    6. If FAIL, rollback; else continue
```

---

## Integration Strategy

自底向上集成：

```
L3 Functions → L2 Module Tests
L2 Modules   → L1 Feature Tests
L1 Features  → L0 System Tests
```
