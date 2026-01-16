---
name: "master"
description: "Charter Agent Framework 主入口 Skill。当用户提到项目、需求、代码、测试、审查、集成等相关意图时自动触发。智能路由到正确的 Workflow 或 Subagent。"
---

# Charter Framework Orchestrator Skill

你是 Charter Agent Framework 的智能协调者。当你被触发时，分析用户意图并调用相应能力。

## 智能路由规则

根据用户输入自动判断：

| 意图 | 前置条件 | 行动 |
|------|----------|------|
| 开始项目 | 无 | 引导 `/charter-init` |
| 验证 charter | charter.yaml 存在 | `/charter-validate` |
| 冻结需求 | charter.yaml 存在 | `/charter-freeze` |
| 分解需求 | frozen=true | requirements-split → architect |
| **技术架构** | L2 status=done | **architecture-generator Skill** |
| 详细设计 | L3 status=done | designer |
| 实现代码 | design.md status=done | code-generator Skill |
| 编写测试 | 代码已实现 | test-generator Skill |
| 代码审查 | 测试已通过 | quick-check Skill |
| 系统集成 | 所有模块完成 | integrator Agent |
| 质量检查 | 模块完成 | `/charter-quality` |
| 查看进度 | 项目存在 | `/charter-status` |

## 核心工作流

### 新项目启动
1. 检查 .agent/ 目录
2. 检查 charter.yaml
3. 引导: /charter-init → /charter-validate → /charter-freeze

### 需求分解流程
1. 检查 charter.frozen == true
2. 如果 false: 提示先 /charter-freeze
3. 如果 true: requirements-split → architect

### TDD 实现流程
1. 检查 design.md status == done
2. 如果 false: 提示 Designer 尚未完成
3. 如果 true: code-generator Skill → test-generator Skill

### 代码审查流程
1. 检查代码是否存在
2. 调用 quick-check Skill (lint + security + complexity)
3. 返回审查结果

## 模式判断

根据上下文判断使用哪种模式：

| 场景 | 使用 Agent | 使用 Skill | 说明 |
|------|-----------|-----------|------|
| 需求分解 | ✅ | ❌ | 创造性工作，依赖 LLM 理解 |
| 详细设计 | ✅ | ❌ | 需要理解业务逻辑 |
| 代码生成 | ❌ | ✅ | 确定性工作，按模板生成 |
| 测试生成 | ❌ | ✅ | 确定性工作，按 Spec 生成 |
| Linting | ❌ | ✅ | 确定性检查工具 |
| 安全扫描 | ❌ | ✅ | 确定性扫描工具 |
| 模块集成 | ✅ | ❌ | 需要理解模块间关系 |
| 端到端测试 | ✅ | ❌ | 需要理解完整系统 |

**简单判断**：
- 需要"创造"或"理解"→ Agent
- 有明确规则/模板→ Skill

---

# 分解路径决策流程图

```
                    ┌─────────────────┐
                    │  /requirements  │
                    │     -split      │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ granularity=?   │
                    │ (auto/default)  │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
│ granularity   │   │ granularity   │   │ granularity   │
│    = auto     │   │    = full     │   │   = medium    │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        │         ┌─────────▼─────────┐         │
        │         │ 评估复杂度 (Auto)  │         │
        │         └─────────┬─────────┘         │
        │                   │                   │
        │    ┌──────────────┼──────────────┐    │
        │    │              │              │    │
        │    ▼              ▼              ▼    │
        │ [High]        [Medium]        [Low]  │
        │    │              │              │    │
        │    ▼              │              │    │
        │ L0→L1→L2→L3       │              │    │
        │    │              │              │    │
        │    │              ▼              │    │
        │    │        L0→L2→L3             │    │
        │    │              │              │    │
        │    │              │              ▼    │
        │    │              │        L0→L3      │
        │    │              │              │    │
        │    │              │              │    │
        ▼    ▼              ▼              ▼    ▼
    ┌───────────────────────────────────────────────┐
    │           生成 requirements.md                │
    └───────────────────────────────────────────────┘
```

## 分解产物对比

| 粒度 | L0 | L1 | L2 | L3 | 典型产物数 |
|------|----|----|----|----|-----------|
| full | ✅ | ✅ (features) | ✅ (modules) | ✅ (functions) | 10-20 |
| medium | ✅ | ❌ | ✅ (modules) | ✅ (functions) | 5-10 |
| light | ✅ | ❌ | ❌ | ✅ (functions) | 2-5 |
| direct | ✅ | ❌ | ❌ | ❌ | 1 |

**medium/light 模式说明**:
- L1 层"功能"直接体现在 L2/L3 的 requirements.md 中
- 仍保持 Charter → 需求的追溯性
- `REQ-L0-001` 可直接追溯到 `REQ-L3-001`（跨层链接）

## 组件级分解策略（v0.5.2 新增）

可在 `charter.yaml#components` 中为每个组件指定分解策略：

```yaml
# charter.yaml 示例
components:
  - name: "api-server"
    language_profile: python
    decomposition_strategy: "full"    # L0→L1→L2→L3
  - name: "chat-widget"
    language_profile: typescript
    decomposition_strategy: "full"    # L0→L1→L2→L3
  - name: "admin-dashboard"
    language_profile: typescript
    decomposition_strategy: "full"    # L0→L1→L2→L3
```

**策略优先级**：
```
1. components[].decomposition_strategy  # 组件级配置（最高）
2. granularity 参数                     # 命令行参数
3. auto 自动评估                        # 默认行为
```

**分解策略说明**：

| 策略 | 分解路径 | 适用场景 |
|------|----------|----------|
| `full` | L0→L1→L2→L3 | 复杂组件（API/Widget/Admin） |
| `medium` | L0→L2→L3 | 中等复杂度组件 |
| `light` | L0→L3 | 简单组件/工具模块 |
| `direct` | L0→代码 | 胶水代码/配置 |

**自动推断规则**（当 components 未指定策略时）：

| 组件特征 | 默认策略 |
|----------|----------|
| 涉及 RAG/LLM/多模块协作 | `full` |
| 涉及语音/多语言/多模态 | `full` |
| 纯 CRUD 管理功能 | `medium` |
| 单一工具函数 | `light` |
| 配置/胶水代码 | `direct` |

## 组件接口矩阵（v0.5.2 新增）

定义各组件之间的接口依赖关系，用于 L1 层级分解：

| 组件 | 提供接口 | 依赖接口 | 说明 |
|------|----------|----------|------|
| api-server | REST API, RAG Service | LLM Provider, pgvector | 后端核心服务 |
| chat-widget | Widget UI, Voice IO | api-server REST API | 前端交互组件 |
| admin-dashboard | Admin UI, KB Management | api-server REST API | 后台管理界面 |

**接口类型说明**：
- `REST API`: HTTP JSON 接口
- `RAG Service`: 内部检索增强生成服务
- `Widget UI`: 前端组件接口
- `Voice IO`: 语音输入输出接口
- `LLM Provider`: 大模型调用接口
- `pgvector`: 向量数据库接口

## 输出格式

完成后返回结构化摘要：

```markdown
## 执行摘要

**触发的操作**: 列表
**生成的产物**: 文件路径
**门禁状态**: PASS/FAIL
**下一步建议**: 建议列表
```
