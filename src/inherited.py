"""Load and manage inherited assets (CSVs). Inherited files are never edited."""

import hashlib
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


def sha256_file(filepath: Path) -> str:
    """Compute SHA-256 hash of a file, formatted ``sha256:<hex>``."""
    digest = hashlib.sha256()
    with open(filepath, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            digest.update(block)
    return f"sha256:{digest.hexdigest()}"


def load_entities(path: Path) -> pd.DataFrame:
    """Load inherited entity list (all columns as strings; empty cells stay empty)."""
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def load_sources(path: Path) -> pd.DataFrame:
    """Load inherited source list (all columns as strings; empty cells stay empty)."""
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def checksum_inherited(
    entities_path: Path, sources_path: Path, output_path: Path
) -> dict[str, Any]:
    """Compute and save checksums + row counts."""
    now = datetime.now(UTC).isoformat()
    checksums = {
        key: {
            "path": path.as_posix(),
            "rows": len(pd.read_csv(path, dtype=str, keep_default_na=False)),
            "sha256": sha256_file(path),
            "loaded_at": now,
        }
        for key, path in (("entities_csv", entities_path), ("sources_csv", sources_path))
    }
    output_path.write_text(yaml.safe_dump(checksums, sort_keys=True), encoding="utf-8")
    return checksums


def ambiguous_abbreviations(entities: pd.DataFrame) -> list[tuple[str, list[str]]]:
    """Abbreviations shared by >1 entity, plus those flagged ambiguous/colliding in notes."""
    by_abbr: dict[str, list[str]] = {}
    flagged: set[str] = set()
    for _, row in entities.iterrows():
        notes = str(row.get("notes", "")).lower()
        abbrs: list[str] = [a.strip() for a in str(row.get("abbreviations", "")).split(";")]
        for abbr in filter(None, abbrs):
            by_abbr.setdefault(abbr, []).append(row["entity_text"])
            if "ambig" in notes or "collid" in notes or "collision" in notes:
                flagged.add(abbr)
    return sorted((a, names) for a, names in by_abbr.items() if len(names) > 1 or a in flagged)


def _counts(series: pd.Series, limit: int | None = None) -> str:
    counts = series.replace("", "(blank)").value_counts()
    if limit:
        counts = counts.head(limit)
    return "".join(f"- {k}: {v}\n" for k, v in counts.items()) + "\n"


def generate_report(entities: pd.DataFrame, sources: pd.DataFrame) -> str:
    """Generate the P0-03 summary report (all numbers computed from the data: FACT)."""
    out = ["# P0-03: Inherited Assets Summary\n\n", "Evidence: FACT (computed from the CSVs).\n\n"]
    out.append(f"## Entities (01_NER_MASTER_LIST.csv)\n\nTotal: {len(entities)}\n\n")
    out.append("### By Type\n" + _counts(entities["entity_type"]))
    out.append("### By Type / Subtype\n")
    pairs = entities.groupby(["entity_type", "subtype"]).size().reset_index(name="n")
    for etype, sub, n in pairs.itertuples(index=False):
        out.append(f"- {etype} / {sub or '(blank)'}: {n}\n")
    out.append("\n### By Confidence\n" + _counts(entities["confidence"]))
    out.append("### By Ontology Status\n" + _counts(entities["ontology_status"]))
    out.append("### By Verification Status\n" + _counts(entities["verification_status"]))
    out.append("### Top Countries (top 10)\n" + _counts(entities["country_region"], 10))
    amb = ambiguous_abbreviations(entities)
    out.append(f"### Ambiguous Abbreviations ({len(amb)})\n")
    out.extend(f"- {a}: {'; '.join(names[:6])}\n" for a, names in amb)
    out.append(f"\n## Sources (02_SOURCE_MASTER_LIST.csv)\n\nTotal: {len(sources)}\n\n")
    out.append("### By Type\n" + _counts(sources["source_type"]))
    out.append("### By Credibility Tier\n" + _counts(sources["credibility_tier"]))
    out.append("### By Access Method\n" + _counts(sources["access_method"]))
    out.append("### By Verification Status\n" + _counts(sources["verification_status"]))
    out.append(
        "## Data Quality Notes\n\nNo manual fixes applied. Issues are documented for later phases.\n"
    )
    return "".join(out)
