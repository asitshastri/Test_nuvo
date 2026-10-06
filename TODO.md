# TODO

This is the master task list. Claude Code reads it before starting work and updates it after every task. The human mainly reads four sections: Dashboard, Current focus, Needs you, and Questions for the human.

Last updated: 6 October 2026. This is the planning baseline and no work has started yet.

## How to use this file

**Status marks**

| Mark | Meaning |
|---|---|
| `[ ]` | To do |
| `[~]` | In progress. Keep this to one or two tasks at a time. |
| `[x]` | Done, with evidence recorded in the Progress log |
| `[!]` | Blocked. The reason goes in Blockers or Questions for the human. |
| `[-]` | Dropped. The reason goes in Decisions. |

**Order.** Work through the phases in order and pick the first task that is not blocked. Two parallel tracks are allowed after Phase 0. The first is Phases 1 → 2, which build the ontology and the knowledge base. The second is Phases 3 → 4 → 5, which handle sources, collection and cleaning. Phase 8 (synthetic data) may run alongside Phases 5 to 7. **No training in Phase 9 may start until P7-02 (the test-set freeze) is done.**

**Tags.** These rules override the task descriptions. Never skip a tagged task to do an easier one, and never mark a tagged task done when its acceptance criteria are only partly met.
- **[INT]** marks an evaluation-integrity task, covering the test set, leakage, and the separation between gold, silver and synthetic data. If an [INT] rule is broken, every benchmark result becomes worthless.
- **[COMP]** marks a source-compliance task, covering robots.txt, rate limits, terms of use, licences and attribution.

**Size:** S is under half a day, M is up to about two days, and L is longer. These are rough guesses.
**Owner:** C means Claude Code, H means the human needs to act, and C+H means both.

**Update protocol for Claude Code (applies to every task, no exceptions)**

1. Before starting, read `CLAUDE.md`, this file, and any docs the task points to. Set the task to `[~]` and update Current focus.
2. Work in small commits and follow the rules in `CLAUDE.md`.
3. Prove the acceptance criteria (AC) by running lint, the type check, the tests, and any data validators the task touches. A task cannot be marked done without evidence. For data tasks, the evidence is the counts and the file paths.
4. When the task is finished, set it to `[x]`, add one line to the Progress log (date, task ID, what changed, checks run, commit hash), update the Dashboard counts, and fix any doc that is now out of date.
5. If a task needs the human (annotation, sign-off, compute, legal or licensing calls, accounts), set it to `[!]`, add it under Needs you or Questions for the human, and move on to the next task that is not blocked. Never wait idle.
6. If you make a design decision or find that a doc is wrong, add a line to Decisions (D-xxx) and update the doc in the same commit.
7. If you discover new work, add it under DISCOVERED with a size, an owner and acceptance criteria, and mention it in the session report.
8. End every working session with a report in the format below.

**Report format (send this to the human at the end of each session)**

```
Update: <date>
Done: <task IDs, one line each>
In progress: <task IDs>
Needs you: <specific asks: what, why, which task needs it>
Next: <next 3 tasks>
Risks and decisions: <anything surprising>
Checks: lint <pass/fail>, types <pass/fail>, tests <n passed, n failed>, leakage check <pass/fail/not yet>
Data: <corpus docs raw/clean, gold sentences, KB entities, if changed>
```

**Data rules (these always apply)**

- The inherited CSVs in `data/inherited/` are read-only. Derived versions are written somewhere else.
- Raw, clean, silver, synthetic and gold data are stored in separate folders, and every annotation record carries its `tier`.
- Every document is traceable to its source, URL, fetch time, content hash and processing version.
- Every annotation records the `ontology_version` it follows.
- Test-set annotations are read only by the evaluation script. They are never used to write prompts, rules, gazetteer entries, synthetic examples or model choices.
- Model development uses the DEV split. Each final candidate model is run on TEST once, and every TEST run is recorded in the Progress log.

**Definition of done:** the acceptance criteria have been shown to pass, tests exist for any new code, data outputs have a stats report and pass their schema validator, docs are updated, the leakage check passes once it exists, and CI is green.

---

## Dashboard

| Phase | Name | Scope | Total | Done | In progress | Blocked |
|---|---|---|---|---|---|---|
| 0 | Project definition and architecture | V0.1 | 13 | 3 | 0 | 3 |
| 1 | Defence NER ontology | V0.1 | 8 | 0 | 0 | 0 |
| 2 | Entity knowledge base | V0.1 | 9 | 0 | 0 | 0 |
| 3 | Source validation and acquisition | V0.1 | 10 | 0 | 0 | 0 |
| 4 | Corpus collection | V0.1 | 6 | 0 | 0 | 0 |
| 5 | Corpus cleaning and quality control | V0.1 | 13 | 0 | 0 | 0 |
| 6 | Annotation system and guidelines | V0.1 | 8 | 0 | 0 | 0 |
| 7 | Gold test set and human annotation | V0.1 | 9 | 0 | 0 | 0 |
| 8 | Synthetic dataset generation | V0.1 | 10 | 0 | 0 | 0 |
| 9 | NER model experiments | V0.1 | 10 | 0 | 0 | 0 |
| 10 | Model evaluation and selection | V0.1 | 7 | 0 | 0 | 0 |
| 11 | Defence NER annotator | V0.1 | 9 | 0 | 0 | 0 |
| 12 | End-to-end V0.1 release | V0.1 | 10 | 0 | 0 | 0 |
| 13 | Continuous web → annotation pipeline | Roadmap | 10 | 0 | 0 | 0 |
| 14 | Human-in-the-loop and active learning | Roadmap | 9 | 0 | 0 | 0 |
| 15 | Continuous model improvement | Roadmap | 10 | 0 | 0 | 0 |
| 16 | Advanced defence NLP platform | Roadmap | 9 | 0 | 0 | 0 |
| | **V0.1 total (Phases 0–12)** | | **122** | **3** | **0** | **3** |
| | **All phases** | | **160** | **3** | **0** | **3** |

