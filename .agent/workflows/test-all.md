---
description: 一键测试流程 - 测试设计、生成、运行、报告
---

# Test All Workflow

一键执行完整测试流程：设计 → 生成 → 运行 → 报告。

## 前置条件

- 代码已完成（`apps/api/` 有可测试代码）
- `/code-review` 已通过（可选但推荐）

## 步骤

1. **测试设计**
   使用 `test-designer` skill 生成测试计划。
   - 输入: `specs/SPEC-*.md`
   - 输出: `docs/testing/test_plan_{spec_id}.md`

2. **测试生成**
   使用 `test-generator` skill 生成测试代码。
   - 输入: 测试计划 + 源代码
   - 输出: `apps/api/tests/**/*.py`

3. **运行测试**
   // turbo
   ```bash
   cd apps/api && pytest tests/ -v --tb=short --cov=. --cov-report=xml --cov-report=term-missing --junitxml=test-results.xml --cov-fail-under=95 2>&1 | head -100
   ```

4. **生成报告**
   使用 `test-reporter` skill 生成测试报告。
   - 输入: `test-results.xml`, `coverage.xml`
   - 输出: `docs/testing/test_report_{timestamp}.md`

5. **更新追踪**
   更新 `docs/L2/execution-tracker.md` 中的测试状态。

## 快速模式

如果只想运行测试而跳过设计/生成步骤：

// turbo
```bash
cd apps/api && pytest tests/ -v --tb=short --cov=. --cov-report=term-missing --cov-fail-under=95
```

## 输出

| 产物 | 路径 |
|------|------|
| 测试计划 | `docs/testing/test_plan_*.md` |
| 测试代码 | `apps/api/tests/**/*.py` |
| JUnit XML | `apps/api/test-results.xml` |
| Coverage XML | `apps/api/coverage.xml` |
| 测试报告 | `docs/testing/test_report_*.md` |

## 质量门禁

| 指标 | 要求 |
|------|------|
| 覆盖率 | ≥ 95% |
| 失败用例 | = 0 |

## 下一步

- PASS → 可以合并/发布
- FAIL → 查看报告，修复后重新运行
