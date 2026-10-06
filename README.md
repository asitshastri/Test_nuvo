# Defence/Security Corpus and NER Platform

The goal is a curated, verified defence and security corpus with human-verified entity annotations. From it we train our own free, locally deployable defence NER model that we control.

## Mission

1. Curated, verified source registry
2. Cleaned, deduplicated, relevance-scored corpus
3. High-quality gold NER dataset + large silver dataset
4. Our own defence NER model (free, deployable)
5. Continuous improvement loop
6. Full documentation

## Quick Start

```bash
git clone <repo-url>
cd <repo>
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
make ci          # or run the commands in the Makefile directly (Windows has no make)
```

## Project Structure

See `CLAUDE.md` for rules and `docs/` for guides. Data lives in physically separate tiers under `data/`.

## Phases

- **Phase 0:** Foundation (this phase)
- **Phase 1–2:** Ontology & KB
- **Phase 3–5:** Sources & collection
- **Phase 6–8:** Annotation & synthetic
- **Phase 9–10:** Training
- **Phase 11–12:** Release

## Data Tiers

`raw/` immutable bytes · `clean/` extracted text · `synthetic/` generated (train only) · `silver/` machine labels · `reviewed/` human-reviewed · `gold/` adjudicated · `slices/` frozen eval · `release/` exports

## Contributing

Follow CLAUDE.md rules and commit often.

## Licence

MIT (code). Corpus licence TBD.
