# P0 Reconciliation

> Evidence labels: `docs/01_EVIDENCE_AND_DECISIONS.md`. Governing documents: `CLAUDE.md` and `TODO.md`.

**Date:** 2026-10-07
**Scope:** compare (A) the original Phase 0 tasks in TODO.md, (B) the 13 tasks run from the pasted P0 prompt, (C) the artefacts actually in the repo. No Phase 1 or 3 work was started. Inherited CSV contents and the ontology were not touched.

## 1. Authority

The earlier decision D-009 ("the pasted prompt's task list supersedes TODO.md") was wrong and has been rewritten. `CLAUDE.md` and `TODO.md` govern. A phase prompt is an execution instruction for an approved phase and cannot silently replace TODO.md task definitions. Historical fact kept: the pasted prompt was used for the first P0 run, and its numbering differs from TODO.md's.

## 2. Original P0 tasks (TODO.md) vs repo

Status key: COMPLETE · PARTIAL · CARRY-FORWARD (not done, kept in TODO.md) · REPLACED · OBSOLETE. A task is `[x]` only when its AC is met.

| ID | Original requirement | What exists now | Evidence | Status | Reason |
|---|---|---|---|---|---|
| P0-01 | Init Git; `.gitignore` for `.env*`, `data/raw/`, large data, model files, caches, venvs; README stub; human picks remote and licence. AC: first commit pushed, README states goal in two sentences | Repo pushed to `asitshastri/Test_nuvo`, MIT, `.gitignore` (now also `.env.*`, `!.env.example`, model-file patterns), README opens with a two-sentence goal | `git log`, `.gitignore`, `README.md`, LICENSE, D-006 | **COMPLETE** | Two small gaps (`.env*`, model files, two-sentence goal) fixed during this reconciliation |
| P0-02 | Write `CLAUDE.md` with context, data rules, layout, commands, [INT]/[COMP] rules, never edit `data/inherited/`. AC: every "Data rules" rule appears | `CLAUDE.md` existed (human-supplied); a "Data rules" section with all six rules, commands and [INT]/[COMP] was added | `CLAUDE.md` "Data rules" | **COMPLETE** | Added section only; no existing rule changed. See Question Q7 about hard rules 1-2 |
| P0-03 | Checksums to `data/inherited/CHECKSUMS.txt`, read-only, test fails if a checksum changes. AC: test passes and changing a byte fails it | `CHECKSUMS.txt` (sha256sum format) + `configs/inherited_checksums.yaml`; read-only attribute; tests incl. a one-byte-flip test | `data/inherited/CHECKSUMS.txt`, `tests/test_inherited.py` | **COMPLETE** | CSV bytes unchanged (hashes identical before and after). `chmod 444` is only the read-only attribute on Windows; the test is the real guard |
| P0-04 | `docs/project-spec.md` (problem, research question, objective, outputs, vision). AC: human reviewed | Not written. CLAUDE.md "Mission" covers part of it | none | **CARRY-FORWARD** | Not done; needs a human review pass. Safe to carry forward (not blocking P1/P3) |
| P0-05 | `docs/v0.1-scope.md` (must/should/later; entity types, languages, source types). AC: human signed off, choices in Decisions | Not written. D-005 (English only) exists; `docs/04_ONTOLOGY_ROADMAP.md` lists inherited types | none | **CARRY-FORWARD** (human) | **Required before P1** (P1-02 label set depends on it). Needs human sign-off |
| P0-06 | `docs/architecture.md` (components, stage I/O formats, storage layout) + `docs/adr/` with template. AC: every stage has input and output formats | Not written; no `docs/adr/`. Partial overlap: `docs/02_DATA_TIERS.md` (tiers, flow), `docs/03_INGESTION_ORDER.md` | none for AC | **CARRY-FORWARD** | **Required before P3** (acquisition stage I/O). Existing docs do not satisfy the AC |
| P0-07 | `docs/data-model.md` and `schemas/`: document/entity/annotation/dataset-version ID schemes, provenance record; JSON Schemas for document, annotation, entity, source, acquisition-log. AC: sample records validate, broken fail, both tested | JSON Schemas for 4 of 5 types in `configs/schemas/` (no acquisition-log, not in `schemas/`); hand-written validators with tests for valid, corrupted and empty samples. No ID schemes or provenance doc. The JSON Schema files themselves are not loaded or tested | `configs/schemas/`, `src/validators.py`, `tests/test_validators.py` | **PARTIAL** | **Required before P3** (provenance, acquisition log). Schema files need a test that uses them |
| P0-08 | Skeleton with modules `acquisition, processing, kb, annotation, synthetic, models, evaluation, annotator`, plus `configs/`, `data/{...}`, `reports/`, `docs/`. AC: tree matches `docs/architecture.md` | Data/config/report/doc folders exist. Packages are CLAUDE.md's names (`collect, process, relevance, annotate, train, eval`); no `kb`, `synthetic`, `annotator` | `src/`, `data/` | **PARTIAL** | CLAUDE.md layout and TODO.md names disagree; AC cannot be checked without architecture.md. Human to choose naming (Q6) |
| P0-09 | Pin Python, env manager with lockfile, ruff, type checker, pytest, pre-commit. AC: lint, types, tests pass; pre-commit runs | Python pinned (`.python-version` 3.11 added, `requires-python>=3.11`); ruff, mypy, black, pytest, pre-commit all run clean. No lockfile (pip only; `uv` not installed) | `pyproject.toml`, `.pre-commit-config.yaml`, check results in section 6 | **PARTIAL** | AC met; the lockfile part of the requirement is not. RECOMMENDATION: add a lockfile with `uv lock` or `pip-compile` before P3; low risk, not blocking P1 |
| P0-10 | YAML configs validated by pydantic, `.env.example` (names only), one seed helper. AC: invalid config fails with clear error, tested | None. `pydantic` is not a dependency; no `.env.example`, no seed helper | none | **CARRY-FORWARD** | **Required before P3** (CLAUDE.md: every script has `--config`, deterministic seeds) |
| P0-11 | Choose experiment tracking and data versioning, record in ADR. AC: dummy run logged with config, data version, git commit | `src/run_log.py` + `src/experiments.py` log config hash, git hash, input/output counts and hashes; a real run is logged by `load_inherited`. No ADR, no explicit data-version field, no formal choice | `src/run_log.py`, `tests/test_run_log.py` | **PARTIAL** (human choice) | Tool choice is C+H. RECOMMENDATION: keep RunLog + hash manifests, no MLflow/DVC for V0.1; needs the human's OK and an ADR (Q5) |
| P0-12 | CI: lint, types, tests, schema validation, secret scan, slot for P7-02 leakage check. AC: green on a test PR | CI runs ruff, black, mypy, pytest on 3.11 and 3.12 and (added now) `python -m src.leakage`. No schema-validation step, no secret scan. Green on pushes to `main`; no test PR run | `.github/workflows/ci.yml`, run 37526762860 | **PARTIAL** | Secret scan and schema step missing; no PR test. Secret scan **required before P3** (before any credentials or bulk data exist) |
| P0-13 | Fill the Human checklist with owners. AC: table filled | `docs/05_HUMAN_REVIEW_CHECKLIST.md` created; owners and dates blank in it and in TODO.md | those files | **CARRY-FORWARD** (human) | Only the human can assign owners |

