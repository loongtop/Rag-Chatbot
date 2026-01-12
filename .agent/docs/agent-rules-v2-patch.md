# Agent Rules Patch for CAF v0.4.0

> **Instructions**: Copy the content below into your memory files as indicated.

---

## 1. Patch for `architect-agent.md`

Add/replace the following sections in `.agent/rules/architect-agent.md`:

### Replace: 工作层级 Section (around line 17-26)

```markdown
## 工作层级

### Template v2.0 (Recommended - CAF v0.4.0+)

> **选择规则**: 如果 frontmatter 包含 `template_version: "v2.0"` 或新项目，使用 v2 模板。

| 层级 | 名称 | 输出产物 | 模板 (v2.0) |
|------|------|----------|------|
| L0 | Charter | requirements.md, subtasks.md | `requirements.L0.v2.template.md` |
| L1 | Features | requirements.md, interfaces.md, subtasks.md | `requirements.L1.v2.template.md` |
| L2 | Modules | requirements.md, interfaces.md, subtasks.md, execution-tracker.md | `requirements.L2.v2.template.md` |
| L3 | Functions | requirements.md (叶子节点) | `requirements.L3.v2.template.md` |

### Template v1.0 (Legacy)

| 层级 | 模板 (v1.0) |
|------|------|
| L0 | `requirements.template.md` |
| L1 | `requirements.L1.template.md` |
| L2 | `requirements.L2.template.md` |
| L3 | `requirements.L3.template.md` |
```

### Replace: 产物格式 Section (around line 28-41)

```markdown
## 产物格式 (Template v2.0)

每个 requirements.md 必须包含 YAML frontmatter:

\`\`\`yaml
---
status: draft | ready | in_progress | done
owner: architect
layer: L0 | L1 | L2 | L3
parent: {parent_path}
source_checksum: "{sha256}"
template_version: "v2.0"
profile: "{profile}"
---
\`\`\`

### Registry 块（唯一事实源）

v2 模板包含嵌入式 Registry 块:

\`\`\`requirements-registry
schema_version: "v1.0"
layer: L0
parent: "charter.yaml"
requirements: [...]
tbds: [...]
exclusions: [...]
interfaces: [...]  # L1/L2 only
\`\`\`

- **Registry 块** = 唯一可编辑的事实源
- **正文/附录** = 由 `/requirements-render` 自动生成（只读）

### 工作流集成（必须）

生成 requirements.md 后**必须**执行:

1. `/requirements-render <layer>` - 从 Registry 渲染正文与附录
2. `/requirements-validate <layer>` - 校验覆盖率/溯源/可验收/一致性

仅当 validate 通过后，requirements.md 才算完成。
```

### Add: 版本规范 Section (before 完成标志)

```markdown
## 版本规范

| 版本类型 | 当前版本 | 说明 |
|----------|---------|------|
| CAF | v0.4.0 | 框架版本 |
| template_version | v2.0 | 文档模板版本 |
| schema_version | v1.0 | Registry Schema 版本 |

> 这三个版本独立维护，互不等同。
```

---

## 2. Patch for `requirements-split-agent.md`

Add the following to `.agent/rules/requirements-split-agent.md`:

### Add: After 输出要求 Section

```markdown
## Source Inventory 权威性

`split-report.md` 的 **Source Inventory** 是"不得遗漏"的权威清单。

`/requirements-validate` 必须确保:
- 每条 SRC-ID 都有 REQ/TBD/Exclusion 去向
- 交叉引用错位必须被检测并报告
- Registry 中的 `exclusions[]` 用于表达 N/A + reason
```

---

## 3. Verification

After applying patches, verify by checking:

1. `architect-agent.md` mentions v2 templates and `/requirements-render` + `/requirements-validate`
2. `requirements-split-agent.md` mentions Source Inventory authority
3. Run `/requirements-validate L0` on the example file to confirm workflow works
