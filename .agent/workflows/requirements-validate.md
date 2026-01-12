---
description: Validate requirements document coverage, traceability, acceptance, and consistency
---

# /requirements-validate Workflow

Validates a requirements document against the Registry Schema rules, ensuring 100% traceability and no requirements drift.

## Prerequisites

- Requirements document contains `requirements-registry` block with `schema_version: "v0.4.0"`
- Registry block is populated
- For L0: `docs/L0/split-report.md` must exist
- For L1+: Parent layer requirements document must exist

## Usage

```
/requirements-validate <layer> [path] [--fix]
```

**Arguments:**
- `layer`: L0 | L1 | L2 | L3
- `path`: (optional) Specific document path
- `--fix`: (optional) Auto-fix simple issues (add missing structure, not content)

**Examples:**
```
/requirements-validate L0
/requirements-validate L1 docs/L1/chat-widget/requirements.md
/requirements-validate L0 --fix
```

## Validation Rules

### Rule 1: Coverage (覆盖率)

**Purpose**: Ensure no Charter/upstream items are missed.

**For L0:**
1. Load `docs/L0/split-report.md` Source Inventory
2. For each `SRC-ID`:
   - Must appear in `requirements[].sources[]`, OR
   - Must appear in `tbds[].sources[]`, OR
   - Must appear in `exclusions[].source`
3. **FAIL** if any SRC-ID is unaccounted for

**For L1/L2/L3:**
1. Load parent layer's `requirements[]` and `tbds[]`
2. For each parent `REQ-ID`:
   - Must be referenced in current layer `sources[]`, OR
   - Must be in `exclusions[]` with reason
3. **FAIL** if any parent REQ-ID is unaccounted for

**Output:**
```
Coverage Check: PASS/FAIL
- Total upstream items: N
- Covered by REQ: M
- Covered by TBD: K
- Excluded (N/A): J
- MISSING: [list of uncovered items]
```

### Rule 2: Traceability (溯源有效性)

**Purpose**: Ensure all source references are valid.

1. For each `requirements[].sources[]`:
   - `path` must be parseable
   - Target document must exist
   - Target item must exist at path
   - If `id` provided, must match target's ID prefix
2. For each `tbds[].sources[]`: Same checks
3. For each `exclusions[].source`: Same checks

**FAIL** if any reference is broken.

**Output:**
```
Traceability Check: PASS/FAIL
- Total references: N
- Valid: M
- BROKEN: [list with details]
```

### Rule 3: Acceptance (可验收性)

**Purpose**: Ensure high-priority requirements are actionable.

1. For each requirement with `priority: P0` or `priority: P1`:
   - `acceptance[]` must be non-empty
   - `acceptance[]` items cannot be just "TBD", "待定", or similar
   - Minimum length: 10 characters per criterion
2. Allow delegation: "见 L1/L2 细化" is acceptable if specific

**FAIL** if P0/P1 has empty or placeholder-only acceptance.

**Output:**
```
Acceptance Check: PASS/FAIL
- P0 requirements: N (all have acceptance: Y/N)
- P1 requirements: M (all have acceptance: Y/N)
- VIOLATIONS: [list of REQ-IDs without proper acceptance]
```

### Rule 4: Consistency (一致性)

**Purpose**: Ensure no cross-reference errors.

1. **TBD References**:
   - Every `requirements[].tbd_refs[]` must exist in `tbds[].id`
   - Every `tbds[].related_reqs[]` must exist in `requirements[].id`

2. **Derived Requirements**:
   - If `derived: true`, `rationale` must be non-empty
   - Derived requirements must still have valid `sources[]`

3. **Appendix Sync** (if rendered):
   - Appendix A must match `requirements[]`
   - Appendix B must match computed coverage
   - Appendix C must match `tbds[]`

4. **ID Uniqueness**:
   - No duplicate `REQ-*` IDs
   - No duplicate `TBD-*` IDs

**FAIL** if any inconsistency found.

**Output:**
```
Consistency Check: PASS/FAIL
- Cross-reference errors: [list]
- Derived without rationale: [list]
- Duplicate IDs: [list]
- Appendix sync issues: [list]
```

### Rule 5: Schema Compliance

**Purpose**: Ensure Registry follows schema.

1. Validate Registry block against `.agent/schemas/requirements-registry.schema.yaml`
2. Check required fields
3. Check enum values
4. Check pattern matching (IDs, paths)

**FAIL** if schema validation fails.

**Output:**
```
Schema Check: PASS/FAIL
- Errors: [list of schema violations]
```

## Gate Check Update

After validation, update the Gate Check section in the document:

```markdown
## 门禁检查

- [x] Registry 所有 `requirements[]` 有非空 `sources[]`
- [x] P0/P1 需求有非空 `acceptance[]`
- [x] Charter/上游条目 100% 覆盖
- [ ] 无交叉引用错位  ← FAIL: TBD-L0-015 reference mismatch
- [x] `derived: true` 的需求有 `rationale`
```

## Summary Report

```
===============================================
Requirements Validation Report
Document: docs/L0/requirements.md
Layer: L0
Schema: v1.0
Timestamp: 2026-01-12T12:30:00Z
===============================================

[✅] Schema Compliance
[✅] Coverage (87/87 items)
[✅] Traceability (142/142 references)
[⚠️] Acceptance (1 warning)
    - REQ-L0-103: acceptance too vague
[❌] Consistency (1 error)
    - REQ-L0-160 references TBD-L0-015 but TBD content mismatch

OVERALL: FAIL (1 error, 1 warning)

Fix required before proceeding to next layer.
===============================================
```

## Auto-Fix Capabilities (`--fix`)

When `--fix` is specified:

| Issue | Auto-Fix Action |
|-------|-----------------|
| Missing `schema_version` | Add `schema_version: "v0.4.0"` |
| Missing `status` on requirements | Add `status: draft` |
| Missing `tbd_refs: []` | Add empty array |
| Empty `acceptance[]` on P2 | No fix (allowed) |
| Broken reference | **Cannot auto-fix** (manual action required) |
| Duplicate ID | **Cannot auto-fix** |

## Integration

This workflow is automatically triggered:
1. After `/requirements-render` completes
2. Before `/requirements-split` generates downstream documents
3. In CI/CD pipeline as a gate

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All checks passed |
| 1 | Warnings only, proceed with caution |
| 2 | Errors found, cannot proceed |
