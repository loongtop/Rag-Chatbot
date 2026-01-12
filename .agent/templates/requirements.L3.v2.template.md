---
status: draft
owner: architect
layer: L3
parent: docs/L2/{feature}/{module}/requirements.md
source_checksum: "{checksum}"
template_version: "v2.0"
profile: "{profile}"
feature: "{feature_name}"
module: "{module_name}"
function: "{function_name}"
---

# L3 Requirements: {function_name}

> ⚠️ **Document Structure (Template v2.0)**
>
> | Section | Type | Edit Policy |
> |---------|------|-------------|
> | `requirements-registry` block | Source | ✅ Editable |
> | Function Spec | Source | ✅ Editable (by Architect) |
> | Test Spec | Source | ✅ Editable (by Tester Phase 1) |
> | Body text | Generated | 🔒 Readonly |

---

## — BEGIN REGISTRY —

```requirements-registry
# =============================================================================
# L3 Requirements Registry - Function Level (Leaf Node)
# Schema: v1.0 | Template: v2.0 | CAF: v0.4.0
# =============================================================================

schema_version: "v1.0"
layer: L3
parent: "docs/L2/{feature}/{module}/requirements.md"
source_checksum: "{checksum}"
profile: "{profile}"

# -----------------------------------------------------------------------------
# Requirements (Function-level - leaf nodes)
# -----------------------------------------------------------------------------
requirements:
  - id: REQ-L3-001
    priority: P0
    statement: "函数应当..."
    sources:
      - id: "REQ-L2-001"
        path: "docs/L2/{feature}/{module}/requirements.md#REQ-L2-001"
    acceptance:
      - "验收条件1"
    status: draft
    section: functional
    tbd_refs: []
    derived: false

# -----------------------------------------------------------------------------
# TBDs (should be resolved at L3, minimal)
# -----------------------------------------------------------------------------
tbds: []

# -----------------------------------------------------------------------------
# Exclusions
# -----------------------------------------------------------------------------
exclusions: []
```

## — END REGISTRY —

---

## Function Spec（由 Architect 填写）

### 签名

```python
def {function_name}(
    param1: Type,
    param2: Type,
    **kwargs
) -> ReturnType:
    """
    函数简述
    
    Args:
        param1: 参数1描述
        param2: 参数2描述
        
    Returns:
        返回值描述
        
    Raises:
        ExceptionType: 异常条件
    """
```

### 职责

{函数的单一职责描述}

### 前置条件

- 条件1
- 条件2

### 后置条件

- 条件1
- 条件2

### 伪代码

```
FUNCTION {function_name}(param1, param2):
    // Step 1: 输入验证
    VALIDATE param1
    VALIDATE param2
    
    // Step 2: 核心逻辑
    result = PROCESS(param1, param2)
    
    // Step 3: 输出
    RETURN result
```

### 边界处理

| 场景 | 处理方式 |
|------|----------|
| param1 为空 | 抛出 ValueError |
| param2 超出范围 | 返回默认值 |

---

## Test Spec（由 Tester Phase 1 填写）

> 在 Function Spec 完成后，由 Tester Agent 补充测试用例。

### 正常用例

| Case ID | Input | Expected Output | 说明 |
|---------|-------|-----------------|------|
| TC-001 | `param1=x, param2=y` | `expected_result` | 正常情况 |

### 边界用例

| Case ID | Input | Expected Output | 说明 |
|---------|-------|-----------------|------|
| TC-B01 | `param1=边界值` | `expected` | 边界条件 |
| TC-B02 | `param1=空` | `ValueError` | 空输入 |

### 异常用例

| Case ID | Input | Expected Exception | 说明 |
|---------|-------|-------------------|------|
| TC-E01 | `param1=无效` | `ValueError` | 无效输入 |

### 性能用例

| Case ID | Condition | Expected | 说明 |
|---------|-----------|----------|------|
| TC-P01 | 1000次调用 | < 100ms 总计 | 性能基线 |

---

<!-- GENERATED CONTENT BELOW - DO NOT EDIT MANUALLY -->

## 附录

### 附录 A：需求表

| REQ-ID | Priority | Statement | Sources | Acceptance | Status |
|--------|----------|-----------|---------|------------|--------|
| {从 Registry 渲染} | | | | | |

### 附录 B：溯源矩阵（L2 → L3）

| L2 Item | Covered By | Status | Notes |
|---------|------------|--------|-------|
| {从 Registry 渲染} | | | |

---

## 门禁检查

- [ ] Function Spec 完整（签名/职责/前置/后置/伪代码）
- [ ] Test Spec 完整（正常/边界/异常/性能各 ≥1 用例）
- [ ] L2 需求 100% 覆盖
- [ ] `status: done` 时可触发 Designer Agent
