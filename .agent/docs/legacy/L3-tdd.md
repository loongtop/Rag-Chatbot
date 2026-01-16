# Legacy: L3 (Function Spec / TDD)

L3 是 CAF 的 legacy 路径：以“函数级规格 + 测试驱动”推进实现。自 v0.6.5 起，推荐优先使用 Phase 2 的 `SPEC-*`（leaf Spec）替代 L3。

## Status / Timeline

- v0.6.5：保留但标记为 legacy（默认路径：L0/L1/L2 → Architecture → SPEC）
- v0.8.0（建议）：将 L3 相关内容隔离到 `legacy/`（仅维护兼容）
- v1.0.0（建议）：移除 L3（如无兼容需求）

## When To Use L3

- 需要严格的函数级 TDD（先测试规格，再实现）
- 迁移存量项目：已有按函数拆分的规格与测试资产

不建议用于新项目的默认路径：容易与 `SPEC-*` 重叠，且增加维护成本。

## Artifacts

- L3 Function Spec（每个 function 一个）：
  - `docs/L3/{function}/requirements.md`
  - 模板：`.agent/templates/requirements.L3.template.md`
- （可选）L3 Test Spec：写在同一文件或同目录的 `test-spec.md`（由团队约定）
- 详细设计（可选）：`design.md`
- 代码：`src/**`
- 测试：`tests/**`

## Suggested Workflow

1. **Architect**：创建/更新 `docs/L3/{function}/requirements.md`
   - `layer: L3`
   - 每条需求必须有 `sources[]`（追溯到 `REQ-L2-*` 或 `SPEC-*` 的上游）
   - Function Spec 完成后将 `status` 设为 `ready`

2. **Tester（Legacy Phase 1）**：补充 Test Spec（如团队仍要求）
   - 目标：把验收标准转为可执行测试用例列表
   - 完成后将 L3 文档 `status` 更新为 `done`（触发 Designer）

3. **Designer（可选）**：为 L3 产物补充 `design.md`

4. **Coder**：实现代码（不得修改 L3 中的需求/契约；如需变更先回到上游修订）

5. **Tester（Phase 3）**：实现并运行测试，覆盖率达标

6. **Reviewer / Integrator**：按常规门禁收敛

## Migration Guidance (L3 → SPEC)

当你想把 legacy L3 迁移到 v0.6.5 的默认路径：

- 将每个 L3 Function Spec 合并为对应模块的一个或多个 `SPEC-*`
- 把 L3 中的测试点迁移到 leaf Spec 的 `Acceptance Tests`
- 保留原测试代码；逐步将溯源锚点从 `docs/L3/...` 迁移到 `specs/SPEC-*`

