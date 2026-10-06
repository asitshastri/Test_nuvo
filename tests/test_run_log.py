"""Tests for run logging and the experiments summary."""

import json
from pathlib import Path

import pytest

from src.experiments import list_all_runs, summarize_runs
from src.run_log import RunLog


def test_create() -> None:
    log = RunLog("test_task")
    assert log.task == "test_task"
    assert log.timestamp
    assert log.git_hash


def test_inputs_outputs_warnings_errors() -> None:
    log = RunLog("t")
    log.add_input("entities", 100)
    log.add_output("cleaned", 95, "sha256:x")
    log.add_warning("w")
    log.add_error("e")
    assert log.inputs["entities"]["count"] == 100
    assert log.outputs["cleaned"] == {"count": 95, "hash": "sha256:x"}
    assert log.warnings == ["w"] and log.errors == ["e"]


def test_save_and_read_back(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    log = RunLog("test_task")
    log.add_input("data", 10)
    path = log.save(runtime_seconds=1.5)
    assert path.exists() and path.name.startswith("RUN-") and path.suffix == ".json"
    data = json.loads(path.read_text())
    assert data["task"] == "test_task"
    assert data["runtime_seconds"] == 1.5
    assert {"timestamp", "git_hash", "config_hash", "inputs", "outputs"} <= data.keys()
    assert list_all_runs(Path("experiments"))[0]["task"] == "test_task"


def test_save_default_runtime(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    path = RunLog("t").save()
    assert json.loads(path.read_text())["runtime_seconds"] >= 0


def test_config_hash(tmp_path: Path) -> None:
    cfg = tmp_path / "c.yaml"
    cfg.write_text("key: value\n")
    log = RunLog("t")
    log.set_config_hash(cfg)
    assert len(log.config_hash) == 8
    log2 = RunLog("t")
    log2.set_config_hash(tmp_path / "missing.yaml")
    assert log2.config_hash == ""


def test_summary(tmp_path: Path) -> None:
    exp = tmp_path / "experiments"
    exp.mkdir()
    (exp / "RUN-1-a.json").write_text(
        json.dumps({"task": "a", "runtime_seconds": 2, "errors": ["x"]})
    )
    (exp / "RUN-2-bad.json").write_text("{not json")
    text = summarize_runs(exp)
    assert "Total runs: 1" in text and "a: 1 run(s)" in text and "Errors detected: 1" in text


def test_summary_empty(tmp_path: Path) -> None:
    assert summarize_runs(tmp_path / "none") == "Total runs: 0"
