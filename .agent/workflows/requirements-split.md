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
- 自动分类 REQ-ID

## 参数（可选）

- `source_path`：上游文档路径（默认：`charter.yaml`）
- `target_dir`：下游产物目录（默认：`docs/L0/`）
- `layer_from`：L0/L1/L2（L3 为 legacy，默认自动推断）
- `layer_to`：L0/L1/L2（L3 为 legacy，默认：按 target_dir 推断）
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

## 粒度模式（v0.6.0）

### Granularity 参数

| 值 | 分解路径 | 适用场景 |
|---|---------|----------|
| `auto` | **自动评估**复杂度选择合适路径 | 默认，推荐 |
| `full` | L0→L1→L2 | 复杂系统，多模块协作 |
| `medium` | L0→L2 | 中等系统，2-3 个模块（跳过 L1） |
| `light` | L0→L1 | 简单系统（模块边界不明显时可先停在 L1） |
| `direct` | L0→L2（单模块） | 单模块项目或边界非常清晰的场景 |

### 自动评估规则

当 `granularity=auto` 时，自动评估复杂度：

```
复杂度 = {
    scope_items: len(charter.scope.must_have),
    components: len(charter.components),
    cross_deps: count_cross_module_dependencies(),
}

if scope_items > 20 OR components >= 3 OR cross_deps > 2:
    granularity = "full"  # v0.6.0: 3+ 组件强制使用 full
elif scope_items > 10 OR components > 1:
    granularity = "medium"
else:
    granularity = "light"
```

### 产物目录结构对比

```
# full (L0→L1→L2)
docs/
├── L0/requirements.md
├── L1/
│   ├── feature-a/requirements.md
│   └── feature-b/requirements.md
├── L2/
│   ├── module-x/requirements.md
│   ├── interfaces.md
│   └── execution-tracker.md
└── (然后进入 /spec 生成 leaf Specs)

# medium (L0→L2)
docs/
├── L0/requirements.md
└── L2/
    ├── module-x/requirements.md
    ├── interfaces.md
    └── execution-tracker.md
    └── (然后进入 /spec)

# light (L0→L1)
docs/
├── L0/requirements.md
└── L1/
    └── feature-a/requirements.md
    └── (再视情况进入 L2 与 /spec)

# direct (L0→L2 单模块)
docs/
└── L0/requirements.md
└── L2/
    ├── module-x/requirements.md
    └── interfaces.md
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
   - 跨层追溯：跳过中间层时需建立 L0→L2（或 L0→SPEC）直接链接

6. **写入 `split-report.md`**
   - 使用模板：`.agent/templates/split-report.template.md`
   - 输出路径：`{target_dir}/split-report.md`

7. **Gate Check**
   - 通过后将 `split-report.md` 的 `status` 设为 `done`
   - 若 FAIL（strict 模式）：先补齐上游澄清/TBD，再进入下游
   - 若 FAIL（assist 模式）：警告但可继续

8. **L1→L2 接口生成（v0.6.0）**
   > 当 `layer_to=L2` 时，**必须同时生成** `docs/L2/interfaces.md`
   
   - 识别跨模块交互（L2 modules 之间的 API/Event/Data 依赖）
   - 为每个交互点创建 `IFC-*` 条目
   - 定义契约（input/output/errors）
   - 确保每个 IFC 有至少 1 个 `sources[]` 指向 L1/L2 REQ
   - 使用模板：`.agent/templates/interfaces.L2.template.md`

## 跨层追溯规则

当跳过中间层时，需在 split-report 中明确跨层链接：

```markdown
## 跨层追溯 (L0 → L2)

| L0 Requirement | L2 Requirement | 链接类型 |
|----------------|----------------|----------|
| REQ-L0-001 | REQ-L2-001 | direct |
| REQ-L0-002 | REQ-L2-002 | derived |
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
/requirements-split source_path=docs/L0/requirements.md target_dir=docs/L1 granularity=light

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

## 10. 自动提取 Exclusions

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

## 11. 自动提取 Constraints

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

## 12. TBD target_layer 智能判断

基于 TBD 内容自动推荐 target_layer：

```python
def suggest_tbd_target_layer(tbd_question, impact, related_reqs):
    """
    智能判断 TBD 应该在哪个层级解决
    
    返回: "L0" | "L1" | "L2" | "SPEC"（或 "L3" legacy）
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

## 13. 多组件 Profile 处理

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

---

## 14. L0 → L1 分类规则（v0.6.1）

在 L0→L1 分解时，需判断每条 L0 需求的处理策略。

### 需求分类决策树

```
L0 Requirement
    │
    ├─ 业务功能 (API/ADM/SHARED) ────────→ strategy: "feature"
    │                                      创建独立 L1 Feature
    │
    ├─ 界面功能 (WGT/UI)
    │       │
    │       ├─ 有业务逻辑 ─────────────→ strategy: "feature"
    │       │   关键词: 登录/验证/切换/上传/处理
    │       │
    │       └─ 纯展示/交互 ────────────→ strategy: "direct_l2"
    │           关键词: 样式/布局/动画/加载/响应式
    │
    └─ 非功能需求 (PERF/SEC/STAB/UX/CON) ─→ strategy: "inherit"
                                           由所有 Feature 继承
