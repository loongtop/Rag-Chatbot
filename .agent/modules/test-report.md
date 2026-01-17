# Test Report Module

> 内部模块 - 由 tester-agent 调用，用户不可直接触发

## 职责

解析测试执行结果，生成结构化测试报告。

## 输入

- `test-results.xml`（JUnit XML）
- `coverage.xml`（Coverage XML）
- pytest 终端输出

## 输出

- `docs/testing/test_report_{timestamp}.md`

## 执行逻辑

1. **收集测试结果**
   
   ```bash
   # 结果文件位置
   apps/api/test-results.xml
   apps/api/coverage.xml
   ```

2. **解析数据**
   
   | 指标 | 来源 |
   |------|------|
   | 总测试数 | JUnit XML `tests` 属性 |
   | 通过数 | `tests - failures - errors` |
   | 失败数 | JUnit XML `failures` 属性 |
   | 覆盖率 | Coverage XML `line-rate` 属性 |

3. **生成报告**
   - 使用模板 `.agent/templates/test_report.template.md`
   - 填充执行摘要、覆盖率详情、失败用例

4. **判定质量门禁**
   
   | 指标 | 要求 | 判定 |
   |------|------|------|
   | 覆盖率 | ≥ 95% | PASS/FAIL |
   | 失败用例 | = 0 | PASS/FAIL |

## 模板

参见 `.agent/templates/test_report.template.md`
