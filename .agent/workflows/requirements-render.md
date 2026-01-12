---
description: Render requirements document body and appendices from Registry block
---

# /requirements-render Workflow

Renders the generated sections (body text + appendices) of a requirements document from its embedded Registry block.

## Prerequisites

- Requirements document contains `requirements-registry` block with `schema_version: "v1.0"`
- Registry block is populated
- Profile is set in frontmatter or Registry

## Usage

```
/requirements-render <layer> [path]
```

**Arguments:**
- `layer`: L0 | L1 | L2 | L3
- `path`: (optional) Specific document path. If omitted, uses default location.

**Examples:**
```
/requirements-render L0
/requirements-render L1 docs/L1/chat-widget/requirements.md
```

## Workflow Steps

### 1. Load Registry Block

1. Open target requirements document
2. Parse the `requirements-registry` fenced code block
3. Validate against `.agent/schemas/requirements-registry.schema.yaml`
4. If validation fails, abort with error report

### 2. Load Profile Configuration

1. Read `profile` from Registry or frontmatter
2. Load profile from `.agent/config/srs-profiles.yaml`
3. Determine applicable sections

### 3. Render Body Text (§1-§5)

For each applicable SRS section:

1. **§1 Introduction**: Generate from `parent`, `source_checksum`, profile
2. **§2 Overall Description**: Generate from `requirements[].sources[]` grouped by Charter section
3. **§3 Specific Requirements**: Generate summaries pointing to Appendix A
4. **§4 Input/Output**: Extract from relevant requirements
5. **§5 Quality Gates**: Extract from `section: quality_gate` requirements

Each paragraph MUST include:
```markdown
_Source_: `{sources[].path}`  
_Covered by_: `{requirement.id}`
```

### 4. Render Appendix A (Requirements Table)

Transform `requirements[]` into table:

```markdown
| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| {id} | {priority} | {statement} | {sources[].id or path} | {acceptance[]} | {status} |
```

Sort by: `section` → `priority` → `id`

### 5. Render Appendix B (Traceability Matrix)

1. Collect all unique `sources[].path` from `requirements[]`, `tbds[]`, `exclusions[]`
2. Group by Charter item
3. Generate matrix:

```markdown
| Charter Item | Covered By | Status | Notes |
|--------------|------------|--------|-------|
| {source.path} | {REQ-IDs / TBD-IDs / N/A} | ✅ | {exclusion.reason if N/A} |
```

### 6. Render Appendix C (TBD Table)

Transform `tbds[]` into table:

```markdown
| TBD-ID | Question | Sources | Impact | Owner | Target Layer | Status |
|--------|----------|---------|--------|-------|--------------|--------|
| {id} | {question} | {sources[]} | {impact} | {owner} | {target_layer} | {status} |
```

### 7. Render Appendix D (Interfaces Table) - L1/L2 Only

If `interfaces[]` exists:

```markdown
| Name | Type | Description | Input | Output | Consumers | Providers |
|------|------|-------------|-------|--------|-----------|-----------|
| {name} | {type} | {description} | {contract.input} | {contract.output} | {consumers[]} | {providers[]} |
```

### 8. Update Generated Content Region

1. Locate `<!-- GENERATED CONTENT BELOW -->` marker
2. Replace all content until end of file (before Gate Check)
3. Preserve Registry block and any editable sections

### 9. Trigger Validation

After render completes, automatically trigger:
```
/requirements-validate <layer> [path]
```

## Output

- Updated requirements document with rendered body and appendices
- Validation report (from chained `/requirements-validate`)

## Error Handling

| Error | Action |
|-------|--------|
| Registry schema invalid | Abort, show validation errors |
| Profile not found | Warn, use `fullstack-web` as fallback |
| Missing required sections | Warn in output, continue render |
| Circular references | Abort, show reference chain |

## Notes

- Generated content is marked `DO NOT EDIT MANUALLY`
- Re-running render overwrites all generated sections
- Manual edits to generated sections will be lost
- Only edit the Registry block and explicitly editable sections (Function Spec, Test Spec in L3)
