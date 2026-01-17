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
   - **[提醒]** 建议此时运行 `/review` 审查生成的测试代码
   - pytest → 运行测试
   - test-report → 生成报告

## 推荐门禁顺序

**需生成测试时（更稳定）**:
```
/test design      → 生成测试计划
/test generate    → 生成测试代码
/review           → 审查源代码 + 测试代码
/test run         → 运行测试
```

**仅运行已有测试（快速）**:
```
/review           → 审查源代码
/test run         → 运行测试
```
/test                    → 完整流程
/test design SPEC-002    → 为 SPEC-002 设计测试
/test run                → 运行现有测试
```
