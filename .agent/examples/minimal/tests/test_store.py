from __future__ import annotations

from pathlib import Path

import pytest

from notes_app.store import add_note, list_notes


def test_list_missing_file_returns_empty(tmp_path: Path) -> None:
    store = tmp_path / "notes.json"
    assert list_notes(store) == []


def test_add_note_creates_store_file(tmp_path: Path) -> None:
    store = tmp_path / "notes.json"
    note = add_note(store, "hello")
    assert store.exists()
    assert note.content == "hello"
    assert note.created_at


def test_list_notes_descending(tmp_path: Path) -> None:
    store = tmp_path / "notes.json"
    add_note(store, "a")
    add_note(store, "b")
    notes = list_notes(store)
    assert [n.content for n in notes] == ["b", "a"]


def test_add_note_rejects_empty_content(tmp_path: Path) -> None:
    store = tmp_path / "notes.json"
    with pytest.raises(ValueError, match="non-empty"):
        add_note(store, "   ")

