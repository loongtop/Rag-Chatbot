---
status: draft
owner: architect
layer: L2
project: {project_name}
---

# Execution Tracker: {project_name}

## 项目进度概览

| 指标 | 数值 |
|------|------|
| L2 模块总数 | 0 |
| 已完成 | 0 |
| 进行中 | 0 |
| 未开始 | 0 |
| 完成率 | 0% |

---

## L1 Feature 进度

| L1 Feature | L2 模块数 | 完成率 | 状态 |
|------------|----------|--------|------|
| Feature 1 | 3 | 0% | ⬜ |
| Feature 2 | 2 | 0% | ⬜ |

---

## L2 模块详细追踪

### Feature 1: {feature_name}

| L2 Module | L3 函数数 | Designer | Coder | Tester | Reviewer | Gate |
|-----------|----------|----------|-------|--------|----------|------|
| Module 1.1 | 3 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| Module 1.2 | 2 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

### Feature 2: {feature_name}

| L2 Module | L3 函数数 | Designer | Coder | Tester | Reviewer | Gate |
|-----------|----------|----------|-------|--------|----------|------|
| Module 2.1 | 4 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

---

## 当前迭代焦点

> **规则**: 每次只推进一个 L2 Module，不允许跨模块并行

**当前正在处理**: `{module_name}`

**下一个待处理**: `{next_module_name}`

---

## Gate 检查记录

| 日期 | 模块 | Gate 结果 | 问题描述 | 处理方式 |
|------|------|-----------|----------|----------|
| YYYY-MM-DD | Module X | ✅ PASS | - | - |
| YYYY-MM-DD | Module Y | ❌ FAIL | 测试覆盖不足 | 回退到 Tester |

---

## Implementation Report 汇总

```yaml
# 最新生成的 Implementation Report
latest_report:
  module: ""
  date: ""
  implemented_functions: []
  tests_passed: false
  coverage: "0%"
  deviations_from_spec: []
  known_issues: []
  gate_check: PENDING
```

---

## 状态图例

| 符号 | 含义 |
|------|------|
| ⬜ | 未开始 |
| 🟡 | 进行中 |
| ✅ | 已完成 |
| ❌ | 失败/阻塞 |
| 🔄 | 需重做 |
