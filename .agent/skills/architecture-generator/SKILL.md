---
name: architecture-generator
description: |
  从 L2 需求和接口定义生成架构设计文档。
  当用户说"生成架构"、"技术设计"、"数据库设计"时自动触发。
  输出 docs/architecture/ 目录下的设计文档。
version: v0.6.3
trigger_keywords:
  - "生成架构"
  - "技术设计"
  - "设计数据库"
  - "架构设计"
  - "generate architecture"
  - "design database"
---

# Architecture Generator Skill

## 概述

在 L2 需求分解完成后、`/spec` 之前，生成技术架构设计文档。

**Phase 1.5: Architecture** - 将"怎么做"固化为可校验的产物。

```
Charter → L0 → L1 → L2 → [Architecture] → /spec → Code
```

## 触发条件

- 用户说"生成架构"、"技术设计"、"设计数据库"
- 或 L2 分解完成后自动提示

## 前置条件

在执行此 Skill 前，必须满足：

- [x] `docs/L2/*/requirements.md` 已生成
- [x] `docs/L2/interfaces.md` 已生成
- [x] `charter.yaml` 存在且 `frozen: true`

## 输入

| 文件 | 用途 |
|------|------|
| `charter.yaml` | 项目约束、技术栈、组件定义 |
| `docs/L2/*/requirements.md` | L2 组件需求 |
| `docs/L2/interfaces.md` | 组件间接口定义 |

## 输出

| 文件 | 说明 |
|------|------|
| `docs/architecture/overview.md` | 系统概览：组件边界、部署拓扑、信任边界 |
| `docs/architecture/database-schema.md` | 数据库设计：实体模型、索引策略、迁移版本 |
| `docs/architecture/core-flows.md` | 核心流程：RAG Pipeline、业务流程 |
| `docs/architecture/api-spec.md` | API 详细规范：从 IFC-* 扩展 |

## 架构 Registry 格式

每个架构文件必须包含 `architecture-registry` 块：

```yaml
architecture-registry:
  schema_version: "v0.6.3"
  type: "overview"  # overview | database | flows | api
  
  items:
    - id: ARCH-OV-001
      statement: "系统采用前后端分离架构"
      sources:
        - id: "IFC-CHAT-API"
          path: "docs/L2/interfaces.md#IFC-CHAT-API"
      rationale: "支持独立部署和扩展"
      
    - id: ARCH-DB-001
      statement: "使用 PostgreSQL + pgvector 存储向量"
      sources:
        - id: "REQ-L2-API-001"
          path: "docs/L2/api-server/requirements.md#REQ-L2-API-001"
      rationale: "满足 RAG 检索需求"
```

## ID 命名规则

| 前缀 | 说明 |
|------|------|
| `ARCH-OV-*` | Overview 决策 |
| `ARCH-DB-*` | Database 决策 |
| `ARCH-FL-*` | Core Flows 决策 |
| `ARCH-API-*` | API Spec 决策 |

## 执行流程

```
1. 读取 L2 需求和接口定义
   ↓
2. 分析技术栈约束 (charter.yaml#constraints.technology_boundary)
   ↓
3. 生成 docs/architecture/overview.md
   ↓
4. 生成 docs/architecture/database-schema.md
   ↓
5. 生成 docs/architecture/core-flows.md
   ↓
6. 从 IFC-* 扩展生成 docs/architecture/api-spec.md
   ↓
7. Gate Check: 
   - [x] 所有 ARCH-* 有 sources[]
   - [x] sources 指向有效的 REQ-* 或 IFC-*
   - [x] 无孤立设计决策
```

## 模板引用

| 产物 | 模板 |
|------|------|
| overview.md | `.agent/templates/architecture.overview.template.md` |
| database-schema.md | `.agent/templates/architecture.database-schema.template.md` |
| core-flows.md | `.agent/templates/architecture.core-flows.template.md` |
| api-spec.md | `.agent/templates/architecture.api-spec.template.md` |

## Gate Check

执行完成后验证：

| Check | 规则 |
|-------|------|
| Sources 覆盖 | 每个 ARCH-* 必须有 `sources[]` |
| 引用有效性 | sources 指向存在的 REQ-* 或 IFC-* |
| 无孤立决策 | 不允许无来源的架构决策 |
| 技术栈一致 | 使用的技术必须在 `allowed` 列表中 |

## 示例命令

```bash
# 生成完整架构
/architecture-generate

# 仅生成数据库设计
/architecture-generate type=database

# 验证架构文档
/architecture-validate
```

## 版本历史

| 版本 | 变更 |
|------|------|
| v0.6.3 | 初始版本，增加 Phase 1.5: Architecture |
