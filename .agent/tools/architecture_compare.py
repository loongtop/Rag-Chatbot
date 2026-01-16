#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

import yaml
from jsonschema import Draft7Validator


FENCE_RE = re.compile(r"```(?P<lang>[a-zA-Z0-9_-]+)[ \t]*\n(?P<body>.*?)\n```", re.DOTALL)


@dataclasses.dataclass(frozen=True)
class Issue:
    level: str  # "ERROR" | "WARN"
    code: str
    message: str
    file: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class DirReport:
    dir_path: str
    files_scanned: int
    registry_files: int
    arch_items: int
    schema_errors: int
    source_errors: int
    missing_rationale: int
    l2_req_total: int
    l2_req_referenced: int
    l2_req_unreferenced: List[str]
    ifc_total: int
    ifc_referenced: int
    ifc_unreferenced: List[str]
    placeholders_mustache: int
    placeholders_tbd: int
    issues: List[Issue]


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
    except Exception as exc:  # noqa: BLE001 - best-effort tool
        return None, [Issue("ERROR", "YAML_PARSE", f"{path_hint}: YAML parse failed: {exc}")]
    if not isinstance(data, dict):
        return None, [Issue("ERROR", "YAML_TYPE", f"{path_hint}: registry must be a YAML mapping/object")]
    return data, []


def _load_schema(schema_path: Path) -> Draft7Validator:
    schema_text = _read_text(schema_path)
    schema = yaml.safe_load(schema_text)
    if not isinstance(schema, dict):
        raise ValueError(f"Invalid schema file: {schema_path}")
    return Draft7Validator(schema)


def _split_anchor(path_with_anchor: str) -> Tuple[str, Optional[str]]:
    if "#" not in path_with_anchor:
        return path_with_anchor, None
    path_part, anchor = path_with_anchor.split("#", 1)
    return path_part, anchor or None


def _file_contains_id(target_file: Path, anchor_id: str) -> bool:
    if not anchor_id:
        return True
    try:
        text = _read_text(target_file)
    except Exception:
        return False
    return re.search(rf"\b{re.escape(anchor_id)}\b", text) is not None


def _count_placeholders(markdown: str) -> Tuple[int, int]:
    mustache = len(re.findall(r"\{\{[^}]+\}\}", markdown))
    tbd = len(re.findall(r"\b(TBD|TODO)\b", markdown, flags=re.IGNORECASE))
    return mustache, tbd


def _collect_l2_req_ids(l2_dir: Path) -> Tuple[Set[str], List[Issue]]:
    issues: List[Issue] = []
    ids: Set[str] = set()
    if not l2_dir.exists():
        return ids, [Issue("WARN", "L2_DIR_MISSING", f"L2 dir not found: {l2_dir}")]

    for req_file in sorted(l2_dir.glob("*/requirements.md")):
        try:
            text = _read_text(req_file)
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("WARN", "READ_FAIL", f"Cannot read {req_file}: {exc}", str(req_file)))
            continue

        blocks = _extract_fence(text, "requirements-registry")
        if not blocks:
            issues.append(Issue("WARN", "REQ_REGISTRY_MISSING", "Missing requirements-registry fence", str(req_file)))
            continue
        if len(blocks) > 1:
            issues.append(Issue("WARN", "REQ_REGISTRY_MULTI", "Multiple requirements-registry fences found", str(req_file)))

        data, parse_issues = _load_yaml(blocks[0], path_hint=str(req_file))
        issues.extend(parse_issues)
        if not data:
            continue
        reqs = data.get("requirements")
        if not isinstance(reqs, list):
            issues.append(Issue("WARN", "REQ_LIST_MISSING", "requirements[] missing or not a list", str(req_file)))
            continue
        for item in reqs:
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                ids.add(item["id"])
    return ids, issues


