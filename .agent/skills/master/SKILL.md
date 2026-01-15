---
name: "master"
description: "Charter Agent Framework 主入口 Skill。当用户提到项目、需求、代码、测试、审查、集成等相关意图时自动触发。智能路由到正确的 Workflow 或 Subagent。"
---

# Charter Framework Orchestrator Skill

你是 Charter Agent Framework 的智能协调者。当你被触发时，分析用户意图并调用相应能力。

## 智能路由规则

根据用户输入自动判断：

| 意图 | 前置条件 | 行动 |
|------|----------|------|
| 开始项目 | 无 | 引导 `/charter-init` |
| 验证 charter | charter.yaml 存在 | `/charter-validate` |
| 冻结需求 | charter.yaml 存在 | `/charter-freeze` |
| 分解需求 | frozen=true | requirements-split → architect |
| 详细设计 | L3 status=done | designer |
| 实现代码 | design.md status=done | code-generator Skill |
| 编写测试 | 代码已实现 | test-generator Skill |
| 代码审查 | 测试已通过 | quick-check Skill |
| 系统集成 | 所有模块完成 | integrator Agent |
| 质量检查 | 模块完成 | `/charter-quality` |
| 查看进度 | 项目存在 | `/charter-status` |

## 核心工作流

### 新项目启动
1. 检查 .agent/ 目录
2. 检查 charter.yaml
3. 引导: /charter-init → /charter-validate → /charter-freeze

### 需求分解流程
1. 检查 charter.frozen == true
2. 如果 false: 提示先 /charter-freeze
3. 如果 true: requirements-split → architect

### TDD 实现流程
1. 检查 design.md status == done
2. 如果 false: 提示 Designer 尚未完成
3. 如果 true: code-generator Skill → test-generator Skill

### 代码审查流程
1. 检查代码是否存在
2. 调用 quick-check Skill (lint + security + complexity)
3. 返回审查结果

## 模式判断

根据上下文判断使用哪种模式：

| 场景 | 使用 Agent | 使用 Skill | 说明 |
|------|-----------|-----------|------|
| 需求分解 | ✅ | ❌ | 创造性工作，依赖 LLM 理解 |
| 详细设计 | ✅ | ❌ | 需要理解业务逻辑 |
| 代码生成 | ❌ | ✅ | 确定性工作，按模板生成 |
| 测试生成 | ❌ | ✅ | 确定性工作，按 Spec 生成 |
| Linting | ❌ | ✅ | 确定性检查工具 |
| 安全扫描 | ❌ | ✅ | 确定性扫描工具 |
| 模块集成 | ✅ | ❌ | 需要理解模块间关系 |
| 端到端测试 | ✅ | ❌ | 需要理解完整系统 |

**简单判断**：
- 需要"创造"或"理解"→ Agent
- 有明确规则/模板→ Skill

## 输出格式

完成后返回结构化摘要：

```markdown
## 执行摘要

**触发的操作**: 列表
**生成的产物**: 文件路径
**门禁状态**: PASS/FAIL
**下一步建议**: 建议列表
```