```

### 判定算法

```python
def classify_l0_to_l1(l0_req):
    """
    判断 L0 需求在 L1 层的处理策略
    
    Returns:
        "feature": 创建独立 L1 Feature
        "direct_l2": 跳过 L1，直接分配到 L2 组件
        "inherit": 由所有 L1 Feature 继承
    """
    category = l0_req.id.split('-')[2]  # e.g., "WGT" from "REQ-L0-WGT-001"
    
    # Rule 1: 非功能需求 → 继承
    if category in ["PERF", "SEC", "STAB", "UX", "CON"]:
        return "inherit"
    
    # Rule 2: 业务功能 → 建 Feature
    if category in ["API", "ADM", "SHARED"]:
        return "feature"
    
    # Rule 3: 界面功能 → 二次判定
    if category in ["WGT", "UI", "FE"]:
        return classify_ui_requirement(l0_req)
    
    # Default: 建 Feature（保守策略）
    return "feature"


def classify_ui_requirement(req):
    """
    界面需求的 L1 决策
    """
    statement = req.statement
    
    # 有业务逻辑的界面需求 → 建 Feature
    business_keywords = [
        "登录", "验证", "切换", "上传", "处理", "提交",
        "认证", "授权", "配置", "管理"
    ]
    if any(kw in statement for kw in business_keywords):
        return "feature"
    
    # 纯展示/交互需求 → 直接 L2
    ui_keywords = [
        "样式", "布局", "动画", "加载", "响应式",
        "显示", "渲染", "嵌入", "集成"
    ]
    if any(kw in statement for kw in ui_keywords):
        return "direct_l2"
    
    # 默认建 Feature（保守策略）
    return "feature"
```

### split-report 必填字段

在 L0→L1 的 `split-report.md` 中，每条映射决策必须包含：

| 字段 | 说明 | 必填 | 示例 |
|------|------|------|------|
| `source` | L0 REQ-ID | ✅ | `REQ-L0-WGT-001` |
| `target` | L1 Feature 或 null | ✅ | `RAGQA` / `null` |
| `strategy` | 处理策略 | ✅ | `feature` / `direct_l2` / `inherit` |
| `rationale` | 决策理由 | ⚠️ 当 strategy≠feature 时必填 | "纯界面需求" |
| `l2_target` | L2 组件（direct_l2 时必填） | ⚠️ | `chat-widget` |

### 示例

```markdown
## 3.2 Widget Capabilities (direct_l2)

| L0 REQ-ID | Strategy | L2 Target | Rationale |
|-----------|----------|-----------|-----------|
| REQ-L0-WGT-001 | direct_l2 | chat-widget | 纯嵌入/集成需求，无业务逻辑 |
| REQ-L0-WGT-002 | feature | → L1-VOICE | 语音交互有 Provider 选择逻辑 |
| REQ-L0-WGT-003 | direct_l2 | chat-widget | 纯界面多语言切换 |
| REQ-L0-WGT-004 | feature | → L1-UPLOAD | 文件上传有格式/大小/解析逻辑 |
```

### Gate Check 增强

| Check | 规则 |
|-------|------|
| Strategy 字段 | 每条 L0→L1 映射必须有 `strategy` |
| Rationale 字段 | `direct_l2` / `inherit` 必须有 `rationale` |
| L2 Target | `direct_l2` 必须指定目标组件 |
| Coverage | 所有 L0 需求都有明确策略 |

---

## 15. Risks 映射规则（v0.6.2）

Charter 中的 `risks[]` 必须映射到 L0 层，确保风险可追溯。

### REQ-ID 前缀

| 类型 | ID 格式 | 说明 |
|------|---------|------|
| 风险缓解 | `REQ-L0-RISK-*` | 对应 charter.yaml#risks 的缓解措施 |

### 映射规则

```python
def extract_risks(charter):
    """
    将 risks 转换为风险缓解需求
    
    规则:
    - 每个 RISK-XXX 必须生成对应的 REQ-L0-RISK-XXX
    - 需求 statement 描述缓解措施（而非风险本身）
    - 原始风险描述保留在 sources 中
    """
    requirements = []
    
    for idx, risk in enumerate(charter.risks):
        risk_id = extract_id(risk)  # e.g., "RISK-001"
        mitigation = extract_mitigation(risk)  # 提取缓解措施
        
        requirements.append({
            "id": f"REQ-L0-RISK-{str(idx+1).zfill(3)}",
            "priority": "P0" if "成本" in risk or "安全" in risk else "P1",
            "statement": f"实施风险缓解: {mitigation}",
            "sources": [{
                "id": risk_id,
                "path": f"charter.yaml#risks[{idx}]"
            }],
            "section": "risk_mitigation"
        })
    
    return requirements


def extract_mitigation(risk_text):
    """
    从风险描述中提取缓解措施
    
    格式: "[RISK-XXX] 风险描述 - 缓解措施"
    """
    if " - " in risk_text:
        return risk_text.split(" - ", 1)[1]
    return risk_text