**Key numbers** (update these when they change)

| Metric | Value |
|---|---|
| Ontology version | none yet |
| KB entities (after deduplication) / inherited | — / 992 |
| Sources validated / selected for V0.1 / inherited | — / — / 207 |
| Corpus documents (raw / clean / relevant) | — / — / — |
| Gold documents (train / dev / test) | — / — / — |
| Inter-annotator agreement (strict span F1) | — |
| Synthetic examples | — |
| Best DEV F1 (model) | — |
| TEST F1 of the selected model | — |

## Current focus

Phase 0 reconciliation done on 2026-10-07 (see `reports/P0_RECONCILIATION.md`). The engineering foundation is built, pushed and CI-green (45 tests, 92% coverage). Of the 13 original P0 tasks, 3 meet their AC (P0-01, P0-02, P0-03). P0-05 (scope) gates P1 and is drafted in `docs/v0.1-scope.md`, waiting for human sign-off; P0-06, P0-07, P0-10 and the CI secret scan gate P3. Verdict: PASS-WITH-FIXES. P1 and P3 have not started.

## Needs you

| Ask | Why | Needed by | Status |
|---|---|---|---|
| Decide repository visibility. `asitshastri/Test_nuvo` is PUBLIC and contains `CLAUDE.md`, `TODO.md` and the inherited CSVs | The CSVs are project assets; Claude did not change visibility | now | Pending |
| Approve or revise `docs/v0.1-scope.md` (draft written 2026-10-07; decisions D1-D8 listed in section 7 of that file) | Gates P1-02 (label set) | P0-05 | Pending |
| Sign off `reports/P0_REPORT.md` and `reports/P0_REVIEW.md` | Phase gate | P0 close | Pending |
| Fill owners and due dates in the Human checklist (below and `docs/05_HUMAN_REVIEW_CHECKLIST.md`) | Annotators and compute have long lead times | P0-13 | Pending |
| Choose experiment tracking and data versioning (Claude recommends RunLog + hash manifests) | Needed for the ADR | P0-11 | Pending |
| Rule on module naming: CLAUDE.md (`collect, process, ...`) or TODO.md (`acquisition, processing, kb, ...`) | Skeleton and architecture.md depend on it | P0-08 | Pending |
| Rewrite CLAUDE.md hard rules 1 and 2, which contradict rule 4 and the [COMP] rules | Compliance risk | before P3 | Pending |
| Inherited CSVs placed in `data/inherited/`; remote `asitshastri/Test_nuvo` and MIT chosen | | P0-01, P0-03 | Done 2026-10-07 |

## Questions for the human (ask these when the human is back)

When the human is away, Claude keeps working and never waits. If a task needs the human's opinion, a review, an answer, compute, or a legal or licensing call, Claude adds a row here, marks the task `[!]` with the reason, and moves on to the next task that is not blocked. Questions are asked only when the phase that needs the answer starts. Do not add questions about later phases in advance. Python packages are not questions: Claude installs them as needed, pins exact versions, and justifies each one in the commit message.

| Added | Task | Question | Why it matters | What Claude did meanwhile |
|---|---|---|---|---|
| 2026-10-07 | P0 | Should the repository stay public? | It holds the inherited CSVs and planning docs | Left unchanged |
| 2026-10-07 | P0-05 | Approve or revise the V0.1 scope in `docs/v0.1-scope.md`: entity buckets (13 MUST / 6 SHOULD / 7 LATER inherited types), English only (D-005), source-type buckets, and decisions D1-D8 (state media, re3d_test, OpenAlex slice, paid/registration sources, GOV_ORG/DEF_INDUSTRY/NSAG). | Gates P1-02 | Draft written; nothing marked approved |
| 2026-10-07 | P0-11 | Accept RunLog + hash manifests, no MLflow/DVC, for V0.1? | Needs an ADR | RunLog already logs runs |
| 2026-10-07 | P0-08 | Module names: CLAUDE.md or TODO.md convention? | Tree must match architecture.md | Kept CLAUDE.md names |
| 2026-10-07 | P0-02 | CLAUDE.md hard rules 1-2 say access controls may be defeated; rule 4 and [COMP] say stop. Which holds? | Compliance | Following rule 4 and [COMP] |
| 2026-10-07 | P0-13 | Who owns each Human checklist item, and by when? | Lead times | Left blank, no invented names or dates |

## Blockers

No engineering blocker. P1 is gated by P0-05 (scope sign-off). P3 is gated by P0-06, P0-07, P0-10 and the CI secret scan from P0-12. Human items are in Needs you.

## DISCOVERED

New tasks found while working. Claude appends them here and the human triages each one into a phase.

