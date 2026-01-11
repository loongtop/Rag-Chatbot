# Quality Standards

代码质量门禁：确保生产级代码质量。

---

## Quality Gates

| Category | Metric | Requirement |
|----------|--------|-------------|
| **Testing** | Coverage | ≥ 95% |
| **Complexity** | Cyclomatic | ≤ 10 |
| **Types** | Annotation | 按语言要求 |
| **Docs** | Docstrings | Required |
| **Security** | Vulnerability Scan | Pass |

---

## Testing Requirements

### Coverage
- Minimum: 95%
- Target: 100%
- Exclusions: 按语言约定（如 `tests/**`, `**/__init__.py`）

### Test Types
| Type | Minimum |
|------|---------|
| Functional | 2 |
| Boundary | 4 |
| Exception | 3 |
| Performance | 1 |

---

## Code Standards

质量工具由 `language_profile` 决定，参见 `.agent/config/quality.{language_profile}.yaml`。

### 常见配置

| 语言 | Linting | Type Check | Security |
|------|---------|------------|----------|
| Python | ruff | mypy | bandit |
| Java | checkstyle | N/A (静态类型) | dependency-check |
| C++ | clang-tidy | N/A (静态类型) | cppcheck |
| Swift | swiftlint | N/A (静态类型) | gitleaks (secrets) |

---

## Security

### Requirements
- No hardcoded secrets
- Input validation
- SQL injection prevention

---

## Review Checklist

### Code Quality
- [ ] Complexity ≤ 10
- [ ] No duplicate code (DRY)
- [ ] Clear naming
- [ ] Single responsibility (SRP)

### Security
- [ ] No hardcoded keys
- [ ] Input validated
- [ ] Injection protected

### Performance
- [ ] No bottlenecks
- [ ] Appropriate caching
- [ ] Optimized queries

---

## Commands

Run quality checks:
```bash
/charter-quality
```

该命令会读取 `charter.yaml` 的 `language_profile`，执行对应的 `{{profile.commands.*}}` 命令。