def _collect_ifc_ids(interfaces_file: Path) -> Tuple[Set[str], List[Issue]]:
    issues: List[Issue] = []
    ids: Set[str] = set()
    if not interfaces_file.exists():
        return ids, [Issue("WARN", "IFC_FILE_MISSING", f"interfaces.md not found: {interfaces_file}")]

    try:
        text = _read_text(interfaces_file)
    except Exception as exc:  # noqa: BLE001
        return ids, [Issue("WARN", "READ_FAIL", f"Cannot read {interfaces_file}: {exc}", str(interfaces_file))]

    blocks = _extract_fence(text, "interfaces-registry")
    if not blocks:
        return ids, [Issue("WARN", "IFC_REGISTRY_MISSING", "Missing interfaces-registry fence", str(interfaces_file))]
    if len(blocks) > 1:
        issues.append(Issue("WARN", "IFC_REGISTRY_MULTI", "Multiple interfaces-registry fences found", str(interfaces_file)))

    data, parse_issues = _load_yaml(blocks[0], path_hint=str(interfaces_file))
    issues.extend(parse_issues)
    if not data:
        return ids, issues
    interfaces = data.get("interfaces")
    if not isinstance(interfaces, list):
        issues.append(Issue("WARN", "IFC_LIST_MISSING", "interfaces[] missing or not a list", str(interfaces_file)))
        return ids, issues

    for item in interfaces:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            ids.add(item["id"])
    return ids, issues


