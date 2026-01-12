---
status: draft
owner: requirements-split
layer_from: L0 | L1 | L2 | L3
layer_to: L0 | L1 | L2 | L3
parent: {source_path}
target: {target_path}
granularity: structured | sentence | paragraph
---

# Split Report: {layer_from} → {layer_to}

## 1. Summary（结论）

- **Decision**: PASS / FAIL
- **Why**: 1–3 句话说明原因（明确性/缺失信息/可验证性/可追溯性）

## 2. Inputs（输入）

| Item | Path | Version/Checksum | Notes |
|------|------|------------------|-------|
| Source | `{source_path}` | `{sha256_or_version}` | |
| Target | `{target_path}` | - | |

## 3. Split Rules（拆分规则）

- **Granularity**: `{granularity}`（structured/sentence/paragraph）
- **No invention**: 不得引入无来源的新需求；只允许“重写为可测试语句”，且必须保留来源
- **REQ-ID**: 建议格式 `REQ-{layer_to}-{NNN}`（例：`REQ-L1-001`）
- **Source format**:
  - `charter.yaml#<yaml_path>`（例：`charter.yaml#scope.must_have[0]`）
  - `REQ-L0-001`（引用上游需求 ID）

## 4. Source Inventory（上游条目清单）

> 逐条列出将被分析的上游条目（可引用原句/原段落或 YAML 路径）

| SRC-ID | Upstream Item | Type | Notes |
|--------|---------------|------|-------|
| SRC-001 | `{quote_or_pointer}` | requirement / metric / constraint / risk / tbd / out_of_scope | |

## 5. Mapping & Split Decisions（映射与拆分决策）

| SRC-ID | Decision | Downstream Output | Source | Notes |
|--------|----------|------------------|--------|-------|
| SRC-001 | split / keep / N/A | `REQ-Lx-000`, `interfaces.md#{name}` | `{source}` | |

## 6. Traceability Matrix（覆盖矩阵）

> 上游每个条目必须映射到下游至少 1 个 REQ/接口，或写 `N/A + 原因`。

| Upstream | Covered By | Status | Notes |
|----------|------------|--------|-------|
| SRC-001 | `REQ-Lx-000` | ✅/❌ | |

## 7. TBD & Questions（待定项）

> 任何不明确/不可验证/不可实现的内容必须进入 TBD，并带来源。

| TBD-ID | Question / Missing Info | Impact | Source |
|--------|--------------------------|--------|--------|
| TBD-001 | {question} | H/M/L | `{source}` |

## 8. Gate Check（门禁检查）

- [ ] 上游每个条目：都有映射或 `N/A + 原因`
- [ ] 下游每个 `REQ-ID`：都有至少一个 `Source`
- [ ] 未出现“无来源的新需求”
- [ ] 关键缺失信息已进入 TBD（且带来源）
