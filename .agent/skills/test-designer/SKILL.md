---
name: "test-designer"
description: "从 Spec 提取验收标准，生成测试计划文档。当用户说\"设计测试\"、\"测试计划\"时自动触发。"
trigger_keywords:
  - "设计测试"
  - "测试计划"
  - "test plan"
  - "test design"
---

# Test Designer Skill

从 leaf Spec 提取 Acceptance Tests，生成结构化测试计划文档。

## 触发条件

1. leaf Spec 存在 (`specs/SPEC-*.md`, `leaf: true`)
2. Spec 包含 Acceptance Tests 部分
3. 或用户明确要求"设计测试"、"测试计划"

## 前置检查

### 1. Spec 检查
- 检查 `specs/SPEC-*.md` 是否存在
- 检查 Spec 是否有 Acceptance Tests 部分
- 若缺失，提示完善 Spec

### 2. 代码检查（可选）
- 若代码已存在，从代码推断额外测试需求
- 若代码不存在，仅基于 Spec 设计

## 执行步骤

### 1. 解析 Spec

从 Spec 提取：
- 功能描述（Summary）
- 验收测试（Acceptance Tests）
- 接口定义（Interfaces Impact）
- 依赖关系（depends_on）

### 2. 设计测试矩阵

为每个验收点设计：

| 类型 | 说明 | 最少数量 |
|------|------|----------|
| 功能测试 | 验证正常流程 | 2 |
| 边界测试 | 边界值/空值/极端值 | 4 |
| 异常测试 | 错误输入/异常恢复 | 3 |
| 性能测试 | 响应时间/并发 | 1 |

### 3. 生成测试计划

使用模板 `.agent/templates/test_plan.template.md` 生成：
- 测试范围
- 测试环境
- 测试矩阵
- 验收标准追溯
- 依赖和前置条件

## 输出产物

- 路径: `docs/testing/test_plan_{spec_id}.md`
- 格式: Markdown（符合模板）

## 输出格式

```markdown
## 测试设计结果

**输入 Spec**: SPEC-{id}
**验收点数量**: N 个
**测试用例设计**: M 个

**测试计划文件**:
- docs/testing/test_plan_SPEC-{id}.md

**测试矩阵**:
| 类型 | 数量 |
|------|------|
| 功能测试 | N |
| 边界测试 | N |
| 异常测试 | N |
| 性能测试 | N |

**下一步**:
- 运行 `/test-generate` 生成测试代码
```

## 注意事项

1. **不生成测试代码**，只设计测试计划
2. 每个验收点至少有一个对应测试用例
3. 边界测试必须覆盖空值、极限值
4. 异常测试必须覆盖所有错误码
