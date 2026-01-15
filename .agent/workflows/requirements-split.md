---
description: Create split-report.md before generating requirements/interfaces with adaptive granularity and auto REQ-ID classification
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
- 自动分类 REQ-ID（v0.5.0 新增）

## 参数（可选）

- `source_path`：上游文档路径（默认：`charter.yaml`）
- `target_dir`：下游产物目录（默认：`docs/L0/`）
- `layer_from`：L0/L1/L2/L3（默认自动推断）
- `layer_to`：L0/L1/L2/L3（默认：按 target_dir 推断）
- `granularity`：auto/full/medium/light/direct（默认：`auto`）

## REQ-ID 自动分类规则（v0.5.0 新增）

### 分类体系

| 分类 | ID 前缀 | 适用场景 |
|------|---------|----------|
| 组件专属 | `REQ-L0-{COMP}-*` | scope 条目关联到具体组件 |
| 共享功能 | `REQ-L0-SHARED-*` | 跨组件功能（LLM 配置等） |
| 性能 | `REQ-L0-PERF-*` | 性能指标 (MET-PERF-*) |
| 安全 | `REQ-L0-SEC-*` | 安全指标 (MET-SEC-*) |
| 稳定 | `REQ-L0-STAB-*` | 稳定性指标 (MET-STAB-*) |
| 易用 | `REQ-L0-UX-*` | 易用性指标 (MET-UX-*) |
| 约束 | `REQ-L0-CON-*` | 技术/资源约束 |

### 组件映射规则

从 `charter.yaml#components` 动态生成前缀：

```yaml
# charter.yaml 示例
components:
  - name: "api-server"      → API
  - name: "chat-widget"     → WGT
  - name: "admin-dashboard" → ADM
  - name: "mobile-app"      → MOB
```

**转换算法**：
```python
def generate_prefix(component_name):
    # 规则1: 驼峰分割取首字母
    words = re.findall('[A-Z][a-z]+', component_name)
    if len(words) >= 2:
        return ''.join(w[0] for w in words).upper()[:3]
    
    # 规则2: 连字符分割取首字母
    words = component_name.split('-')
    if len(words) >= 2:
        return ''.join(w[0] for w in words).upper()[:3]
    
    # 规则3: 截取前3字符
    return component_name[:3].upper()
```

示例：
- `api-server` → `API`
- `chat-widget` → `CW`（或 `WGT`）
- `admin-dashboard` → `ADM`
- `mobile-app` → `MOB`

### Scope 条目分类逻辑

```python
def classify_scope_item(item, components, component_keywords):
    """
    分类 scope 条目到对应组件
    
    优先级:
    1. 精确匹配组件名
    2. 模糊匹配关键词
    3. 默认 SHARED
    """
    # Step 1: 构建关键词表
    keywords = {}
    for c in components:
        keywords[c.name] = [c.name]
        if hasattr(c, 'description'):
            keywords[c.name].extend(c.description.split())
    
    # Step 2: 精确匹配
    for name, kws in keywords.items():
        for kw in kws:
            if kw in item:
                return generate_prefix(name)
    
    # Step 3: 模糊匹配（常见功能词）
    function_keywords = {
        'API': ['API', '接口', '服务', '后端'],
        'WGT': ['Widget', 'widget', '前端', '交互', '语音', '多语言'],
        'ADM': ['管理', '后台', 'Admin', 'admin', '上传', '索引'],
        'SHARED': ['LLM', '配置', '登录', '邮箱', '验证码'],
    }
    for prefix, kws in function_keywords.items():
        for kw in kws:
            if kw in item:
                return prefix
    
    # Step 4: 默认 SHARED
    return "SHARED"
```

### Metrics 分类映射

| 原 ID | 分类 | 新前缀 |
|-------|------|--------|
| MET-PERF-* | 性能 | REQ-L0-PERF-* |
| MET-SEC-* | 安全 | REQ-L0-SEC-* |
| MET-STAB-* | 稳定 | REQ-L0-STAB-* |
| MET-UX-* | 易用 | REQ-L0-UX-* |