def _validate_architecture_dir(
    base_dir: Path,
    *,
    validator: Draft7Validator,
    repo_root: Path,
    l2_req_ids: Set[str],
    ifc_ids: Set[str],
) -> DirReport:
    issues: List[Issue] = []

    if not base_dir.exists():
        return DirReport(
            dir_path=str(base_dir),
            files_scanned=0,
            registry_files=0,
            arch_items=0,
            schema_errors=1,
            source_errors=1,
            missing_rationale=0,
            l2_req_total=len(l2_req_ids),
            l2_req_referenced=0,
            l2_req_unreferenced=sorted(l2_req_ids),
            ifc_total=len(ifc_ids),
            ifc_referenced=0,
            ifc_unreferenced=sorted(ifc_ids),
            placeholders_mustache=0,
            placeholders_tbd=0,
            issues=[Issue("ERROR", "ARCH_DIR_MISSING", f"Architecture dir not found: {base_dir}")],
        )

    md_files = sorted([p for p in base_dir.rglob("*.md") if p.is_file()])
    files_scanned = len(md_files)

    registry_files = 0
    arch_items = 0
    schema_errors = 0
    source_errors = 0
    missing_rationale = 0
    referenced_sources: Set[str] = set()
    placeholders_mustache = 0
    placeholders_tbd = 0

    for md_file in md_files:
        try:
            text = _read_text(md_file)
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("WARN", "READ_FAIL", f"Cannot read {md_file}: {exc}", str(md_file)))
            continue

        mustache, tbd = _count_placeholders(text)
        placeholders_mustache += mustache
        placeholders_tbd += tbd

        blocks = _extract_fence(text, "architecture-registry")
        if not blocks:
            continue

        registry_files += 1
        if len(blocks) > 1:
            issues.append(Issue("WARN", "ARCH_REGISTRY_MULTI", "Multiple architecture-registry fences found", str(md_file)))

        registry, parse_issues = _load_yaml(blocks[0], path_hint=str(md_file))
        issues.extend(parse_issues)
        if not registry:
            schema_errors += 1
            continue

        for err in validator.iter_errors(registry):
            schema_errors += 1
            issues.append(Issue("ERROR", "SCHEMA", f"{err.message}", str(md_file)))

        items = registry.get("items")
        if not isinstance(items, list):
            continue

        doc_type = registry.get("type")
        expected_prefix: Optional[str] = None
        if doc_type == "overview":
            expected_prefix = "ARCH-OV-"
        elif doc_type == "database":
            expected_prefix = "ARCH-DB-"
        elif doc_type == "flows":
            expected_prefix = "ARCH-FL-"
        elif doc_type == "api":
            expected_prefix = "ARCH-API-"

        for item in items:
            if not isinstance(item, dict):
                continue
            item_id = item.get("id")
            if not isinstance(item_id, str):
                continue

            arch_items += 1
            if expected_prefix and not item_id.startswith(expected_prefix):
                issues.append(
                    Issue(
                        "WARN",
                        "ARCH_ID_PREFIX",
                        f"{item_id}: unexpected prefix for type={doc_type} (expected {expected_prefix}*)",
                        str(md_file),
                    )
                )

            if not isinstance(item.get("rationale"), str) or not item.get("rationale", "").strip():
                missing_rationale += 1

            sources = item.get("sources")
            if not isinstance(sources, list) or not sources:
                source_errors += 1
                issues.append(Issue("ERROR", "MISSING_SOURCES", f"{item_id}: missing sources[]", str(md_file)))
                continue

            for source in sources:
                if not isinstance(source, dict):
                    continue
                source_id = source.get("id")
                source_path = source.get("path")
                if isinstance(source_id, str):
                    referenced_sources.add(source_id)
                if not isinstance(source_path, str) or not source_path.strip():
                    source_errors += 1
                    issues.append(Issue("ERROR", "SOURCE_PATH_MISSING", f"{item_id}: source.path missing", str(md_file)))
                    continue

                path_part, anchor = _split_anchor(source_path.strip())
                target_file = (repo_root / path_part).resolve()
                if not target_file.exists():
                    source_errors += 1
                    issues.append(
                        Issue("ERROR", "SOURCE_FILE_MISSING", f"{item_id}: source file not found: {path_part}", str(md_file))
                    )
                    continue
                if anchor and not _file_contains_id(target_file, anchor):
                    source_errors += 1
                    issues.append(
                        Issue("ERROR", "SOURCE_ANCHOR_MISSING", f"{item_id}: anchor id not found: {source_path}", str(md_file))
                    )

    l2_req_unreferenced = sorted([req_id for req_id in l2_req_ids if req_id not in referenced_sources])
    ifc_unreferenced = sorted([ifc_id for ifc_id in ifc_ids if ifc_id not in referenced_sources])

    return DirReport(
        dir_path=str(base_dir),
        files_scanned=files_scanned,
        registry_files=registry_files,
        arch_items=arch_items,
        schema_errors=schema_errors,
        source_errors=source_errors,
        missing_rationale=missing_rationale,
        l2_req_total=len(l2_req_ids),
        l2_req_referenced=len(l2_req_ids) - len(l2_req_unreferenced),
        l2_req_unreferenced=l2_req_unreferenced,
        ifc_total=len(ifc_ids),
        ifc_referenced=len(ifc_ids) - len(ifc_unreferenced),
        ifc_unreferenced=ifc_unreferenced,
        placeholders_mustache=placeholders_mustache,
        placeholders_tbd=placeholders_tbd,
        issues=issues,
    )


def _format_percent(part: int, total: int) -> str:
    if total <= 0:
        return "n/a"
    return f"{(part / total) * 100:.1f}%"


