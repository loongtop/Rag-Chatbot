#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import yaml
from jsonschema import Draft7Validator


FENCE_RE = re.compile(r"```(?P<lang>[a-zA-Z0-9_-]+)[ \t]*\n(?P<body>.*?)\n```", re.DOTALL)


@dataclasses.dataclass(frozen=True)
class Issue:
    level: str  # ERROR | WARN
    code: str
    message: str
    file: Optional[str] = None


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_fence(text: str, lang: str) -> List[str]:
    blocks: List[str] = []
    for match in FENCE_RE.finditer(text):
        if match.group("lang") == lang:
            blocks.append(match.group("body").strip())
    return blocks


def _load_yaml(yaml_text: str, *, path_hint: str) -> Tuple[Optional[Dict[str, Any]], List[Issue]]:
    try:
        data = yaml.safe_load(yaml_text)
    except Exception as exc:  # noqa: BLE001 - best-effort validator
        return None, [Issue("ERROR", "YAML_PARSE", f"{path_hint}: YAML parse failed: {exc}")]
    if not isinstance(data, dict):
        return None, [Issue("ERROR", "YAML_TYPE", f"{path_hint}: registry must be a YAML mapping/object")]
    return data, []


def _load_schema(schema_path: Path) -> Draft7Validator:
    schema = yaml.safe_load(_read_text(schema_path))
    if not isinstance(schema, dict):
        raise ValueError(f"Invalid schema file: {schema_path}")
    return Draft7Validator(schema)


def _split_anchor(path_with_anchor: str) -> Tuple[str, Optional[str]]:
    if "#" not in path_with_anchor:
        return path_with_anchor, None
    path_part, anchor = path_with_anchor.split("#", 1)
    return path_part, anchor or None


def _file_contains_anchor(target_file: Path, anchor: str) -> bool:
    if not anchor:
        return True
    try:
        text = _read_text(target_file)
    except Exception:  # noqa: BLE001
        return False
    return re.search(rf"\b{re.escape(anchor)}\b", text) is not None


def _issues_summary(issues: Sequence[Issue]) -> Tuple[int, int]:
    errors = sum(1 for i in issues if i.level == "ERROR")
    warns = sum(1 for i in issues if i.level == "WARN")
    return errors, warns


def _validate_requirements_files(
    repo_root: Path, docs_dir: Path, validator: Draft7Validator
) -> List[Issue]:
    issues: List[Issue] = []
    if not docs_dir.exists():
        return [Issue("WARN", "DOCS_DIR_MISSING", f"docs dir not found: {docs_dir}", str(docs_dir))]

    req_files = sorted(p for p in docs_dir.rglob("requirements.md") if p.is_file())
    for req_file in req_files:
        rel = str(req_file.relative_to(repo_root))
        try:
            text = _read_text(req_file)
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("WARN", "READ_FAIL", f"Cannot read: {exc}", rel))
            continue

        blocks = _extract_fence(text, "requirements-registry")
        if not blocks:
            issues.append(Issue("WARN", "REQ_REGISTRY_MISSING", "Missing requirements-registry fence", rel))
            continue
        if len(blocks) > 1:
            issues.append(Issue("WARN", "REQ_REGISTRY_MULTI", "Multiple requirements-registry fences found", rel))

        registry, parse_issues = _load_yaml(blocks[0], path_hint=rel)
        issues.extend(parse_issues)
        if not registry:
            continue

        for err in validator.iter_errors(registry):
            issues.append(Issue("ERROR", "REQ_SCHEMA", err.message, rel))

        reqs = registry.get("requirements")
        if not isinstance(reqs, list):
            continue
        for req in reqs:
            if not isinstance(req, dict):
                continue
            pr = req.get("priority") if isinstance(req.get("priority"), str) else ""
            if pr in {"P0", "P1"}:
                acc = req.get("acceptance")
                if not isinstance(acc, list) or not acc:
                    rid = req.get("id") if isinstance(req.get("id"), str) else "(unknown)"
                    issues.append(Issue("WARN", "ACCEPTANCE_MISSING", f"{rid}: P0/P1 missing acceptance[]", rel))

    return issues


