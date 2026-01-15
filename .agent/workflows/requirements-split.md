---
description: Create split-report.md before generating requirements/interfaces
---

# /requirements-split

在生成下一层 `requirements.md` / `interfaces.md` 前，根据 `traceability.mode` 决定是否产出 `split-report.md`：

| mode | 行为 |
|------|------|
| `strict` | **必须**产出 split-report 且 Gate PASS，才能进入下游 |
| `assist` | **推荐**产出，Gate FAIL 仅警告 |
| `off` | **跳过**，直接进入下游 |

split-report 用于：
- 判断上游内容是否"可拆分"为可实现/可测试需求
- 生成覆盖矩阵，保证可追溯

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

2. **读取 traceability.mode**
   - 如果 `strict`: 必须执行完整 Gate Check
   - 如果 `assist`: 生成覆盖矩阵但仅警告
   - 如果 `off`: 跳过此步骤

3. **列出上游条目清单（Source Inventory）**
   - Charter：按 YAML 路径列出关键条目（scope/metrics/constraints/...）
   - Requirements：按 `REQ-ID` 与关键段落列出

4. **逐条做拆分决策（Mapping & Split Decisions）**
   - 每条上游内容必须：
     - 映射到下游 REQ/接口，或
     - 标记 `N/A + 原因`（明确为什么不进入下游）

5. **生成覆盖矩阵（Traceability Matrix）**
   - 检查是否存在"上游遗漏"或"下游无来源新增"

6. **写入 `split-report.md`**
   - 使用模板：`.agent/templates/split-report.template.md`
   - 输出路径：`{target_dir}/split-report.md`

7. **Gate Check**
   - 通过后将 `split-report.md` 的 `status` 设为 `done`
   - 若 FAIL（strict 模式）：先补齐上游澄清/TBD，再进入下游
   - 若 FAIL（assist 模式）：警告但可继续

## 使用示例

```
/requirements-split source_path=charter.yaml target_dir=docs/L0
```

```
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L1/chat-widget
```
/requirements-split source_path=charter.yaml target_dir=docs/L0
```

```
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L1/chat-widget
```