| Date | Found during | Task | Size | Owner | Acceptance criteria | Triage |
|---|---|---|---|---|---|---|
| 2026-10-07 | P0 reconciliation | Fix dangling references in CLAUDE.md (`docs/07_TODO.md`, `docs/12_PIPELINE_V0_1_OPENALEX.md`, `docs/web-scraping-knowledge-base.md`, `prompts/P00-P14`): create, repoint or remove | S | C+H | No CLAUDE.md path points to a missing file | Untriaged |
| 2026-10-07 | P0 reconciliation | Test that loads the JSON Schemas in `configs/schemas/` and validates valid and broken samples (needs `jsonschema` or pydantic) | S | C | Valid samples pass and broken fail, via the schema files | Untriaged (fold into P0-07) |
| 2026-10-07 | P0 reconciliation | Near-duplicate leakage check (content hash / MinHash) alongside the `doc_id` check | M | C | An injected near-duplicate across gold and train is detected | Untriaged (P5 / P7-02) |

## Later: ideas for after V0.1

Ideas that are not in Phases 13 to 16 but should not be forgotten. Each row says what the idea is and where it came from.

| What | Where it came from | Notes |
|---|---|---|
| | | |

---

## Phase 0: Project definition and architecture

Goal: decide exactly what we are building before writing the system.

- [x] **P0-01** (S, C+H) Initialise the Git repository. Add a `.gitignore` that excludes `.env*`, `data/raw/`, large data and model files, caches and virtual environments. Add a README stub. The human chooses the remote and the code licence. *AC:* the first commit is pushed and the README states the project goal in two sentences. *Status:* Done 2026-10-07: pushed to asitshastri/Test_nuvo, MIT; see reports/P0_RECONCILIATION.md.
- [x] **P0-02** (S, C) Write `CLAUDE.md`, covering the project context, the data rules from this file, the folder layout, the commands to run, the [INT] and [COMP] rules, and a rule never to edit `data/inherited/`. *AC:* the file exists and every rule in "Data rules" above appears in it. *Status:* Done 2026-10-07: Data rules, commands and [INT]/[COMP] added to CLAUDE.md.
- [x] **P0-03** (S, C+H) Bring in the inherited assets. The human places the two CSVs. Claude writes SHA-256 checksums to `data/inherited/CHECKSUMS.txt`, sets the files read-only, and adds a test that fails if a checksum changes. *AC:* the checksum test passes, and changing a byte makes it fail. *Status:* Done 2026-10-07: data/inherited/CHECKSUMS.txt, byte-flip test, files read-only.
- [ ] **P0-04** (S, C+H) Write `docs/project-spec.md`, covering the problem, the research question, the technical objective, the expected outputs and the long-term vision. *AC:* the human has reviewed it. *Status:* Not written. Safe to carry forward.
- [!] **P0-05** (S, C+H) Write `docs/v0.1-scope.md`. It splits work into must-have, should-have and later, and records the scope choices: entity types, languages and source types. *AC:* the human has signed it off and the choices are recorded in Decisions. *Status:* Draft written 2026-10-07 in `docs/v0.1-scope.md`; blocked on human sign-off (decisions D1-D8 in that file). Not done.
- [ ] **P0-06** (M, C) Write `docs/architecture.md`. It covers the components (sources → acquisition → raw → processing → annotation → gold/silver/synthetic → training → model → automatic annotation), the inputs and outputs of each stage, the storage layout, and an `docs/adr/` folder with a template. *AC:* every stage has defined input and output formats.  *Status:* Not written. Required before P3. Partial overlap: docs/02_DATA_TIERS.md, docs/03_INGESTION_ORDER.md.
- [ ] **P0-07** (M, C) Define the data model in `docs/data-model.md` and `schemas/`. This covers the document ID, entity ID, annotation ID and dataset version schemes, and the provenance record. Write JSON Schemas for document, annotation, entity, source and acquisition-log records. *AC:* sample records validate, broken samples fail, and both cases are tested. *Status:* Partial: 4 of 5 JSON Schemas in configs/schemas/ and validators with tests; no acquisition-log schema, ID schemes or provenance doc. Required before P3.
- [ ] **P0-08** (S, C) Create the repository skeleton. The package has modules for `acquisition`, `processing`, `kb`, `annotation`, `synthetic`, `models`, `evaluation` and `annotator`. Also create `configs/`, `data/{inherited,raw,clean,gold,silver,synthetic}/`, `reports/` and `docs/`. *AC:* the tree matches `docs/architecture.md`. *Status:* Partial: folders exist; package names follow CLAUDE.md, not this list. Needs the human's naming ruling.
- [ ] **P0-09** (S, C) Set up the toolchain. Pin the Python version, choose an environment manager with a lockfile, and add ruff, a type checker, pytest and pre-commit. *AC:* lint, the type check and the tests pass on a sample test, and pre-commit runs. *Status:* Partial: AC met (ruff, mypy, pytest, pre-commit pass) but no lockfile yet.
- [ ] **P0-10** (S, C) Build the configuration system: YAML configs validated with pydantic, a `.env.example` containing names only, and a single helper that sets the random seed. *AC:* an invalid config fails with a clear error, and this is tested. *Status:* Not done: no pydantic config, .env.example or seed helper. Required before P3.
- [!] **P0-11** (S, C+H) Choose experiment tracking (for example local MLflow) and data versioning (for example DVC, or hash manifests), and record the choice in an ADR. *AC:* a dummy run is logged with its config, its data version and the git commit. *Status:* Blocked on the human's tooling choice. Partial: src/run_log.py logs config hash, git hash, inputs and outputs; no ADR.
- [ ] **P0-12** (S, C) Set up CI: lint, type check, tests, schema validation, a secret scan, and a slot for the P7-02 leakage check. *AC:* CI is green on a test pull request. *Status:* Partial: CI runs lint, types, tests and src.leakage on 3.11 and 3.12; secret scan, schema step and a test PR missing. Secret scan required before P3.
- [!] **P0-13** (S, H) Fill in the Human checklist below with owners. *AC:* the table is filled. *Status:* Blocked on the human: owners and dates are blank.

