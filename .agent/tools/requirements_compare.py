#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

import yaml


FENCE_RE = re.compile(r"```(?P<lang>[a-zA-Z0-9_-]+)[ \t]*\n(?P<body>.*?)\n```", re.DOTALL)
FRONT_MATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)


@dataclasses.dataclass(frozen=True)
class Issue:
    level: str  # ERROR | WARN
    code: str
    message: str
    file: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class ReqReport:
    root: str
    files_scanned: int
    req_files: int
    layers: Dict[str, int]
    total_requirements: int
    by_priority: Dict[str, int]
    missing_sources: int
    missing_acceptance_p01: int
    registry_parse_errors: int
    missing_summary_section: int
    missing_traceability_section: int
    missing_gate_section: int
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


def _parse_front_matter(text: str) -> Dict[str, Any]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group("body")) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def _count_placeholders(markdown: str) -> Tuple[int, int]:
    mustache = len(re.findall(r"\{\{[^}]+\}\}", markdown))
    tbd = len(re.findall(r"\b(TBD|TODO)\b", markdown, flags=re.IGNORECASE))
    return mustache, tbd


def _has_section(text: str, heading: str) -> bool:
    return re.search(rf"^##\s+{re.escape(heading)}\s*$", text, flags=re.MULTILINE) is not None


def _scan_docs(root: Path) -> ReqReport:
    issues: List[Issue] = []
    md_files = sorted([p for p in root.rglob("*.md") if p.is_file()])
    req_files = [p for p in md_files if p.name == "requirements.md"]

    layers: Dict[str, int] = {}
    total_requirements = 0
    by_priority: Dict[str, int] = {}
    missing_sources = 0
    missing_acceptance_p01 = 0
    registry_parse_errors = 0
    missing_summary_section = 0
    missing_traceability_section = 0
    missing_gate_section = 0
    placeholders_mustache = 0
    placeholders_tbd = 0

    for file_path in req_files:
        try:
            text = _read_text(file_path)
        except Exception as exc:  # noqa: BLE001
            issues.append(Issue("WARN", "READ_FAIL", f"Cannot read: {exc}", str(file_path)))
            continue

        mustache, tbd = _count_placeholders(text)
        placeholders_mustache += mustache
        placeholders_tbd += tbd

        fm = _parse_front_matter(text)
        layer = fm.get("layer") if isinstance(fm.get("layer"), str) else "unknown"
        layers[layer] = layers.get(layer, 0) + 1

        blocks = _extract_fence(text, "requirements-registry")
        if not blocks:
            registry_parse_errors += 1
            issues.append(Issue("WARN", "REQ_REGISTRY_MISSING", "Missing requirements-registry fence", str(file_path)))
            continue
        if len(blocks) > 1:
            issues.append(Issue("WARN", "REQ_REGISTRY_MULTI", "Multiple requirements-registry fences found", str(file_path)))

        try:
            registry = yaml.safe_load(blocks[0]) or {}
        except Exception as exc:  # noqa: BLE001
            registry_parse_errors += 1
            issues.append(Issue("ERROR", "YAML_PARSE", f"Registry YAML parse failed: {exc}", str(file_path)))
            continue
        if not isinstance(registry, dict):
            registry_parse_errors += 1
            issues.append(Issue("ERROR", "YAML_TYPE", "Registry must be a YAML mapping/object", str(file_path)))
            continue

        reqs = registry.get("requirements")
        if not isinstance(reqs, list):
            continue

        if not _has_section(text, "Summary"):
            missing_summary_section += 1
        if not _has_section(text, "Traceability"):
            missing_traceability_section += 1
        if not _has_section(text, "Gate Check"):
            missing_gate_section += 1

        for req in reqs:
            if not isinstance(req, dict):
                continue
            total_requirements += 1
            pr = req.get("priority") if isinstance(req.get("priority"), str) else "?"
            by_priority[pr] = by_priority.get(pr, 0) + 1

            sources = req.get("sources")
            if not isinstance(sources, list) or not sources:
                missing_sources += 1

            if pr in {"P0", "P1"}:
                acc = req.get("acceptance")
                if not isinstance(acc, list) or not acc:
                    missing_acceptance_p01 += 1

    return ReqReport(
        root=str(root),
        files_scanned=len(md_files),
        req_files=len(req_files),
        layers=layers,
        total_requirements=total_requirements,
        by_priority=by_priority,
        missing_sources=missing_sources,
        missing_acceptance_p01=missing_acceptance_p01,
        registry_parse_errors=registry_parse_errors,
        missing_summary_section=missing_summary_section,
        missing_traceability_section=missing_traceability_section,
        missing_gate_section=missing_gate_section,
        placeholders_mustache=placeholders_mustache,
        placeholders_tbd=placeholders_tbd,
        issues=issues,
    )