---

## 粒度模式（v0.5.0 新增）

### Granularity 参数

| 值 | 分解路径 | 适用场景 |
|---|---------|----------|
| `auto` | **自动评估**复杂度选择合适路径 | 默认，推荐 |
| `full` | L0→L1→L2→L3 | 复杂系统，多模块协作 |
| `medium` | L0→L2→L3 | 中等系统，2-3 个模块 |
| `light` | L0→L3 | 简单功能，单一模块 |
| `direct` | L0→代码 | 纯配置、胶水代码 |

### 自动评估规则

当 `granularity=auto` 时，自动评估复杂度：

```
复杂度 = {
    scope_items: len(charter.scope.must_have),
    components: len(charter.components),
    cross_deps: count_cross_module_dependencies(),
}

if scope_items > 20 OR components > 3 OR cross_deps > 2:
    granularity = "full"
elif scope_items > 10 OR components > 1:
    granularity = "medium"
else:
    granularity = "light"
```

### 产物目录结构对比

```
# full (L0→L1→L2→L3)
docs/
├── L0/requirements.md
├── L1/
│   ├── feature-a/requirements.md
│   └── feature-b/requirements.md
├── L2/
│   └── feature-a/module-x/requirements.md
└── L3/
    └── feature-a/module-x/function-y/requirements.md

# medium (L0→L2→L3)
docs/
├── L0/requirements.md
└── L2/
    └── feature-a/module-x/requirements.md
        └── L3/ (嵌套在 requirements.md 中)

# light (L0→L3)
docs/
├── L0/requirements.md
└── L3/
    └── feature-a/function-y/requirements.md

# direct (L0→代码)
docs/
└── L0/requirements.md
    └── 直接进入 code-generator
```

## 步骤

1. **确定迁移阶段与粒度**
   - 如果 `granularity=auto`：先评估复杂度
   - 否则使用指定粒度
   - 根据粒度决定 `granularity` 参数值

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
   - 跨层追溯：medium/light 模式下需建立 L0→L3 直接链接

6. **写入 `split-report.md`**
   - 使用模板：`.agent/templates/split-report.template.md`
   - 输出路径：`{target_dir}/split-report.md`

7. **Gate Check**
   - 通过后将 `split-report.md` 的 `status` 设为 `done`
   - 若 FAIL（strict 模式）：先补齐上游澄清/TBD，再进入下游
   - 若 FAIL（assist 模式）：警告但可继续

## 跨层追溯规则

当跳过 L1/L2 层时，需在 split-report 中明确跨层链接：

```markdown
## 跨层追溯 (L0 → L3)

| L0 Requirement | L3 Requirement | 链接类型 |
|----------------|----------------|----------|
| REQ-L0-001 | REQ-L3-001 | direct |
| REQ-L0-002 | REQ-L3-002 | derived |
```

## 使用示例

```bash
# 自动评估粒度（推荐）
/requirements-split source_path=charter.yaml target_dir=docs/L0

# 强制全链路分解
/requirements-split source_path=charter.yaml target_dir=docs/L0 granularity=full

# 中等分解（跳过 L1）
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L2 granularity=medium

# 轻量分解（跳过 L1/L2）
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L3 granularity=light

# 直接实现（仅 L0）
/requirements-split source_path=charter.yaml target_dir=docs/L0 granularity=direct
```

### REQ-ID 生成示例

基于以下 charter 配置：

```yaml
# charter.yaml
components:
  - name: "api-server"
  - name: "chat-widget"
  - name: "admin-dashboard"
```

**自动生成结果**：

