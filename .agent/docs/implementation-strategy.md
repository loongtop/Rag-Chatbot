# Phase 3 Implementation Strategy (CAF v0.6.5)

三段式实现策略：从 Spec 到代码的最佳实践。

> **适用场景**：当 `/spec` 完成后，准备进入 Phase 3 编码阶段时使用。

---

## 阶段 0：约束对齐（一次性）

在动手编码前，先确认以下决策：

### 0.1 代码落点

以 `charter.yaml#components[*].path` 为准：

```yaml
components:
  - name: "api-server"
    path: "apps/api"          # ← 后端代码落点
  - name: "chat-widget"
    path: "apps/widget"       # ← 前端 Widget 落点
  - name: "admin-dashboard"
    path: "apps/admin"        # ← 后台 UI 落点
```

同步确保 `.agent/config/quality.{language}.yaml` 的扫描目标与这些目录一致。

### 0.2 最小 TBD 决策

只为"能跑通"做决策，后续可替换：

| TBD | 最小决策 | 说明 |
|-----|----------|------|
| LLM Provider | 默认 OpenAI-compatible + mock 单测 | 可后换 Ollama/其他 |
| 后台鉴权 | Basic Auth / 静态 Token | v0.2 再升 SSO |
| STT/TTS | Stub + 503 + 明确错误码 | 前端做降级提示 |

> 更新相关 Spec 的 TBD 状态为 `resolved (fallback)`。

---

## 阶段 1：骨架落地

先实现"不会再拆、返工风险最低"的横切能力。

### 1.1 目标

把后续所有 leaf 都会复用的能力先铺好：

- 配置加载
- 统一错误模型 + request_id
- 日志
- HTTP client 基础
- Provider 抽象与工厂
- 超时/错误映射
- （可选）DB 连接/会话管理

### 1.2 推荐结构（Python/FastAPI 示例）

```
apps/api/
├── config/
│   └── settings.py       # 配置加载
├── core/
│   ├── errors.py         # 统一错误模型
│   ├── logging.py        # 日志
│   └── middleware.py     # request_id、限流
├── providers/
│   ├── base.py           # Provider 抽象
│   ├── llm.py            # LLM Provider 工厂
│   └── embedding.py      # Embedding Provider
└── db/
    └── session.py        # DB 连接
```

### 1.3 退出条件

- [ ] 后端能启动（`uvicorn apps.api:app`）
- [ ] Provider 可被单测 mock
- [ ] 后续 Specs 不需要重复"造轮子"

---

## 阶段 2：Leaf 就绪度巡检

对每个 `leaf=true` 的 Spec 做 checklist 判定。

### 2.1 判定结果

| 结果 | 条件 | 行动 |
|------|------|------|
| **Ready** | 接口/输入输出/错误语义明确；依赖已具备；验收可测 | 标记 `status: ready` 或确认 Leaf Checklist |
| **Needs Split** | 覆盖 >1 端点，或范围过大 | 进入拆分（阶段 3）|
| **Blocked** | 存在 impact=H 的 TBD 或契约缺口 | 先补齐 TBD/接口契约 |

### 2.2 同步更新

- `specs/spec-tree.md`：覆盖矩阵 + leaf 数量
- `docs/L2/execution-tracker.md`：状态汇总

---

## 阶段 3：拆分 Needs Split 的 Leaf

仅对"范围过大"的 leaf 进行拆分，通常不超过 1 次递归。

### 3.1 拆分规则（满足任一）

1. 一个 Spec 覆盖 >1 个端点
2. 端点 + 持久化 + 异步任务混在一起
3. 触达 >2 个子系统（DB + Provider + 状态机）
4. 验收无法写成可执行断言

### 3.2 拆分方式

1. 将原 Spec 变为 `leaf=false`（保留 Traceability）
2. 新增 2-5 个子 leaf（每个只做一件事）
3. 若第二层仍"范围太大"，再拆一层
4. **不超过 3 层深度**

### 3.3 退出条件

每个 leaf 都能：
- [ ] 一次 PR 内完成
- [ ] 有明确验收
- [ ] 依赖清晰

---

## 阶段 4：编码循环

一次只实现一个 leaf。

### 4.1 循环步骤

```python
for leaf in get_ready_specs():
    # 1. 预检查
    if will_change_interface(leaf):
        update("docs/L2/interfaces.md")  # 先改契约
        update("docs/architecture/*.md")  # 必要时同步
    
    # 2. 实现代码 + 最小测试
    implement(leaf)
    write_tests(leaf.acceptance_tests)
    
    # 3. 质量检查
    run_lint()
    run_typecheck()
    run_tests()
    
    # 4. 状态更新
    leaf.status = "done"
    update("docs/L2/execution-tracker.md")
```

### 4.2 推荐顺序

```
阶段 1：基础设施（无依赖）
  └─ Provider 抽象 (SPEC-003 类)

阶段 2：数据层（可并行）
  ├─ 产品数据 (SPEC-004 类)
  └─ 知识库索引 (SPEC-006 类)

阶段 3：核心功能（依赖 1+2）
  └─ 核心 API (SPEC-002 类)

阶段 4：前端基线（可并行）
  ├─ Widget 核心 (SPEC-012 类)
  └─ Admin Shell (SPEC-019 类)

阶段 5：其余 leaf（并行）
```

### 4.3 接口变更规则

> **重要**：若实现过程中需要新增/修改跨组件接口：
> 1. 先更新 `docs/L2/interfaces.md`
> 2. 必要时同步 `docs/architecture/api-spec.md`
> 3. 再修改 Spec/代码

---

## 关于拆分深度

**不按"几级"定，而按"能否一次 PR 完成"定。**

| 类型 | 典型拆分深度 |
|------|--------------|
| 简单 CRUD | 0（直接 leaf）|
| 多端点聚合 | 1 层（3-5 个子 leaf）|
| 链路型 Spec（RAG/Indexing）| 2 层 |
| 最大深度 | 3 层（极少需要）|

---

## 检查清单

### 阶段 0 完成标志
- [ ] 代码落点已确认
- [ ] 最小 TBD 已决策
- [ ] 质量配置已对齐

### 阶段 1 完成标志
- [ ] 骨架代码可启动
- [ ] Provider 可 mock
- [ ] 横切能力已就绪

### 阶段 2 完成标志
- [ ] 所有 leaf 已分类（Ready/Needs Split/Blocked）
- [ ] spec-tree.md 已更新
- [ ] execution-tracker.md 已更新

### 阶段 3 完成标志
- [ ] 所有 Needs Split 已拆分
- [ ] 每个 leaf 可一次 PR 完成

### 阶段 4 完成标志
- [ ] 所有 leaf 状态为 done
- [ ] 测试覆盖率达标
- [ ] 质量门禁通过
