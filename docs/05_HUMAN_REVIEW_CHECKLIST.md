# Human Review Checklist

Things only the human can do or approve. This file mirrors the "Human checklist" table in `TODO.md` (the source of truth for owners and status) and adds sign-off columns. Dates are UNKNOWN until the human sets them; the project deadline is 31 Oct 2026 (CLAUDE.md).

| Phase | Item | Needed by task | Owner | Due | Sign-off |
|---|---|---|---|---|---|
| P0 | Git remote and code licence. FACT: remote `asitshastri/Test_nuvo`, MIT, confirmed by the human 2026-10-07 | P0-01 | | | ☐ |
| P0 | Repository visibility. FACT: currently PUBLIC; no decision recorded | P0-01 | | | ☐ |
| P0 | Inherited CSVs placed in `data/inherited/` (done, 2026-10-07) | P0-03 | | | ☐ |
| P0 | V0.1 scope signed off | P0-05 | | | ☐ |
| P0 | `reports/P0_RECONCILIATION.md`, `P0_REPORT.md` and `P0_REVIEW.md` read and approved | P0 gate | | | ☐ |
| P1 | Ontology label set approved, ontology signed off | P1-02, P1-08 | | | ☐ |
| P3 | Source credibility tiers reviewed | P3-03 | | | ☐ |
| P3 | Terms-of-use and licence policy for restricted sources | P3-05, P12-07 | | | ☐ |
| P5 | Relevance labels for about 200 documents | P5-10 | | | ☐ |
| P6 | Annotators recruited (2+, defence knowledge) | P6-06 | | | ☐ |
| P7 | Hours committed for test and gold annotation | P7-03, P7-04 | | | ☐ |
| P8 | Synthetic data sample reviewed | P8-09 | | | ☐ |
| P9 | Compute (GPU access or budget) | P9-01 | | | ☐ |
| P12 | Release sign-off | P12-10 | | | ☐ |

## What sign-off means

Sign-off: you have reviewed the item, asked your questions and approve proceeding.
Not sign-off: you have not looked yet, or you have open concerns. Record concerns under "Blockers" in `TODO.md` and ask Claude Code to address them.
