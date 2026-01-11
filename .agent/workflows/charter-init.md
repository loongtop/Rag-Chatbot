---
description: Initialize a new Charter Framework project
---

# /charter-init

初始化一个新的 Charter Framework 项目。

## 步骤

1. **创建项目目录结构**
   ```bash
   mkdir -p docs/L0 src tests
   ```

2. **复制 Charter 模板**
   ```bash
   cp charter.template.yaml charter.yaml
   ```
   或创建新的 `charter.yaml`，包含以下必填字段:
   - `meta` - 项目元信息
   - `objective` - 核心目标
   - `scope` - 功能范围
   - `metrics` - 成功指标
   - `environments` - 环境配置
   - `quality_requirements` - 质量要求
   - `language_profile` 或 `components` - 语言配置（二选一）

3. **创建初始文档**
   - 在 `docs/L0/` 创建 `requirements.md`

4. **提示用户**
   - 编辑 `charter.yaml` 填写项目详情
   - 运行 `/charter-validate` 验证格式

## 使用示例

```
/charter-init
```

然后按提示编辑 charter.yaml。