## Phase 1: Defence NER ontology

Goal: decide what entities the model will recognise. The master list is an input to this phase, not the final ontology.

- [ ] **P1-01** (M, C) Profile `01_NER_MASTER_LIST.csv`: its columns, types, subtypes, counts per type, duplicates, aliases, abbreviations, inconsistencies and missing values. Write the results to `reports/ner-master-profile.md` using a script. *AC:* re-running the script reproduces every number.
- [ ] **P1-02** (M, C+H) Propose the V0.1 label set and a mapping from every master-list type to a label (or an explicit exclusion), and save it as `ontology/ontology_v0.1.yaml`. The candidates are weapon, platform, military organisation or unit, facility, operation or exercise, programme, sensor or C4ISR system, person and military role. *AC:* no master-list type is left unmapped, and the human approves the label set.
- [ ] **P1-03** (M, C) Write a definition card for each label: definition, inclusion rules, exclusion rules, at least 3 examples and at least 3 counterexamples, in `docs/ontology_v0.1.md`. *AC:* every label has a complete card.
- [ ] **P1-04** (S, C) Write the span boundary rules: determiners, ranks and titles, designations and model numbers ("Su-30MKI", "INS Vikrant"), possessives, coordinated names, and parentheses around acronyms. *AC:* each rule has a correct example and an incorrect one.
- [ ] **P1-05** (M, C) Write the ambiguity rules: one name for several entities ("Prithvi"), acronym clashes, organisation versus programme, platform versus weapon, person versus organisation, and metonymy ("New Delhi said", "the Navy announced"). *AC:* each case has a decision rule and examples.
- [ ] **P1-06** (S, C+H) Decide whether entities may be nested or annotation stays flat, and record the reason in an ADR. *AC:* the ADR is accepted, and P6-01 and P9 follow it.
- [ ] **P1-07** (S, C) Set up ontology versioning: a version field, a changelog, and a rule for migrating annotations when a label changes. *AC:* the changelog exists and the version is read by the annotation schema.
- [ ] **P1-08** (S, H) The human signs off Ontology V0.1. *AC:* the sign-off is recorded in Decisions and the git tag `ontology-v0.1` exists.

## Phase 2: Entity knowledge base

Goal: turn the NER master list into a structured defence entity resource with stable IDs.

- [ ] **P2-01** (S, C) Import the master list into the KB working format without changing the source, and link every record to its CSV row number. *AC:* 992 rows go in and 992 records come out, each with a row reference.
- [ ] **P2-02** (M, C) Normalise names, aliases, abbreviations and spelling variants: Unicode, case and spacing, and designation variants such as "Su-30MKI", "Su 30 MKI" and "Su30MKI". *AC:* the rules are unit tested, and the original strings are kept next to the normalised ones.
- [ ] **P2-03** (M, C) Find duplicate candidates, both exact and fuzzy, and write a report with a reason for each pair. *AC:* `reports/kb-duplicates.md` lists every candidate pair.
- [ ] **P2-04** (M, C+H) Resolve each candidate pair as same, different or uncertain. Uncertain pairs go into a human review list. *AC:* every pair has a decision, and the human has resolved the uncertain list or deferred it with a reason.
- [ ] **P2-05** (S, C) Assign canonical IDs (for example `ENT-000001`). IDs are stable and never reused, and the ID registry is append-only. *AC:* there is a test that IDs survive a re-import.
- [ ] **P2-06** (S, C) Give each entity a verification state: `VERIFIED`, `UNVERIFIED`, `CONFLICTING` or `NEEDS_REVIEW`, recording who changed it and when. *AC:* every entity has a state.
- [ ] **P2-07** (S, C) Map every KB entity to an Ontology V0.1 label, and list the entities that cannot be mapped. *AC:* entities that are neither mapped nor listed number 0.
- [ ] **P2-08** (M, C) Build the gazetteer: alias → (entity ID, label) with a fast matcher, and a flag on aliases that point to more than one entity. *AC:* lookup tests cover an ambiguous alias, an abbreviation and a case variant.
- [ ] **P2-09** (S, C) Write a KB stats report and validators (counts per label, per state and per source, plus the alias count). *AC:* `reports/kb-v0.1-stats.md` exists and the Key numbers above are updated.

## Phase 3: Source validation and web acquisition

Goal: turn the source list into a working acquisition system that follows the rules.

- [ ] **P3-01** (S, C) Import `02_SOURCE_MASTER_LIST.csv` into the source registry, with row provenance. *AC:* 207 records, each traceable to its row.
- [ ] **P3-02** (M, C) Validate each source automatically: the URL resolves, the status code, redirects, content type, a language guess, and evidence of recent updates. *AC:* every source has a validation result with a timestamp.
- [ ] **P3-03** (M, C+H) Classify each source by type, country, language, credibility tier and relevance. The human reviews the credibility tiers. *AC:* every source is classified, and the tiers have been reviewed.
- [ ] **P3-04** (M, C) Find the access method for each source: API, RSS, sitemap, HTML listing, or downloadable documents. *AC:* every accessible source has a method and an entry URL.
- [ ] **P3-05** (M, C+H) **[COMP]** Record compliance for each source: robots.txt rules, terms-of-use notes, licence and reuse terms, and the attribution needed. Each source gets a status of `allowed`, `restricted` or `excluded`. *AC:* every V0.1 source has a status, and the human confirms the policy for restricted sources.
- [ ] **P3-06** (S, C+H) Rank the sources and choose the V0.1 set using priority tiers. *AC:* the selection and the reasons are recorded in Decisions.
- [ ] **P3-07** (L, C) **[COMP]** Build the acquisition engine: robots.txt checking, a rate limit per domain, an honest user agent with contact details, retries with backoff, conditional requests, a cache, and the ability to resume. *AC:* tests against a local test server show that disallowed paths are never fetched and the rate limit holds.
- [ ] **P3-08** (M, C) Build connectors for RSS, sitemaps, generic HTML listings and PDF downloads. Write a source-specific connector only when a generic one fails. *AC:* each connector type is tested against stored test pages.
- [ ] **P3-09** (S, C) Write the acquisition log: source, URL, timestamp, status, error and content hash, validated against its schema. *AC:* every fetch attempt appears in the log, including failures.
- [ ] **P3-10** (S, C) Run a pilot: crawl 3 sources from start to finish and review the log. *AC:* a pilot report with document counts and an error breakdown.

