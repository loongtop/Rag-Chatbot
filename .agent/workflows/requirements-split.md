---
description: Create split-report.md before generating requirements/interfaces
---

# /requirements-split

在生成下一层 `requirements.md` / `interfaces.md` 前，先产出 `split-report.md`，用于：
- 判断上游内容是否“可拆分”为可实现/可测试需求
- 生成覆盖矩阵，保证 100% 可追溯（Source 必填）

## 参数（可选）

- `source_path`：上游文档路径（默认：`charter.yaml`）
- `target_dir`：下游产物目录（默认：`docs/L0/`）
- `layer_from`：L0/L1/L2/L3（默认自动推断）
- `layer_to`：L0/L1/L2/L3（默认：按 target_dir 推断）
- `granularity`：structured/sentence/paragraph（默认：按层级规则）

## 步骤

1. **确定迁移阶段**
   - Charter→L0：`granularity=structured`
   - L0→L1：`granularity=sentence`
   - L1→L2：`granularity=paragraph`（必要时可细到 sentence）

2. **列出上游条目清单（Source Inventory）**
   - Charter：按 YAML 路径列出关键条目（scope/metrics/constraints/...）
   - Requirements：按 `REQ-ID` 与关键段落列出

3. **逐条做拆分决策（Mapping & Split Decisions）**
   - 每条上游内容必须：
     - 映射到下游 REQ/接口，或
     - 标记 `N/A + 原因`（明确为什么不进入下游）

4. **生成覆盖矩阵（Traceability Matrix）**
   - 检查是否存在“上游遗漏”或“下游无来源新增”

5. **写入 `split-report.md`**
   - 使用模板：`.agent/templates/split-report.template.md`
   - 输出路径：`{target_dir}/split-report.md`

6. **Gate Check**
   - 通过后将 `split-report.md` 的 `status` 设为 `done`
   - 若 FAIL：先补齐上游澄清/TBD，再进入下游 requirements/interfaces

## 使用示例

```
/requirements-split source_path=charter.yaml target_dir=docs/L0
```

```
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L1/chat-widget
```
