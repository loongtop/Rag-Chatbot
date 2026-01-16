# Quick Reference Card

常用命令和操作速查表。

---

## Workflow Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `/charter-init` | Initialize new project | `--profile rag-web` |
| `/charter-validate` | Validate charter.yaml | |
| `/charter-freeze` | Lock charter (before L1) | recommended `chmod a-w charter.yaml` |
| `/charter-unfreeze` | Unlock for modifications | if needed `chmod u+w charter.yaml` |
| `/charter-status` | Check project progress | |
| `/charter-quality` | Run quality gates | |
| `/requirements-split` | Create split-report.md + traceability matrix | `granularity=auto/full/medium/light/direct` |
| `/requirements-render` | Registry → body + appendices | |
| `/requirements-validate` | Coverage/traceability/acceptance gates | |
| `/spec` | L2 requirements → Spec tree (recursive) | `source_path=docs/L2/{module}/requirements.md` |

### Granularity 参数（v0.6.0）

| 值 | 分解路径 | 适用场景 |
|---|---------|----------|
| `auto` | **自动评估**复杂度选择 | 默认，推荐 |
| `full` | L0→L1→L2 | 复杂系统，多模块 |
| `medium` | L0→L2 | 中等系统，跳过 L1 |
| `light` | L0→L1 | 简单系统，先停在 L1 |
| `direct` | L0→L2（单模块） | 单模块/边界清晰 |

```bash
# 自动评估（推荐）
/requirements-split source_path=charter.yaml target_dir=docs/L0

# 强制全链路
/requirements-split granularity=full

# 轻量分解
/requirements-split granularity=light
```

### REQ-ID 分类规则（v0.5.0）

| 分类 | ID 前缀 | 判定规则 |
|------|---------|----------|
| 组件专属 | `REQ-L0-{COMP}-*` | 基于 charter.yaml#components |
| 共享功能 | `REQ-L0-SHARED-*` | 跨组件功能 |
| 性能 | `REQ-L0-PERF-*` | MET-PERF-* |
| 安全 | `REQ-L0-SEC-*` | MET-SEC-* |
| 稳定 | `REQ-L0-STAB-*` | MET-STAB-* |
| 易用 | `REQ-L0-UX-*` | MET-UX-* |
| 约束 | `REQ-L0-CON-*` | constraints |

**组件前缀示例**:
- `api-server` → API
- `chat-widget` → WGT
- `admin-dashboard` → ADM

---

## Layer-Specific Templates

> Registry block is single source of truth. All templates use embedded Registry.

| Layer | Template | Key Contents |
|-------|----------|--------------|
| Any | `split-report.template.md` | Splitability + Traceability matrix |
| L0 | `requirements.L0.template.md` | Registry (requirements/tbds/exclusions) + SRS body |
| L1 | `requirements.L1.template.md` | Feature requirements + subtasks |
| L2 | `requirements.L2.template.md` | Module requirements |
| L2 | `interfaces.L2.template.md` | Inter-module contracts (API/Event/Data) |
| L2 | `execution-tracker.template.md` | Progress tracking |
| SPEC | `spec.template.md` | Implementation spec (leaf-ready) |
| SPEC | `spec-tree.template.md` | Spec tree + coverage matrix |

---

## Agent Roles

| Agent | Trigger | Output |
|-------|---------|--------|
| Requirements Split | before writing requirements/interfaces | split-report.md |
| Architect | charter.yaml exists + `freeze.frozen=true` | requirements.md, subtasks.md |
| Spec | L2 requirements done | specs/*.md, specs/spec-tree.md |
| Designer | leaf Spec ready (optional) | design.md |
| Coder | leaf Spec ready (or design.md done) | src/**/* |
| Tester (P2) | src/**/* exists | tests/**/* (实现+执行) |
| Reviewer | tests passed | review_report.md |
| Integrator | all subtasks done | integration_report.md |

---

## Artifact Status

```yaml
---
status: draft | ready | in_progress | done
owner: requirements-split | architect | spec | designer | coder | tester | reviewer | integrator
layer: L0 | L1 | L2 | SPEC | L3(legacy)
parent: {parent_path}
source_checksum: "{sha256}"
profile: "{profile}"
schema_version: "v0.6.0"
---
```

---

## Registry Block Structure

```requirements-registry
schema_version: "v0.6.0"
layer: L0 | L1 | L2 | L3(legacy)
parent: "{parent_path}"
requirements: [...]
tbds: [...]
exclusions: [...]
interfaces: [...]  # legacy：旧版在 L1/L2 内嵌；v0.6.0 推荐使用 docs/L2/interfaces.md（interfaces-registry）
```

---

## (Legacy) TDD Workflow (L3)

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
4. **Specs First**: L2 完成后先 `/spec`，leaf Spec 再实现
5. **Gate Check**: 每个模块完成后检查
6. **Traceability First**: 先写 `split-report.md`，再写 requirements/interfaces（每条都要 Source）
7. **Render + Validate**: 完成后执行 `/requirements-render` + `/requirements-validate`

---

## Version Matrix

| Component | Version |
|-----------|--------|
| CAF | v0.6.0 |
| schema_version | v0.6.0 |
