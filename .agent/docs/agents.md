# Agent Collaboration

八大 Agent 协作模型：专业分工，产物驱动。

---

## Agent Roster

| Agent | Phase | Role | Trigger |
|-------|-------|------|---------|
| **Requirements Split** | Decomposition | 可拆分性分析 & 溯源门禁 | before writing requirements/interfaces |
| **Architect** | Decomposition | 需求分析 & 任务分解 | charter.yaml exists |
| **Architecture Generator** | Architecture | 技术架构设计 (v0.6.3) | L2 + interfaces done |
| **Spec** | Spec | 实现规格拆分（递归到 leaf） | Architecture done |
| **Designer** | Transition | 详细设计（可选） | leaf Spec ready (or legacy L3 done) |
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
- 提取需求，分解需求文档层级 (L0→L1→L2)
- 在 L2 统一定义模块间接口契约：`docs/L2/interfaces.md`
- 输出: requirements.md, subtasks.md, interfaces.md (L2)

### Spec
- 将 L2 Requirements 分解为可实现的 Spec 树（直到 leaf）
- 输出: `specs/SPEC-*.md` + `specs/spec-tree.md`
- 门禁: leaf Spec 必须“可直接写代码”，且 100% 可追溯到 `REQ-L2-*`

### Designer
- 为 leaf Spec（或 legacy L3）创建详细设计（必要时）
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
- 自底向上验证 (leaf Spec→L2→L1→L0，L3 为 legacy)
- 输出: integration_report.md

---

## Communication Protocol

```
Requirements Split ──split-report──► Architect ──L2+IFC──► Architecture Generator
                                                                    │
                                                               architecture
                                                                    │
                                                                    ▼
                                                                  Spec ──leaf specs──► Coder
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

## 并行执行（Multi-Module Development）

**规则**：
- 单个 Agent 实例**每次只处理一个 Module/Feature**
- 多人/多 Agent 实例可并行处理**不同**模块
- 每个并行分支需独立维护 `execution-tracker.md`
- L1 集成门禁统一验证所有模块后通过

```
模块 A (Auth) execution-tracker ─┐
模块 B (Cart) execution-tracker ─┼─► 并行开发 → L1 统一集成门禁
模块 C (Payment) execution-tracker ─┘
```

**限制**：
- ❌ 单个 Agent 不应同时处理多个模块
- ✅ 多人协作时可并行，每个负责独立模块
- ⚠️ 并行开发的模块需独立验收后统一集成

---
