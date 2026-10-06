# Data Tiers

Eight physically separate folders under `data/` (plus `data/inherited/` for read-only starting assets). Separation prevents leakage. Source of truth: CLAUDE.md "Data tiers".

| Tier | Contents | Rules | Phase |
|---|---|---|---|
| `inherited/` | The two starting CSVs | Read-only, checksummed in `configs/inherited_checksums.yaml` | P0 |
| `raw/` | Immutable fetched bytes + headers | Never edited | P4 |
| `clean/` | Extracted, filtered, deduplicated, language-tagged text | Derived from raw | P5 |
| `synthetic/` | Generated from our entity inventories | Train only, never dev/test | P8 |
| `silver/` | Machine / weak-supervision labels | Keep generator, version, confidence. Never auto-promoted to gold | P6–9 |
| `reviewed/` | Human-reviewed, not yet adjudicated | Transitional | P7 |
| `gold/` | Double-annotated and adjudicated | Ground truth | P7 |
| `slices/` | Frozen eval slices (`ner_dev`, `ner_test`, ...) | Read-only after freeze; `ner_test` touched once at the end | P7 |
| `release/` | Exports, cards, checksums | Checksummed | P12 |

## Data flow

```
Sources -> Collect -> raw/ -> Clean -> clean/
                                         |
              +--------------------------+-----------------+
              v                          v                 v
          synthetic/                  silver/       reviewed/ -> gold/ -> slices/
          (train only)             (machine labels)                      (dev | test frozen)
              \                          |                 /
               +-------------------> Train -> Eval -> Model -> release/
```

## Hard rules

1. No document in two label-bearing tiers (`synthetic`, `silver`, `reviewed`, `gold`, `slices`). Slices never overlap training data.
2. Gold never leaks into development; `ner_test` is frozen before any model selection.
3. Synthetic never touches dev or test.
4. Every document carries provenance (`source_id`, `fetch_time`, hash, `processing_version`); no provenance, not in the corpus.
5. Every tier record carries `ontology_version` and `processing_version`.

Note: the same document legitimately exists as `raw` and `clean` (derived forms). The leakage check therefore compares only the *label-bearing* tiers: `synthetic`, `silver`, `reviewed`, `gold` and `slices`.

## Checking

```bash
python -m src.tier_utils --check-all-tiers
python -m src.leakage
```

Both scan JSONL files under `data/<tier>/` for `doc_id`. With empty tiers they pass trivially (P0 state).