| Scope 条目 | 判定组件 | REQ-ID |
|-----------|---------|--------|
| 嵌入式 Chatbot Widget | chat-widget | REQ-L0-WGT-001 |
| 产品数据导入与查询 | admin-dashboard | REQ-L0-ADM-001 |
| 知识库导入与索引 | admin-dashboard | REQ-L0-ADM-002 |
| RAG 问答 | api-server | REQ-L0-API-001 |
| 产品推荐 | api-server | REQ-L0-API-002 |
| 产品比较 | api-server | REQ-L0-API-003 |
| 上下文感知 | api-server | REQ-L0-API-004 |
| 对话历史管理 | api-server | REQ-L0-API-005 |
| 后台管理 UI | admin-dashboard | REQ-L0-ADM-003 |
| LLM Provider 可配置切换 | api-server | REQ-L0-API-006 |
| 人工/AI 入口切换 | api-server | REQ-L0-API-007 |
| 语音交互 | chat-widget | REQ-L0-WGT-002 |
| 多语言支持 | chat-widget | REQ-L0-WGT-003 |
| 文件/图片输入 | chat-widget | REQ-L0-WGT-004 |
| 邮箱登录（验证码） | shared | REQ-L0-SHARED-001 |

**Metrics 映射**：

| 原 ID | REQ-ID |
|-------|--------|
| MET-PERF-001 | REQ-L0-PERF-001 |
| MET-SEC-001 | REQ-L0-SEC-001 |
| MET-STAB-001 | REQ-L0-STAB-001 |
| MET-UX-001 | REQ-L0-UX-001 |

---

## 10. 自动提取 Exclusions（v0.5.1 新增）

从 `charter.yaml#scope.out_of_scope` 逐条生成 exclusions：

```yaml
# 提取规则
exclusions:
  - source:
      id: "{SCOPE-OOS-XXX}"
      path: "charter.yaml#scope.out_of_scope[{index}]"
    reason: "{out_of_scope 条目原文}"
    category: scope | deferred | superseded
```

**示例**：

| source | reason | category |
|--------|--------|----------|
| SCOPE-OOS-001 | 不做完整认证/账号体系 | scope |
| SCOPE-OOS-002 | 订单处理和支付功能 | scope |
| SCOPE-OOS-005 | 知识库自动爬取/同步 | deferred |
| SCOPE-OOS-006 | 自建 LLM 训练 | scope |

---

## 11. 自动提取 Constraints（v0.5.1 新增）

从 `charter.yaml#constraints` 自动提取所有约束：

### 资源约束

| ID | Statement | Source | Priority |
|----|-----------|--------|----------|
| REQ-L0-CON-BUDGET | 云服务月成本 < $5000 | `constraints.resource.budget` | P0 |
| REQ-L0-CON-TIMELINE | 交付截止日期: 2026-02-28 | `constraints.resource.timeline` | P0 |

### 技术约束

| ID | Statement | Source | Category |
|----|-----------|--------|----------|
| REQ-L0-CON-TECH-ALLOWED | 允许: Python, TypeScript, PostgreSQL+pgvector... | `technology_boundary.allowed` | allowed |
| REQ-L0-CON-TECH-FORBIDDEN | 禁止: 自建 LLM 训练, Pinecone, 私有化数据库 | `technology_boundary.forbidden` | forbidden |

**提取规则**：

```python
def extract_constraints(charter):
    constraints = []
    
    # 资源约束
    if "budget" in charter.constraints.resource:
        constraints.append({
            "id": "REQ-L0-CON-BUDGET",
            "statement": f"云服务月成本 < {charter.constraints.resource.budget}",
            "sources": ["constraints.resource.budget"],
            "section": "constraint"
        })
    
    if "timeline" in charter.constraints.resource:
        constraints.append({
            "id": "REQ-L0-CON-TIMELINE",
            "statement": f"交付截止日期: {charter.constraints.resource.timeline}",
            "sources": ["constraints.resource.timeline"],
            "section": "constraint"
        })
    
    # 技术约束 - allowed
    allowed_tech = charter.constraints.technology_boundary.allowed
    constraints.append({
        "id": "REQ-L0-CON-TECH-ALLOWED",
        "statement": f"允许的技术栈: {', '.join(allowed_tech)}",
        "sources": ["technology_boundary.allowed"],
        "section": "constraint"
    })
    
    # 技术约束 - forbidden
    forbidden_tech = charter.constraints.technology_boundary.forbidden
    constraints.append({
        "id": "REQ-L0-CON-TECH-FORBIDDEN",
        "statement": f"禁止: {', '.join(forbidden_tech)}",
        "sources": ["technology_boundary.forbidden"],
        "section": "constraint"
    })
    
    return constraints
```

