# Test Report: {PROJECT_NAME}

> 生成时间: {TIMESTAMP}
> 执行环境: {ENVIRONMENT}

---

## 1. 执行摘要

| 指标 | 结果 |
|------|------|
| **总测试数** | {TOTAL_TESTS} |
| **通过** | {PASSED} ✅ |
| **失败** | {FAILED} ❌ |
| **跳过** | {SKIPPED} ⏭️ |
| **覆盖率** | {COVERAGE}% |
| **耗时** | {DURATION}s |

### 质量门禁

| 门禁 | 要求 | 结果 | 状态 |
|------|------|------|------|
| 覆盖率 | ≥ 95% | {COVERAGE}% | {COVERAGE_STATUS} |
| 失败用例 | = 0 | {FAILED} | {FAILED_STATUS} |
| 关键路径 | 100% | {CRITICAL_COVERAGE}% | {CRITICAL_STATUS} |

**整体判定**: {OVERALL_STATUS}

---

## 2. 覆盖率详情

### 2.1 模块覆盖

| 模块 | 行覆盖 | 分支覆盖 | 缺失行 |
|------|--------|----------|--------|
| {MODULE_1} | {LINE_COV}% | {BRANCH_COV}% | {MISSING} |
| {MODULE_2} | {LINE_COV}% | {BRANCH_COV}% | {MISSING} |

### 2.2 低覆盖文件

> [!WARNING]
> 以下文件覆盖率低于 80%，需要补充测试：

| 文件 | 覆盖率 | 缺失行数 |
|------|--------|----------|
| {FILE_1} | {COV}% | {LINES} |

---

## 3. 测试结果详情

### 3.1 按类型统计

| 类型 | 通过 | 失败 | 跳过 |
|------|------|------|------|
| 功能测试 | {N} | {N} | {N} |
| 边界测试 | {N} | {N} | {N} |
| 异常测试 | {N} | {N} | {N} |
| 性能测试 | {N} | {N} | {N} |

### 3.2 失败用例详情

> [!CAUTION]
> 以下测试用例失败，需要修复：

#### ❌ {TEST_NAME_1}

- **文件**: `{TEST_FILE}`
- **错误类型**: `{ERROR_TYPE}`
- **错误信息**: 
  ```
  {ERROR_MESSAGE}
  ```
- **堆栈**:
  ```
  {STACK_TRACE}
  ```
- **建议修复**: {FIX_SUGGESTION}

---

## 4. 性能指标

| 指标 | 值 | 阈值 | 状态 |
|------|-----|------|------|
| 平均耗时 | {AVG}ms | < 100ms | {STATUS} |
| P95 耗时 | {P95}ms | < 500ms | {STATUS} |
| 最慢用例 | {SLOWEST}ms | - | - |

---

## 5. 建议和下一步

### 5.1 待修复

- [ ] 修复失败用例: {FAILED_TESTS}
- [ ] 补充低覆盖模块测试: {LOW_COV_MODULES}

### 5.2 改进建议

1. {SUGGESTION_1}
2. {SUGGESTION_2}

### 5.3 下一步

- {OVERALL_STATUS == "PASS"} → 可以合并/发布
- {OVERALL_STATUS == "FAIL"} → 修复后重新运行 `/test-all`

---

## 6. 附录

### 6.1 测试命令

```bash
pytest apps/api/tests/ -m "not performance" --cov=apps/api --cov-report=xml:apps/api/coverage.xml --junitxml=apps/api/test-results.xml
```

### 6.2 结果文件

- JUnit XML: `apps/api/test-results.xml`
- Coverage XML: `apps/api/coverage.xml`
- 本报告: `docs/testing/test_report_{TIMESTAMP}.md`
