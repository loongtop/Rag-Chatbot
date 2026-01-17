---
description: 代码审查流程 - 自动运行 lint/typecheck/安全检查并生成报告
---

# Code Review Workflow

执行自动化代码审查，生成审查报告。

## 步骤

1. **运行 Linter (ruff)**
   // turbo
   ```bash
   cd apps/api && ruff check . --output-format=json > ruff_report.json 2>&1 || true
   ```

2. **运行类型检查 (mypy)**
   // turbo
   ```bash
   cd apps/api && mypy . --ignore-missing-imports --no-error-summary 2>&1 | head -50 || true
   ```

3. **运行安全检查 (bandit)**
   // turbo
   ```bash
   cd apps/api && bandit -r . -f json -o security_report.json 2>&1 || true
   ```

4. **生成审查报告**
   - 解析 ruff_report.json 获取代码风格问题
   - 解析 security_report.json 获取安全问题
   - 汇总 mypy 输出获取类型问题
   - 生成 `docs/reviews/{timestamp}-review.md`

5. **判定结果**
   - 无 Critical 问题 → PASS → 可进入测试
   - 存在 Critical 问题 → FAIL → 返回修复

## 输出

- `docs/reviews/{timestamp}-review.md` - 审查报告
- `ruff_report.json` - Linter 原始输出
- `security_report.json` - 安全检查原始输出

## 下一步

- PASS → 运行 `/test-all` 进入测试流程
- FAIL → 修复后重新运行 `/code-review`
