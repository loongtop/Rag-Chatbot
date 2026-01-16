# Minimal Example: notes-cli (single module, Python)

目标：提供一个“最小但完整”的 CAF v0.6.5 端到端样例，可用于演示 Phase 0→3 的全流程产物结构。

## Files

- `charter.yaml`: 冻结后的 Charter（示例）
- `docs/L0/requirements.md`: L0 需求（Registry 为单一事实源）
- `docs/L2/notes-store/requirements.md`: 单模块 L2 需求
- `docs/L2/interfaces.md`: 本示例无跨模块契约（interfaces=[]）
- `docs/architecture/*.md`: Phase 1.5 架构产物（含 `architecture-registry`）
- `specs/SPEC-001.md`: leaf Spec（可直接实现）
- `src/notes_app/store.py`: 示例实现
- `tests/test_store.py`: 示例测试

## Suggested Workflow (copy/paste prompts)

1. `/charter-validate` → `/charter-freeze`
2. `/requirements-split source_path=charter.yaml target_dir=docs/L0`
3. `/requirements-render L0 docs/L0/requirements.md` → `/requirements-validate L0 docs/L0/requirements.md`
4. `/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L2 granularity=direct`
5. `/architecture-generate` → `/architecture-validate`
6. `/spec source_path=docs/L2/notes-store/requirements.md`
7. 实现 `src/` + `tests/` → `/charter-quality`