def _print_report(label: str, report: DirReport) -> None:
    print(f"\n== {label} ==")
    print(f"dir: {report.dir_path}")
    print(f"files_scanned: {report.files_scanned}")
    print(f"registry_files: {report.registry_files}")
    print(f"arch_items: {report.arch_items}")
    print(f"schema_errors: {report.schema_errors}")
    print(f"source_errors: {report.source_errors}")
    print(f"missing_rationale: {report.missing_rationale}")
    print(
        "l2_coverage: "
        f"{report.l2_req_referenced}/{report.l2_req_total} ({_format_percent(report.l2_req_referenced, report.l2_req_total)})"
    )
    print(f"ifc_coverage: {report.ifc_referenced}/{report.ifc_total} ({_format_percent(report.ifc_referenced, report.ifc_total)})")
    print(f"placeholders: mustache:{report.placeholders_mustache}, TBD/TODO:{report.placeholders_tbd}")

    error_count = sum(1 for issue in report.issues if issue.level == "ERROR")
    warn_count = sum(1 for issue in report.issues if issue.level == "WARN")
    print(f"issues: {error_count} errors, {warn_count} warnings")

    if error_count or warn_count:
        for issue in report.issues[:40]:
            where = f" ({issue.file})" if issue.file else ""
            print(f"- {issue.level} {issue.code}: {issue.message}{where}")
        if len(report.issues) > 40:
            print(f"... ({len(report.issues) - 40} more)")


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Compare CAF architecture outputs (docs/architecture) across two runs.",
    )
    parser.add_argument("--baseline", required=True, help="Baseline architecture directory (e.g., docs/architecture)")
    parser.add_argument("--candidate", required=True, help="Candidate architecture directory (e.g., docs/architecture.v063)")
    parser.add_argument("--repo-root", default=".", help="Repo root (default: .)")
    parser.add_argument("--l2-dir", default="docs/L2", help="L2 directory (default: docs/L2)")
    parser.add_argument("--interfaces", default="docs/L2/interfaces.md", help="Interfaces file (default: docs/L2/interfaces.md)")
    parser.add_argument(
        "--schema",
        default=".agent/schemas/architecture-registry.schema.yaml",
        help="Architecture registry schema (default: .agent/schemas/architecture-registry.schema.yaml)",
    )
    parser.add_argument("--strict", action="store_true", help="Non-zero exit if any ERROR exists")
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    schema_path = (repo_root / args.schema).resolve()
    validator = _load_schema(schema_path)

    l2_req_ids, l2_issues = _collect_l2_req_ids((repo_root / args.l2_dir).resolve())
    ifc_ids, ifc_issues = _collect_ifc_ids((repo_root / args.interfaces).resolve())

    baseline_report = _validate_architecture_dir(
        (repo_root / args.baseline).resolve(),
        validator=validator,
        repo_root=repo_root,
        l2_req_ids=l2_req_ids,
        ifc_ids=ifc_ids,
    )
    candidate_report = _validate_architecture_dir(
        (repo_root / args.candidate).resolve(),
        validator=validator,
        repo_root=repo_root,
        l2_req_ids=l2_req_ids,
        ifc_ids=ifc_ids,
    )

    baseline_report = dataclasses.replace(baseline_report, issues=baseline_report.issues + l2_issues + ifc_issues)
    candidate_report = dataclasses.replace(candidate_report, issues=candidate_report.issues + l2_issues + ifc_issues)

    _print_report("BASELINE", baseline_report)
    _print_report("CANDIDATE", candidate_report)

    print("\n== DELTA (candidate - baseline) ==")
    print(f"arch_items: {candidate_report.arch_items - baseline_report.arch_items:+d}")
    print(f"schema_errors: {candidate_report.schema_errors - baseline_report.schema_errors:+d}")
    print(f"source_errors: {candidate_report.source_errors - baseline_report.source_errors:+d}")
    print(f"missing_rationale: {candidate_report.missing_rationale - baseline_report.missing_rationale:+d}")
    print(
        "l2_coverage: "
        f"{candidate_report.l2_req_referenced - baseline_report.l2_req_referenced:+d} "
        f"({candidate_report.l2_req_referenced}/{candidate_report.l2_req_total} vs "
        f"{baseline_report.l2_req_referenced}/{baseline_report.l2_req_total})"
    )
    print(
        "ifc_coverage: "
        f"{candidate_report.ifc_referenced - baseline_report.ifc_referenced:+d} "
        f"({candidate_report.ifc_referenced}/{candidate_report.ifc_total} vs "
        f"{baseline_report.ifc_referenced}/{baseline_report.ifc_total})"
    )
    print(f"placeholders_mustache: {candidate_report.placeholders_mustache - baseline_report.placeholders_mustache:+d}")
    print(f"placeholders_tbd: {candidate_report.placeholders_tbd - baseline_report.placeholders_tbd:+d}")

    if args.strict:
        has_error = any(issue.level == "ERROR" for issue in (baseline_report.issues + candidate_report.issues))
        return 2 if has_error else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
