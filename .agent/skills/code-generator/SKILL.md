---
name: "code-generator"
description: "根据 design.md 自动生成代码。当用户说\"生成代码\"、\"实现功能\"、\"写代码\"时自动触发。自动识别语言类型并遵循项目规范。"
trigger_keywords:
  - "生成代码"
  - "实现功能"
  - "写代码"
  - "code"
---

# Code Generator Skill

根据详细设计文档自动生成代码。

## 触发条件

- `design.md` 存在且 `status=done`
- 或用户明确要求"生成代码"、"实现功能"

## 前置检查

1. 检查 `design.md` 的 `status` 是否为 `done`
2. 如果 `draft` 或 `in_progress`，提示先完成设计
3. 检查语言配置文件 `.agent/config/quality.{language}.yaml`

## 执行步骤

### 1. 读取设计文档
- 读取 `docs/L3/{function}/design.md`
- 提取算法设计、数据结构、接口定义

### 2. 确定语言和路径
- 从 `charter.yaml` 获取 `language_profile` 或 `components`
- 确定代码输出路径（`src/` 或 `apps/{component}/`）

### 3. 应用代码规范

读取对应语言配置：
- `.agent/config/quality.python.yaml`（Python）
- `.agent/config/quality.java.yaml`（Java）
- `.agent/config/quality.cpp.yaml`（C++）
- `.agent/config/quality.swift.yaml`（Swift）

> **注意**: 根据 `charter.yaml` 的 `language_profile` 或 `components[*].language_profile` 选择对应配置。

应用规范：
- 类型注解要求
- 文档字符串要求
- 命名规范
- 代码复杂度限制（≤ 10）

### 4. 生成代码
根据设计文档生成代码文件：
- 遵循 `{{profile.source.structure}}` 组织
- 添加类型注解
- 添加文档字符串
- 处理边界情况

### 5. 验证生成
- 运行 linter 检查格式
- 验证类型注解
- 检查复杂度

## 输出产物

- `src/**/*{{profile.source.extensions}}`
- 代码文件（.py, .ts, .java, .cpp 等）

## 输出格式

```markdown
## 代码生成结果

**生成的文件**:
- 文件路径
- 文件路径

**语言配置**: python/typescript
**代码规范**: 遵循 quality.{language}.yaml

**质量检查**:
- Linting: PASS/FAIL
- 类型检查: PASS/FAIL
- 复杂度: 符合/超标

**下一步**:
- 运行 test-generator Skill 生成测试
- 或手动 Review 代码
```
