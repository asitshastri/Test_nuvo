# Evidence Labels and Decision Rules

Every claim in a report, doc or code comment carries one of five labels (CLAUDE.md, "Evidence labels").

| Label | Meaning | Use when |
|---|---|---|
| `FACT` | Checked source | A claim you verified against a named source or computed from our data |
| `INFERENCE` | Reasoned | A deduction from several facts; name the facts |
| `RECOMMENDATION` | Our choice | A design decision, justified but not "true" or "false" |
| `UNKNOWN` | Not established | No source or evidence yet. Never guess |
| `UNVERIFIED` | Source exists, not checked | A claim lifted from an unchecked source (e.g. a vendor page, an inherited CSV row) |

## Examples

- `FACT [data/inherited/01_NER_MASTER_LIST.csv]: 992 entity rows, computed by src/load_inherited.py.`
- `INFERENCE [SRC-001, SRC-003]: Wikipedia and Wikidata overlap on military units, so de-duplicating across them is needed.`
- `RECOMMENDATION: Start collection with API sources because they have the lowest compliance risk.`
- `UNKNOWN: Redistribution terms for SRC-175.`
- `UNVERIFIED [SRC-042]: Vendor claims a 500 km range.`

Every inherited row has `verification_status = UNVERIFIED` until a phase checks it. Treat inherited facts as `UNVERIFIED`.

## How to cite

- One source: `FACT [SRC-042]: ...`
- Several: `FACT [SRC-001, SRC-042]: ...`
- Computed from our data: cite the file or script.
- No source: use `UNKNOWN` or `INFERENCE`, never an unlabelled statement.

## Decision log format

Decisions go in the "Decisions" section of `TODO.md`:

| Date | ID | Decision | Reason |
|---|---|---|---|
| 2026-10-07 | D-001 | Python 3.11 | Fixed by CLAUDE.md coding conventions |
| 2026-10-07 | D-002 | MIT licence for code | Permissive; corpus licence decided separately in P3 |

An experiment-backed decision also links its `experiments/EXP-YYYYMMDD-NN.md`.

## Good and bad

Good: "FACT [SRC-001]: X. INFERENCE [SRC-001, SRC-003]: Y. RECOMMENDATION: Z because Y."

Bad: "The Navy has about 150 ships." No label, no source.

## Hard rule

Never invent citations, numbers, source policies or results. Unknown means `UNKNOWN`.

Report and review templates (`templates/`) reference this document.
