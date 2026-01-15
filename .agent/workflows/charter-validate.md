---
description: Validate charter.yaml format and completeness
---

# /charter-validate

验证 charter.yaml 的格式和完整性。

## 步骤

1. **读取 charter.yaml**
   ```bash
   cat charter.yaml
   ```

2. **检查必需字段**

   | 字段 | 类型 | 说明 |
   |------|------|------|
   | `meta` | 必填 | id, name, owner, version |
   | `objective` | 必填 | problems, business_goals |
   | `scope` | 必填 | must_have, out_of_scope |
   | `deliverables` | 必填 | mandatory 列表 |
   | `quality_requirements` | 必填 | code, performance, security |
   | `language_profile` 或 `components` | 必填 | 二选一 |
   | `metrics` | 建议 | performance, security, stability, usability |
   | `environments` | 建议 | dev, staging, production 配置 |
   | `stakeholders` | 可选 | 用户画像 |
   | `constraints` | 可选 | resource, technology_boundary |
   | `dependencies` | 可选 | external_systems, resources |
   | `risks` | 可选 | 风险及应对措施 |

3. **验证 YAML 语法**
   ```bash
   # 方式 A：Python（需要 PyYAML）
   python3 -c "import yaml; yaml.safe_load(open('charter.yaml'))"
   
   # 方式 B：yq（无 Python 依赖）
   yq eval '.' charter.yaml > /dev/null
   ```

   > **依赖说明**: `yaml.safe_load` 需要 PyYAML 库（`pip install pyyaml`）。

4. **报告结果**
   - ✅ 通过: 所有必需字段存在且格式正确
   - ❌ 错误: 缺少必需字段，必须修复
   - ⚠️ 警告: 建议补充但不阻塞（metrics, environments 等）

## 使用示例

```
/charter-validate
```

或指定路径:
```
/charter-validate charter_path=./my-project/charter.yaml
```

## 常见错误

- 缺少 `objective.problems`
- `scope.must_have` 为空
- YAML 语法错误（缩进、引号）
- 缺少 `quality_requirements` 配置
