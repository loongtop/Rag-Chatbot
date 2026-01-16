---
description: Decompose L2 requirements into a recursive implementation Spec tree until leaf specs are directly codable
---

# /spec

将 **需求文档层（L0-L2）** 连接到 **可实现规格层（Spec）**。

输入可以是：
- L2 模块需求：`docs/L2/{module}/requirements.md`
- 非 leaf 的 Spec：`specs/SPEC-xxx.md`（继续递归分解）

输出：
- `specs/` 下的 Spec 树文件（`SPEC-001.md`, `SPEC-001-A.md`, ...）
- `specs/spec-tree.md`（全局树与映射）

## 参数（可选）

- `source_path`：输入文档路径（默认：`docs/L2/{module}/requirements.md`）
- `target_dir`：输出目录（默认：`specs/`）
- `mode`：`create` | `refine`（默认：自动判断）
  - `create`：从 L2 创建顶层 Spec
  - `refine`：对非 leaf Spec 继续拆分

## 入口条件（v0.6.5）

> `/spec` 是从 **需求层（L0-L2）** 到 **实现层（Spec→Code）** 的桥梁

**前置条件**：
1. L2 requirements 已完成（`docs/L2/{module}/requirements.md` 存在）
2. L2 interfaces 已定义（`docs/L2/interfaces.md` 存在）
3. **Architecture 已完成**（`docs/architecture/*.md` 存在）← v0.6.5
4. 所有 P0/P1 TBD 已解决或有明确 fallback

**触发方式**：
```bash
# 从 L2 模块开始分解
/spec source_path=docs/L2/api-server/requirements.md

# 对非 leaf Spec 继续分解
/spec source_path=specs/SPEC-001.md mode=refine
```

## Leaf 判定（必须显式检查）

一个 Spec 只有在满足以下条件时才能标记为 `leaf: true`：
- 输入/输出与错误语义明确（或明确 N/A）
- 依赖已明确（含接口契约 `docs/L2/interfaces.md` 的引用）
- 可验收：包含可执行的验收标准/测试点
- 可实现：范围可在一次小迭代/PR 内完成
- 无阻塞性 TBD（impact=H）或已给出规避方案

否则必须继续分解（生成子 Spec）。

## 过程（推荐）

1. **读取输入**
   - 若输入为 L2 requirements：聚焦“模块职责 + REQ-L2-* + 数据模型 + 依赖”
   - 若输入为 Spec：聚焦“当前 Spec 的 scope/risks/tbds/leaf checklist”

2. **建立溯源映射**
   - 每个 Spec 必须绑定至少 1 个 `REQ-L2-*`（或父 Spec）
   - 任何新增技术决策必须写在 Spec 的 `Rationale/Decisions`

3. **分解为若干 Spec（Spec 树）**
   - 优先按：Pipeline 阶段 / 数据流 / 风险点 / 组件边界分解
   - 保持 Spec 之间依赖最小化

4. **为每个 Spec 判断 leaf**
   - leaf=true → 填写“Implementation Plan + Acceptance Tests + Interfaces Impact”
   - leaf=false → 只写清范围/接口影响/子任务拆分依据，并生成子 Spec

5. **写入输出**
   - 顶层：`specs/SPEC-001.md`, `SPEC-002.md`, ...
   - 子 Spec：`SPEC-001-A.md`, `SPEC-001-B.md`, ...
   - 更新/生成：`specs/spec-tree.md`

## ID 规则（建议）

- 顶层：`SPEC-001`, `SPEC-002`, ...
- 子层：`SPEC-001-A`, `SPEC-001-B`, ...
- 更深层：`SPEC-001-A-1`, `SPEC-001-A-2`, ...

## Gate（建议）

- 非 leaf Spec：必须有明确的拆分依据与子 Spec 列表
- leaf Spec：必须满足 Leaf 判定，并且“可直接写代码”（不需要再发明需求）
