---
id: "SPEC-004"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-008"
interfaces:
  - "IFC-ADMIN-API"
depends_on: []
profile: "python"
---

# Spec: Product Data Admin APIs (Import/Version/Query)

## 0. Summary

- Goal: 提供产品数据管理 API：上传/替换产品 JSON 并支持查询与检索。
- Non-goals: 完整的字段级后台可配置与版本回滚 UI（后续在后台侧迭代）。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/admin/products`：上传产品 JSON（约 600 SKU），校验并写入数据库，返回导入版本信息。
- `GET /api/admin/products`：分页查询与关键词检索。
- 数据契约遵循 `IFC-PRODUCT-DATA`（required/optional 字段），保留 raw JSON。

### Out of Scope
- 高级搜索（复杂过滤 DSL）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-008 | admin 端点 + 结构化存储 + 版本记录 | 支撑 recommend/compare 与后台展示 |

## 3. Design / Decisions

### Proposed Approach
- 双层存储：
  - `product_imports`：每次上传的文件元信息 + checksum + raw_json。
  - `products`：结构化字段（id/name/category/url/specs/price/short_description）+ raw。
- 替换策略：单次上传在 DB transaction 内执行“写新版本 + upsert products”，失败整体回滚。

### Key Decisions
- Decision: 校验最小字段集（id/name/category/url）
  - Rationale: 与 Charter 契约一致，避免脏数据导致推荐/对比不可用。
  - Alternatives: 不校验（运行时风险高）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | provide | `/api/admin/products` 上传与列表 |

## 5. Implementation Plan

1. 定义上传输入：`multipart/form-data`（file），支持 `.json`。
2. 校验：
   - JSON 为数组；
   - 每项包含 required 字段且 `id` 唯一。
3. DB 写入：
   - 写入 `product_imports`（checksum/created_at）；
   - upsert `products`（import_id 指向最新导入）。
4. 查询接口：
   - `page/pageSize/query`；
   - query 搜索 name/category/specs(文本化)。
5. 单测：上传校验、重复 id、查询分页。

### Files / Modules
- `apps/api/api/admin_products.py`
- `apps/api/models/product.py`, `apps/api/models/product_import.py`
- `apps/api/services/products.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| upload ok | valid JSON list | 返回 `count` + `version` | count=记录数 |
| upload invalid | 缺少 required 字段 | 422/400 + 错误详情 | |
| list paging | page/pageSize | 返回 data + pagination | |
| search | query keyword | 返回匹配产品子集 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-005 | 推荐/比较字段配置来源 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