def _validate_architecture_files(
    repo_root: Path, project_root: Path, arch_dir: Path, validator: Draft7Validator
) -> List[Issue]:
    issues: List[Issue] = []
    if not arch_dir.exists():
        return [Issue("WARN", "ARCH_DIR_MISSING", f"architecture dir not found: {arch_dir}", str(arch_dir))]

    required = ["overview.md", "database-schema.md", "core-flows.md", "api-spec.md"]
    for name in required:
        path = arch_dir / name
        if not path.exists():
            issues.append(Issue("WARN", "ARCH_FILE_MISSING", f"Missing architecture file: {path}", str(path)))

    md_files = sorted(p for p in arch_dir.rglob("*.md") if p.is_file())
    for md_file in md_files:
        rel = str(md_file.relative_to(repo_root))
        try:
            text = _read_text(md_file)
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("WARN", "READ_FAIL", f"Cannot read: {exc}", rel))
            continue

        blocks = _extract_fence(text, "architecture-registry")
        if not blocks:
            issues.append(Issue("WARN", "ARCH_REGISTRY_MISSING", "Missing architecture-registry fence", rel))
            continue
        if len(blocks) > 1:
            issues.append(Issue("WARN", "ARCH_REGISTRY_MULTI", "Multiple architecture-registry fences found", rel))

        registry, parse_issues = _load_yaml(blocks[0], path_hint=rel)
        issues.extend(parse_issues)
        if not registry:
            continue

        for err in validator.iter_errors(registry):
            issues.append(Issue("ERROR", "ARCH_SCHEMA", err.message, rel))

        items = registry.get("items")
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            sources = item.get("sources")
            if not isinstance(sources, list):
                continue
            for src in sources:
                if not isinstance(src, dict):
                    continue
                spath = src.get("path")
                if not isinstance(spath, str) or not spath:
                    continue
                file_part, anchor = _split_anchor(spath)
                target = (project_root / file_part).resolve()
                if not target.exists():
                    issues.append(Issue("ERROR", "SOURCE_MISSING", f"Missing source file: {file_part}", rel))
                    continue
                if anchor and not _file_contains_anchor(target, anchor):
                    issues.append(Issue("WARN", "ANCHOR_MISSING", f"Anchor not found: {spath}", rel))
    return issues


def _validate_interfaces_file(repo_root: Path, interfaces_file: Path) -> List[Issue]:
    if not interfaces_file.exists():
        return [Issue("WARN", "IFC_FILE_MISSING", f"interfaces.md not found: {interfaces_file}", str(interfaces_file))]

    rel = str(interfaces_file.relative_to(repo_root))
    try:
        text = _read_text(interfaces_file)
    except Exception as exc:  # noqa: BLE001
        return [Issue("WARN", "READ_FAIL", f"Cannot read: {exc}", rel)]

    blocks = _extract_fence(text, "interfaces-registry")
    if not blocks:
        return [Issue("WARN", "IFC_REGISTRY_MISSING", "Missing interfaces-registry fence", rel)]
    return []


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(description="CAF artifact validator (schemas + basic traceability checks).")
    parser.add_argument("--root", default=".", help="Repository root (default: .)")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root used to resolve docs/* source paths (default: same as --root)",
    )
    parser.add_argument("--docs-dir", default="docs", help="Docs directory (default: docs)")
    parser.add_argument("--arch-dir", default="docs/architecture", help="Architecture directory (default: docs/architecture)")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings (as well as errors)")
    args = parser.parse_args(argv)

    repo_root = Path(args.root).resolve()
    project_root = (repo_root / args.project_root).resolve()
    docs_dir = (repo_root / args.docs_dir).resolve()
    arch_dir = (repo_root / args.arch_dir).resolve()

    req_schema = _load_schema(repo_root / ".agent/schemas/requirements-registry.schema.yaml")
    arch_schema = _load_schema(repo_root / ".agent/schemas/architecture-registry.schema.yaml")

    issues: List[Issue] = []
    issues.extend(_validate_requirements_files(repo_root, docs_dir, req_schema))
    issues.extend(_validate_interfaces_file(repo_root, docs_dir / "L2/interfaces.md"))
    issues.extend(_validate_architecture_files(repo_root, project_root, arch_dir, arch_schema))

    errors, warns = _issues_summary(issues)
    for issue in issues:
        where = f" ({issue.file})" if issue.file else ""
        print(f"{issue.level} {issue.code}: {issue.message}{where}")

    print(f"\nSummary: {errors} errors, {warns} warnings")

    if errors:
        return 2
    if warns:
        return 2 if args.strict else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
