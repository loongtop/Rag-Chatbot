---
name: "test-reporter"
description: "解析测试结果，生成结构化测试报告。当用户说\"测试报告\"、\"生成报告\"时自动触发。"
trigger_keywords:
  - "测试报告"
  - "生成报告"
  - "test report"
---

# Test Reporter Skill

解析测试执行结果，生成结构化测试报告。

## 触发条件

1. 测试已执行（存在 `pytest` 输出或结果文件）
2. 或用户明确要求"测试报告"

## 前置检查

### 1. 测试结果检查
检查以下文件是否存在：
- `test-results.xml`（JUnit XML）
- `coverage.xml`（Coverage XML）
- `pytest` 终端输出

### 2. 若无结果
提示先运行 `/test-run` 或 `pytest`

## 执行步骤

### 1. 收集测试结果

从以下来源收集：

```bash
# JUnit XML (测试通过/失败)
apps/api/test-results.xml

# Coverage XML (覆盖率)
apps/api/coverage.xml

# 安全检查 (如有)
apps/api/security_report.json
```

### 2. 解析数据

提取关键指标：

| 指标 | 来源 |
|------|------|
| 总测试数 | JUnit XML `tests` 属性 |
| 通过数 | JUnit XML `tests - failures - errors` |
| 失败数 | JUnit XML `failures` 属性 |
| 跳过数 | JUnit XML `skipped` 属性 |
| 覆盖率 | Coverage XML `line-rate` 属性 |
| 耗时 | JUnit XML `time` 属性 |

### 3. 生成报告

使用模板 `.agent/templates/test_report.template.md` 生成：

- 执行摘要
- 覆盖率统计（行/分支/函数）
- 通过/失败/跳过统计
- 失败用例详情（如有）
- 质量门禁判定
- 建议和下一步

### 4. 更新追踪

更新 `docs/L2/execution-tracker.md`:
- 测试状态
- 覆盖率
- 最后测试时间

## 输出产物

- 路径: `docs/testing/test_report_{timestamp}.md`
- 格式: Markdown（符合模板）

## 输出格式

```markdown
## 测试报告生成结果

**执行时间**: YYYY-MM-DD HH:MM:SS
**总耗时**: N.N 秒

**测试结果**:
- 通过: N ✅
- 失败: N ❌
- 跳过: N ⏭️

**覆盖率**: XX.X%

**质量门禁**: PASS/FAIL

**报告文件**:
- docs/testing/test_report_{timestamp}.md

**下一步**:
- PASS → 可以合并/发布
- FAIL → 查看失败详情并修复
```

## 质量门禁标准

| 指标 | 要求 | 结果 |
|------|------|------|
| 覆盖率 | ≥ 95% | PASS/FAIL |
| 失败用例 | = 0 | PASS/FAIL |
| 关键路径覆盖 | 100% | PASS/FAIL |

## 注意事项

1. **不修改测试代码**，只生成报告
2. 失败用例必须包含完整堆栈信息
3. 覆盖率低于门槛时提供缺失文件列表
4. 报告应包含可操作建议
