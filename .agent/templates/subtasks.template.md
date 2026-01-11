---
status: draft
owner: architect
parent_task: {parent_task_name}
layer: L0 | L1 | L2
---

# Subtasks for: {parent_task_name}

## 分解策略 (Decomposition Strategy)

本任务从 **L{X}** 分解为 **L{X+1}** 层，分解依据：
- [ ] 按功能模块分解
- [ ] 按数据流分解
- [ ] 按依赖关系分解

---

## 子任务列表 (Subtasks)

### Subtask 1: {subtask_name_1}

**路径**: `docs/L{X+1}/{subtask_name_1}/`

**职责**: 
- 描述这个子任务的主要功能

**输入**:
- 来自: {parent_task_name}
- 数据: {...}

**输出**:
- 产物: requirements.md, interfaces.md
- 触发: Subtask 2 (依赖关系)

**状态**: ⬜ 未开始 / 🟡 进行中 / ✅ 已完成

---

### Subtask 2: {subtask_name_2}

**路径**: `docs/L{X+1}/{subtask_name_2}/`

**职责**: 
- 描述这个子任务的主要功能

**输入**:
- 来自: Subtask 1
- 数据: {...}

**输出**:
- 产物: requirements.md, interfaces.md
- 触发: Subtask 3 (依赖关系)

**状态**: ⬜ 未开始 / 🟡 进行中 / ✅ 已完成

---

### Subtask 3: {subtask_name_3}

**路径**: `docs/L{X+1}/{subtask_name_3}/`

**职责**: 
- 描述这个子任务的主要功能

**输入**:
- 来自: Subtask 2
- 数据: {...}

**输出**:
- 产物: requirements.md, interfaces.md
- 触发: (无，叶子节点)

**状态**: ⬜ 未开始 / 🟡 进行中 / ✅ 已完成

---

## 依赖关系图 (Dependency Graph)

```
Subtask 1
    ↓
Subtask 2
    ↓
Subtask 3
```

---

## 集成策略 (Integration Strategy)

当所有子任务完成后：
1. 集成测试: [描述测试方案]
2. 验收标准: [描述验收条件]
3. 上报至: {parent_task_name}