def _format_dict(d: Dict[str, int]) -> str:
    items = sorted(d.items(), key=lambda x: x[0])
    return ", ".join(f"{k}={v}" for k, v in items) if items else "(none)"


def _print_report(label: str, report: ReqReport) -> None:
    print(f"\n== {label} ==")
    print(f"root: {report.root}")
    print(f"md_files: {report.files_scanned}")
    print(f"requirements.md: {report.req_files}")
    print(f"layers: {_format_dict(report.layers)}")
    print(f"total_requirements: {report.total_requirements}")
    print(f"by_priority: {_format_dict(report.by_priority)}")
    print(f"missing_sources: {report.missing_sources}")
    print(f"missing_acceptance(P0/P1): {report.missing_acceptance_p01}")
    print(f"registry_parse_errors: {report.registry_parse_errors}")
    print(f"missing_section(Summary): {report.missing_summary_section}")
    print(f"missing_section(Traceability): {report.missing_traceability_section}")
    print(f"missing_section(Gate Check): {report.missing_gate_section}")
    print(f"placeholders: mustache:{report.placeholders_mustache}, TBD/TODO:{report.placeholders_tbd}")

    err_count = sum(1 for i in report.issues if i.level == "ERROR")
    warn_count = sum(1 for i in report.issues if i.level == "WARN")
    if err_count or warn_count:
        print(f"issues: {err_count} errors, {warn_count} warnings")
        for issue in report.issues[:40]:
            where = f" ({issue.file})" if issue.file else ""
            print(f"- {issue.level} {issue.code}: {issue.message}{where}")
        if len(report.issues) > 40:
            print(f"... ({len(report.issues) - 40} more)")


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(description="Compare CAF requirements docs across two outputs.")
    parser.add_argument("--baseline", required=True, help="Baseline docs dir (e.g., docs)")
    parser.add_argument("--candidate", required=True, help="Candidate docs dir (e.g., docs.__caf_v063__)")
    parser.add_argument("--strict", action="store_true", help="Non-zero exit if any ERROR exists")
    args = parser.parse_args(argv)

    baseline = Path(args.baseline).resolve()
    candidate = Path(args.candidate).resolve()

    baseline_report = _scan_docs(baseline)
    candidate_report = _scan_docs(candidate)

    _print_report("BASELINE", baseline_report)
    _print_report("CANDIDATE", candidate_report)

    print("\n== DELTA (candidate - baseline) ==")
    print(f"requirements.md: {candidate_report.req_files - baseline_report.req_files:+d}")
    print(f"total_requirements: {candidate_report.total_requirements - baseline_report.total_requirements:+d}")
    print(f"missing_sources: {candidate_report.missing_sources - baseline_report.missing_sources:+d}")
    print(f"missing_acceptance(P0/P1): {candidate_report.missing_acceptance_p01 - baseline_report.missing_acceptance_p01:+d}")
    print(f"registry_parse_errors: {candidate_report.registry_parse_errors - baseline_report.registry_parse_errors:+d}")
    print(f"missing_section(Summary): {candidate_report.missing_summary_section - baseline_report.missing_summary_section:+d}")
    print(f"missing_section(Traceability): {candidate_report.missing_traceability_section - baseline_report.missing_traceability_section:+d}")
    print(f"missing_section(Gate Check): {candidate_report.missing_gate_section - baseline_report.missing_gate_section:+d}")
    print(f"placeholders_mustache: {candidate_report.placeholders_mustache - baseline_report.placeholders_mustache:+d}")
    print(f"placeholders_tbd: {candidate_report.placeholders_tbd - baseline_report.placeholders_tbd:+d}")

    if args.strict:
        has_error = any(i.level == "ERROR" for i in (baseline_report.issues + candidate_report.issues))
        return 2 if has_error else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

