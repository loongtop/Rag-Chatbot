# Agent Collaboration

七大 Agent 协作模型：专业分工，产物驱动。

---

## Agent Roster

| Agent | Phase | Role | Trigger |
|-------|-------|------|---------|
| **Requirements Split** | Decomposition | 可拆分性分析 & 溯源门禁 | before writing requirements/interfaces |
| **Architect** | Decomposition | 需求分析 & 任务分解 | charter.yaml exists |
| **Designer** | Transition | L3 详细设计 | requirements.md (L3) done |
| **Coder** | Implementation | 代码生成 | design.md done |
| **Tester** | Implementation | 测试生成 | src/*{{profile.source.extensions}} exists |
| **Reviewer** | Implementation | 代码审查 | tests passed |
| **Integrator** | Implementation | 集成验证 | all subtasks done |

---

## Responsibilities

### Requirements Split
- 在 Charter→L0、L0→L1、L1→L2 迁移前执行
- 输出: split-report.md（覆盖矩阵、拆分决策、TBD）
- 门禁: 下游每条需求/接口必须带 Source，可追溯到上游

### Architect
- 提取需求，分解任务 (L0→L1→L2→L3)
- 定义模块间接口
- 输出: requirements.md, interfaces.md, subtasks.md

### Designer
- 为 L3 函数创建详细设计
- 定义算法、数据结构、测试用例
- 输出: design.md

### Coder
- 根据 design.md 生成代码
- 添加类型注解和文档
- 输出: src/**/*{{profile.source.extensions}}

### Tester
- 生成全面测试 (95%+ 覆盖)
- 覆盖正常、边界、异常情况
- 输出: tests/**/*{{profile.test.extensions}}

### Reviewer
- 代码质量审查
- 安全扫描、性能分析
- 输出: review_report.md

### Integrator
- 模块集成测试
- 自底向上验证 (L3→L2→L1→L0)
- 输出: integration_report.md

---

## Communication Protocol

```
Requirements Split ──split-report──► Architect ──artifacts──► Designer ──artifacts──► Coder
                                                   │
                                              artifacts
                                                   │
                                                   ▼
Integrator ◄──artifacts── Reviewer ◄──artifacts── Tester
```

**规则**:
- Agent 之间**不直接调用**
- 通过**产物状态**触发
- 只有 `status=done` 的产物才能触发下游

---

## Parallel Execution

独立的 L1 功能可并行开发：

```
Feature A (Auth)    ─┐
Feature B (Cart)    ─┼─► Parallel Development
Feature C (Payment) ─┘
```
