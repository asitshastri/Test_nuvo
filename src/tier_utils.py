"""Data tier separation helpers: collect doc_ids per tier from JSONL files."""

import argparse
import json
from pathlib import Path

DATA_ROOT = Path("data")
# raw and clean hold derived forms of the same document, so they may share ids.
LABEL_TIERS = ("synthetic", "silver", "reviewed", "gold", "slices")
ALL_TIERS = ("raw", "clean", *LABEL_TIERS)


def get_tier_doc_ids(tier: str, root: Path = DATA_ROOT) -> set[str]:
    """Return every ``doc_id`` found in ``*.jsonl`` files under ``root/tier``."""
    tier_path = root / tier
    ids: set[str] = set()
    if not tier_path.exists():
        return ids
    for path in sorted(tier_path.rglob("*.jsonl")):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    doc_id = json.loads(line).get("doc_id")
                    if doc_id:
                        ids.add(str(doc_id))
    return ids


def find_cross_tier_overlaps(
    tiers: tuple[str, ...] = LABEL_TIERS, root: Path = DATA_ROOT
) -> dict[str, list[str]]:
    """Map doc_id -> tiers it appears in, for ids present in more than one tier."""
    seen: dict[str, list[str]] = {}
    for tier in tiers:
        for doc_id in get_tier_doc_ids(tier, root):
            seen.setdefault(doc_id, []).append(tier)
    return {d: t for d, t in sorted(seen.items()) if len(t) > 1}


def check_no_overlap(root: Path = DATA_ROOT) -> bool:
    """True if no document appears in two label-bearing tiers."""
    overlaps = find_cross_tier_overlaps(root=root)
    for doc_id, tiers in list(overlaps.items())[:10]:
        print(f"ERROR: {doc_id} in tiers {tiers}")
    if not overlaps:
        print(f"OK: no overlaps across {len(LABEL_TIERS)} label-bearing tiers")
    return not overlaps


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check-all-tiers", action="store_true")
    ap.add_argument("--root", type=Path, default=DATA_ROOT)
    args = ap.parse_args()
    ok = check_no_overlap(args.root)
    for tier in ALL_TIERS:
        print(f"{tier}: {len(get_tier_doc_ids(tier, args.root))} docs")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
