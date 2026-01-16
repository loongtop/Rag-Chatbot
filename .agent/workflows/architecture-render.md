---
description: Render architecture documents from registry to body (optional)
version: v0.6.3
---

# /architecture-render

从 architecture-registry 块渲染文档 Body（可选工作流）。

## 说明

与 `/requirements-render` 类似，此工作流从架构文档的 `architecture-registry` 块渲染可读的文档正文部分。

**适用场景**：
- Registry 更新后需要重新渲染 Body
- 从 Registry 生成 OpenAPI/Swagger 规范
- 生成架构决策日志 (ADR)

## 前置条件

- 架构文档 `— BEGIN REGISTRY —` 块已填写

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `source_path` | string | `docs/architecture` | 输入目录 |
| `output_type` | string | `body` | `body` / `openapi` / `adr` |

## 渲染类型

### 1. body (默认)

渲染文档 `— END REGISTRY —` 之后的 Body 部分。

```markdown
## — BEGIN REGISTRY —
```architecture-registry
...
`` `
## — END REGISTRY —

<!-- 以下由 /architecture-render 生成 -->

## 1. 决策概览

| ID | Statement | Rationale |
|----|-----------|-----------|
| ARCH-DB-001 | 使用 pgvector | 满足向量检索需求 |
...
```

### 2. openapi

从 `api-spec.md` 生成 OpenAPI 3.0 规范。

**输出**: `docs/architecture/openapi.yaml`

```yaml
openapi: 3.0.3
info:
  title: RAG Chatbot API
  version: 1.0.0
paths:
  /api/chat:
    post:
      summary: RAG 问答
      ...
```

### 3. adr (Architecture Decision Records)

从所有 ARCH-* 条目生成 ADR 文件。

**输出**: `docs/adr/ADR-*.md`

```
docs/adr/
├── ADR-001-vector-database.md    # 来自 ARCH-DB-001
├── ADR-002-embedding-model.md    # 来自 ARCH-FL-001
└── ...
```

## 执行流程

```
1. 解析源文件 architecture-registry 块
   ↓
2. 根据 output_type 选择渲染器
   ↓
3. 生成输出
   - body: 更新源文件 Body 部分
   - openapi: 生成 openapi.yaml
   - adr: 生成 ADR-*.md 文件
   ↓
4. 验证输出格式
```

## 使用示例

```bash
# 渲染文档 Body
/architecture-render

# 生成 OpenAPI 规范
/architecture-render output_type=openapi

# 生成 ADR 文件
/architecture-render output_type=adr
```

## OpenAPI 映射规则

| architecture-registry 字段 | OpenAPI 字段 |
|---------------------------|--------------|
| `items[].id` | `operationId` |
| `items[].statement` | `summary` |
| `items[].sources[].path` | `x-requirement-ref` |
| (从模板提取) endpoints | `paths.*.methods` |

## ADR 模板

```markdown
# ADR-{{NNN}}: {{Title}}

## Status

Accepted

## Context

{{从 sources 提取的需求描述}}

## Decision

{{statement}}

## Rationale

{{rationale}}

## Consequences

- Positive: {{benefits}}
- Negative: {{tradeoffs}}

## References

{{sources 列表}}
```

## 与其他工作流的关系

```
/architecture-generate
    ↓ 生成 Registry
/architecture-render
    ↓ 渲染 Body/OpenAPI/ADR
/architecture-validate
    ↓ 验证追溯性
/spec
```
