---
id: "SPEC-007"
status: draft
owner: spec
leaf: true
parent: "SPEC-001"
source_requirements:
  - "REQ-L2-API-007"
interfaces:
  - "IFC-CHAT-API"
depends_on: []
profile: "python"
---

# Spec: Email OTP Auth APIs

## 0. Summary

- Goal: 实现邮箱验证码登录：发送验证码 + 验证并返回 token/user。
- Non-goals: 密码登录、OAuth/SSO、多因素认证。
- Leaf: `true`

## 1. Scope

### In Scope
- `POST /api/auth/send-code`：输入 email，生成验证码并发送（验证码不回显）。
- `POST /api/auth/verify`：校验验证码并返回 token + user。
- 频控与滥用防护：过期时间、尝试次数、IP 维度限制（最小实现）。

### Out of Scope
- 复杂权限体系（后台鉴权另见 TBD-L0-003）。

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-API-007 | send-code + verify + token | Widget 登录 UI 依赖 |

## 3. Design / Decisions

### Proposed Approach
- DB：
  - `users(email, verified_at)`；
  - `email_verification_codes(email, code_hash, expires_at, attempts, used_at, ip, user_agent)`。
- Token：v0.1 可用 JWT（HMAC）或 opaque token（实现选择可后续替换）。

### Key Decisions
- Decision: 验证码仅存 hash
  - Rationale: 降低泄露风险，满足安全指标。
  - Alternatives: 明文存储（不推荐）。

## 4. Interfaces Impact

| Interface | Role | Notes |
|----------|------|------|
| IFC-CHAT-API | provide | auth endpoints |

## 5. Implementation Plan

1. 定义请求/响应模型；email 格式校验。
2. send-code：
   - 生成 6 位码；
   - 存 code_hash + expires；
   - 调用 EmailProvider（可 stub）。
3. verify：
   - 校验 expires/attempts；
   - upsert user（verified_at）；
   - 生成 token 并返回。
4. 单测：成功/失败/过期/多次尝试/频控。

### Files / Modules
- `apps/api/api/auth.py`
- `apps/api/services/email.py`
- `apps/api/services/tokens.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| send ok | valid email | `{success:true}` | |
| verify ok | correct code | 返回 token + user | |
| verify bad | wrong code | 400/401，attempts+1 | |
| expired | expired code | 400/401 | |
| rate limit | too frequent | 429 | 基线策略即可 |

## 7. Open Questions (TBD)

| TBD | Question | Impact | Owner | Status |
|-----|----------|--------|-------|--------|
| TBD-L0-010 | 邮箱验证码登录方案与防刷机制细节 | M | Product Owner | open |

## 8. Leaf Checklist

- [ ] 输入/输出/错误语义明确
- [ ] 依赖与接口契约明确（IFC 引用完整或 N/A）
- [ ] 有可执行验收/测试点
- [ ] 范围可在一次小迭代/PR 内完成
- [ ] 无阻塞性 TBD（impact=H）或已提供 fallback

