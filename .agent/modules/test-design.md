# Test Design Module

> 内部模块 - 由 tester-agent 调用，用户不可直接触发

## 职责

从 leaf Spec 提取验收标准，生成测试计划文档。

## 输入

- `specs/SPEC-*.md`（leaf=true）的 Acceptance Tests 部分
- 或 `design.md` 的 Test Spec 部分

## 输出

- `docs/testing/test_plan_{spec_id}.md`

## 执行逻辑

1. **解析 Spec**
   - 提取功能描述（Summary）
   - 提取验收测试（Acceptance Tests）
   - 提取接口定义（Interfaces Impact）

2. **设计测试矩阵**
   
   | 类型 | 说明 | 最少数量 |
   |------|------|----------|
   | 功能测试 | 验证正常流程 | 2 |
   | 边界测试 | 边界值/空值/极端值 | 4 |
   | 异常测试 | 错误输入/异常恢复 | 3 |
   | 性能测试 | 响应时间/并发 | 1 |

3. **生成测试计划**
   - 使用模板 `.agent/templates/test_plan.template.md`
   - 填充测试矩阵和追溯表

## 模板

参见 `.agent/templates/test_plan.template.md`
