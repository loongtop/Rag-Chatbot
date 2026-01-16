---
description: Check project progress through Charter phases
---

# /charter-status

检查项目在 Charter 两阶段流程中的进度。

## 步骤

1. **检查 Charter 冻结状态**
   ```bash
   grep "frozen:" charter.yaml
   ```

2. **检查 Phase 1 (分解阶段)**
   
   | 层级 | 检查项 | 位置 |
   |------|--------|------|
   | L0 | requirements.md, subtasks.md, split-report.md(可选) | `docs/L0/` |
   | L1 | requirements.md, subtasks.md, split-report.md(可选) | `docs/L1/*/` |
   | L2 | requirements.md, **interfaces.md**, execution-tracker.md, split-report.md(可选) | `docs/L2/` + `docs/L2/*/` |

3. **检查 Phase 1.5 (架构阶段)** ← v0.6.5
   
   | 检查项 | 位置 |
   |--------|------|
   | overview.md | `docs/architecture/` |
   | database-schema.md | `docs/architecture/` |
   | core-flows.md | `docs/architecture/` |
   | api-spec.md | `docs/architecture/` |

4. **检查 Phase 2 (Spec 阶段)**
   
   | 检查项 | 位置 |
   |--------|------|
   | SPEC-*.md, spec-tree.md | `specs/` |

5. **检查 Phase 3 (实现阶段)**
   
   | 产物 | 检查项 | 位置 |
   |------|--------|------|
   | 设计(可选) | design.md | `docs/**/` |
   | 代码 | src/**/* | 按 language_profile |
   | 测试 | tests/**/* | 按 language_profile |

6. **产物 status 枚举**
   
   | 状态 | 含义 | 下一步 |
   |------|------|--------|
   | `draft` | 草稿 | 继续编写 |
   | `ready` | leaf Spec 就绪（可实现） | Coder 开始实现 |
   | `in_progress` | 进行中 | 等待完成 |
   | `done` | 完成 | 触发下一 Agent |

7. **生成进度报告**
   ```
   Charter: frozen ✅
   Phase 1: L0 ✅ → L1 ✅ → L2 ✅
   Phase 1.5: Architecture ⏳
   Phase 2: SPEC ❌
   Phase 3: Code ❌ → Tests ❌
   ```

## 使用示例

```
/charter-status
```
