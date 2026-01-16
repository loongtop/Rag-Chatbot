---
description: Compare two architecture outputs (A/B) without renaming docs/
version: v0.6.5
---

# /architecture-compare

对比两次架构文档输出（A/B），用于验证框架/提示词版本升级是否提升了输出质量。

> 目的：验证“改进是否合理”；不是引入新的交付物，也不改变需求冻结策略。

## 核心原则（避免本末倒置）

- **不改需求**：L0/L1/L2 与 `charter.yaml (frozen=true)` 视为只读输入。
- **不重命名 `docs/`**：路径是追溯/门禁的锚点，改名会引入噪声和额外风险。
- **隔离实验输出**：用 `target_dir` 或 `git worktree` 生成候选版本，避免污染主输出。
- **评价以结构质量为主**：追溯覆盖、可校验性、占位符残留；内容措辞仅作辅因。

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `baseline_dir` | string | `docs/architecture` | 基线架构目录 |
| `candidate_dir` | string | `docs/architecture.__candidate__` | 候选架构目录 |
| `type` | string | `all` | 透传给 `/architecture-generate` |
| `strict` | bool | `false` | 透传给 `/architecture-validate`（对比阶段建议 false） |

## 推荐流程（不改 `docs/`）

1. **确认输入稳定**
   - `charter.yaml` 已冻结（`frozen: true`）
   - `docs/L2/*/requirements.md` 与 `docs/L2/interfaces.md` 已完成且不再变更

2. **准备基线**
   - 若 `baseline_dir` 已存在：保持不动作为基线
   - 若不存在：先用当前版本生成一次作为基线：`/architecture-generate target_dir={{baseline_dir}} type={{type}}`

3. **生成候选**
   - `/architecture-generate target_dir={{candidate_dir}} type={{type}}`

4. **分别验证（结构门禁）**
   - `/architecture-validate source_path={{baseline_dir}} strict={{strict}}`
   - `/architecture-validate source_path={{candidate_dir}} strict={{strict}}`

5. **对比差异（内容层）**
   - `git diff --no-index {{baseline_dir}} {{candidate_dir}}`
   - 或 `diff -ru {{baseline_dir}} {{candidate_dir}}`

6. **对比指标（可选，自动化）**
   - `python3 .agent/tools/architecture_compare.py --baseline {{baseline_dir}} --candidate {{candidate_dir}}`

7. **结论与处置**
   - 若候选更好：将候选“晋升”为正式输出（建议通过 git 操作/目录替换完成）
   - 若差异不显著：保留基线，记录结论即可

## 进阶：使用 git worktree 隔离对比（可选）

当你希望“同路径输出”也能隔离时：

```bash
git worktree add ../caf-arch-candidate HEAD
```

在 `../caf-arch-candidate` 目录内运行 `/architecture-generate`（默认输出到 `docs/architecture`），再与主工作区对比。