Result: 3 COMPLETE, 6 PARTIAL/CARRY-FORWARD with Claude-owned remaining work, 4 needing the human. Nothing is OBSOLETE or REPLACED outright.

## 3. The 13 prompt tasks (B) mapped to TODO.md

| Prompt task | Maps to TODO.md | Note |
|---|---|---|
| prompt P0-01 repo/tooling | P0-01, P0-09 | |
| prompt P0-02 schemas/validators | P0-07 (partial) | |
| prompt P0-03 inherited assets | P0-03 | |
| prompt P0-04 evidence doc | none | Supports CLAUDE.md "Evidence labels" |
| prompt P0-05 templates | none | CLAUDE.md names the templates |
| prompt P0-06 data tiers | P0-06 / P0-08 (partial overlap) | |
| prompt P0-07 CI + tests | P0-12 (partial) | |
| prompt P0-08 ingestion order | none | Input to P3-01 and P4 |
| prompt P0-09 ontology roadmap | none | Input to P1-01..P1-05 |
| prompt P0-10 human checklist | P0-13 (partial) | |
| prompt P0-11 leakage framework | P0-12 slot / P7-02 prerequisite | [INT] |
| prompt P0-12 run logging | P0-11 (partial) | |
| prompt P0-13 report/handoff | CLAUDE.md phase workflow | |

