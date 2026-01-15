---
name: "quick-check"
description: "代码质量快速检查工具。当用户说\"检查代码\"、\"运行测试\"、\"质量检查\"时自动触发。自动执行 lint、类型检查、覆盖率验证。"
trigger_keywords:
  - "检查代码"
  - "质量检查"
  - "运行测试"
  - "check"
  - "quality"
---

# Quick Check Skill

代码质量快速检查工具集。

## 触发条件

- 用户说"检查代码"、"质量检查"、"运行测试"
- 或作为其他工作流的一部分自动调用

## 检查类型

| 触发词 | 检查内容 | 命令 |
|--------|----------|------|
| 检查代码 | 复杂度、规范 | `ruff check` / `eslint` |
| 运行测试 | 测试通过 | `pytest` / `npm test` |
| 覆盖率 | 测试覆盖 | `pytest --cov` |
| 检查类型 | 类型注解 | `mypy` / `tsc --noEmit` |
| 安全扫描 | 漏洞检查 | `bandit` / `npm audit` |
| 完整检查 | 所有项目 | 运行完整质量门禁 |

## 执行步骤

### 1. 确定语言配置
- 读取 `charter.yaml` 的 `language_profile`
- 加载对应配置 `.agent/config/quality.{language}.yaml`

### 2. 运行 Linting
```bash
{{profile.commands.lint}}
```
要求：无错误

### 3. 运行类型检查
```bash
{{profile.commands.typecheck}}
```
要求：无错误（或 N/A）

### 4. 运行测试
```bash
{{profile.commands.test}}
```
要求：全部通过

### 5. 检查覆盖率
```bash
pytest --cov=src --cov-fail-under=95
```
要求：≥ 95%

### 6. 运行安全扫描
```bash
{{profile.commands.security}}
```
要求：无高危漏洞

## 输出格式

```markdown
## 质量检查结果

**检查项目** | **状态** | **说明**
-------------|----------|----------
Linting | ✅/❌ | 结果
类型检查 | ✅/❌ | 结果
测试通过 | ✅/❌ | N passed / N failed
测试覆盖率 | ✅/❌ | XX%
安全扫描 | ✅/❌ | 结果

**整体状态**: PASS / FAIL

**问题列表** (如果有):
1. 问题描述
   - 文件: 路径
   - 建议修复: 方案
```

## 作为 Workflow 调用

可被 `/charter-quality` 调用：

```markdown
/charter-quality
  → quick-check Skill
  → 返回检查结果
  → 生成报告
```
