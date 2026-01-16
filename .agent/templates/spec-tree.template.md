---
status: draft
owner: architect
layer: SPEC
parent: docs/L2
profile: "{profile}"
---

# Spec Tree

> 目的：把 L2 Requirements 映射到可实现的 leaf Specs，并提供进度与覆盖视图。

## 1. Tree View

```
REQ-L2-xxx
  ├─ SPEC-001 (leaf=false)
  │    ├─ SPEC-001-A (leaf=true)
  │    └─ SPEC-001-B (leaf=true)
  └─ SPEC-002 (leaf=true)
```

## 2. Coverage Matrix (L2 → Spec)

| REQ-L2 | SPEC | Leaf | Status | Notes |
|--------|------|------|--------|------|
| REQ-L2-xxx | SPEC-001 | false | draft | |
| REQ-L2-xxx | SPEC-001-A | true | draft | |

## 3. Leaf Queue

| SPEC | Priority | Owner | Ready For Code | Notes |
|------|----------|-------|----------------|------|
| SPEC-001-A | P0 | | yes/no | |

## 4. Interface Touchpoints

| SPEC | IFC | Role | Notes |
|------|-----|------|------|
| SPEC-001-A | IFC-001 | consume | |

## 5. Gate Check

- [ ] 每个 Spec 都有 `source_requirements`
- [ ] 每个 REQ-L2 至少映射到 1 个 Spec（或标注 N/A + reason）
- [ ] leaf Spec 的 Leaf Checklist 全部满足
