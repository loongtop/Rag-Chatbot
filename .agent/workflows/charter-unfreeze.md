---
description: Unfreeze a charter to allow modifications
---

# Charter Unfreeze Workflow

解锁已冻结的 Charter 文件，允许修改需求。

## 使用场景

当需要修改已冻结的 charter.yaml 时使用。

> ⚠️ **警告**: 解冻后修改 Charter 可能导致已完成工作与新需求不一致。请谨慎使用。

## 执行步骤

### 1. 确认当前状态

// turbo
```bash
grep -A4 "^freeze:" charter.yaml
```

### 2. 验证解冻必要性

在解冻前，请确认：
- [ ] 确实需要修改 Charter 内容
- [ ] 已评估对现有工作的影响
- [ ] 已备份当前 charter.yaml

### 3. 执行解冻

修改 charter.yaml 中的 freeze 部分：
```yaml
freeze:
  frozen: false
  checksum: ""
  frozen_at: ""
  frozen_by: ""
```

### 4. 进行必要修改

修改 charter.yaml 的相关内容。

### 5. 重新冻结

修改完成后，执行 `/charter-freeze` 重新锁定。

## 最佳实践

- 解冻后尽快完成修改并重新冻结
- 记录修改原因和影响范围
- 通知相关团队成员需求变更
