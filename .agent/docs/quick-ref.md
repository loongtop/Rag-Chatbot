# Quick Reference Card

常用命令和操作速查表。

---

## Workflow Commands

| Command | Description |
|---------|-------------|
| `/charter-init` | Initialize new project |
| `/charter-validate` | Validate charter.yaml |
| `/charter-freeze` | Lock charter (before L1); recommended `chmod a-w charter.yaml` |
| `/charter-unfreeze` | Unlock for modifications; if needed `chmod u+w charter.yaml` |
| `/charter-status` | Check project progress |
| `/charter-quality` | Run quality gates |
| `/requirements-split` | Create split-report.md + traceability matrix |
| `/requirements-render` | Registry → body + appendices |
| `/requirements-validate` | Coverage/traceability/acceptance gates |

---

## Layer-Specific Templates

> Registry block is single source of truth. All templates use embedded Registry.

| Layer | Template | Key Contents |
|-------|----------|--------------|
| Any | `split-report.template.md` | Splitability + Traceability matrix |
| L0 | `requirements.L0.template.md` | Registry (requirements/tbds/exclusions) + SRS body |
| L1 | `requirements.L1.template.md` | Registry + interfaces[] |
| L2 | `requirements.L2.template.md` | Registry + interfaces[] + module design |
| L2 | `execution-tracker.template.md` | Progress tracking |
| L3 | `requirements.L3.template.md` | Registry + Function Spec + Test Spec |

---

## Agent Roles

| Agent | Trigger | Output |
|-------|---------|--------|
| Requirements Split | before writing requirements/interfaces | split-report.md |
| Architect | charter.yaml exists + `freeze.frozen=true` | requirements.md, subtasks.md |
| Tester (P1) | L3 requirements.md `status=ready` | Test Spec (填写) |
| Designer | L3 requirements.md `status=done` | design.md |
| Coder | design.md `status=done` | src/**/* |
| Tester (P2) | src/**/* exists | tests/**/* (实现+执行) |
| Reviewer | tests passed | review_report.md |
| Integrator | all subtasks done | integration_report.md |

---

## Artifact Status

```yaml
---
status: draft | ready | in_progress | done
owner: requirements-split | architect | designer | coder | tester | reviewer | integrator
layer: L0 | L1 | L2 | L3
parent: {parent_path}
source_checksum: "{sha256}"
profile: "{profile}"
schema_version: "v0.4.0"
---
```

---

## Registry Block Structure

```requirements-registry
schema_version: "v0.4.0"
layer: L0 | L1 | L2 | L3
parent: "{parent_path}"
requirements: [...]
tbds: [...]
exclusions: [...]
interfaces: [...]  # L1/L2 only
```

---

## TDD Workflow (L3)

```
1. Architect → Function Spec (status: ready)
2. Tester P1 → Test Spec (status: done)
3. Designer → design.md
4. Coder → 实现代码
5. Tester P2 → 实现测试 + 运行
```

---

## Gate Check

```yaml
Gate_Check:
  tests_passed: true
  coverage: ">= 95%"
  deviations_from_spec: []
```

---

## Key Rules

1. **Freeze First**: 在 L1 前执行 `/charter-freeze`
2. **Single Module**: 每次只推进一个 Feature/Module
3. **Use Templates**: 使用层级特定模板 + Registry 块
4. **TDD Mode**: L3 先 Test Spec 后实现
5. **Gate Check**: 每个模块完成后检查
6. **Traceability First**: 先写 `split-report.md`，再写 requirements/interfaces（每条都要 Source）
7. **Render + Validate**: 完成后执行 `/requirements-render` + `/requirements-validate`

---

## Version Matrix

| Component | Version |
|-----------|--------|
| CAF | v0.4.0 |
| schema_version | v0.4.0 |