## Phase 4: Corpus collection

Goal: build the raw defence corpus.

- [ ] **P4-01** (M, C) **[COMP]** Run the initial crawl of every source selected for V0.1. *AC:* the crawl finishes and every failure has a logged reason.
- [ ] **P4-02** (S, C) Assign document IDs at ingest, using a scheme from P0-07. *AC:* no duplicate IDs, and the same content always gets the same ID (tested).
- [ ] **P4-03** (M, C) Extract metadata: title, author, publisher, date, URL, source and language. *AC:* field coverage is reported, and missing values are left empty, never guessed.
- [ ] **P4-04** (S, C) Store the raw documents as they were fetched, never changed, with their hashes. *AC:* a re-hash check passes on all raw files.
- [ ] **P4-05** (S, C) Write a provenance validator: every document has a source, URL, fetch time and hash. *AC:* the validator passes, and a broken record makes it fail (tested).
- [ ] **P4-06** (S, C) Write a raw corpus stats report: counts by source, language, date and document type. *AC:* `reports/raw-corpus-stats.md` exists and the Key numbers above are updated.

## Phase 5: Corpus cleaning and quality control

Goal: turn raw documents into reliable machine-learning text.

- [ ] **P5-01** (M, C) Extract the main content from HTML. *AC:* tested on a set of stored pages, and a manual check of 20 pages finds no navigation text or comments left in.
- [ ] **P5-02** (M, C) Extract text from PDFs, and flag scanned PDFs that have no text layer. *AC:* the scanned flag is tested, and offsets are kept in the extracted text.
- [ ] **P5-03** (S, C) Normalise encoding: Unicode NFC, broken characters, and spacing. *AC:* unit tested.
- [ ] **P5-04** (S, C) Remove boilerplate that repeats across a site (footers, cookie notices, related-article lists). *AC:* there are before and after examples for each major source.
- [ ] **P5-05** (S, C) Detect the language of each document and store it with a confidence score. Non-English documents are set aside, not deleted (D-005). *AC:* every document has a language label, and only English documents go on to the next steps.
- [ ] **P5-06** (S, C) Filter by quality: length, symbol ratio and repetition, with thresholds set in the config. *AC:* the reasons for removal are counted and a sample of removed documents has been checked.
- [ ] **P5-07** (S, C) Remove exact duplicates using the content hash. *AC:* the counts before and after are reported.
- [ ] **P5-08** (M, C) Detect near-duplicates, for example with MinHash, and write the duplicate clusters to a file. *AC:* the clusters are stored, because P7-01 uses them to keep near-duplicates out of different splits.
- [ ] **P5-09** (S, C) Detect syndication, meaning the same story republished on other sites, and keep one canonical copy per cluster. *AC:* the syndication clusters are stored and linked.
- [ ] **P5-10** (M, C+H) Classify relevance as `RELEVANT`, `NOT_RELEVANT` or `UNCERTAIN`. Version 0 uses gazetteer density and keywords. The human labels about 200 documents to measure it. *AC:* precision and recall on the labelled sample are reported.
- [ ] **P5-11** (S, C) Split documents into sentences and paragraphs, keeping character offsets that point back to the clean text. *AC:* a round-trip test shows the offsets rebuild the text exactly.
- [ ] **P5-12** (S, C+H) Audit the corpus by hand: review a sample of 100 documents and report the problems found. *AC:* `reports/clean-corpus-audit.md` exists, and each problem is either fixed or added to DISCOVERED.
- [ ] **P5-13** (S, C) Stamp a processing version on every clean document and write the clean corpus stats. *AC:* the Key numbers above are updated.

## Phase 6: Annotation system and guidelines

Goal: build the infrastructure people will use to create the gold data.

- [ ] **P6-01** (S, C) Define the annotation schema: document, text, start, end, label, entity ID, annotator, timestamp, `tier`, `ontology_version` and `pre_annotated` (true or false). *AC:* the JSON Schema exists and is tested.
- [ ] **P6-02** (M, C) Store annotations as JSONL in the canonical format, with converters to and from the tool format, BIO tags and span lists. *AC:* the round-trip tests are lossless.
- [ ] **P6-03** (M, C+H) Choose the annotation tool, set it up locally, and record the choice in an ADR. *AC:* an annotator can open a document, label spans and export them into our format.
- [ ] **P6-04** (M, C) **[INT]** Add pre-annotation from the gazetteer and rules (model predictions come later). It must be switched off for the test documents and hard-blocked there. *AC:* a test shows that pre-labels can never be attached to a test document.
- [ ] **P6-05** (L, C+H) Write the annotation guidelines in `docs/annotation-guidelines-v0.1.md`. They cover the labels, boundaries, ambiguity, nesting, hard cases and worked examples. *AC:* the human has reviewed them.
- [ ] **P6-06** (M, H) Run a pilot: 2 annotators each annotate about 20 documents. *AC:* the pilot annotations are exported and the disagreements are listed.
- [ ] **P6-07** (S, C+H) Revise the guidelines and ontology after the pilot, and bump the version if any rule changed. *AC:* every pilot disagreement type is covered by a rule, and the changelog is updated.
- [ ] **P6-08** (S, C+H) Calibrate annotators with a short practice set and an answer key. *AC:* each annotator reaches the agreed threshold before starting gold work.

