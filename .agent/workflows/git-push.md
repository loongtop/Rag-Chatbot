---
description: Stage, commit, and push all local changes to GitHub
---

# Git Push Workflow

Push all local changes to the remote repository.

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

3. Commit with a descriptive message (auto-generate based on changes):
```bash
git commit -m "chore: update files"
```

4. Push to origin:
```bash
git push origin main
```

## Notes

- If no changes to commit, step 3 will be skipped
- Default branch is `main`, modify if using a different branch
- Commit message can be customized when running the workflow
