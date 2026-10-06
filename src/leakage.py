"""Leakage detection: prevent gold/synthetic/test data mixing."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any

from src.tier_utils import DATA_ROOT, find_cross_tier_overlaps, get_tier_doc_ids


def check_no_overlap(set1: set[str], set2: set[str], name1: str, name2: str) -> bool:
    """Ensure two sets of doc IDs don't overlap."""
    overlap = set1 & set2
    if overlap:
        print(f"ERROR: {len(overlap)} docs in both {name1} and {name2}: {sorted(overlap)[:5]}")
        return False
    print(f"OK: no overlap between {name1} and {name2}")
    return True


def check_no_duplicate_annotations(annotations: Iterable[dict[str, Any]]) -> bool:
    """Ensure each (doc, start, end, tier) is annotated only once."""
    seen: set[tuple[Any, ...]] = set()
    for ann in annotations:
        key = (ann.get("doc_id"), ann.get("start"), ann.get("end"), ann.get("tier"))
        if key in seen:
            print(f"ERROR: duplicate annotation {key}")
            return False
        seen.add(key)
    print("OK: no duplicate annotations")
    return True


def check_synthetic_isolation(gold_ids: set[str], synthetic_ids: set[str]) -> bool:
    """Ensure synthetic docs don't appear in gold."""
    return check_no_overlap(gold_ids, synthetic_ids, "gold", "synthetic")


def check_tier_folder_isolation(root: Path = DATA_ROOT) -> bool:
    """Scan data/ tiers and fail if any doc_id sits in two label-bearing tiers."""
    overlaps = find_cross_tier_overlaps(root=root)
    for doc_id, tiers in list(overlaps.items())[:5]:
        print(f"ERROR: {doc_id} in {tiers}")
    if not overlaps:
        print("OK: tier folder isolation")
    return not overlaps


def run_all(root: Path = DATA_ROOT) -> bool:
    """Run every check against the data folders."""
    gold = get_tier_doc_ids("gold", root)
    slices = get_tier_doc_ids("slices", root)
    synthetic = get_tier_doc_ids("synthetic", root)
    return all(
        [
            check_no_overlap(gold, slices, "gold", "slices"),
            check_synthetic_isolation(gold | slices, synthetic),
            check_tier_folder_isolation(root),
        ]
    )


if __name__ == "__main__":
    print("Running leakage checks...")
    ok = run_all()
    print("All leakage checks passed" if ok else "Leakage detected")
    raise SystemExit(0 if ok else 1)