## Phase 7: Gold test set and human annotation

Goal: create the trustworthy dataset that decides whether the models work. This is the most important phase.

- [ ] **P7-01** (M, C) **[INT]** Select the test documents before any training. Stratify them by source, document type and date, and never split a near-duplicate or syndication cluster across splits. *AC:* the test size and the stratification are reported.
- [ ] **P7-02** (S, C) **[INT]** Freeze the test set: a lock file with the document IDs, content hashes and cluster IDs, and a leakage-check script that runs in CI. The script fails if any test document or cluster appears in train, dev, silver or synthetic data. *AC:* a deliberately planted leak makes CI fail.
- [ ] **P7-03** (L, H) **[INT]** Annotate the test set by hand from scratch, with no pre-labels. *AC:* every test document is annotated and the records show `pre_annotated=false`.
- [ ] **P7-04** (L, H) Annotate the gold training data. Pre-labels are allowed here and recorded as such. *AC:* the annotated documents are exported and their counts are reported.
- [ ] **P7-05** (M, H) Double-annotate a subset, at least 20% of the test set and some of the training data. *AC:* the overlap set is complete.
- [ ] **P7-06** (S, C) Measure inter-annotator agreement: strict and partial span F1, both per label and overall. *AC:* `reports/iaa-v0.1.md` exists and the Key numbers above are updated.
- [ ] **P7-07** (M, H) Adjudicate the disagreements and log every change. *AC:* there are no unresolved disagreements, and the adjudication log is stored.
- [ ] **P7-08** (S, C) Build the TRAIN, DEV and TEST splits by document and cluster as `data/gold/v0.1/`. *AC:* the leakage check passes and the splits are versioned.
- [ ] **P7-09** (S, C) Write the dataset statistics (documents, tokens, entities, entities per label, source distribution) and a first draft of the datasheet. *AC:* the Key numbers above are updated.

## Phase 8: Synthetic dataset generation

Goal: use the existing entity knowledge to bootstrap training, without pretending synthetic data is gold.

- [ ] **P8-01** (M, C+H) **[INT]** Build the generation framework behind an adapter that supports templates and local or API LLM backends. Which backend is allowed is decided when Phase 8 starts. No test-set text may appear in prompts or few-shot examples. *AC:* a prompt audit test confirms that no test text appears.
- [ ] **P8-02** (M, C) Generate example contexts around KB entities, with the entity conditioned on its label.
- [ ] **P8-03** (S, C) Generate contexts that contain several entities.
- [ ] **P8-04** (S, C) Vary aliases and abbreviations using the gazetteer.
- [ ] **P8-05** (S, C) Generate ambiguous examples, where the same surface form has different labels depending on context.
- [ ] **P8-06** (S, C) Generate hard negatives: defence-like text with no entities, and non-defence uses of ambiguous names.
- [ ] **P8-07** (S, C) Augment rare labels, boosting labels that have few examples in the KB and gold statistics.
- [ ] **P8-08** (S, C) Align and validate spans automatically: every offset must match its text and every label must exist in the ontology. *AC:* no invalid spans, and every record has `tier=synthetic`.
- [ ] **P8-09** (S, C+H) Run quality control on synthetic data: the human reviews a sample of 100 examples. *AC:* the error rate is reported, and the generator is fixed if the rate is above the threshold.
- [ ] **P8-10** (S, C) **[INT]** Check synthetic data for near-duplicates against the test set. *AC:* zero matches above the threshold, and the leakage check passes.

## Phase 9: NER model experiments

Goal: find out which type of model works best for our ontology. The winner is not decided in advance. Every experiment uses DEV only.

- [ ] **P9-01** (M, C) Build a shared training and evaluation harness: the same data loaders, splits, seeds and logging for every model, and every run recorded with its config, data version and commit. *AC:* a dummy model trains and evaluates end to end.
- [ ] **P9-02** (S, C) Build a gazetteer and rule baseline. *AC:* DEV scores are logged.
- [ ] **P9-03** (M, C) Train a DeBERTa token-classification NER model. *AC:* DEV scores are logged for at least 3 seeds.
- [ ] **P9-04** (M, C) Run GLiNER zero-shot and fine-tuned. *AC:* DEV scores are logged for both.
- [ ] **P9-05** (L, C) Build our own span-based model. *AC:* it trains reproducibly and its DEV scores are logged.
- [ ] **P9-06** (M, C) Run training-data ablations: gold; gold + synthetic; gold + silver; gold + synthetic + silver. *AC:* a comparison table goes into the Progress log.
- [ ] **P9-07** (S, C) Run rare-entity experiments. *AC:* recall per rare label is compared across models.
- [ ] **P9-08** (S, C) Run hard-negative experiments. *AC:* the change in false positives is measured.
- [ ] **P9-09** (S, C) Run confidence and calibration experiments. *AC:* reliability plots and the expected calibration error per model.
- [ ] **P9-10** (M, C) Iterate based on errors: build an error taxonomy on DEV, and record which error each experiment targets. *AC:* `reports/error-taxonomy.md` exists.

