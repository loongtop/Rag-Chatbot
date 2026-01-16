#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import yaml


FENCE_RE = re.compile(r"```(?P<lang>[a-zA-Z0-9_-]+)[ \t]*\n(?P<body>.*?)\n```", re.DOTALL)
FRONT_MATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)


@dataclasses.dataclass(frozen=True)
class RegenStats:
    files_total: int = 0
    files_rendered: int = 0
    files_version_bumped: int = 0


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _extract_fence(text: str, lang: str) -> List[str]:
    blocks: List[str] = []
    for match in FENCE_RE.finditer(text):
        if match.group("lang") == lang:
            blocks.append(match.group("body").strip())
    return blocks


def _split_front_matter_raw(md: str) -> Tuple[Optional[str], str]:
    match = FRONT_MATTER_RE.match(md)
    if not match:
        return None, md
    raw = match.group(0)
    remainder = md[len(raw) :]
    return raw, remainder.lstrip("\n")


def _parse_front_matter(raw: str) -> Dict[str, Any]:
    match = FRONT_MATTER_RE.match(raw)
    if not match:
        return {}
    try:
        parsed = yaml.safe_load(match.group("body")) or {}
    except Exception:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _upsert_front_matter_key(raw: Optional[str], key: str, value: str) -> str:
    if not raw:
        fm = {key: value}
        dumped = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).rstrip()
        return f"---\n{dumped}\n---\n\n"

    lines = raw.splitlines()
    # lines include: --- , ... , ---.
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            lines[i] = f"{key}: {value}"
            return "\n".join(lines).rstrip() + "\n\n"

    # insert before the ending --- (last line)
    if lines and lines[-1].strip() == "---":
        lines.insert(len(lines) - 1, f"{key}: {value}")
    return "\n".join(lines).rstrip() + "\n\n"


def _update_registry_schema_version(registry_yaml: str, target_version: str) -> str:
    # Preserve formatting as much as possible; do a minimal line replacement.
    lines = registry_yaml.splitlines()
    for i, line in enumerate(lines):
        match = re.match(r"^(?P<indent>\s*)schema_version:\s*(?P<val>.+?)\s*$", line)
        if not match:
            continue
        val = match.group("val")
        quote = '"' if '"' in val else ("'" if "'" in val else "")
        rendered = f'{quote}{target_version}{quote}' if quote else target_version
        lines[i] = f"{match.group('indent')}schema_version: {rendered}"
        return "\n".join(lines).rstrip()
    # If not found, insert at top.
    return f'schema_version: "{target_version}"\n' + registry_yaml.rstrip()


