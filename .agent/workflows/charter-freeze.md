---
description: Freeze a charter to prevent requirement drift
---

# Charter Freeze Workflow

锁定 Charter 文件，防止后续流程中的需求漂移。

## 使用场景

当 charter.yaml 经过充分讨论并确认后，执行此工作流锁定 Charter。

## 执行步骤

### 0. 前置验证（必须）

执行 `/charter-validate`，只有验证通过后才能继续冻结：

```
/charter-validate
```

**判断结果**：
- ✅ **PASS** → 继续执行 Step 1
- ❌ **FAIL** → **终止冻结**，输出错误信息，要求修复 `charter.yaml` 后重试
- ⚠️ **WARNING** → 可继续，但提示用户确认是否忽略警告

> 冻结一个有问题的 Charter 会导致错误传播到整个 L0→L1→L2→L3 分解链。

### 1. 验证 Charter 完整性

// turbo
```bash
grep -E "^meta:|^objective:|^scope:|^metrics:" charter.yaml
```

### 2. 生成校验和

使用以下命令生成校验和（排除 `freeze` 区块）：

**方法 A：Python（推荐，跨平台兼容）**
```bash
python3 -c "
import yaml
import hashlib
import json
from datetime import datetime, timezone

with open('charter.yaml', 'r') as f:
    data = yaml.safe_load(f)

# 移除 freeze 区块
data.pop('freeze', None)

# 生成稳定的 JSON 表示（确保跨平台一致）
content = json.dumps(data, sort_keys=True, ensure_ascii=False)
checksum = hashlib.sha256(content.encode('utf-8')).hexdigest()
print(checksum)
"
```

**方法 B：sed（POSIX 系统）**
```bash
# 使用 Python 生成临时文件（更可靠）
python3 -c "
import yaml
import json
with open('charter.yaml') as f:
    data = yaml.safe_load(f)
data.pop('freeze', None)
with open('.charter-temp.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=True, allow_unicode=True)
"
shasum -a 256 .charter-temp.yaml | cut -d' ' -f1
rm -f .charter-temp.yaml
```

### 3. 更新冻结状态

修改 charter.yaml 中的 freeze 部分：
```yaml
freeze:
  frozen: true
  checksum: "{上一步生成的 checksum}"
  frozen_at: "{当前 ISO 8601 时间戳}"
  frozen_by: "{执行者}"
```

### 4. 验证冻结

// turbo
```bash
grep -A4 "^freeze:" charter.yaml
```

### 5. （推荐）物理只读锁定（POSIX）

在 macOS/Linux 等 POSIX 系统上，建议同步将文件设为只读，降低误改风险。

// turbo
```bash
chmod a-w charter.yaml
ls -l charter.yaml
```

## 注意事项

- 冻结前**必须**先通过 `/charter-validate` 验证
- 冻结后如需修改 Charter，使用 `/charter-unfreeze` 解冻
- 所有 Agent 在执行时应检查 `frozen: true`，若已冻结则禁止修改 Charter
- 建议在 L1 分析开始前完成冻结
- `chmod` 是本地工作区保护手段，不是强安全机制；必要时可手动恢复写权限或用 `/charter-unfreeze`
