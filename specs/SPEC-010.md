---
id: "SPEC-010"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-012"
interfaces:
  - "IFC-CHAT-API"
depends_on:
  - "SPEC-006"
profile: "python"
---

# Spec: Upload Parsing API (File/Image → extracted_content)

## 0. Summary

- Goal: 实现 `POST /api/upload`，将用户上传的文件/图片解析为文本并返回 `extracted_content`（可选 document_id）。
- Non-goals: 全格式解析覆盖（先支持最小集合）。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/upload`：multipart 上传，返回 extracted_content。
- 类型/大小校验；解析失败的错误语义（可观测）。
- 与索引链路复用 Extractor（与 SPEC-006 共用服务）。

### Out of Scope
- 上传文件长期存储策略细化（TBD）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-012 | upload endpoint + extracted_content | Widget 上传 UI 依赖 |

## 3. Design / Decisions

### Proposed Approach
- 先支持：`text/plain`（txt）；其余类型按配置启用（pdf/docx/image）。
- 可选：将上传内容落入 `documents(source=chat)` 并返回 document_id（用于引用追溯）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | upload endpoint |

## 5. Implementation Plan

1. 定义请求：multipart(file)；校验 content-type 与大小上限。
2. 调用 Extractor 返回 extracted_content（失败返回 415/422）。
3. 可选写入 documents（source=chat），返回 document_id。
4. 单测：txt 成功、超大失败、类型不支持、写入可选分支。

### Files / Modules
- `apps/api/api/upload.py`
- `apps/api/services/extract.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| upload txt | txt file | 返回 extracted_content 非空 | |
| unsupported | pdf (未启用) | 415/400 | |
| oversize | >limit | 413 | |
| optional doc | enable store | 返回 document_id | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-008 | 文件/图片存储与保留期 | M | Product Owner | open |
| TBD-L1-UPLOAD-001 | 支持格式与大小限制细化 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

