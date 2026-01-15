---
name: "test-generator"
description: "根据 design.md 和生成的代码自动生成测试用例。当用户说\"生成测试\"、\"写测试\"时自动触发。"
trigger_keywords:
  - "生成测试"
  - "写测试"
  - "测试用例"
  - "test"
---

# Test Generator Skill

根据设计文档和生成的代码自动生成测试。

## 触发条件

- `design.md` 存在且 `status=done`
- 代码文件已生成
- 或用户明确要求"生成测试"、"写测试"

## 前置检查

1. 检查 `design.md` 的 `Test Spec` 部分是否完整
2. 如果 Test Spec 为空，提示先完成 Test Spec
3. 检查测试目录结构

## 执行步骤

### 1. 读取测试规格
- 读取 `docs/L3/{function}/design.md` 的 Test Spec 部分
- 提取测试用例（正常/边界/异常/性能）

### 2. 读取代码
- 读取生成的源代码文件
- 理解函数签名和实现逻辑

### 3. 生成测试代码
根据测试规格生成测试文件：

#### 功能测试 (Functional)
- 输入正常数据
- 验证预期输出
- 覆盖主要功能路径

#### 边界测试 (Boundary)
- 边界值输入
- 空值/None 处理
- 极端值处理

#### 异常测试 (Exception)
- 无效输入处理
- 异常情况恢复
- 错误消息验证

#### 性能测试 (Performance)
- 执行时间测试
- 资源使用测试
- 基准测试（如果需要）

### 4. 运行测试
```bash
pytest tests/ -v --tb=short
```

### 5. 验证覆盖率
```bash
pytest --cov=src --cov-fail-under=95
```

## 测试类型要求

| 类型 | 最少数量 |
|------|----------|
| 功能测试 | 2 |
| 边界测试 | 4 |
| 异常测试 | 3 |
| 性能测试 | 1 |

## 输出产物

- `tests/**/*test.{{profile.test.extensions}}`
- 测试覆盖率报告

## 输出格式

```markdown
## 测试生成结果

**生成的测试文件**:
- tests/test_{module}.py

**测试用例统计**:
- 功能测试: N 个
- 边界测试: N 个
- 异常测试: N 个
- 性能测试: N 个

**测试执行结果**:
- 通过: N 个
- 失败: N 个
- 跳过: N 个

**覆盖率**: XX%

**下一步**:
- 运行 /charter-quality 门禁检查
- 或手动 Review 测试代码
```