## Phase 10: Model evaluation and selection

Goal: choose the model based on evidence from the frozen test set.

- [ ] **P10-01** (M, C) Build the evaluation library: strict and partial span F1, per-label scores, a confusion matrix, and a boundary error breakdown. *AC:* toy cases are checked against a known reference implementation.
- [ ] **P10-02** (S, C) **[INT]** Run each final candidate model on the frozen TEST set, once. *AC:* every TEST run is logged, with no repeated runs used to tune a model.
- [ ] **P10-03** (S, C) Report rare-label recall and the precision and recall trade-offs (curves over confidence thresholds). *AC:* the plots are in the benchmark report.
- [ ] **P10-04** (M, C) Analyse errors on TEST: confusion pairs, boundary errors and the main failure types. *AC:* the analysis is in the report, with examples.
- [ ] **P10-05** (S, C) Measure inference speed and memory on the hardware the annotator will run on, on both CPU and GPU. *AC:* measured numbers are in the report.
- [ ] **P10-06** (M, H) Measure the human correction rate: compare the time to correct model output with the time to annotate from scratch, on a small sample. *AC:* minutes per document are reported for both.
- [ ] **P10-07** (S, C+H) Select the model and write `reports/benchmark-v0.1.md`. *AC:* the decision and the reasons are recorded in Decisions.

## Phase 11: Defence NER annotator

Goal: turn the selected model into a tool that can annotate documents.

- [ ] **P11-01** (S, C) Build the input interface: a Python API and a command-line tool that accept text, files and folders.
- [ ] **P11-02** (S, C) Reuse the Phase 5 preprocessing so that offsets match the clean text.
- [ ] **P11-03** (S, C) Run NER inference with batching.
- [ ] **P11-04** (S, C) Integrate the gazetteer and attach entity IDs where the match is unambiguous.
- [ ] **P11-05** (S, C) Resolve overlapping and conflicting spans, following the nesting ADR.
- [ ] **P11-06** (S, C) Add confidence scores and a human-review threshold set in the config.
- [ ] **P11-07** (S, C) Produce structured output that is valid against the schema, with `tier=silver`, the model version and the ontology version.
- [ ] **P11-08** (M, C) Make the tool run locally and offline: no network calls, a CPU fallback, and a container image. *AC:* it runs with the network switched off.
- [ ] **P11-09** (S, C) Test the annotator on unseen documents, including empty, very long and non-English inputs. *AC:* the tests pass.

## Phase 12: End-to-end V0.1 release

Goal: show the whole system working: source → scraper → raw → cleaning → corpus → NER → annotated document.

- [ ] **P12-01** (M, C) Integrate the pipeline so a single command runs every stage, driven by the config.
- [ ] **P12-02** (S, C) Write integration tests on small test-fixture sources.
- [ ] **P12-03** (S, C) Validate every data folder against its schema.
- [ ] **P12-04** (S, C) **[INT]** Run a final leakage audit across all splits and tiers. *AC:* clean, with the report stored.
- [ ] **P12-05** (S, C) Test reproducibility: rebuild from a clean environment and reproduce the DEV score of the selected model. *AC:* the score is reproduced within tolerance.
- [ ] **P12-06** (S, C) Benchmark the performance of the full pipeline. *AC:* throughput is measured and reported.
- [ ] **P12-07** (S, C+H) **[COMP]** Package the corpus following the redistribution decision: full text only where allowed, and URLs with offsets otherwise. *AC:* each source's packaging matches its compliance status.
- [ ] **P12-08** (S, C) Package the model with a model card covering its intended use, data, metrics and limits.
- [ ] **P12-09** (M, C) Write the documentation: datasheet, data statement, guidelines, benchmark results, limitations and a how-to.
- [ ] **P12-10** (S, H) The human signs off the release, and the release is tagged `v0.1`. *AC:* the tag exists and Decisions has a release entry.

---

## Roadmap (after V0.1)

Do not start these phases before P12-10 unless the human decides otherwise in Decisions. Before a phase starts, add sizes, owners and acceptance criteria to its tasks.

## Phase 13: Continuous web → annotation pipeline

- [ ] **P13-01** Scheduled scraping
- [ ] **P13-02** Detect new documents
- [ ] **P13-03** Process documents incrementally
- [ ] **P13-04** Annotate new documents automatically with NER
- [ ] **P13-05** Create the silver dataset
- [ ] **P13-06** Route annotations by confidence
- [ ] **P13-07** Detect entities not in the KB
- [ ] **P13-08** Human review queue
- [ ] **P13-09** Promote reviewed annotations to gold
- [ ] **P13-10** Version the corpus

## Phase 14: Human-in-the-loop and active learning

- [ ] **P14-01** Uncertainty sampling
- [ ] **P14-02** Sampling where models disagree
- [ ] **P14-03** Rare-label sampling
- [ ] **P14-04** Sampling of entities not in the KB
- [ ] **P14-05** Diversity sampling
- [ ] **P14-06** Prioritise the review queue
- [ ] **P14-07** Capture human corrections
- [ ] **P14-08** Measure annotation efficiency
- [ ] **P14-09** Run active-learning rounds

## Phase 15: Continuous model improvement

