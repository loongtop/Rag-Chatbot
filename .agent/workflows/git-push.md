---
description: Stage, commit, and push all local changes to GitHub
---

# Git Push Workflow

Push all local changes to the remote repository with auto-generated commit messages.

// turbo-all

## Steps

1. Check git status to see what needs to be committed:
```bash
git status
```

2. Stage all changes:
```bash
git add -A
```

3. View the staged changes to understand what was modified:
```bash
git diff --cached --stat
```

4. **Generate commit message based on changes**:
   - Analyze the changed files from step 3
   - Use conventional commit format:
     - `feat:` for new features or files
     - `fix:` for bug fixes  
     - `docs:` for documentation changes (.md files)
     - `chore:` for maintenance tasks
     - `refactor:` for code refactoring
     - `style:` for formatting changes
     - `test:` for test files
   - Include a brief description of what changed

5. Commit with the generated message:
```bash
git commit -m "<generated-message>"
```

6. Push to origin:
```bash
git push origin main
```

## Commit Message Examples

| Changed Files | Generated Message |
|--------------|-------------------|
| `.md` files only | `docs: update documentation` |
| `src/*.py` | `feat: add/update Python source files` |
| `tests/*` | `test: update test files` |
| `*.yaml` config | `chore: update configuration` |
| Bug fix context | `fix: resolve issue in <component>` |
| Mixed changes | `chore: update multiple files` |

## Notes

- If no changes to commit, the workflow will skip commit and push
- Default branch is `main`, modify if using a different branch
- The agent will analyze `git diff --cached --stat` output to determine the appropriate commit type
