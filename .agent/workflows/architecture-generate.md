---
description: Generate architecture design documents from L2 requirements and interfaces
version: v0.6.3
---

# /architecture-generate

从 L2 需求和接口定义生成架构设计文档。

## 前置条件

- `docs/L2/*/requirements.md` 已生成
- `docs/L2/interfaces.md` 已生成
- `charter.yaml` 存在且 `frozen: true`

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `type` | string | `all` | `all` / `overview` / `database` / `flows` / `api` |
| `target_dir` | string | `docs/architecture` | 输出目录 |

## 执行流程

```
1. 验证前置条件
   ↓
2. 读取 L2 需求和接口
   - docs/L2/*/requirements.md
   - docs/L2/interfaces.md
   ↓
3. 读取配置
   - charter.yaml#constraints.technology_boundary
   - .agent/config/architecture-defaults.yaml (可选)
   ↓
4. 生成架构文档
   - overview.md (组件边界、部署、信任边界)
   - database-schema.md (ER、表、索引)
   - core-flows.md (RAG Pipeline、业务流)
   - api-spec.md (鉴权、错误码、端点)
   ↓
5. Gate Check
   - [ ] 所有 ARCH-* 有 sources[]
   - [ ] sources 指向有效 REQ-* 或 IFC-*
   ↓
6. 输出结构
   docs/architecture/
   ├── overview.md
   ├── database-schema.md
   ├── core-flows.md
   └── api-spec.md
```

## 模板引用

| 输出 | 模板 |
|------|------|
| overview.md | `.agent/templates/architecture.overview.template.md` |
| database-schema.md | `.agent/templates/architecture.database-schema.template.md` |
| core-flows.md | `.agent/templates/architecture.core-flows.template.md` |
| api-spec.md | `.agent/templates/architecture.api-spec.template.md` |

## ARCH-ID 命名规则

| 前缀 | 说明 |
|------|------|
| `ARCH-OV-*` | Overview 决策 |
| `ARCH-DB-*` | Database 决策 |
| `ARCH-FL-*` | Core Flows 决策 |
| `ARCH-API-*` | API Spec 决策 |

## 配置参数 (architecture-defaults.yaml)

```yaml
# 可在项目级覆盖的参数
embedding:
  dim: 1536                    # {{embedding.dim}}
  model: "text-embedding-ada-002"  # {{embedding.model}}

chunking:
  strategy: "recursive"        # {{chunking.strategy}}
  size: 500                    # {{chunking.size}}
  overlap: 50                  # {{chunking.overlap}}

vector:
  index_type: "hnsw"           # {{vector.index_type}}
  distance: "cosine"           # {{vector.distance}}
```

## 使用示例

```bash
# 生成全部架构文档
/architecture-generate

# 仅生成数据库设计
/architecture-generate type=database

# 指定输出目录
/architecture-generate target_dir=docs/design
```

## Gate Check 规则

```python
def gate_check(architecture_docs):
    errors = []
    
    for doc in architecture_docs:
        registry = parse_architecture_registry(doc)
        for item in registry.items:
            # 1. 必须有 sources
            if not item.sources:
                errors.append(f"{item.id}: missing sources[]")
            
            # 2. sources 必须有效
            for source in item.sources:
                if not source_exists(source.path):
                    errors.append(f"{item.id}: invalid source {source.id}")
    
    return len(errors) == 0, errors
```

## 输出示例

```
## 执行摘要

**命令**: /architecture-generate
**输入**:
  - docs/L2/api-server/requirements.md (12 REQs)
  - docs/L2/chat-widget/requirements.md (6 REQs)
  - docs/L2/admin-dashboard/requirements.md (4 REQs)
  - docs/L2/interfaces.md (4 IFCs)

**输出**:
  - docs/architecture/overview.md (5 ARCH-OV-*)
  - docs/architecture/database-schema.md (7 ARCH-DB-*)
  - docs/architecture/core-flows.md (8 ARCH-FL-*)
  - docs/architecture/api-spec.md (6 ARCH-API-*)

**Gate Check**: ✅ PASS
**下一步**: /architecture-validate 或 /spec
```
