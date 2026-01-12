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
   | L1 | requirements.md, interfaces.md, subtasks.md, split-report.md(可选) | `docs/L1/*/` |
   | L2 | requirements.md, interfaces.md, execution-tracker.md, split-report.md(可选) | `docs/L2/*/` |
   | L3 | requirements.md (含 Function Spec + Test Spec) | `docs/L3/*/` |

3. **检查 Phase 2 (实现阶段)**
   
   | 产物 | 检查项 | 位置 |
   |------|--------|------|
   | 设计 | design.md | `docs/L3/*/` |
   | 代码 | src/**/* | 按 language_profile |
   | 测试 | tests/**/* | 按 language_profile |

4. **产物 status 枚举**
   
   | 状态 | 含义 | 下一步 |
   |------|------|--------|
   | `draft` | 草稿 | 继续编写 |
   | `ready` | Function Spec 完成 | Tester 填 Test Spec |
   | `in_progress` | 进行中 | 等待完成 |
   | `done` | 完成 | 触发下一 Agent |

5. **生成进度报告**
   ```
   Charter: frozen ✅
   Phase 1: L0 ✅ → L1 ✅ → L2 ⏳ → L3 ❌
   Phase 2: Design ❌ → Code ❌ → Tests ❌
   ```

## 使用示例

```
/charter-status
```