def _render_requirements_body(registry: Dict[str, Any]) -> str:
    requirements = registry.get("requirements") if isinstance(registry.get("requirements"), list) else []
    tbds = registry.get("tbds") if isinstance(registry.get("tbds"), list) else []
    exclusions = registry.get("exclusions") if isinstance(registry.get("exclusions"), list) else []

    def _get_priority(req: Dict[str, Any]) -> str:
        p = req.get("priority")
        return p if isinstance(p, str) else ""

    def _sources_str(req: Dict[str, Any]) -> str:
        sources = req.get("sources")
        if not isinstance(sources, list):
            return ""
        ids: List[str] = []
        for src in sources:
            if isinstance(src, dict) and isinstance(src.get("id"), str):
                ids.append(src["id"])
        return ", ".join(ids)

    def _acceptance_count(req: Dict[str, Any]) -> int:
        acc = req.get("acceptance")
        return len(acc) if isinstance(acc, list) else 0

    total = len(requirements)
    by_priority: Dict[str, int] = {}
    missing_sources = 0
    missing_acceptance_p01 = 0
    for req in requirements:
        if not isinstance(req, dict):
            continue
        pr = _get_priority(req) or "?"
        by_priority[pr] = by_priority.get(pr, 0) + 1
        sources = req.get("sources")
        if not isinstance(sources, list) or not sources:
            missing_sources += 1
        if pr in {"P0", "P1"} and _acceptance_count(req) == 0:
            missing_acceptance_p01 += 1

    summary_lines = [
        "## Summary",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total requirements | {total} |",
        f"| P0 | {by_priority.get('P0', 0)} |",
        f"| P1 | {by_priority.get('P1', 0)} |",
        f"| P2 | {by_priority.get('P2', 0)} |",
        f"| TBDs | {len(tbds)} |",
        f"| Exclusions | {len(exclusions)} |",
        "",
    ]

    table_lines = [
        "## Requirements",
        "",
        "| ID | Priority | Statement | Sources | Acceptance | Status |",
        "|----|----------|-----------|---------|------------|--------|",
    ]
    for req in requirements:
        if not isinstance(req, dict):
            continue
        rid = req.get("id") if isinstance(req.get("id"), str) else ""
        pr = _get_priority(req)
        st = req.get("statement") if isinstance(req.get("statement"), str) else ""
        st = st.replace("\n", " ").strip()
        if len(st) > 120:
            st = st[:117] + "..."
        srcs = _sources_str(req)
        acc_n = _acceptance_count(req)
        status = req.get("status") if isinstance(req.get("status"), str) else ""
        table_lines.append(f"| {rid} | {pr} | {st} | {srcs} | {acc_n} | {status} |")
    table_lines.append("")

    trace_lines = [
        "## Traceability",
        "",
        "| Requirement | Source ID | Source Path |",
        "|------------|-----------|-------------|",
    ]
    for req in requirements:
        if not isinstance(req, dict):
            continue
        rid = req.get("id") if isinstance(req.get("id"), str) else ""
        sources = req.get("sources")
        if not isinstance(sources, list) or not sources:
            trace_lines.append(f"| {rid} | (missing) | (missing) |")
            continue
        for src in sources:
            if not isinstance(src, dict):
                continue
            sid = src.get("id") if isinstance(src.get("id"), str) else ""
            spath = src.get("path") if isinstance(src.get("path"), str) else ""
            trace_lines.append(f"| {rid} | {sid} | {spath} |")
    trace_lines.append("")

    extras: List[str] = []
    if tbds:
        extras.extend(
            [
                "## TBDs",
                "",
                "| TBD ID | Question | Target Layer | Impact | Status |",
                "|--------|----------|--------------|--------|--------|",
            ]
        )
        for tbd in tbds:
            if not isinstance(tbd, dict):
                continue
            tid = tbd.get("id") if isinstance(tbd.get("id"), str) else ""
            q = ""
            if isinstance(tbd.get("question"), str):
                q = tbd.get("question", "")
            elif isinstance(tbd.get("statement"), str):
                q = tbd.get("statement", "")
            tl = tbd.get("target_layer") if isinstance(tbd.get("target_layer"), str) else ""
            impact = tbd.get("impact") if isinstance(tbd.get("impact"), str) else ""
            status = tbd.get("status") if isinstance(tbd.get("status"), str) else ""
            extras.append(f"| {tid} | {q} | {tl} | {impact} | {status} |")
        extras.append("")

    if exclusions:
        extras.extend(["## Exclusions", ""])
        for ex in exclusions:
            if isinstance(ex, dict):
                src = ex.get("source") if isinstance(ex.get("source"), str) else ""
                reason = ex.get("reason") if isinstance(ex.get("reason"), str) else ""
                extras.append(f"- {src}: {reason}".rstrip())
            elif isinstance(ex, str):
                extras.append(f"- {ex}")
        extras.append("")

    gate_lines = [
        "## Gate Check",
        "",
        f"- [{'x' if missing_sources == 0 else ' '}] All requirements have `sources[]` ({total - missing_sources}/{total})",
        f"- [{'x' if missing_acceptance_p01 == 0 else ' '}] All P0/P1 have `acceptance[]`",
        "",
    ]

    return "\n".join(summary_lines + table_lines + trace_lines + extras + gate_lines).rstrip() + "\n"


