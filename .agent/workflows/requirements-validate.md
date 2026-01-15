---
description: Validate requirements document coverage, traceability, acceptance, and consistency
---

# /requirements-validate Workflow

> ⚠️ **重要说明**: 此工作流描述了复杂的数据验证逻辑，推荐实现为 CLI 工具（如 `caf-validate`）。LLM 应仅调用工具，而非直接执行此逻辑。

## 使用方式

```
/requirements-validate <layer> [path] [--fix]
```

**Arguments:**
- `layer`: L0 | L1 | L2 | L3
- `path`: (可选) 文档路径
- `--fix`: (可选) 自动修复简单问题（仅结构，不改内容）

**推荐 CLI 实现:**
```bash
# 验证
caf-validate --layer L0 --input docs/L0/requirements.md
caf-validate --layer L1 --input docs/L1/chat-widget/requirements.md

# 验证并自动修复
caf-validate --layer L0 --input docs/L0/requirements.md --fix
```

## 验证规则

### Rule 1: Coverage（覆盖率）

检查上游内容无遗漏。

| 层级 | 检查点 |
|------|--------|
| L0 | Charter 中每个 `scope.must_have` 必须有对应 REQ 或 TBD |
| L1+ | 父层每个 REQ-ID 必须在当前层有引用或 exclusion |

### Rule 2: Traceability（溯源）

根据 `charter.yaml` 的 `traceability.mode` 检查：
- `strict`: **必须**每条需求都有 `Source`
- `assist`: **推荐**有 Source（警告但不阻塞）
- `off`: **跳过**溯源检查

```yaml
requirements:
  - id: REQ-L1-001
    sources:
      - id: "SCOPE-MH-001"
        path: "charter.yaml#scope.must_have[0]"
```

### Rule 3: Acceptance（验收条件）

检查每个 REQ 有验收条件。

```yaml
requirements:
  - id: REQ-L1-001
    acceptance:
      - "验收条件1"
      - "验收条件2"
```

### Rule 4: Consistency（一致性）

1. TBD References: 检查 `requirements[].tbd_refs[]` 存在 `tbds[].id`
2. Derived Requirements: `derived: true` 必须有 `rationale`
3. ID Uniqueness: 无重复 REQ-ID/TBD-ID

### Rule 5: Schema Compliance

校验 `requirements-registry` 块符合 `.agent/schemas/requirements-registry.schema.yaml`。

## 输出示例

```
✅ Coverage Check: PASS
   - 上游条目: 15
   - REQ 覆盖: 12
   - TBD 标记: 2
   - Exclusions: 1

✅ Traceability Check: PASS
   - 总需求数: 8
   - 有 Source: 8
   - 无 Source: 0

❌ Acceptance Check: FAIL
   - 缺少验收条件: REQ-L1-003, REQ-L1-005

🔧 建议: 添加 --fix 参数自动修复简单问题
```

## CI 集成

```yaml
# .github/workflows/requirements-validate.yml
name: Requirements Validation
on:
  pull_request:
    paths: ['docs/L*/**/*.md']

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install CAF CLI
        run: pip install caf-tools
      - name: Validate requirements
        run: |
          caf-validate --layer L0
          caf-validate --layer L1
          caf-validate --layer L2
```

## Gate Check

验证通过后更新文档的 Gate Check 部分：

```markdown
## 门禁检查

- [x] Coverage: 100%
- [x] Traceability: 所有需求有 Source
- [x] Acceptance: P0/P1 有验收条件
- [x] Consistency: 无交叉引用错误
- [x] Schema: 符合 v0.5.0 规范
```

## Auto-Fix Capabilities (`--fix`)

| Issue | Auto-Fix Action |
|-------|----------------|
| Missing `schema_version` | Add `schema_version: "v0.5.0"` |
| Missing `status` on requirements | Add `status: draft` |
| Missing `tbd_refs: []` | Add empty array |
| Empty `acceptance[]` on P2 | No fix (allowed) |
| Broken reference | **Cannot auto-fix** |
| Duplicate ID | **Cannot auto-fix** |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All checks passed |
| 1 | Warnings only, proceed with caution |
| 2 | Errors found, cannot proceed |
