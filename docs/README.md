# Project Documentation

此目录用于存放项目文档。

## 目录用途

| 目录/文件 | 用途 |
|-----------|------|
| `docs/` | 项目特定文档（用户手册、API 文档等） |
| `.agent/docs/` | Charter Agent Framework 框架文档（架构说明、使用指南等） |

## 建议结构

```
docs/
├── README.md              # 本文件
├── user-guide.md          # 用户使用指南
├── api/                   # API 文档
│   ├── README.md
│   └── openapi.yaml
├── architecture/          # 架构文档
│   └── system-design.md
└── deployment/            # 部署文档
    └── setup-guide.md
```

## 注意事项

- `.agent/docs/` 中的文件属于框架，不应修改
- 项目特定文档放在此 `docs/` 目录
