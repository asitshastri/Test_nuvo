"""Tests for tier utilities and leakage checks."""

import json
from pathlib import Path

from src import leakage, tier_utils


def _write(root: Path, tier: str, ids: list[str]) -> None:
    d = root / tier
    d.mkdir(parents=True, exist_ok=True)
    (d / "x.jsonl").write_text("\n".join(json.dumps({"doc_id": i}) for i in ids) + "\n")


def test_empty_state_passes(tmp_path: Path) -> None:
    assert tier_utils.check_no_overlap(tmp_path) is True
    assert leakage.run_all(tmp_path) is True


def test_raw_and_clean_may_share_ids(tmp_path: Path) -> None:
    _write(tmp_path, "raw", ["D1"])
    _write(tmp_path, "clean", ["D1"])
    assert leakage.run_all(tmp_path) is True


def test_overlap_detected(tmp_path: Path) -> None:
    _write(tmp_path, "gold", ["D1", "D2"])
    _write(tmp_path, "silver", ["D2"])
    assert tier_utils.find_cross_tier_overlaps(root=tmp_path) == {"D2": ["silver", "gold"]}
    assert leakage.check_tier_folder_isolation(tmp_path) is False


def test_synthetic_in_gold_fails(tmp_path: Path) -> None:
    _write(tmp_path, "gold", ["D1"])
    _write(tmp_path, "synthetic", ["D1"])
    assert leakage.run_all(tmp_path) is False


def test_check_no_overlap_sets() -> None:
    assert leakage.check_no_overlap({"a"}, {"b"}, "x", "y") is True
    assert leakage.check_no_overlap({"a"}, {"a"}, "x", "y") is False


def test_synthetic_isolation_sets() -> None:
    assert leakage.check_synthetic_isolation({"a"}, {"b"}) is True
    assert leakage.check_synthetic_isolation({"a"}, {"a"}) is False


def test_duplicate_annotations() -> None:
    a = {"doc_id": "D", "start": 0, "end": 3, "tier": "gold"}
    assert leakage.check_no_duplicate_annotations([a]) is True
    assert leakage.check_no_duplicate_annotations([a, dict(a)]) is False
    assert leakage.check_no_duplicate_annotations([a, {**a, "tier": "silver"}]) is True


def test_missing_tier_dir(tmp_path: Path) -> None:
    assert tier_utils.get_tier_doc_ids("nope", tmp_path) == set()
