---
status: draft
owner: architect
layer: L3
parent: L2/{parent_module}
---

# L3 Requirements: {function_name}

## 1. Function Specification (函数规格)

### 签名 (Signature)

```
function_name(
    param1: Type,      # 参数1说明
    param2: Type,      # 参数2说明
    *,                 # 关键字参数分隔
    option1: Type = default
) -> ReturnType
```

### 职责 (Responsibility)

单一职责描述：此函数负责 [具体职责]

### 前置条件 (Preconditions)

- param1 必须满足: [条件]
- param2 必须满足: [条件]

### 后置条件 (Postconditions)

- 返回值保证: [条件]
- 副作用: [描述任何副作用]

## 2. Algorithm Design (算法设计)

### 核心逻辑

1. 步骤 1: [描述]
2. 步骤 2: [描述]
3. 步骤 3: [描述]

### 伪代码

```
FUNCTION function_name(param1, param2):
    # 输入验证
    IF not valid(param1) THEN
        RAISE ValidationError
    
    # 核心逻辑
    result = process(param1, param2)
    
    # 返回结果
    RETURN result
```

## 3. Test Specification (测试规格)

> ⚠️ 此部分由 tester-agent 在 Phase 1 填写

### 正常用例 (Happy Path)

| ID | 输入 | 预期输出 | 描述 |
|----|------|----------|------|
| T01 | `(a, b)` | `expected` | 正常情况 |
| T02 | `(x, y)` | `expected` | 另一正常情况 |

### 边界用例 (Boundary)

| ID | 输入 | 预期输出 | 描述 |
|----|------|----------|------|
| T03 | `(empty, 0)` | `edge_case` | 空输入 |
| T04 | `(max, limit)` | `edge_case` | 最大值 |

### 异常用例 (Error Cases)

| ID | 输入 | 预期异常 | 描述 |
|----|------|----------|------|
| T05 | `(null, -)` | `NullError` | 空参数 |
| T06 | `(invalid, -)` | `ValidationError` | 无效输入 |

### 性能用例 (Performance)

| ID | 场景 | 预期 | 描述 |
|----|------|------|------|
| T07 | 1000 items | < 100ms | 批量处理 |

## 4. Performance Considerations (性能考虑)

- **时间复杂度**: O(?)
- **空间复杂度**: O(?)
- **瓶颈分析**: [描述可能的性能瓶颈]

## 5. Error Handling (错误处理)

| 错误类型 | 触发条件 | 处理方式 |
|----------|----------|----------|
| ValidationError | 参数无效 | 返回明确错误信息 |
| TimeoutError | 处理超时 | 重试或降级 |

## 6. Implementation Notes (实现备注)

- 注意事项 1: [描述]
- 注意事项 2: [描述]

---

**Gate Check**: 
- [ ] Function Spec 完整
- [ ] Test Spec 完整
- [ ] 可直接转化为 design.md