```

### 示例

| Charter Risk | REQ-ID | Statement |
|--------------|--------|-----------|
| `[RISK-001] LLM API 成本可能超出预算 - 实施 Token 用量监控、缓存与限流策略` | REQ-L0-RISK-001 | 实施风险缓解: Token 用量监控、缓存与限流策略 |
| `[RISK-004] Prompt Injection/数据外泄风险 - 输入输出过滤、引用转义...` | REQ-L0-RISK-004 | 实施风险缓解: 输入输出过滤、引用转义、最小权限、审计日志 |

### split-report 必填

| 字段 | 说明 |
|------|------|
| Section 5.6 | Risks Inventory（风险清单） |
| Section 6.4 | Risks → Requirements 映射表 |
| Section 8 | Traceability Matrix 包含 risks 行 |

---

## 16. Dependencies 映射规则（v0.6.2）

Charter 中的 `dependencies` 必须转换为可验证的依赖约束。

### REQ-ID 前缀

| 类型 | ID 格式 | 说明 |
|------|---------|------|
| 外部依赖 | `REQ-L0-DEP-*` | 必须满足的外部系统/资源依赖 |

### 映射规则

```python
def extract_dependencies(charter):
    """
    将 dependencies 转换为依赖约束需求
    """
    requirements = []
    idx = 1
    
    # External Systems
    for ext in charter.dependencies.external_systems:
        requirements.append({
            "id": f"REQ-L0-DEP-{str(idx).zfill(3)}",
            "priority": "P0",
            "statement": f"依赖外部系统: {ext}",
            "sources": [{
                "path": f"charter.yaml#dependencies.external_systems"
            }],
            "section": "dependency",
            "acceptance": [
                "依赖系统可用性验证",
                "接口契约已确认"
            ]
        })
        idx += 1
    
    # Required Resources
    for res in charter.dependencies.resources:
        requirements.append({
            "id": f"REQ-L0-DEP-{str(idx).zfill(3)}",
            "priority": "P0",
            "statement": f"依赖资源: {res}",
            "sources": [{
                "path": f"charter.yaml#dependencies.resources"
            }],
            "section": "dependency"
        })
        idx += 1
    
    return requirements
```

### 示例

| Charter Dependency | REQ-ID | Statement |
|--------------------|--------|-----------|
| 现有产品网站（提供嵌入入口） | REQ-L0-DEP-001 | 依赖外部系统: 现有产品网站（提供嵌入入口） |
| PostgreSQL（启用 pgvector 扩展） | REQ-L0-DEP-003 | 依赖资源: PostgreSQL + pgvector |

---

## 17. Data Contracts 处理（v0.6.2）

Charter 中的数据契约（如 `product_data_contract`, `widget_context_contract`）需要特殊处理。

### 处理方式

| 契约类型 | 处理方式 | 说明 |
|----------|----------|------|
| `*_contract` | → `docs/L2/interfaces.md` 的 `IFC-*` 条目 | 在 L2 层定义具体接口 |
| 或 | → TBD（若细节未确定） | 标记为待定 |

### 映射规则

```python
def extract_data_contracts(charter):
    """
    提取数据契约，转换为接口条目或 TBD
    """
    contracts = []
    
    for key in charter.keys():
        if key.endswith("_contract"):
            contract = charter[key]
            
            # 如果有足够细节 → 生成 IFC 条目
            if "minimum_fields" in contract:
                contracts.append({
                    "id": f"IFC-{key.upper()}",
                    "type": "Data",
                    "name": key,
                    "description": f"数据契约: {key}",
                    "source": f"charter.yaml#{key}"
                })
            # 否则 → 标记为 TBD
            else:
                contracts.append({
                    "type": "tbd",
                    "id": f"TBD-CONTRACT-{key.upper()}",
                    "question": f"数据契约 {key} 的具体定义",
                    "source": f"charter.yaml#{key}"
                })
    
    return contracts
```

### split-report 必填

| 字段 | 说明 |
|------|------|
| Section 5.7 | Contracts Inventory（契约清单） |
| Section 6.5 | Contracts → IFC/TBD 映射 |

---

## 18. Gate Check 完整清单（v0.6.2）

Charter → L0 的完整门禁检查：

| Check | 规则 | v0.6.2 新增 |
|-------|------|-------------|
| Scope 覆盖 | `must_have[]` 100% 映射到 REQ-L0-* | |
| Metrics 覆盖 | `metrics.*[]` 100% 映射到 REQ-L0-{PERF/SEC/STAB/UX}-* | |
| Constraints 覆盖 | `constraints.*` 100% 映射到 REQ-L0-CON-* | |
| Exclusions 覆盖 | `out_of_scope[]` 100% 记录 | |
| TBD 覆盖 | `open_questions[]` 100% 映射到 TBD-L0-* | |
| **Risks 覆盖** | `risks[]` 100% 映射到 REQ-L0-RISK-* | ✅ |
| **Dependencies 覆盖** | `dependencies.*[]` 100% 映射到 REQ-L0-DEP-* | ✅ |
| **Contracts 覆盖** | `*_contract` 100% 映射到 IFC/TBD | ✅ |


