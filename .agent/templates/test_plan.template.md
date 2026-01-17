# Test Plan: {SPEC_ID}

> 生成时间: {TIMESTAMP}
> 基于 Spec: {SPEC_ID} - {SPEC_TITLE}

---

## 1. 测试范围

### In Scope
- {功能点 1}
- {功能点 2}

### Out of Scope
- {排除项 1}

---

## 2. 测试环境

| 环境 | 配置 |
|------|------|
| Python | 3.10+ |
| 数据库 | PostgreSQL + pgvector (Docker) |
| 依赖 | pytest, pytest-asyncio, httpx |

---

## 3. 验收标准追溯

| 验收点 | 来源 | 测试用例 |
|--------|------|----------|
| {验收点 1} | {Spec Acceptance Tests} | TC-001, TC-002 |
| {验收点 2} | {Spec Acceptance Tests} | TC-003 |

---

## 4. 测试矩阵

### 4.1 功能测试 (Functional)

| ID | 描述 | 输入 | 预期输出 | 优先级 |
|----|------|------|----------|--------|
| TC-F-001 | {正常流程} | {输入} | {输出} | P0 |
| TC-F-002 | {正常流程变体} | {输入} | {输出} | P0 |

### 4.2 边界测试 (Boundary)

| ID | 描述 | 输入 | 预期行为 | 优先级 |
|----|------|------|----------|--------|
| TC-B-001 | 空值输入 | null/empty | 返回验证错误 | P0 |
| TC-B-002 | 最大长度 | 4000 字符 | 正常处理 | P1 |
| TC-B-003 | 超长输入 | 4001 字符 | 返回验证错误 | P0 |
| TC-B-004 | 特殊字符 | SQL注入尝试 | 安全处理 | P0 |

### 4.3 异常测试 (Exception)

| ID | 描述 | 场景 | 预期错误码 | 优先级 |
|----|------|------|------------|--------|
| TC-E-001 | Provider 超时 | LLM 30s 无响应 | LLM_TIMEOUT | P0 |
| TC-E-002 | 未授权访问 | 无/错误 token | UNAUTHORIZED | P0 |
| TC-E-003 | 资源不存在 | 查询不存在的 ID | NOT_FOUND | P1 |

### 4.4 性能测试 (Performance)

| ID | 描述 | 指标 | 阈值 | 优先级 |
|----|------|------|------|--------|
| TC-P-001 | 响应时间 | P95 延迟 | < 3s | P1 |

---

## 5. 依赖和前置条件

### 5.1 外部依赖

| 依赖 | 状态 | Mock 方案 |
|------|------|-----------|
| LLM Provider | {SPEC-003} | MockLLMProvider |
| Database | Docker Compose | SQLite in-memory |

### 5.2 测试数据

- 使用 fixture 提供测试数据
- 每个测试独立，不依赖执行顺序

---

## 6. 测试执行计划

```bash
# 从仓库根目录执行

# 单元测试（默认排除性能测试）
pytest apps/api/tests/unit/ -v -m "not performance"

# 集成测试（需要 docker-compose up -d postgres）
pytest apps/api/tests/integration/ -v -m "integration"

# 完整测试 + 覆盖率
pytest apps/api/tests/ -m "not performance" --cov=apps/api --cov-report=term-missing

# 性能测试（单独运行，夜间/手动）
pytest apps/api/tests/ -m "performance" -v
```

---

## 7. 质量门禁

| 指标 | 默认门槛 | 推荐目标 |
|------|----------|----------|
| 覆盖率 | ≥ 80% | 95% |
| 失败用例 | = 0 | = 0 |
| 边界覆盖 | 完整 | 完整 |
| 异常覆盖 | 完整 | 完整 |

> **注**: 覆盖率只统计业务代码（`apps/api/`），不含 `tests/`、`migrations/` 等
