---
description: 代码审查流程 - 激活 reviewer-agent 执行审查
---

# /review Workflow

**映射**: reviewer-agent (mode=full)

## 说明

此命令激活 `reviewer-agent` 执行代码审查。

## 执行流程

1. 激活 reviewer-agent
2. 调用 code-quality 模块
   // turbo
   ```bash
   cd apps/api && ruff check . --output-format=json > ruff_report.json 2>&1 || true
   ```
   // turbo
   ```bash
   cd apps/api && mypy . --ignore-missing-imports 2>&1 | head -50 || true
   ```
   // turbo
   ```bash
   cd apps/api && bandit -r . -f json -o security_report.json 2>&1 || true
   ```
3. 汇总检查结果
4. 生成审查报告到 `docs/reviews/`
5. 判定 PASS/FAIL

## 快捷模式

| 命令 | 模式 | 说明 |
|------|------|------|
| `/review` | full | 完整检查 |
| `/review lint` | lint-only | 仅 lint |
| `/review security` | security-only | 仅安全检查 |

## 示例

```
/review           → 完整代码审查
/review lint      → 仅检查代码风格
/review security  → 仅安全扫描
```