---

## 12. TBD target_layer 智能判断（v0.5.1 新增）

基于 TBD 内容自动推荐 target_layer：

```python
def suggest_tbd_target_layer(tbd_question, impact, related_reqs):
    """
    智能判断 TBD 应该在哪个层级解决
    
    返回: "L0" | "L1" | "L2" | "L3"
    """
    
    # 规则1: 影响架构设计的高影响 TBD → L0
    architecture_keywords = ["鉴权", "架构", "安全", "技术选型", " Provider"]
    if impact == "H" and any(kw in tbd_question for kw in architecture_keywords):
        return "L0"
    
    # 规则2: 界面/Widget 相关 → L2
    ui_keywords = ["Widget", "UI", "界面", "加载", "体积", "自适应"]
    if any(kw in tbd_question for kw in ui_keywords):
        return "L2"
    
    # 规则3: 高影响 → L1
    if impact == "H":
        return "L1"
    
    # 规则4: 中低影响默认 L1
    return "L1"


def resolve_tbds(open_questions, scope_items, metrics):
    """处理所有 open_questions，生成 TBD 列表"""
    tbds = []
    
    for idx, q in enumerate(open_questions):
        question = q.get("question", "")
        
        # 从 ID 提取 impact（如 TBD-001 → 第一个，默认 M）
        impact_map = {"1": "H", "2": "M", "3": "L"}
        impact = impact_map.get(str(idx + 1)[-1], "M")
        
        # 智能判断 target_layer
        target_layer = suggest_tbd_target_layer(question, impact, [])
        
        tbds.append({
            "id": f"TBD-L0-{str(idx+1).zfill(3)}",
            "question": question,
            "sources": [{
                "id": f"TBD-{str(idx+1).zfill(3)}",
                "path": f"charter.yaml#open_questions[{idx}]"
            }],
            "impact": impact,
            "owner": "",
            "target_layer": target_layer,
            "status": "open",
            "related_reqs": []
        })
    
    return tbds
```

**判断示例**：

| TBD 问题 | 关键词 | Impact | 推荐 Layer |
|----------|--------|--------|------------|
| 后台鉴权方式 | 鉴权 + 高 | H | **L0** |
| LLM Provider/Model 选择 | Provider + 高 | H | **L0** |
| Widget 资源体积 | Widget + 体积 | L | **L2** |
| 多语言策略细节 | 多语言 + 中 | M | **L1** |

---

## 13. 多组件 Profile 处理（v0.5.1 新增）

当 `charter.yaml#components` 包含多个技术栈时：

```yaml
# charter.yaml 示例
components:
  - name: "api-server"
    language_profile: python
  - name: "chat-widget"
    language_profile: typescript
  - name: "admin-dashboard"
    language_profile: typescript

# 生成 profile
profile: ["python", "typescript"]

# 或者按组件分组
requirements:
  - id: REQ-L0-API-001
    profile: "python"      # 后端需求
    ...
  - id: REQ-L0-WGT-001
    profile: "typescript"  # 前端需求
    ...
```

**处理逻辑**：

```python
def get_profiles(charter):
    """提取所有语言 profile"""
    profiles = set()
    for c in charter.components:
        if hasattr(c, 'language_profile'):
            profiles.add(c.language_profile)
    
    if len(profiles) == 1:
        return list(profiles)[0]  # 单组件返回字符串
    else:
        return list(profiles)  # 多组件返回列表
```