def _render_requirements_doc(
    md_path: Path,
    *,
    target_caf_version: str,
    render_body: bool,
    bump_schema_version: bool,
) -> Tuple[str, bool, bool]:
    """
    Returns (new_markdown, did_render, did_bump).
    """
    original = _read_text(md_path)
    fm_raw, remainder = _split_front_matter_raw(original)
    fm_raw = _upsert_front_matter_key(fm_raw, "caf_version", target_caf_version) if target_caf_version else (fm_raw or "")

    fm_parsed = _parse_front_matter(fm_raw)
    blocks = _extract_fence(remainder, "requirements-registry")
    if not blocks:
        return (fm_raw + remainder) if fm_raw else remainder, False, True

    registry_yaml = blocks[0]
    bumped = False
    if bump_schema_version and target_caf_version:
        updated_registry_yaml = _update_registry_schema_version(registry_yaml, target_caf_version)
        bumped = updated_registry_yaml != registry_yaml
    else:
        updated_registry_yaml = registry_yaml

    registry_data = yaml.safe_load(updated_registry_yaml) or {}
    if not isinstance(registry_data, dict):
        registry_data = {}

    # Replace only the first registry block, keep other markdown intact around it.
    def _replace_first_registry(md: str) -> str:
        replaced = False

        def _sub(match: re.Match[str]) -> str:
            nonlocal replaced
            if replaced or match.group("lang") != "requirements-registry":
                return match.group(0)
            replaced = True
            return f"```requirements-registry\n{updated_registry_yaml}\n```"

        return FENCE_RE.sub(_sub, md, count=0)

    new_remainder = _replace_first_registry(remainder)

    did_render = False
    if render_body:
        # Append missing generated sections without overwriting any hand-written text.
        # This preserves manual rationale sections while improving readability/consistency.

        def _has_heading(heading: str) -> bool:
            return re.search(rf"^##\s+{re.escape(heading)}\s*$", new_remainder, flags=re.MULTILINE) is not None

        def _split_h2_sections(body: str) -> Dict[str, str]:
            sections: Dict[str, List[str]] = {}
            current: Optional[str] = None
            for line in body.splitlines():
                match = re.match(r"^##\s+(?P<title>.+?)\s*$", line)
                if match:
                    current = match.group("title")
                    sections.setdefault(current, []).append(line)
                    continue
                if current is not None:
                    sections[current].append(line)
            return {k: ("\n".join(v).rstrip() + "\n") for k, v in sections.items()}

        generated = _render_requirements_body(registry_data)
        generated_sections = _split_h2_sections(generated)
        desired_order = ["Summary", "Requirements", "Traceability", "TBDs", "Exclusions", "Gate Check"]

        append_blocks: List[str] = []
        for heading in desired_order:
            if _has_heading(heading):
                continue
            section = generated_sections.get(heading)
            if section:
                append_blocks.append(section.strip())

        if append_blocks:
            new_remainder = new_remainder.rstrip() + "\n\n---\n\n" + "\n\n".join(append_blocks).rstrip() + "\n"
            did_render = True

    final = (fm_raw + new_remainder.lstrip("\n")) if fm_raw else new_remainder.lstrip("\n")
    # Preserve a single trailing newline.
    if not final.endswith("\n"):
        final += "\n"
    return final, did_render, bumped or True


def _copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def _iter_requirement_docs(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("requirements.md") if p.is_file()])


def _iter_interfaces_docs(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("interfaces.md") if p.is_file()])


def _iter_split_reports(root: Path) -> List[Path]:
    return sorted([p for p in root.rglob("split-report.md") if p.is_file()])


def _bump_interfaces_doc(md_path: Path, *, target_caf_version: str, bump_schema_version: bool) -> bool:
    original = _read_text(md_path)
    fm_raw, remainder = _split_front_matter_raw(original)
    fm_raw = _upsert_front_matter_key(fm_raw, "caf_version", target_caf_version) if target_caf_version else (fm_raw or "")

    blocks = _extract_fence(remainder, "interfaces-registry")
    if not blocks:
        _write_text(md_path, (fm_raw + remainder) if fm_raw else remainder)
        return True

    registry_yaml = blocks[0]
    if bump_schema_version and target_caf_version:
        registry_yaml = _update_registry_schema_version(registry_yaml, target_caf_version)

    replaced = False

    def _sub(match: re.Match[str]) -> str:
        nonlocal replaced
        if replaced or match.group("lang") != "interfaces-registry":
            return match.group(0)
        replaced = True
        return f"```interfaces-registry\n{registry_yaml}\n```"

    new_remainder = FENCE_RE.sub(_sub, remainder)
    final = (fm_raw + new_remainder.lstrip("\n")) if fm_raw else new_remainder.lstrip("\n")
    if not final.endswith("\n"):
        final += "\n"
    _write_text(md_path, final)
    return True


