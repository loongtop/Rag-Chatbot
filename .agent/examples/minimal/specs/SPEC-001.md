---
id: "SPEC-001"
status: done
owner: coder
leaf: true
parent: "docs/L2/notes-store/requirements.md"
source_requirements:
  - "REQ-L2-NS-001"
  - "REQ-L2-NS-002"
interfaces: []
depends_on: []
profile: "python"
---

# Spec: Local JSON Note Store

## 0. Summary

- Goal: 实现本地 JSON 笔记存储的 add/list 能力
- Leaf: `true`

## 1. Scope

### In Scope
- load/create store file
- add_note: append + persist
- list_notes: sort desc + return

### Out of Scope
- 云同步、全文检索、加密

## 2. Traceability

| Source REQ | How Covered | Notes |
|------------|-------------|------|
| REQ-L2-NS-001 | `add_note()` + 持久化 | 缺失文件自动初始化 |
| REQ-L2-NS-002 | `list_notes()` 排序倒序 | created_at ISO8601 |

## 3. Design / Decisions

- 使用 JSON 文件存储 `[{id, content, created_at}]`
- created_at 使用 UTC ISO 8601 字符串，排序用字符串比较（ISO 格式可字典序排序）

## 4. Interfaces Impact

N/A（单模块，无跨模块接口）

## 5. Implementation Plan

1. 定义 `Note` 数据结构（dict 或 dataclass）
2. 实现 `load_notes(path)`：文件缺失返回空列表；内容非法抛 ValueError
3. 实现 `persist_notes(path, notes)`：原子写入（临时文件 + replace）
4. 实现 `add_note(path, content)`：生成 id，追加并排序后持久化
5. 实现 `list_notes(path)`：加载并排序返回

### Files / Modules
- `src/notes_app/store.py`
- `tests/test_store.py`

## 6. Acceptance Tests

| Case | Input | Expected | Notes |
|------|-------|----------|------|
| create-on-first-add | empty store + "hello" | file created with 1 note | created_at exists |
| list-desc | add "a" then "b" | list returns ["b","a"] | time order |
| missing-file | list on missing file | [] | no exception |

## 7. Open Questions (TBD)

None

## 8. Leaf Checklist

- [x] 输入/输出/错误语义明确
- [x] 依赖与接口契约明确（N/A）
- [x] 有可执行验收/测试点
- [x] 范围可在一次小迭代/PR 内完成
- [x] 无阻塞性 TBD

