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

### 2. 单模块推进

每次只处理**一个 Feature/Module**，不允许跨模块并行。

---

## Agent 触发条件

| Agent | 触发条件 | 产出 |
|-------|---------|------|
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
| L0 | `requirements.template.md` |
| L1 | `requirements.L1.template.md` |
| L2 | `requirements.L2.template.md` + `execution-tracker.template.md` |
| L3 | `requirements.L3.template.md` |

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
