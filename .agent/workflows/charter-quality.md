---
description: Run quality gates on generated code
---

# /charter-quality

运行质量门禁检查。

## 步骤

// turbo-all

0. **读取语言配置**
   - 从 `charter.yaml` 获取 `language_profile` 或 `components`
   - 加载对应的 `.agent/config/quality.{language_profile}.yaml`

1. **运行测试和覆盖率**
   ```bash
   {{profile.commands.test}}
   ```
   要求: 覆盖率 ≥ 95%

2. **运行 Linting**
   ```bash
   {{profile.commands.lint}}
   ```

3. **运行类型检查**
   ```bash
   {{profile.commands.typecheck}}  # 若为 null 则跳过
   ```

4. **运行安全扫描**
   ```bash
   {{profile.commands.security}}
   ```

5. **生成报告**
   
   | 检查项 | 状态 | 说明 |
   |--------|------|------|
   | 测试 | ✅/❌ | 测试结果 |
   | 覆盖率 | ✅/❌ | ≥95% 通过 |
   | Linting | ✅/❌ | 无错误 |
   | 类型检查 | ✅/❌ | 无错误或 N/A |
   | 安全 | ✅/❌ | 无高危 |

## 前置条件

确保已安装依赖:
```bash
{{profile.dependencies.install}}
```

## 使用示例

```
/charter-quality
```

## 质量标准

- 测试覆盖率: ≥ 95%
- 代码复杂度: ≤ 10
- 类型覆盖: 按语言要求
- 安全扫描: 无高危漏洞

## 混合语言项目

当 `charter.yaml` 定义了 `components` 时，将对每个组件分别执行质量检查。
