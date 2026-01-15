---
name: "context-injector"
description: "上下文注入工具。当用户切换模块、进入新功能上下文时自动触发。注入相关领域知识、技术约束、代码位置信息。"
trigger_keywords:
  - "切换模块"
  - "上下文"
  - "context"
  - "module"
---

# Context Injector Skill

根据当前上下文注入相关知识。

## 触发条件

- 用户提到特定模块名
- 用户切换到新功能
- 进入新的开发上下文

## 注入场景

### RAG 模块上下文
```
相关文件:
- src/rag/: RAG 核心引擎
- src/embeddings/: Embedding 相关
- tests/test_rag/: RAG 测试

技术栈:
- Python, FastAPI
- PostgreSQL + pgvector
- OpenAI/ollama LLM

关键约束:
- 检索延迟 ≤ 500ms
- 上下文 token 限制: 16k
```

### Widget 模块上下文
```
相关文件:
- apps/widget/: 前端组件
- tests/test_widget/: Widget 测试

技术栈:
- TypeScript, React
- Web Components (可选)

集成方式:
- Script 标签嵌入
- npm 包发布
```

### Admin 模块上下文
```
相关文件:
- apps/admin/: 后台管理
- tests/test_admin/: Admin 测试

技术栈:
- TypeScript, React
- 管理界面组件

功能:
- 产品 JSON 管理
- 文档上传
- 索引构建状态
```

## 执行步骤

### 1. 识别当前模块
- 从用户输入识别模块名
- 或从当前工作目录推断

### 2. 注入领域知识
- 相关文件路径
- 技术栈信息
- 关键依赖
- 性能约束

### 3. 注入代码规范
- 语言配置路径
- 代码风格要求
- 测试要求

### 4. 提供快捷命令
- 运行测试的命令
- 代码检查的命令
- 常用操作

## 输出格式

```markdown
## 上下文已切换到 {模块名}

**注入的知识**:

### 技术栈
- 语言: Python/TypeScript
- 框架: FastAPI/React
- 数据库: PostgreSQL + pgvector

### 关键文件
- 核心文件: 路径
- 测试文件: 路径
- 配置文件: 路径

### 代码规范
- 遵循: quality.{language}.yaml
- 测试覆盖率: ≥ 95%
- 类型覆盖: 100%

### 快捷命令
```bash
# 运行测试
pytest tests/test_{module}/ -v

# 代码检查
ruff check src/{module}/

# 完整质量检查
/charter-quality
```
```

## 使用示例

```
用户: "切换到 RAG 模块"
→ context-injector Skill
→ 注入 RAG 相关上下文
→ 用户可以继续开发
```
