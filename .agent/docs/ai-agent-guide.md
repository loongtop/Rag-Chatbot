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

---

## Agent 触发条件

| Agent | 触发条件 | 产出 |
|-------|---------|------|
| Requirements Split | before writing requirements/interfaces | split-report.md |
| Architect | charter.yaml + `freeze.frozen=true` | requirements.md, subtasks.md |
| Tester (P1) | L3 requirements.md `status=ready` | Test Spec (补充) |
| Designer | L3 requirements.md `status=done` | design.md |
| Coder | design.md `status=done` | src/**/* |
| Tester (P2) | src/**/* 存在 | tests/**/* (实现+执行) |
| Reviewer | tests passed | review_report.md |
| Integrator | 所有模块完成 | integration_report.md |

---

## TDD 模式

L3 阶段必须采用测试先行：

1. **Architect**: 填写 Function Spec → `status: ready`
2. **Tester (P1)**: 填写 Test Spec → `status: done`
3. **Designer**: 整合为 design.md
4. **Coder**: 实现代码
5. **Tester (P2)**: 实现测试 + 执行

---

## 模板选择

| Layer | Template |
|-------|----------|
| Any | `split-report.template.md` |
| L0 | `requirements.L0.template.md` |
| L1 | `requirements.L1.template.md` |
| L2 | `requirements.L2.template.md` + `execution-tracker.template.md` |
| L3 | `requirements.L3.template.md` |

> **v0.5.0 必须**: 所有模板使用 Registry 块作为唯一事实源。生成后执行 `/requirements-render` + `/requirements-validate`。

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
