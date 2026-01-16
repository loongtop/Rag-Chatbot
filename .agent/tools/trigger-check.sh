#!/usr/bin/env bash
set -euo pipefail

root="${1:-.}"

cd "$root"

bold() { printf "\033[1m%s\033[0m" "$1"; }
ok() { printf "[x] %s\n" "$1"; }
no() { printf "[ ] %s\n" "$1"; }

has_file() { [[ -f "$1" ]]; }
has_any_glob() { compgen -G "$1" >/dev/null 2>&1; }
has_files_under() { [[ -d "$1" ]] && find "$1" -type f -print -quit | grep -q .; }

get_freeze_frozen() {
  # Best-effort YAML read without external deps.
  # Prints: true|false|unknown
  if ! has_file "charter.yaml"; then
    echo "unknown"
    return 0
  fi
  awk '
    $1 == "freeze:" { in_freeze=1; next }
    in_freeze && $1 == "frozen:" { print $2; exit }
    in_freeze && $0 !~ /^[[:space:]]/ { in_freeze=0 }
  ' charter.yaml | tr -d '"' | tr -d "'" | tr -d '\r' | {
    read -r v || true
    case "$v" in
      true|false) echo "$v" ;;
      *) echo "unknown" ;;
    esac
  }
}

echo "$(bold "CAF Trigger Check (v0.6.5)")"
echo "root: $(pwd)"
echo

next_hint=""

# Phase 0: Charter
if has_file "charter.yaml"; then
  ok "Charter exists: charter.yaml"
else
  no "Charter exists: charter.yaml"
  next_hint="Create charter: cp charter.template.yaml charter.yaml (or /charter-init), then /charter-validate"
fi

frozen="$(get_freeze_frozen)"
if [[ "$frozen" == "true" ]]; then
  ok "Charter frozen: freeze.frozen=true"
elif [[ "$frozen" == "false" ]]; then
  no "Charter frozen: freeze.frozen=true"
  next_hint="${next_hint:-Run /charter-freeze (after /charter-validate)}"
else
  no "Charter frozen: freeze.frozen=true (unknown)"
  next_hint="${next_hint:-Check charter.yaml freeze block, then /charter-freeze}"
fi

echo

# Phase 1: Requirements (L0→L2)
if has_file "docs/L0/requirements.md"; then
  ok "L0 requirements: docs/L0/requirements.md"
else
  no "L0 requirements: docs/L0/requirements.md"
  next_hint="${next_hint:-Run /requirements-split source_path=charter.yaml target_dir=docs/L0}"
fi

if has_any_glob "docs/L1/*/requirements.md"; then
  ok "L1 requirements: docs/L1/*/requirements.md"
else
  no "L1 requirements: docs/L1/*/requirements.md (optional)"
fi

if has_any_glob "docs/L2/*/requirements.md"; then
  ok "L2 requirements: docs/L2/*/requirements.md"
else
  no "L2 requirements: docs/L2/*/requirements.md"
  next_hint="${next_hint:-Run /requirements-split source_path=docs/L0/requirements.md target_dir=docs/L2 granularity=medium/direct}"
fi

if has_file "docs/L2/interfaces.md"; then
  ok "L2 interfaces: docs/L2/interfaces.md"
else
  no "L2 interfaces: docs/L2/interfaces.md"
  next_hint="${next_hint:-Generate/Update docs/L2/interfaces.md (interfaces-registry) before /spec}"
fi

if has_file "docs/L2/execution-tracker.md"; then
  ok "Execution tracker: docs/L2/execution-tracker.md"
else
  no "Execution tracker: docs/L2/execution-tracker.md"
fi

echo

# Phase 1.5: Architecture
arch_ok=true
for f in overview.md database-schema.md core-flows.md api-spec.md; do
  if has_file "docs/architecture/$f"; then
    ok "Architecture: docs/architecture/$f"
  else
    no "Architecture: docs/architecture/$f"
    arch_ok=false
  fi
done
if [[ "$arch_ok" != "true" ]]; then
  next_hint="${next_hint:-Run /architecture-generate then /architecture-validate}"
fi

echo

# Phase 2: Specs
if has_any_glob "specs/SPEC-*.md"; then
  ok "Specs: specs/SPEC-*.md"
else
  no "Specs: specs/SPEC-*.md"
  next_hint="${next_hint:-Run /spec source_path=docs/L2/<module>/requirements.md target_dir=specs}"
fi
if has_file "specs/spec-tree.md"; then
  ok "Spec tree: specs/spec-tree.md"
else
  no "Spec tree: specs/spec-tree.md"
fi

echo

# Phase 3: Code & Tests
if has_files_under "src"; then
  ok "Source exists under src/"
else
  no "Source exists under src/"
  next_hint="${next_hint:-Implement leaf Specs into src/ (Coder)}"
fi

if has_files_under "tests"; then
  ok "Tests exist under tests/"
else
  no "Tests exist under tests/"
  next_hint="${next_hint:-Add tests from leaf Spec acceptance tests (Tester)}"
fi

echo
echo "$(bold "Recommended Next")"
echo "- ${next_hint:-Run /charter-quality and /charter-status}"
