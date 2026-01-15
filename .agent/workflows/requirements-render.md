---
description: Render requirements document body and appendices from Registry block
---

# /requirements-render Workflow

> ⚠️ **重要说明**: 此工作流描述了复杂的数据转换逻辑，推荐实现为 CLI 工具（如 `caf-render`）。LLM 应仅调用工具，而非直接执行此逻辑。

## 使用方式

```
/requirements-render <layer> [path]
```

**Arguments:**
- `layer`: L0 | L1 | L2 | L3
- `path`: (可选) 文档路径，省略时使用默认位置

## 推荐 CLI 实现

```bash
# 推荐使用专用 CLI 工具
caf-render --layer L0 --input docs/L0/requirements.md
caf-render --layer L1 --input docs/L1/chat-widget/requirements.md

# 或通过 Python 脚本调用
python -m caf.tools.render requirements.md --output docs/L0/requirements.md
```

## 核心逻辑

### 1. 读取 Registry 块

从 requirements.md 中提取 `requirements-registry` 代码块。

### 2. 生成内容

基于 Registry 数据生成文档正文和附录：

| 章节 | 内容 |
|------|------|
| §1 Introduction | 项目信息、来源 |
| §2 Overall Description | 需求来源汇总 |
| §3 Specific Requirements | 需求摘要 |
| 附录 A | 需求表格 |
| 附录 B | 溯源矩阵 |
| 附录 C | TBD 表格 |
| 附录 D | 接口表格（L1/L2） |

### 3. 写入规则

1. 找到 `<!-- GENERATED CONTENT BELOW -->` 标记
2. 替换该标记之后、Gate Check 之前的**所有内容**
3. **保留** Registry 块和显式标记为可编辑的部分

## 注意事项

- 生成内容标记为 `<!-- GENERATED -->`，手动编辑会被覆盖
- 重新运行会覆盖所有生成内容
- 手动编辑仅限 Registry 块和显式标记的可编辑区域