def _bump_split_report(md_path: Path, *, target_caf_version: str) -> bool:
    original = _read_text(md_path)
    fm_raw, remainder = _split_front_matter_raw(original)
    fm_raw = _upsert_front_matter_key(fm_raw, "caf_version", target_caf_version) if target_caf_version else (fm_raw or "")

    # Minimal, targeted replacements in body (avoid touching unrelated version strings).
    new_remainder = remainder
    new_remainder = re.sub(
        r"^(#\s+Split Report:.*\()v0\.[0-9]+\.[0-9]+(\).*)$",
        rf"\g<1>{target_caf_version}\2",
        new_remainder,
        flags=re.MULTILINE,
    )
    new_remainder = re.sub(
        r"^(\s*-\s*\*\*CAF Version\*\*:\s*)v0\.[0-9]+\.[0-9]+\s*$",
        rf"\g<1>{target_caf_version}",
        new_remainder,
        flags=re.MULTILINE,
    )
    new_remainder = re.sub(r"\bv0\.6\.0\b", target_caf_version, new_remainder)

    final = (fm_raw + new_remainder.lstrip("\n")) if fm_raw else new_remainder.lstrip("\n")
    if not final.endswith("\n"):
        final += "\n"
    _write_text(md_path, final)
    return True


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(description="Regenerate CAF docs/L0-L2 into a candidate directory for comparison.")
    parser.add_argument("--baseline", default="docs", help="Baseline docs directory (default: docs)")
    parser.add_argument("--output", default="docs.__caf_v063__", help="Candidate docs directory to write")
    parser.add_argument("--caf-version", default="v0.6.5", help="CAF version tag to write into front matter")
    parser.add_argument(
        "--bump-schema-version",
        action="store_true",
        help="Update requirements-registry.schema_version to match --caf-version",
    )
    parser.add_argument(
        "--render-layers",
        default="L1,L2",
        help="Comma-separated layers to render body for (default: L1,L2). Use 'none' to disable.",
    )
    args = parser.parse_args(argv)

    baseline = Path(args.baseline).resolve()
    output = Path(args.output).resolve()

    if not baseline.exists():
        print(f"ERROR: baseline dir not found: {baseline}", file=sys.stderr)
        return 2

    _copy_tree(baseline, output)

    render_layers = set()
    if args.render_layers.strip().lower() != "none":
        render_layers = {x.strip() for x in args.render_layers.split(",") if x.strip()}

    stats = RegenStats()
    for doc in _iter_requirement_docs(output):
        stats = dataclasses.replace(stats, files_total=stats.files_total + 1)
        md = _read_text(doc)
        fm_raw, _ = _split_front_matter_raw(md)
        fm = _parse_front_matter(fm_raw or "")
        layer = fm.get("layer") if isinstance(fm.get("layer"), str) else ""
        render_body = layer in render_layers

        new_md, did_render, _did_bump = _render_requirements_doc(
            doc,
            target_caf_version=args.caf_version,
            render_body=render_body,
            bump_schema_version=args.bump_schema_version,
        )
        _write_text(doc, new_md)
        if did_render:
            stats = dataclasses.replace(stats, files_rendered=stats.files_rendered + 1)
        stats = dataclasses.replace(stats, files_version_bumped=stats.files_version_bumped + 1)

    for doc in _iter_interfaces_docs(output):
        _bump_interfaces_doc(doc, target_caf_version=args.caf_version, bump_schema_version=args.bump_schema_version)

    for doc in _iter_split_reports(output):
        _bump_split_report(doc, target_caf_version=args.caf_version)

    print("OK: regenerated docs")
    print(f"baseline: {baseline}")
    print(f"output:   {output}")
    print(f"requirements.md files: {stats.files_total}")
    print(f"rendered body:         {stats.files_rendered}")
    print(f"caf_version updated:   {stats.files_version_bumped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
