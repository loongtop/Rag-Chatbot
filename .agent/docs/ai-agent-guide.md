# AI Agent Integration Guide

本指南帮助 AI Agent 正确使用 Charter Agent Framework。

---

## 核心原则

### 1. 冻结优先（Freeze-First）

在开始 L1 分析前，**必须先冻结 Charter**：

```
/charter-freeze
```

冻结后，所有 Agent 只能**引用**，不得**修改** Charter。

### 2. 单模块推进（Single Module）

单个 Agent 实例**每次只处理一个 Feature/Module**。

**多人协作时可并行**：不同成员可同时处理不同模块，每个模块需独立维护 `execution-tracker.md`，L1 集成门禁统一验证。

---

## 溯源门禁（Traceability-First）

根据 `charter.yaml` 的 `traceability.mode` 配置决定行为：

| mode | split-report | Source 要求 | 阻塞 |
|------|--------------|-------------|------|
| `strict` | 必须 | 必填 | 阻塞 |
| `assist` | 推荐 | 建议 | 不阻塞 |
| `off` | 跳过 | 无要求 | 不阻塞 |

生成下一层 `requirements.md` / `interfaces.md` 前：
- 产出同目录 `split-report.md`
- 生成覆盖矩阵：上游条目 → 下游 REQ/接口（或 N/A + 原因）
- 工作流：`/requirements-split`

v0.6.5 约定：
- L1 不产出模块间接口契约
- 模块间契约统一在 `docs/L2/interfaces.md` 定义，并同样纳入覆盖矩阵与 Source 要求

---

## Agent 触发条件

| Agent | 触发条件 | 产出 |
|-------|---------|------|
| Requirements Split | before writing requirements/interfaces | split-report.md |
| Architect | charter.yaml + `freeze.frozen=true` | requirements.md, subtasks.md |
| **Architecture Generator** | L2 requirements + interfaces.md done | docs/architecture/*.md (v0.6.5) |
| Spec | Architecture done + L2 requirements | specs/*.md, specs/spec-tree.md |
| Designer | leaf Spec ready（可选） | design.md |
| Coder | leaf Spec ready（或 design.md done） | src/**/* |
| Tester (P2) | src/**/* 存在 | tests/**/* (实现+执行) |
| Reviewer | tests passed | review_report.md |
| Integrator | 所有模块完成 | integration_report.md |

> L3（Function Spec / TDD）为 legacy 路径；如需使用见 `.agent/docs/legacy/L3-tdd.md`。

---

## Phase 1.5: Architecture (v0.6.5)

当 L2 完成后，先使用 `/architecture-generate` 生成架构设计文档：

- 输入：`docs/L2/*/requirements.md` + `docs/L2/interfaces.md`
- 输出：`docs/architecture/*.md` (overview, database-schema, core-flows, api-spec)
- 验证：`/architecture-validate` 检查追溯性
- 门禁：所有 ARCH-* 必须有 sources[] 指向 REQ-* 或 IFC-*
- 版本改进验证（可选）：使用 `/architecture-compare`，通过 `target_dir` 生成候选输出，避免重命名 `docs/`

---

## /spec（从需求到实现规格）

**前置条件** (v0.6.5)：
1. L2 requirements 已完成 (`docs/L2/{module}/requirements.md`)
2. L2 interfaces 已定义 (`docs/L2/interfaces.md`)
3. **Architecture 已完成** (`docs/architecture/*.md`)

使用 `/spec` 将 L2 requirements 递归分解为 Spec 树，直到 leaf Spec 可直接写代码：

- 输入：`docs/L2/{module}/requirements.md`（必要时结合 `docs/L2/interfaces.md`）
- 输出：`specs/SPEC-*.md` + `specs/spec-tree.md`
- leaf 判定：必须满足输入/输出/依赖/验收清晰等条件（见 `/spec` 工作流）

---

## 模板选择

| Layer | Template |
|-------|----------|
| Any | `split-report.template.md` |
| L0 | `requirements.L0.template.md` |
| L1 | `requirements.L1.template.md` |
| L2 | `requirements.L2.template.md` + `interfaces.L2.template.md` + `execution-tracker.template.md` |
| Architecture | `architecture.*.template.md` (v0.6.5) |
| SPEC | `spec.template.md` + `spec-tree.template.md` |

> 所有 requirements 模板使用 Registry 块作为唯一事实源。生成后执行 `/requirements-render` + `/requirements-validate`。

---

## Gate 检查

每个模块完成后自动检查：

```yaml
Gate_Check:
  tests_passed: true
  coverage: ">= 95%"
  deviations_from_spec: []
```

---

## 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| 跳过 Freeze | 需求漂移 | 始终先 `/charter-freeze` |
| 错误模板 | 层级不匹配 | 检查 layer 字段 |
| 跨模块并行 | AI 发散 | 用 execution-tracker 追踪 |
| 改冻结 Charter | 违规 | 先 `/charter-unfreeze` |
| 无来源新增需求 | 需求漂移 | 先写 split-report 覆盖矩阵，并为每条需求/接口填写 Source |
