---
id: "SPEC-006"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-009"
interfaces:
  - "IFC-ADMIN-API"
depends_on:
  - "SPEC-003"
profile: "python"
---

# Spec: Knowledge Base Docs + Index Jobs APIs

## 0. Summary

- Goal: 实现知识库文档上传与索引构建 API，并提供可查询的索引状态与失败原因。
- Non-goals: 分布式任务队列（v0.1 采用进程内后台任务）。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/admin/docs`：上传文档，写入 documents 元数据并返回 doc_id。
- `GET /api/admin/docs`：分页查询文档列表（用于后台展示）。
- `POST /api/admin/index/rebuild`：触发重建，返回 job_id。
- `GET /api/admin/index/status`：返回 `idle|building|error` + progress。
- `GET /api/admin/logs`：查询操作/索引相关日志（最小实现：审计日志表分页）。
- Ingestion pipeline：extract → chunk → embed → store(chunks)。

### Out of Scope
- 自动爬取/同步（明确 out_of_scope）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-009 | docs upload + index jobs + status | 后台 UI 依赖 |

## 3. Design / Decisions

### Proposed Approach
- 文档存储：
  - `documents` 记录文件名/类型/source/status/extracted_text/metadata；
  - `chunks` 记录 chunk_index/content/embedding/metadata。
- 索引任务：
  - `index_jobs` 记录 job_type/status/progress/error_message；
  - rebuild 触发后台任务扫描待索引 documents 并生成 chunks。

### Key Decisions
- Decision: v0.1 使用 FastAPI BackgroundTasks + DB job 记录
  - Rationale: 满足“可观测”与“可重试”的最小闭环，不引入额外 infra。
  - Alternatives: Celery/队列（运维成本更高）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-ADMIN-API | provide | docs + index endpoints |

## 5. Implementation Plan

1. 定义上传接口：`multipart/form-data`（file），限制类型/大小（与 SPEC-010 共用）。
2. 实现 Extractor：
   - txt 直接读取；
   - 其他类型在 v0.1 可先返回“unsupported”（或接入可选依赖）。
3. 切块：配置 chunk_size/overlap；metadata 记录来源位置。
4. embedding：调用 `LLMProvider.embed_texts()`，写入 `chunks.embedding`。
5. 实现 index_jobs：
   - rebuild 创建 job 并异步执行；
   - status 读取最新 job。
6. 实现列表与日志：
   - `GET /api/admin/docs`：分页 + query（filename/status）。
   - `GET /api/admin/logs`：分页读取 `audit_logs`（scope 作为 metadata 过滤）。
7. 单测：上传 txt→rebuild→status→docs list 流程（mock embed）。

### Files / Modules
- `apps/api/api/admin_docs.py`
- `apps/api/api/admin_index.py`
- `apps/api/services/indexing.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| upload doc | txt file | 返回 doc_id，documents.status=pending | |
| rebuild | none | 返回 job_id，status=building | |
| status | job running | progress 单调上升或可用 | 允许近似 |
| rebuild fail | embed error | status=error 且带 error_message | |
| docs list | query/page | 返回 docs[] + total | |
| logs | scope=index | 返回 logs[] + total | |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-008 | 支持格式/大小/存储方式与留存 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback
