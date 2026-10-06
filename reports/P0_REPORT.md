# Phase Report: P0 Foundation (P0-01 to P0-13)

> Evidence labels: `docs/01_EVIDENCE_AND_DECISIONS.md`.

**Date:** 2026-10-07
**Status:** COMPLETE, awaiting human sign-off.
**Task list used:** the pasted P0 prompt (human ruling 2026-10-07, TODO.md D-009).

## Summary

Repository, tooling, schemas, validators, inherited-asset ingestion, documentation, templates, tier and leakage checks, and run logging are built, pushed to `https://github.com/asitshastri/Test_nuvo` and green in CI on Python 3.11 and 3.12.

## Tasks

| Task | Status | Evidence |
|---|---|---|
| P0-01 repo + tooling | Done | folders, pyproject, Makefile, pre-commit, CI yml |
| P0-02 configs, schemas, validators | Done | `configs/schemas/*.json`, `src/validators.py` |
| P0-03 inherited assets | Done | 992 entities, 207 sources; `configs/inherited_checksums.yaml`; `reports/P0-03_INHERITED_ASSETS.md` |
| P0-04 evidence doc | Done | `docs/01_EVIDENCE_AND_DECISIONS.md` |
| P0-05 templates | Done | `templates/`, `tests/test_templates.py` |
| P0-06 data tiers | Done | `docs/02_DATA_TIERS.md`, `src/tier_utils.py` |
| P0-07 CI + tests | Done | GitHub Actions run 37526419956: success on 3.11 and 3.12 |
| P0-08 ingestion order | Done | `docs/03_INGESTION_ORDER.md` (computed counts) |
| P0-09 ontology roadmap | Done | `docs/04_ONTOLOGY_ROADMAP.md` (computed counts) |
| P0-10 human checklist | Done (owners and dates blank, human to fill) | `docs/05_HUMAN_REVIEW_CHECKLIST.md` |
| P0-11 leakage framework | Done | `src/leakage.py`, `reports/P0-11_LEAKAGE_CHECK.md` |
| P0-12 run logging | Done | `src/run_log.py`, `src/experiments.py`, wired into `src/load_inherited.py` |
| P0-13 report + handoff | Done | this file, `reports/P0_REVIEW.md`, TODO.md dashboard, CLAUDE.md state |

## Key numbers (FACT)

| Metric | Value |
|---|---|
| Tasks | 13/13 |
| Tests | 43 pass, 0 fail, 0 skip (7 test modules) |
| Coverage | 92% of `src/` |
| ruff / black / mypy --strict / pre-commit (7 hooks) | all clean |
| CI | green on 3.11 and 3.12 |
| Commits | 8 on `main` |
| Tracked files | 69 |

## Decisions (TODO.md D-006 to D-009)

- D-006 MIT code licence (confirmed by the human); remote `asitshastri/Test_nuvo`. Corpus licence is decided in P3.
- D-007 heavy or Windows-fragile libraries are optional extras.
- D-008 pre-commit excludes `data/inherited/`, `TODO.md`, `CLAUDE.md`.
- D-009 the phase prompt's task list is authoritative; TODO.md is the dashboard.

## Deviations from the prompts

1. Counts in the ontology and ingestion docs are computed from the CSVs; the prompt's illustrative numbers did not match the data (26 real entity types).
2. CSVs moved from `docs/` to `data/inherited/`; `.gitattributes` keeps their bytes stable.
3. `chmod 444` is only a read-only attribute on Windows; the checksum test is the real guard.
4. `make` is not installed locally, so the Makefile targets were not run; the same commands run in CI and pass. `make ci` is UNVERIFIED locally.
5. The human-supplied P0-13 draft claimed 25+ commits, 38/42 tests, 85% coverage and a "Wikipedia + Wikidata" first slice. Those do not match reality or CLAUDE.md (first slice is OpenAlex). This report uses measured numbers.
6. P0-12 `RunLog` uses timezone-aware timestamps (no deprecated `utcnow`) and filenames `RUN-YYYYMMDD-HHMMSS-task.json`. Run logs are git-ignored by design.

## Risks and open items

- **The GitHub repository is PUBLIC** (FACT, `gh repo view`). It now contains `CLAUDE.md`, `TODO.md` and the two inherited CSVs. Make it private if that is not intended.
- Original TODO.md Phase 0 items not covered by the prompt (project-spec, v0.1-scope sign-off, architecture, data-model, pydantic configs, experiment-tracking ADR, secret scan) are in DISCOVERED, untriaged.
- Leakage check compares `doc_id` only; near-duplicate leakage needs P5 MinHash (UNKNOWN until then).
- `gold/` vs `slices/` disjointness is an assumption (see `reports/P0-11_LEAKAGE_CHECK.md`).
- Human checklist owners and dates unfilled.

## Next steps

1. Human: review and sign off this report and `reports/P0_REVIEW.md`; fill checklist owners.
2. Start P1 (ontology) and P3 (sources) once the phase prompts are provided.

## Reproducibility

```bash
git clone https://github.com/asitshastri/Test_nuvo.git
cd Test_nuvo
python -m venv .venv && .venv/Scripts/activate   # POSIX: source .venv/bin/activate
pip install -e ".[dev]"
ruff check . && black --check src tests && mypy src --strict && pytest   # = make ci
```

Human sign-off: ____________________ (date: ________)
