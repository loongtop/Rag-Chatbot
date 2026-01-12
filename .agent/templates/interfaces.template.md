---
status: draft
owner: architect
layer: L1 | L2
parent: {requirements_path}
---

# Interfaces: {module_or_feature_name}

> 本文件必须可追溯到同目录下的 `requirements.md`。每个接口至少关联 1 条 `REQ-*`。

## 0. Traceability（需求关联）

| Interface | Related REQ-ID(s) | Source | Notes |
|----------|--------------------|--------|-------|
| `{interface_name}` | `REQ-Lx-001` | `REQ-Lx-001` | |

## 1. Scope

Briefly describe the exposed surface and boundaries.

## 2. Public Interfaces

### Interface: {interface_name}

- Purpose: Describe intent
- Related Requirements: `REQ-Lx-001`, `REQ-Lx-002`
- Source: `REQ-Lx-001` / `docs/Lx/...#...`
- Input:
  - param1: Type, description
  - param2: Type, description
- Output:
  - return: ReturnType, description
- Errors:
  - ErrorType: Trigger condition

## 3. Data Contracts

- Request/response schema
- Key fields and constraints

## 4. Dependencies

- Upstream: Modules/systems this depends on
- Downstream: Modules/systems that depend on this
