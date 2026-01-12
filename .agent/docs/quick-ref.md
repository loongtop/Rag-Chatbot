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

---

## Layer-Specific Templates

| Layer | Template | Key Contents |
|-------|----------|--------------|
| Any | `split-report.template.md` | Splitability + Traceability matrix |
| L0 | `requirements.template.md` | General requirements |
| L1 | `requirements.L1.template.md` | Goals, Constraints, Risks |
| L2 | `requirements.L2.template.md` | Features, Interfaces, Data Models |
| L2 | `execution-tracker.template.md` | Progress tracking |
| L3 | `requirements.L3.template.md` | Function Spec + Test Spec (TDD) |

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
---
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
3. **Use Layer Templates**: 使用层级特定模板
4. **TDD Mode**: L3 先 Test Spec 后实现
5. **Gate Check**: 每个模块完成后检查
6. **Traceability First**: 先写 `split-report.md`，再写 requirements/interfaces（每条都要 Source）
