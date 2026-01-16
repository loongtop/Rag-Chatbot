---
description: Validate architecture documents for traceability and completeness
version: v0.6.5
---

# /architecture-validate

验证架构设计文档的追溯性和完整性。

## 前置条件

- `docs/architecture/*.md` 已生成
- `docs/L2/*/requirements.md` 存在
- `docs/L2/interfaces.md` 存在

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `source_path` | string | `docs/architecture` | 架构文档目录 |
| `strict` | bool | `true` | 严格模式 (FAIL 阻塞) |

## 验证规则

### 1. Registry 格式验证

必须使用 code fence 格式：

````
```architecture-registry
schema_version: "v0.6.5"
items:
  - id: ARCH-*-NNN
    statement: "..."
    sources:
      - id: "REQ-*" | "IFC-*"
        path: "..."
```
````

### 2. Sources 覆盖验证

| Check | 规则 | 错误 |
|-------|------|------|
| 必填 | 每个 ARCH-* 必须有 `sources[]` | `ARCH-DB-001: missing sources` |
| 有效性 | sources.path 必须指向存在的文件#ID | `ARCH-DB-001: invalid source` |
| 类型 | sources.id 必须是 `REQ-*` 或 `IFC-*` | `ARCH-DB-001: invalid source type` |

### 3. ID 格式验证

| 文件 | 前缀 | 格式 |
|------|------|------|
| overview.md | `ARCH-OV-` | `ARCH-OV-NNN` |
| database-schema.md | `ARCH-DB-` | `ARCH-DB-NNN` |
| core-flows.md | `ARCH-FL-` | `ARCH-FL-NNN` |
| api-spec.md | `ARCH-API-` | `ARCH-API-NNN` |

### 4. 技术栈一致性验证

```python
def validate_tech_stack(arch_docs, charter):
    allowed = charter.constraints.technology_boundary.allowed
    forbidden = charter.constraints.technology_boundary.forbidden
    
    for tech in extract_technologies(arch_docs):
        if tech in forbidden:
            error(f"Forbidden technology: {tech}")
        if tech not in allowed:
            warning(f"Unlisted technology: {tech}")
```

### 5. L2 覆盖验证

```python
def validate_l2_coverage(arch_docs, l2_reqs, interfaces):
    # 检查所有 REQ-L2-* 是否被架构文档引用
    referenced = set()
    for item in arch_docs.all_items():
        for source in item.sources:
            referenced.add(source.id)
    
    for req in l2_reqs:
        if req.id not in referenced:
            warning(f"L2 requirement not referenced: {req.id}")
```

## 执行流程

```
1. 扫描 docs/architecture/*.md
   ↓
2. 解析每个文件的 architecture-registry 块
   ↓
3. 运行验证规则 (5 项)
   ↓
4. 生成验证报告
   ↓
5. 判定结果
   - strict=true: 任一 ERROR → FAIL
   - strict=false: 仅 WARNING
```

## 输出格式

```markdown
# Architecture Validation Report

## Summary

| Check | Status | Count |
|-------|--------|-------|
| Registry 格式 | ✅ PASS | 4/4 |
| Sources 覆盖 | ✅ PASS | 26/26 |
| ID 格式 | ✅ PASS | 26/26 |
| 技术栈一致性 | ✅ PASS | 0 violations |
| L2 覆盖 | ⚠️ WARN | 2 not referenced |

## Errors (0)

None

## Warnings (2)

- `REQ-L2-WGT-003` not referenced by any architecture item
- `REQ-L2-ADM-004` not referenced by any architecture item

## Result: ✅ PASS (with warnings)
```

## 使用示例

```bash
# 验证架构文档
/architecture-validate

# 非严格模式 (仅报告不阻塞)
/architecture-validate strict=false

# 指定路径
/architecture-validate source_path=docs/design

# A/B 对比阶段建议 strict=false，并配合 /architecture-compare
```

## 与 requirements-validate 的关系

| Workflow | 验证对象 | 追溯方向 |
|----------|----------|----------|
| `/requirements-validate` | L0/L1/L2 需求 | 向上追溯 Charter |
| `/architecture-validate` | 架构文档 | 向上追溯 L2/IFC |
