---
id: "SPEC-000"
status: draft
owner: architect
leaf: false
parent: "REQ-L2-000"
source_requirements:
  - "REQ-L2-000"
interfaces:
  - "IFC-000"
depends_on: []
profile: "{profile}"
---

# Spec: {spec_title}

## 0. Summary

- Goal: {one_sentence_goal}
- Non-goals: {explicit_non_goals}
- Leaf: `{leaf}`

## 1. Scope

### In Scope
- {item}

### Out of Scope
- {item}

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-000 | {explain} | |

## 3. Design / Decisions

### Proposed Approach
- {approach}

### Key Decisions
- Decision: {what}
  - Rationale: {why}
  - Alternatives: {considered}

## 4. Interfaces Impact

> 引用 `docs/L2/interfaces.md` 的 `IFC-*` 条目；若无跨模块交互，写 N/A。

| Interface | Role | Notes |
|----------|------|------|
| IFC-000 | provide/consume | |

## 5. Implementation Plan

> leaf Spec 必填：要达到“可直接写代码”的粒度（文件/函数/数据结构/错误处理）。

1. {step}
2. {step}

### Files / Modules
- {path_or_module}

### Risks & Mitigations
- Risk: {risk}
  - Mitigation: {mitigation}

## 6. Acceptance Tests

> leaf Spec 必填：用可执行/可验证语言描述（测试用例或验收标准）。

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| 정상 | ... | ... | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-SPEC-000 | ... | H/M/L | | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback
