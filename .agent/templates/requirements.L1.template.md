---
status: draft
owner: architect
layer: L1
parent: docs/L0/requirements.md
---

# L1 Requirements: {feature_name}

> 本 L1 Feature 必须可追溯到上游 L0 需求（逐句/逐条映射）。任何新增内容必须有来源，否则视为需求漂移。

## 0. Traceability（L0 → L1）

### 覆盖矩阵

| L0 REQ-ID / Source | Covered By (L1 REQ-ID / Section) | Status | Notes |
|--------------------|----------------------------------|--------|-------|
| `REQ-L0-001` | `REQ-L1-001` | ✅/❌ | |

### 上游引用清单（可选）

- Covered L0 Requirements: `REQ-L0-001`, `REQ-L0-002`

## 1. Goals (目标)

明确此功能要实现的核心目标：

- [ ] Goal 1: 描述
- [ ] Goal 2: 描述

## 1.1 Feature Requirements（需求条目）

| REQ-ID | Priority | Requirement | Source (L0) | Acceptance Criteria |
|--------|----------|-------------|-------------|---------------------|
| REQ-L1-001 | P0/P1/P2 | 本功能应当... | `REQ-L0-001` | ... |

## 2. Non-Goals (非目标)

本版本明确不做的事项：

- 非目标 1: 原因
- 非目标 2: 原因

## 3. Constraints (约束条件)

- 技术约束: [描述]
- 资源约束: [描述]
- 时间约束: [描述]

## 4. Assumptions (假设)

- 假设 1: [描述]
- 假设 2: [描述]

## 5. Risks (风险)

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|----------|
| 风险 1 | H/M/L | H/M/L | 措施 |

## 6. Success Criteria (成功标准)

- [ ] 标准 1: 可验证的条件
- [ ] 标准 2: 可验证的条件

## 7. Dependencies (依赖)

### 上游依赖
- 依赖于: {其他 L1 模块}

### 下游依赖
- 被依赖于: {其他 L1 模块}

## 8. Gate Check（门禁）

- [ ] 覆盖矩阵完整：相关 L0 需求逐条映射到 L1（或 N/A + 原因）
- [ ] 100% L1 需求条目包含 `Source`（引用 L0 `REQ-ID` 或 `charter.yaml#...`）
- [ ] 未引入无来源的新需求
