---
status: draft
owner: architect
layer: L2
parent: L1/{parent_feature}
---

# L2 Requirements: {module_name}

## 1. Module Overview (模块概述)

简述此模块的核心职责和在系统中的位置。

## 2. Features (功能列表)

### Feature 2.1: {feature_name}
- **描述**: 功能说明
- **优先级**: P0 / P1 / P2
- **状态**: ⬜ 未开始 / 🟡 进行中 / ✅ 已完成

### Feature 2.2: {feature_name}
- **描述**: 功能说明
- **优先级**: P0 / P1 / P2
- **状态**: ⬜ 未开始 / 🟡 进行中 / ✅ 已完成

## 3. Interfaces (接口定义)

### 对外接口 (Public API)

```
function_name(param1: Type, param2: Type) -> ReturnType
    描述: 功能说明
    参数: 参数说明
    返回: 返回值说明
    异常: 可能抛出的异常
```

### 内部接口 (Internal)

```
_internal_function(param: Type) -> ReturnType
```

## 4. Data Models (数据模型)

```
struct/class ModelName:
    field1: Type  # 说明
    field2: Type  # 说明
```

## 5. Dependencies (依赖关系)

### 外部依赖
- 第三方库: [名称, 版本, 用途]

### 内部依赖
- 模块: [描述依赖关系]

## 6. Execution Tracker (执行追踪)

| 子任务 | 路径 | 状态 | 负责 Agent | 备注 |
|--------|------|------|------------|------|
| Subtask 1 | `docs/L3/...` | ⬜ | architect | |
| Subtask 2 | `docs/L3/...` | ⬜ | architect | |

## 7. Integration Points (集成点)

- 与 {其他模块} 的集成方式: [描述]
- 集成测试策略: [描述]
