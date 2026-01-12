---
status: draft
owner: architect
layer: L0
parent: charter.yaml
source_checksum: ""   # 可选：charter.yaml 的 SHA-256（用于审计/追溯）
---

# L0 Requirements: {system_name}

> 本文档必须 100% 可追溯到 `charter.yaml`。任何无法落地的内容请进入 `TBD` 并标注来源。

## 0. Sources（来源）

- `charter.yaml`（checksum: `{source_checksum}`）

## 1. Traceability Matrix（覆盖矩阵：Charter → L0）

> `charter.yaml` 的每个关键条目必须映射到至少 1 条 L0 需求，或写 `N/A + 原因`。

| Charter Item | Covered By (REQ-ID) | Status | Notes |
|-------------|----------------------|--------|-------|
| `charter.yaml#scope.must_have[0]` | `REQ-L0-001` | ✅/❌ | |

## 2. Functional Requirements

> 建议使用 “shall/应当” 句式，确保可测试、可验收、可实现。

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-001 | P0/P1/P2 | 系统应当... | `charter.yaml#...` | 可验证条件... |

## 3. Non-Functional Requirements

### Performance

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-1xx | P0/P1/P2 | 系统应当... | `charter.yaml#metrics.performance[0]` | ... |

### Security

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-2xx | P0/P1/P2 | 系统应当... | `charter.yaml#metrics.security[0]` | ... |

### Reliability

| REQ-ID | Priority | Requirement | Source | Acceptance Criteria |
|--------|----------|-------------|--------|---------------------|
| REQ-L0-3xx | P0/P1/P2 | 系统应当... | `charter.yaml#metrics.stability[0]` | ... |

## 4. Inputs/Outputs

**Inputs**:
- param1: Type, description
- param2: Type, description

**Outputs**:
- return: Type, description
- side_effects: [Description]

## 5. Constraints

- Technology stack: [Required technologies]
- Dependencies: [External dependencies]
- Limitations: [Any constraints]

## 6. TBD / Open Questions（待定项）

| TBD-ID | Question | Source | Notes |
|--------|----------|--------|-------|
| TBD-L0-001 | ... | `charter.yaml#open_questions[0]` | |

## 7. Gate Check（门禁）

- [ ] 100% L0 需求条目包含 `Source`
- [ ] `charter.yaml` 关键条目已覆盖（或 N/A + 原因）
- [ ] 未引入“无来源的新需求”
