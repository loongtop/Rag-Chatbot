# Code Quality Module

> 内部模块 - 由 reviewer-agent 调用，用户不可直接触发

## 职责

执行自动化代码质量检查（lint、typecheck、安全扫描）。

## 输入

- 源代码目录（如 `apps/api/`）
- 语言配置（`.agent/config/quality.{lang}.yaml`）

## 输出

- `docs/reviews/{timestamp}-review.md`
- `ruff_report.json`（原始 lint 结果）
- `security_report.json`（原始安全扫描结果）

## 执行逻辑

1. **运行 Linter**
   
   ```bash
   cd apps/api && ruff check . --output-format=json > ruff_report.json
   ```

2. **运行类型检查**
   
   ```bash
   cd apps/api && mypy . --ignore-missing-imports
   ```

3. **运行安全检查**
   
   ```bash
   cd apps/api && bandit -r . -f json -o security_report.json
   ```

4. **汇总结果**
   
   | 类别 | 来源 | 严重级别 |
   |------|------|----------|
   | 代码风格 | ruff | Warning |
   | 类型错误 | mypy | Critical |
   | 安全漏洞 | bandit | Critical |

5. **生成审查报告**
   - 按严重程度分类问题
   - 提供修复建议
   - 判定 PASS/FAIL

## 质量门禁

| 检查项 | 要求 |
|--------|------|
| Critical 问题 | = 0 |
| 类型错误 | = 0 |
| 高危安全漏洞 | = 0 |
