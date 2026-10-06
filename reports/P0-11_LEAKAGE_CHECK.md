# P0-11: Leakage Detection Framework

## Overview

Leakage checks stop gold, test and synthetic data from contaminating model development (CLAUDE.md rules 7 and 8). See `docs/02_DATA_TIERS.md`.

## Checks implemented (`src/leakage.py`)

1. `check_no_overlap()`: two doc-id sets must not intersect (e.g. gold vs slices).
2. `check_synthetic_isolation()`: synthetic docs must not appear in gold/slices.
3. `check_no_duplicate_annotations()`: no (doc, start, end, tier) annotated twice.
4. `check_tier_folder_isolation()`: scans `data/<tier>/**/*.jsonl` for `doc_id`; no id in two label-bearing tiers (`synthetic`, `silver`, `reviewed`, `gold`, `slices`). `raw` and `clean` may share ids (derived forms).

## Scope and limits

- FACT: checks work on `doc_id` equality only. Near-duplicate leakage (same text, different id) is not detected here. UNKNOWN until P5 MinHash dedup exists; a content-hash/MinHash overlap check must be added then.
- FACT: only `.jsonl` files with a `doc_id` field are scanned. Other formats are ignored.

## When it runs

- P0: baseline on the empty state (passes trivially).
- P7: after the test slice is frozen. P12: final audit before release.

## How to run

```bash
python -m src.leakage
python -m src.tier_utils --check-all-tiers
```

## Result at P0

FACT: all tiers empty, all checks pass; `tests/test_tiers_leakage.py` covers pass and fail paths for each check (no false positives on raw/clean sharing ids).

## Design assumption (RECOMMENDATION, confirm in P7)

`slices/` holds the frozen dev/test documents and `gold/` holds only training-eligible gold. Documents are moved, not copied, into slices, so "no doc_id in both gold and slices" is the invariant. If P7 keeps slice docs inside `gold/`, the gold-vs-slices check must compare gold-train vs slices instead.

## Design assumption (RECOMMENDATION, confirm in P7)

`slices/` holds the frozen dev/test documents and `gold/` holds only training-eligible gold. Documents are moved, not copied, into slices, so "no doc_id in both gold and slices" is the invariant. If P7 keeps slice docs inside `gold/`, the gold-vs-slices check must compare gold-train vs slices instead.
