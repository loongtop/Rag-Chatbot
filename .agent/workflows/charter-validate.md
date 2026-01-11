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
   验证以下顶级字段存在（与 charter.template.yaml 一致）:
   - `meta` (id, name, owner, version)
   - `objective` (problems, business_goals)
   - `scope` (must_have, out_of_scope)
   - `metrics` (performance, security, stability)
   - `environments` (dev, staging, production)
   - `quality_requirements` (code, performance, security)
   - `language_profile` 或 `components`（二选一必填）

3. **验证 YAML 语法**
   ```bash
   python -c "import yaml; yaml.safe_load(open('charter.yaml'))"
   ```

4. **报告结果**
   - ✅ 通过: 所有必需字段存在且格式正确
   - ❌ 错误: 必须修复才能继续
   - ⚠️ 警告: 建议改进但不阻塞

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
