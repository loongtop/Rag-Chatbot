---
description: 测试流程 - 激活 tester-agent 执行测试
---

# /test Workflow

**映射**: tester-agent (mode=full)

## 说明

此命令激活 `tester-agent` 执行完整测试流程。

## 执行流程

1. 激活 tester-agent
2. 识别执行模式（默认 full）
3. 依次调用内部模块：
   - test-design → 生成测试计划
   - test-generate → 生成测试代码
   - pytest → 运行测试
   - test-report → 生成报告

## 快捷模式

| 命令 | 模式 | 说明 |
|------|------|------|
| `/test` | full | 完整流程 |
| `/test design` | design | 仅生成测试计划 |
| `/test generate` | generate | 仅生成测试代码 |
| `/test run` | run | 仅运行测试 |
| `/test report` | report | 仅生成报告 |

## 示例

```
/test                    → 完整流程
/test design SPEC-002    → 为 SPEC-002 设计测试
/test run                → 运行现有测试
```
