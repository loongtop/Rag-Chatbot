---
id: "SPEC-001"
status: ready
owner: spec
leaf: true
parent: "docs/L2/api-server/requirements.md"
source_requirements:
  - "REQ-L2-API-001"
interfaces:
  - "IFC-CHAT-API"
depends_on: []
profile: "python"
---

# Spec: /api/chat Endpoint (RAG QA)

## 0. Summary

- Goal: 实现符合 IFC-CHAT-API 的 /api/chat 端点
- Leaf: `true`

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-001 | endpoint + response schema | include references |

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | request/response must match |

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| basic | message="hi" | answer + references[] | references non-empty when hit |