Prompt artefacts with no TODO.md counterpart (evidence doc, templates, ingestion order, ontology roadmap) are kept as supplementary; they do not count toward TODO.md P0 completion.

## 4. Previously "discovered" items

These are original P0 tasks, not new work, so they were removed from DISCOVERED and classified here.

| Item | Original task | Classification |
|---|---|---|
| `docs/project-spec.md` | P0-04 | safe to carry forward |
| `docs/v0.1-scope.md` | P0-05 | **required before P1** (human sign-off) |
| `docs/architecture.md` (+ `docs/adr/`) | P0-06 | **required before P3** |
| `docs/data-model.md` + schemas | P0-07 | **required before P3** |
| pydantic config validation | P0-10 | **required before P3** |
| `.env.example` | P0-10 | **required before P3** (trivial; needs no credentials yet) |
| seed helper | P0-10 | **required before P3** (any sampling or model code) |
| experiment-tracking / data-versioning ADR | P0-11 | safe to carry forward (RunLog already covers V0.1 needs; human decision pending) |
| CI secret scan | P0-12 | **required before P3** |
| CI run of `python -m src.leakage` | P0-12 | done in this reconciliation (CI step added); the full [INT] check stays P7-02 |

Not implemented here, per instruction: no large body of new work was created to fill the dashboard.

## 5. New findings (added to TODO.md DISCOVERED or Questions)

- **Q7:** `CLAUDE.md` hard rules 1-2 read as permission to defeat CAPTCHA, logins, paywalls, robots.txt and rate limits and to use stealth and proxy rotation. That contradicts hard rule 3-4 and TODO.md's [COMP] rules. Claude Code has not acted on rules 1-2 and follows rule 4 and [COMP] until the human rewrites them.
- CLAUDE.md references files that do not exist: `docs/07_TODO.md`, `docs/12_PIPELINE_V0_1_OPENALEX.md`, `docs/web-scraping-knowledge-base.md`, `prompts/P00-P14`. Added as a DISCOVERED task.
- Leakage check compares `doc_id` only. Near-duplicate detection needs P5 MinHash (UNKNOWN until then).
- `gold/` vs `slices/` disjointness is an assumption (see `reports/P0-11_LEAKAGE_CHECK.md`).

## 6. Validation run (2026-10-07, Python 3.11.4, Windows)

| Command | Result |
|---|---|
| `pytest` (with `--cov=src`) | 45 passed, 0 failed, 0 skipped; coverage 92% |
| `ruff check .` | all checks passed |
| `black --check src tests` | clean |
| `mypy src --strict` | no issues in 14 files |
| `pre-commit run --all-files` | all 7 hooks passed |
| `python -m src.leakage` | all checks passed (empty tiers) |
| `python -m src.tier_utils --check-all-tiers` | no overlaps |
| `python -m src.load_inherited --dry-run` | 992 entities, 207 sources loaded (also covered by tests) |
| GitHub Actions | last pushed commit green on 3.11 and 3.12 (run 37526762860); reconciliation commit 5a593be: run 37527734304 green on 3.11 and 3.12, including the new `python -m src.leakage` step |

`make` is not installed on this machine: `make help` and `make ci` were **not** run. The equivalent commands above were run directly.

Earlier numbers (43 tests) are superseded: two tests were added for `CHECKSUMS.txt` and the byte-flip check. Coverage stayed 92%.

## 7. Verdict

**PASS-WITH-FIXES.**

The infrastructure is sound and nothing needs rework. Phase 0 is not closed under TODO.md: 3 of 13 original tasks meet their AC. Before P1 starts: draft and get sign-off on `docs/v0.1-scope.md` (P0-05). Before P3 starts: P0-06, P0-07, P0-10 and the secret scan from P0-12. Human-only items remain (repository visibility, scope sign-off, report sign-off, checklist owners, tracking choice, naming convention, hard rules 1-2). Human sign-off is **not** the only thing remaining.
