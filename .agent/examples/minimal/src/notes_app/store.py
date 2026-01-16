from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class Note:
    id: str
    content: str
    created_at: str  # ISO 8601 (UTC)


def _now_iso_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_notes(store_path: str | os.PathLike[str]) -> List[Note]:
    path = Path(store_path)
    if not path.exists():
        return []

    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:  # noqa: PERF203 - clarity over micro-optimizations in examples
        raise ValueError(f"Invalid JSON store: {path}") from exc

    if not isinstance(data, list):
        raise ValueError("Store must be a JSON array")

    notes: List[Note] = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each note must be an object")
        note_id = item.get("id")
        content = item.get("content")
        created_at = item.get("created_at")
        if not (isinstance(note_id, str) and isinstance(content, str) and isinstance(created_at, str)):
            raise ValueError("Invalid note fields")
        notes.append(Note(id=note_id, content=content, created_at=created_at))
    return notes


def _persist_notes(path: Path, notes: List[Note]) -> None:
    payload = [{"id": n.id, "content": n.content, "created_at": n.created_at} for n in notes]
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp_path.replace(path)


def add_note(store_path: str | os.PathLike[str], content: str) -> Note:
    if not content.strip():
        raise ValueError("content must be non-empty")

    path = Path(store_path)
    notes = load_notes(path)
    note = Note(id=str(uuid.uuid4()), content=content, created_at=_now_iso_utc())
    notes.append(note)
    notes.sort(key=lambda n: n.created_at, reverse=True)
    _persist_notes(path, notes)
    return note


def list_notes(store_path: str | os.PathLike[str]) -> List[Note]:
    notes = load_notes(store_path)
    notes.sort(key=lambda n: n.created_at, reverse=True)
    return notes

