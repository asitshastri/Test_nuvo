"""CLI smoke test for src.load_inherited (dry-run writes nothing)."""

import sys
from pathlib import Path

import pytest

from src import load_inherited


def test_dry_run(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    root = Path(__file__).resolve().parent.parent
    monkeypatch.chdir(root)
    monkeypatch.setattr(sys, "argv", ["load_inherited", "--dry-run"])
    load_inherited.main()
    out = capsys.readouterr().out
    assert "Loaded 992 entities, 207 sources" in out
    assert "nothing written" in out
