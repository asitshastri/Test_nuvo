# Phase Report: P0 (partial: P0-01 to P0-11 of the pasted prompt)

> Evidence labels: `docs/01_EVIDENCE_AND_DECISIONS.md`.

**Date:** 2026-10-07
**Status:** PARTIAL. The pasted prompt was truncated inside P0-11, so P0-12 and P0-13 were never received (UNKNOWN content). The phase is not closed.

## Tasks

| Task | Status | Evidence |
|---|---|---|
| P0-01 repo + tooling | Done, with gaps below | folders, pyproject, Makefile, CI yml, pre-commit config, `.venv` |
| P0-02 configs + schemas + validators | Done | 4 JSON schemas in `configs/schemas/`, 4 validators |
| P0-03 inherited assets | Done | 992 entities, 207 sources; checksums in `configs/inherited_checksums.yaml`; report `reports/P0-03_INHERITED_ASSETS.md` |
| P0-04 evidence doc | Done | `docs/01_EVIDENCE_AND_DECISIONS.md` |
| P0-05 templates | Done | `templates/`, section test |
| P0-06 data tiers | Done | `docs/02_DATA_TIERS.md`, `src/tier_utils.py` |
| P0-07 CI + tests | Partial | local ruff/black/mypy/pytest pass; GitHub Actions run not verified (no remote) |
| P0-08 ingestion order | Done | `docs/03_INGESTION_ORDER.md` (counts computed from the CSV) |
| P0-09 ontology roadmap | Done | `docs/04_ONTOLOGY_ROADMAP.md` (counts computed from the CSV) |
| P0-10 human checklist | Done | `docs/05_HUMAN_REVIEW_CHECKLIST.md` |
| P0-11 leakage framework | Done | `src/leakage.py`, `reports/P0-11_LEAKAGE_CHECK.md` |
| P0-12, P0-13 | NOT DONE | prompt text missing |

## Key numbers (FACT)

- 36 tests pass; coverage 91%.
- ruff clean, black clean, mypy `--strict` clean on 12 source files.
- Commits: 4 local, on branch `main`.

## Deviations from the pasted prompt

1. **Counts regenerated, not copied.** The prompt's ontology table (MIL_ORG 180, PLATFORM_NAVAL 45, ...) and ingestion table (API 45, BULK 62, ...) did not match the CSVs (26 real entity types, e.g. MIL_ORG 111, PLATFORM_SEA 51; access methods are multi-valued). Docs use computed numbers.
2. **CSVs moved** from `docs/` to `data/inherited/` (user confirmed). Checksum test guards them; `.gitattributes` sets `-text` on them so CRLF conversion cannot change the hash.
3. **Dependencies:** `fasttext`, `glot_id`, `playwright`, `trafilatura`, `pymupdf`, `datasketch`, `httpx` moved from core to optional extras (fragile on Windows; not needed until P4/P5). `glot_id` is not a verified package name (UNVERIFIED).
4. **ruff / pre-commit versions** aligned (spec pinned ruff>=0.31 in dev but v0.1.8 in hooks; ruff `select` moved under `[tool.ruff.lint]`). `make ci` made non-mutating (`black --check`).
5. **Validators** count a row once even with several errors, treat empty strings as missing, and tolerate non-dict rows.
6. **Tier checks** are real (scan JSONL `doc_id`), not placeholders; `raw`/`clean` are exempt from overlap because they are derived forms of one document. Assumption about `gold/` vs `slices/` recorded in the leakage report.
7. **Checklist dates** from the prompt fall after the 31 Oct 2026 deadline, so due dates are left blank. The checklist follows TODO.md's Human checklist.

## Not verified

- `make help` / `make ci`: `make` is not installed on this Windows machine. The underlying commands were run directly.
- pre-commit: FACT, `pre-commit run --all-files` passes all 7 hooks (excludes `data/inherited/`, `TODO.md`, `CLAUDE.md` so hooks cannot rewrite them; the first run tried to).
- Python 3.12 test run: not run; only 3.11.4 available (UNVERIFIED). CI matrix covers it once pushed.
- `chmod 444`: on Windows this sets the read-only attribute only; integrity relies on the checksum test.
- Git push: no remote provided; nothing pushed.

## Conflict to resolve (needs the human)

`TODO.md` defines a *different* Phase 0 (P0-01..P0-13: project-spec, v0.1-scope, architecture, data-model, pydantic configs, `data/inherited/CHECKSUMS.txt`, experiment tracking ADR, secret scan, ...). The pasted prompt's task list differs. Decision D-005 in TODO.md says English only; the prompt's validators accept any 2-letter language code (harmless). Which list is authoritative? Not yet resolved; TODO.md was not edited.

## Next steps

1. Human: provide GitHub remote (push P0-01/03/07), the missing P0-12/P0-13 text, and the TODO.md-vs-prompt ruling.
2. Install `make`/`pre-commit` or accept the direct commands.
3. Then close P0 and update CLAUDE.md "Current state".
