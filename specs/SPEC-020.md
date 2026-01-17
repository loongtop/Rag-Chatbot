---
id: "SPEC-020"
status: draft
owner: spec
leaf: true
parent: "SPEC-018"
source_requirements:
  - "REQ-L2-ADM-001"
interfaces:
  - "IFC-ADMIN-API"
depends_on:
  - "SPEC-019"
  - "SPEC-004"
profile: "typescript"
---

# Spec: Products Management UI

## 0. Summary

- Goal: 提供产品数据管理 UI：JSON 上传/替换/查看/搜索。
- Non-goals: 字段级编辑器（v0.1 以批量 JSON 为主）。
- Leaf: `true`

## 1. Scope

### In Scope
- 页面：Products 列表（表格）、搜索框、上传 JSON 按钮。
- API：
  - `GET /api/admin/products`（分页 + query）
  - `POST /api/admin/products`（上传）
- 上传成功后自动刷新列表并显示导入版本/数量。

### Out of Scope
- 版本回滚 UI（先预留入口）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-ADM-001 | products page + upload + search | |

## 3. Design / Decisions

### Proposed Approach
- 列表字段：id/name/category/url（可展开 raw/specs）。
- 上传校验：前端仅做扩展名提示，后端为最终校验。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | consume | products endpoints |

## 5. Implementation Plan

1. ProductsPage：拉取列表并渲染表格。
2. Search：debounce query；分页控件。
3. Upload：选择文件→调用 POST→显示结果（count/version）。
4. 错误处理：展示后端错误消息（validation/rate limit）。

### Files / Modules
- `apps/admin/src/pages/ProductsPage.tsx`
- `apps/admin/src/api/products.ts`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| list | 打开页面 | 展示 products 列表 | mock |
| search | query keyword | 列表筛选 | |
| upload | valid json | 显示 count/version 且刷新列表 | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-005 | 字段配置与展示策略 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

