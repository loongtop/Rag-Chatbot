---
status: done
owner: requirements_split
layer_from: L0
layer_to: L1
parent: docs/L0/requirements.md
target: docs/L1/
granularity: full
caf_version: v0.6.5
---

# Split Report: L0 → L1 (v0.6.5)

## 1. Summary

- **Decision**: PASS
- **Why**: 52 L0 需求全部映射到 7 个 L1 Features + L2 Direct + Inherited
- **Granularity Mode**: `full` (L0→L1→L2)
- **Config**: `.agent/config/split-rules.yaml` (多语言关键词)

## 2. L1 Feature Identification

基于 v0.6.2 分类规则，识别以下 7 个 L1 Features：

| Feature ID | Feature Name | 描述 | Strategy |
|------------|--------------|------|----------|
| **RAGQA** | RAG 问答服务 | 核心问答能力 | feature |
| **PRDREC** | 产品推荐对比 | 推荐与比较功能 | feature |
| **USRMGMT** | 用户管理 | 邮箱登录 | feature |
| **ADMGMT** | 后台管理 | 产品/知识库管理 | feature |
| **HANDOFF** | 人机转接 | 人工客服切换 | feature |
| **VOICE** | 语音交互 | STT/TTS (v0.6.2) | feature |
| **UPLOAD** | 文件上传 | 文件/图片处理 (v0.6.2) | feature |

> **说明**：v0.6.2 基于 `classify_ui_requirement()` 规则，将有业务逻辑的 WGT 需求提升为独立 Feature

## 3. L0 → L1 Mapping with Strategy

### 3.1 Functional Requirements

| L0 REQ-ID | Statement | Strategy | L1 Target | Rationale |
|-----------|-----------|----------|-----------|-----------|
| REQ-L0-API-001 | RAG 问答 | feature | RAGQA | 核心业务 |
| REQ-L0-API-002 | 产品推荐 | feature | PRDREC | 核心业务 |
| REQ-L0-API-003 | 产品比较 | feature | PRDREC | 核心业务 |
| REQ-L0-API-004 | 上下文感知 | feature | RAGQA | 核心业务 |
| REQ-L0-API-005 | 对话历史 | feature | RAGQA | 核心业务 |
| REQ-L0-API-006 | LLM 切换 | feature | RAGQA | 核心业务 |
| REQ-L0-API-007 | 人工/AI 切换 | feature | HANDOFF | 核心业务 |
| REQ-L0-ADM-001 | 产品数据 | feature | ADMGMT | 核心业务 |
| REQ-L0-ADM-002 | 知识库索引 | feature | ADMGMT | 核心业务 |
| REQ-L0-ADM-003 | 后台 UI | feature | ADMGMT | 核心业务 |
| REQ-L0-SHARED-001 | 邮箱登录 | feature | USRMGMT | 含验证逻辑 |
| REQ-L0-WGT-001 | Widget 嵌入 | direct_l2 | chat-widget | 纯嵌入/集成 |
| REQ-L0-WGT-002 | 语音交互 | **feature** | **VOICE** | 含 Provider 选择 |
| REQ-L0-WGT-003 | 多语言 | direct_l2 | chat-widget | 纯界面切换 |
| REQ-L0-WGT-004 | 文件上传 | **feature** | **UPLOAD** | 含格式/解析逻辑 |

### 3.2 Non-Functional Requirements

| L0 Category | Count | Strategy | Rationale |
|-------------|-------|----------|-----------|
| REQ-L0-PERF-* | 3 | inherit | 所有 Feature 继承 |
| REQ-L0-SEC-* | 4 | inherit | 所有 Feature 继承 |
| REQ-L0-STAB-* | 2 | inherit | 所有 Feature 继承 |
| REQ-L0-UX-* | 3 | inherit | Widget 相关继承 |
| REQ-L0-CON-* | 4 | inherit | 项目约束 |

### 3.3 Risk Mitigation (v0.6.2)

| L0 REQ-ID | Strategy | L1 Target | Rationale |
|-----------|----------|-----------|-----------|
| REQ-L0-RISK-001 | inherit | RAGQA | Token 监控 |
| REQ-L0-RISK-002 | inherit | RAGQA | 检索准确性 |
| REQ-L0-RISK-003 | inherit | ADMGMT | 知识库版本 |
| REQ-L0-RISK-004 | inherit | RAGQA | Prompt 安全 |
| REQ-L0-RISK-005 | inherit | ALL | 高并发 |
| REQ-L0-RISK-006 | inherit | UPLOAD | 文件安全 |
| REQ-L0-RISK-007 | inherit | VOICE | 语音降级 |
| REQ-L0-RISK-008 | inherit | RAGQA | 多语言质量 |
| REQ-L0-RISK-009 | inherit | USRMGMT | 验证码防刷 |
| REQ-L0-RISK-010 | inherit | HANDOFF | 客服 SLA |
| REQ-L0-RISK-011 | inherit | ADMGMT | 寻价隐私 |

### 3.4 Dependencies (v0.6.2)

| L0 REQ-ID | Strategy | L1 Target |
|-----------|----------|-----------|
| REQ-L0-DEP-001~010 | inherit | 对应 Feature |

## 4. Traceability Matrix

| L0 Category | Total | Feature | Direct L2 | Inherit | Coverage |
|-------------|-------|---------|-----------|---------|----------|
| Functional (API/ADM/SHARED) | 11 | 11 | 0 | 0 | 100% |
| Widget (WGT) | 4 | **2** | 2 | 0 | 100% |
| Performance | 3 | 0 | 0 | 3 | 100% |
| Security | 4 | 0 | 0 | 4 | 100% |
| Stability | 2 | 0 | 0 | 2 | 100% |
| Usability | 3 | 0 | 0 | 3 | 100% |
| Constraints | 4 | 0 | 0 | 4 | 100% |
| **Risk** | 11 | 0 | 0 | 11 | 100% |
| **Dependency** | 10 | 0 | 0 | 10 | 100% |
| **Total** | **52** | **13** | **2** | **37** | **100%** |

## 5. Output Structure

```
docs/L1/
├── split-report.md           # 本文件
├── ragqa/requirements.md     # RAG 问答 (4 REQs)
├── prdrec/requirements.md    # 产品推荐 (2 REQs)
├── usrmgmt/requirements.md   # 用户管理 (1 REQ)
├── admgmt/requirements.md    # 后台管理 (3 REQs)
├── handoff/requirements.md   # 人机转接 (1 REQ)
├── voice/requirements.md     # 语音交互 (1 REQ) ← v0.6.2
└── upload/requirements.md    # 文件上传 (1 REQ) ← v0.6.2
```

## 6. Gate Check (v0.6.2)

- [x] All L0 requirements have strategy field
- [x] All `direct_l2` have rationale
- [x] All `direct_l2` have l2_target
- [x] WGT-002 (语音) → VOICE Feature ✅
- [x] WGT-004 (上传) → UPLOAD Feature ✅
- [x] Risks inherit correctly
- [x] Dependencies inherit correctly

---

**Result**: ✅ **PASS**

**Improvement over v0.6.1**:
- WGT-002 → VOICE Feature (有 STT/TTS Provider 选择逻辑)
- WGT-004 → UPLOAD Feature (有格式/大小/解析逻辑)
