# Ingestion Order and Vertical Slice

Order follows CLAUDE.md "Ingestion order": API, bulk/dataset, RSS/sitemap, polite HTML, rendering, archive (CC/Wayback), permission request.

RECOMMENDATION: the first vertical slice is OpenAlex (CLAUDE.md names `docs/12_PIPELINE_V0_1_OPENALEX.md`, which is not in this repo yet: UNKNOWN details). Wikipedia/Wikidata dumps are the next candidates for gazetteer building.

All access respects robots.txt, terms and rate limits. On 401/403/challenge/CAPTCHA the domain is stopped, logged and routed to API/archive/permission request.

## Priority order

1. **API** (stable, documented)
2. **BULK** dumps / datasets
3. **RSS / sitemap**
4. **HTML** (polite crawl)
5. **PDF / rendering** (Playwright only for public pages where automated access is permitted)
6. **ARC** archives (Common Crawl, Wayback)
7. **REG / PAY** registration, permission or payment: needs a human decision

## Inherited sources by access method (FACT: computed from 02_SOURCE_MASTER_LIST.csv)

Total sources: 207. A source can list several methods, so token counts sum to more than 207.

| Method | Sources listing it | Sources where it is listed first |
|---|---|---|
| API | 27 | 10 |
| BULK | 36 | 30 |
| RSS | 23 | 1 |
| HTML | 155 | 153 |
| PDF | 43 | 9 |
| ARC | 2 | 0 |
| REG | 5 | 2 |
| PAY | 2 | 2 |

### Exact combinations

| access_method value | Count |
|---|---|
| HTML | 86 |
| HTML;PDF | 34 |
| HTML;RSS | 22 |
| BULK | 20 |
| PDF | 9 |
| BULK;API | 8 |
| HTML;API | 7 |
| API | 5 |
| API;REG | 3 |
| HTML;BULK | 3 |
| PAY | 2 |
| API;BULK | 1 |
| BULK;HTML | 1 |
| REG;BULK | 1 |
| REG;API | 1 |
| HTML;API;BULK | 1 |
| RSS;HTML | 1 |
| BULK;ARC | 1 |
| API;ARC | 1 |

### Examples by first-listed method

- **API**: Wikidata, OpenStreetMap military tags, SAM.gov Entity Information, UCDP API, Malpedia
- **BULK**: Wikidata database dumps, Wikipedia dumps, DBpedia, GeoNames, GLEIF LEI Golden Copy
- **RSS**: Press Information Bureau
- **HTML**: Wikipedia, Wikipedia (Hindi), Wikipedia (Urdu), Wikipedia (Bengali), Wikipedia (Chinese)
- **PDF**: Comptroller and Auditor General, DoD China Military Power Report, CASI, RAND Corporation, BIISS
- **REG**: START Global Terrorism Database, ACLED
- **PAY**: Janes, LDC Catalog (ACE 2005 and OntoNotes)

## Per-source mapping

The per-source mapping is the `access_method` column of `data/inherited/02_SOURCE_MASTER_LIST.csv`. UNVERIFIED: every row has `verification_status = UNVERIFIED`. Rate limits and authentication needs are UNKNOWN until P3 verification.
