# L0 → L1 Split Report

## 1. Summary

| 属性 | 值 |
|------|-----|
| Source | `docs/L0/requirements.md` |
| Target | `docs/L1/` |
| Granularity | `full` (L0→L1→L2) |
| Traceability | `strict` |
| Gate Status | `PENDING` |

## 2. L1 Feature Identification

基于 L0 需求的业务能力分组，识别以下 5 个 L1 Features：

| Feature ID | Feature Name | 描述 | L0 Sources |
|------------|--------------|------|------------|
| **RAGQA** | RAG 问答服务 | 核心问答能力，含检索、引用、上下文 | API-001,004,005,006 |
| **PRDREC** | 产品推荐对比 | 产品推荐与比较功能 | API-002,003 |
| **USRMGMT** | 用户管理 | 邮箱登录/验证码 | SHARED-001 |
| **ADMGMT** | 后台管理 | 产品/知识库/线索管理 | ADM-001,002,003 |
| **HANDOFF** | 人机转接 | 人工客服转接 | API-007 |

> **跨 Feature 能力**（由各 Feature 继承）：
> - Widget 交互 (WGT-001~004) → 在 L2 直接分配到 `chat-widget` 组件
> - 非功能需求 (PERF/SEC/STAB/UX/CON) → 各 Feature 继承

## 3. L0 → L1 Mapping

### 3.1 Functional Requirements Mapping

| L0 REQ-ID | L0 Statement | L1 Feature | L1 REQ-ID |
|-----------|--------------|------------|-----------|
| REQ-L0-API-001 | RAG 问答，附带来源引用 | RAGQA | REQ-L1-RAGQA-001 |
| REQ-L0-API-004 | 上下文感知检索 | RAGQA | REQ-L1-RAGQA-002 |
| REQ-L0-API-005 | 对话历史管理 | RAGQA | REQ-L1-RAGQA-003 |
| REQ-L0-API-006 | LLM Provider 可配置 | RAGQA | REQ-L1-RAGQA-004 |
| REQ-L0-API-002 | 产品推荐 Top-N | PRDREC | REQ-L1-PRDREC-001 |
| REQ-L0-API-003 | 产品比较 | PRDREC | REQ-L1-PRDREC-002 |
| REQ-L0-SHARED-001 | 邮箱验证码登录 | USRMGMT | REQ-L1-USRMGMT-001 |
| REQ-L0-ADM-001 | 产品数据导入查询 | ADMGMT | REQ-L1-ADMGMT-001 |
| REQ-L0-ADM-002 | 知识库导入索引 | ADMGMT | REQ-L1-ADMGMT-002 |
| REQ-L0-ADM-003 | 后台管理UI | ADMGMT | REQ-L1-ADMGMT-003 |
| REQ-L0-API-007 | 人工/AI 切换 | HANDOFF | REQ-L1-HANDOFF-001 |

### 3.2 Widget Capabilities (L2 Direct)

| L0 REQ-ID | L0 Statement | L2 Target |
|-----------|--------------|-----------|
| REQ-L0-WGT-001 | 可嵌入 Widget | chat-widget |
| REQ-L0-WGT-002 | 语音 STT/TTS | chat-widget |
| REQ-L0-WGT-003 | 多语言支持 | chat-widget |
| REQ-L0-WGT-004 | 文件上传 | chat-widget |

> 说明：Widget 需求在 L1 层不单独建 Feature，直接在 L2 层映射到 `chat-widget` 组件。

### 3.3 Non-Functional Requirements (Inherited)

| L0 Category | REQ Count | 继承方式 |
|-------------|-----------|----------|
| Performance (PERF) | 3 | 所有 Feature 继承 |
| Security (SEC) | 4 | 所有 Feature 继承 |
| Stability (STAB) | 2 | 所有 Feature 继承 |
| Usability (UX) | 3 | Widget 相关 Feature 继承 |
| Constraints (CON) | 4 | 项目级约束 |

## 4. TBD Assignment

| TBD-ID | Question | Impact | Target Feature |
|--------|----------|--------|----------------|
| TBD-L0-001 | LLM Provider/Model 选择 | H | RAGQA |
| TBD-L0-002 | 降级策略 | M | RAGQA |
| TBD-L0-003 | 后台鉴权方式 | H | ADMGMT |
| TBD-L0-004 | 对话留存策略 | M | RAGQA |
| TBD-L0-005 | 推荐/比较字段配置 | L | PRDREC |
| TBD-L0-006 | Widget 资源体积 | L | (L2-WGT) |
| TBD-L0-007 | STT/TTS Provider | M | (L2-WGT) |
| TBD-L0-008 | 文件上传格式/大小 | M | (L2-WGT) |
| TBD-L0-009 | 多语言策略 | M | (L2-WGT) |
| TBD-L0-010 | 邮箱验证码防刷 | M | USRMGMT |
| TBD-L0-011 | 人工客服转接方案 | M | HANDOFF |
| TBD-L0-012 | 寻价功能定义 | M | ADMGMT |

## 5. Traceability Matrix

| L0 REQ/Category | L1 Feature | Status |
|-----------------|------------|--------|
| REQ-L0-API-001 | RAGQA | ✅ Covered |
| REQ-L0-API-002 | PRDREC | ✅ Covered |
| REQ-L0-API-003 | PRDREC | ✅ Covered |
| REQ-L0-API-004 | RAGQA | ✅ Covered |
| REQ-L0-API-005 | RAGQA | ✅ Covered |
| REQ-L0-API-006 | RAGQA | ✅ Covered |
| REQ-L0-API-007 | HANDOFF | ✅ Covered |
| REQ-L0-ADM-001 | ADMGMT | ✅ Covered |
| REQ-L0-ADM-002 | ADMGMT | ✅ Covered |
| REQ-L0-ADM-003 | ADMGMT | ✅ Covered |
| REQ-L0-SHARED-001 | USRMGMT | ✅ Covered |
| REQ-L0-WGT-* (4) | → L2 Direct | ✅ Deferred to L2 |
| REQ-L0-PERF-* (3) | Inherited | ✅ |
| REQ-L0-SEC-* (4) | Inherited | ✅ |
| REQ-L0-STAB-* (2) | Inherited | ✅ |
| REQ-L0-UX-* (3) | Inherited | ✅ |
| REQ-L0-CON-* (4) | Project-level | ✅ |

**Coverage**: 31/31 L0 requirements → 100%

## 6. Output Structure

```
docs/L1/
├── split-report.md           # 本文件
├── ragqa/
│   └── requirements.md       # RAG 问答服务
├── prdrec/
│   └── requirements.md       # 产品推荐对比
├── usrmgmt/
│   └── requirements.md       # 用户管理
├── admgmt/
│   └── requirements.md       # 后台管理
└── handoff/
    └── requirements.md       # 人机转接
```

## 7. Gate Check

| Check | Status |
|-------|--------|
| L0 Coverage | ✅ 100% |
| Each L1 has sources[] | ✅ |
| TBDs assigned | ✅ |
| No interface contracts at L1 | ✅ |
| Traceability complete | ✅ |

**Result**: ✅ **PASS**
