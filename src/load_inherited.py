#!/usr/bin/env python3
"""Ingest inherited assets, write checksums + report, mark CSVs read-only.

Run from the repo root: ``python -m src.load_inherited [--config PATH] [--dry-run]``
"""

import argparse
import stat
from pathlib import Path

import yaml

from src.inherited import checksum_inherited, generate_report, load_entities, load_sources

DEFAULT_CONFIG = Path("configs/pipeline.yaml")
DEFAULTS = {
    "entities": "data/inherited/01_NER_MASTER_LIST.csv",
    "sources": "data/inherited/02_SOURCE_MASTER_LIST.csv",
    "checksums": "configs/inherited_checksums.yaml",
    "report": "reports/P0-03_INHERITED_ASSETS.md",
}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    ap.add_argument("--dry-run", action="store_true", help="load and report, write nothing")
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8")) or {}
    paths = {**DEFAULTS, **(cfg.get("inherited") or {})}
    entities_path, sources_path = Path(paths["entities"]), Path(paths["sources"])

    entities, sources = load_entities(entities_path), load_sources(sources_path)
    print(f"Loaded {len(entities)} entities, {len(sources)} sources")
    report = generate_report(entities, sources)
    if args.dry_run:
        print("dry-run: nothing written")
        return

    checksum_inherited(entities_path, sources_path, Path(paths["checksums"]))
    Path(paths["report"]).write_text(report, encoding="utf-8")
    for p in (entities_path, sources_path):
        p.chmod(stat.S_IREAD)  # 0o444 on POSIX; read-only attribute on Windows
    print(f"Wrote {paths['checksums']} and {paths['report']}; CSVs set read-only")


if __name__ == "__main__":
    main()