- [ ] **P15-01** Version the datasets
- [ ] **P15-02** Retrain on a schedule
- [ ] **P15-03** Train on gold plus validated silver data
- [ ] **P15-04** Refresh the synthetic data
- [ ] **P15-05** Train on known errors
- [ ] **P15-06** Regression tests against the frozen test set and earlier models
- [ ] **P15-07** Calibrate the model
- [ ] **P15-08** Version the models (V0.1 → V0.2 → … → V1.0)
- [ ] **P15-09** Evaluate models automatically
- [ ] **P15-10** Release models in a controlled way

## Phase 16: Advanced defence NLP platform

- [ ] **P16-01** Entity linking
- [ ] **P16-02** Entity discovery
- [ ] **P16-03** Alias discovery
- [ ] **P16-04** Relation extraction
- [ ] **P16-05** Event extraction (deployments, exercises, acquisitions, launches, announcements, programmes)
- [ ] **P16-06** Knowledge graph
- [ ] **P16-07** Entity-aware search across the corpus
- [ ] **P16-08** Domain language models (domain-adaptive pretraining, instruction tuning)
- [ ] **P16-09** Integrated defence AI platform

---

## Human checklist

These are things Claude Code cannot do. Fill in the owner for each one.

| Item | Needed by | Lead time | Owner | Status |
|---|---|---|---|---|
| Git remote and code licence | P0-01 | Short | | |
| Place the inherited CSVs | P0-03 | Short | | |
| Sign off the V0.1 scope | P0-05 | Short | | |
| Compute (GPU access or budget) | P9-01 | Days to weeks | | |
| Approve the ontology label set and sign off the ontology | P1-02, P1-08 | Short | | |
| Review source credibility tiers | P3-03 | Days | | |
| Terms of use and licence policy for restricted sources | P3-05, P12-07 | Days to weeks | | |
| Annotators recruited and available (ideally 2 or more, with defence knowledge) | P6-06 | Weeks. Start now. | | |
| Hours for test and gold annotation | P7-03, P7-04 | Weeks | | |
| Relevance labels for about 200 documents | P5-10 | Days | | |
| Review the synthetic data sample | P8-09 | Short | | |
| Release sign-off | P12-10 | Short | | |

---

## Decisions log

| Date | ID | Decision | Reason |
|---|---|---|---|
| 2026-10-06 | D-001 | The project starts from zero. The only inherited assets are `01_NER_MASTER_LIST.csv` (992 entities) and `02_SOURCE_MASTER_LIST.csv` (207 sources), and both are read-only. | No corpus, pipeline, model or final ontology exists yet. |
| 2026-10-06 | D-002 | V0.1 is Phases 0 to 12. Phases 13 to 16 are the expansion roadmap. | V0.1 must show the full source-to-annotated-document loop first. |
| 2026-10-06 | D-003 | The model is chosen by evidence from the frozen test set. DeBERTa, GLiNER and a custom span model are baselines, not a pre-chosen winner. | This is the project goal. |
| 2026-10-06 | D-004 | Raw, silver, synthetic and gold data are kept separate. The test set is annotated from scratch and frozen before training. | This keeps the benchmark unbiased. |
| 2026-10-06 | D-005 | The corpus, annotation and models are English only for now. Every document still gets a language label (P5-05). | Human decision. Other languages can be added later. |
| 2026-10-07 | D-006 | The code licence is MIT and the Git remote is `https://github.com/asitshastri/Test_nuvo.git`. The corpus licence is decided in P3. | Human confirmed both on 2026-10-07. |
| 2026-10-07 | D-007 | Heavy or Windows-fragile libraries (fasttext, playwright, trafilatura, pymupdf, datasketch, httpx) are optional extras, added in the phase that needs them. | Keeps `pip install -e .[dev]` reliable. |
| 2026-10-07 | D-008 | Pre-commit excludes `data/inherited/`, `TODO.md`, `CLAUDE.md`. | Hooks must never rewrite read-only inherited data. |
| 2026-10-07 | D-009 | CLAUDE.md and TODO.md are the governing documents. A phase prompt is an execution instruction for the approved phase and cannot silently replace TODO.md task definitions. The first P0 run used a pasted prompt with its own 13-task list; that fact is kept (an earlier version of this decision wrongly made that list authoritative). Reconciliation: `reports/P0_RECONCILIATION.md`. | Human correction, 2026-10-07. |

## Progress log

Newest first, one line per finished task.

| Date | Task | What changed | Checks | Commit |
|---|---|---|---|---|
| 2026-10-06 | Planning | Wrote TODO.md from the 17-phase project plan, in the format of the reference TODO | n/a | n/a |
| 2026-10-07 | P0 first run (pasted prompt, not TODO.md numbering) | Built repo tooling, validators, schemas, docs, templates, tier and leakage checks, RunLog; pushed to GitHub | 43 tests, 92% coverage, ruff, black, mypy, pre-commit; CI 3.11 and 3.12 green | 1275739 |
| 2026-10-07 | P0-01, P0-02, P0-03 | Marked done after fixing .gitignore, README goal, CLAUDE.md Data rules, CHECKSUMS.txt, byte-flip test | 45 tests, 92% coverage; ruff, black, mypy clean | reconciliation commit |
| 2026-10-07 | P0 reconciliation | Wrote reports/P0_RECONCILIATION.md; corrected D-009; reclassified the 13 tasks; added the leakage step to CI | see report section 6 | reconciliation commit |
| 2026-10-07 | P0-05 (draft only, not done) | Wrote docs/v0.1-scope.md; task stays `[!]` until the human signs off | docs only; 45 tests, ruff, black, mypy, pre-commit, leakage re-run clean | scope-draft commit |
