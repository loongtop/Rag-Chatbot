---
id: "SPEC-005"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-005"
  - "REQ-L2-API-006"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-004"
  - "SPEC-003"
profile: "python"
---

# Spec: Recommend & Compare APIs

## 0. Summary

- Goal: 实现 `/api/recommend` 与 `/api/compare`，提供可用的产品推荐与结构化对比。
- Non-goals: 行业/类目级精调推荐模型（后续迭代）。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/recommend`：`query` + `top_n?` + `language?` → `products[]` + `reasons[]`。
- `POST /api/compare`：`product_ids[2..4]` + `language?` → `comparison`（columns/rows）。
- 推荐/对比使用 `products` 数据表；可选调用 LLM 生成 reasons（可配置开关）。

### Out of Scope
- 后台可配置对比字段（TBD）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-005 | `/api/recommend` + reasons | Top-N 默认 3 |
| REQ-L2-API-006 | `/api/compare` 返回 ComparisonTable | 2–4 products |

## 3. Design / Decisions

### Proposed Approach
- Recommend（v0.1 基线）：
  1) 用文本检索从 products 找候选（query→name/category/specs）；
  2) 计算简单分数（命中字段数/类别匹配等）；
  3) 返回 Top-N；reasons 由规则模板或 LLM（可选）生成。
- Compare（v0.1 基线）：
  - columns=product_ids；rows=基础字段（name/category/price/url）+ specs keys 的并集。

### Key Decisions
- Decision: v0.1 不引入产品向量索引
  - Rationale: 降低数据准备成本；后续可按需要增加 `product_embeddings`。
  - Alternatives: 产品 embedding（质量更好但引入额外构建链路）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | `/api/recommend`、`/api/compare` |

## 5. Implementation Plan

1. 定义请求/响应模型（对齐 `docs/L2/interfaces.md`）。
2. 实现 recommend：
   - 参数校验：top_n 默认 3；
   - 查询候选并打分；
   - 生成 reasons（规则/LLM 开关）。
3. 实现 compare：
   - 校验 product_ids 长度 2–4；
   - 批量查询 products；
   - 组装 ComparisonTable（字段 + specs union）。
4. 单测：top_n 默认、非法 product_ids、rows/columns 维度一致。

### Files / Modules
- `apps/api/api/recommend.py`
- `apps/api/api/compare.py`
- `apps/api/services/recommendation.py`
- `apps/api/services/comparison.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| recommend default | query only | 返回 3 个 products + 3 条 reasons | |
| recommend top_n | top_n=5 | 返回 5 个 products | |
| compare ok | 2 ids | rows 中每行 values 长度=2 | |
| compare invalid | 1 id / 5 ids | 422 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-005 | 推荐/比较字段配置策略 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

