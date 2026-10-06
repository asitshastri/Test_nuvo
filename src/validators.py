"""Schema validators for all data types.

Each validator returns ``{"valid": n, "total": n, "errors": [...], "warnings": [...]}``.
Matching JSON Schemas live in ``configs/schemas/``.
"""

from collections.abc import Iterable
from typing import Any

Record = dict[str, Any]
Result = dict[str, Any]


def _check_required(records: list[Record], required: Iterable[str], errors: list[str]) -> set[int]:
    """Append an error per record missing required/empty fields; return bad row indices."""
    bad: set[int] = set()
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            errors.append(f"Row {i}: not a mapping")
            bad.add(i)
            continue
        missing = sorted(f for f in required if f not in rec or rec[f] in (None, ""))
        if missing:
            errors.append(f"Row {i}: missing {missing}")
            bad.add(i)
    return bad


def _result(records: list[Record], bad: set[int], errors: list[str], warnings: list[str]) -> Result:
    return {
        "valid": len(records) - len(bad),
        "total": len(records),
        "errors": errors,
        "warnings": warnings,
    }


def validate_entities(entities: list[Record]) -> Result:
    """Validate entity records (entity_id, entity_text, entity_type, subtype required)."""
    errors: list[str] = []
    warnings: list[str] = []
    bad = _check_required(entities, ("entity_id", "entity_text", "entity_type", "subtype"), errors)
    for i, ent in enumerate(entities):
        if isinstance(ent, dict) and "confidence" in ent:
            if ent["confidence"] not in ("high", "medium", "low"):
                warnings.append(f"Row {i}: confidence={ent['confidence']}")
    return _result(entities, bad, errors, warnings)


def validate_sources(sources: list[Record]) -> Result:
    """Validate source records (source_id, source_name, url, domain, source_type required)."""
    errors: list[str] = []
    warnings: list[str] = []
    bad = _check_required(
        sources, ("source_id", "source_name", "url", "domain", "source_type"), errors
    )
    for i, src in enumerate(sources):
        if isinstance(src, dict) and "credibility_tier" in src:
            if src["credibility_tier"] not in ("A", "B", "C"):
                warnings.append(f"Row {i}: tier={src['credibility_tier']}")
    return _result(sources, bad, errors, warnings)


def validate_documents(documents: list[Record]) -> Result:
    """Validate document records (provenance fields required)."""
    errors: list[str] = []
    warnings: list[str] = []
    bad = _check_required(
        documents, ("doc_id", "source_id", "url", "fetch_time", "raw_bytes_hash", "tier"), errors
    )
    for i, doc in enumerate(documents):
        if isinstance(doc, dict) and "language" in doc and len(str(doc["language"])) != 2:
            warnings.append(f"Row {i}: language={doc['language']}")
    return _result(documents, bad, errors, warnings)


def validate_annotations(annotations: list[Record]) -> Result:
    """Validate annotation records (span, label and tier required; start < end)."""
    errors: list[str] = []
    warnings: list[str] = []
    bad = _check_required(
        annotations, ("doc_id", "start", "end", "text", "entity_id", "entity_type", "tier"), errors
    )
    for i, ann in enumerate(annotations):
        if i in bad:
            continue
        if "confidence" in ann and not 0.0 <= ann["confidence"] <= 1.0:
            warnings.append(f"Row {i}: confidence={ann['confidence']} not in [0.0, 1.0]")
        if ann["start"] >= ann["end"]:
            errors.append(f"Row {i}: start >= end")
            bad.add(i)
    return _result(annotations, bad, errors, warnings)
