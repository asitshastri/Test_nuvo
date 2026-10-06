"""Tests for validators: empty, valid and corrupted samples."""

from typing import Any

import pytest

from src.validators import (
    validate_annotations,
    validate_documents,
    validate_entities,
    validate_sources,
)

CASES = [
    (validate_entities, "entity"),
    (validate_sources, "source"),
    (validate_documents, "document"),
    (validate_annotations, "annotation"),
]


@pytest.mark.parametrize(("fn", "fixture"), CASES)
def test_empty(fn: Any, fixture: str) -> None:
    assert fn([]) == {"valid": 0, "total": 0, "errors": [], "warnings": []}


@pytest.mark.parametrize(("fn", "fixture"), CASES)
def test_valid(fn: Any, fixture: str, request: pytest.FixtureRequest) -> None:
    result = fn([request.getfixturevalue(fixture)])
    assert result["valid"] == 1
    assert result["errors"] == []


@pytest.mark.parametrize(("fn", "fixture"), CASES)
def test_corrupted(fn: Any, fixture: str, request: pytest.FixtureRequest) -> None:
    result = fn([{"junk": 1}, request.getfixturevalue(fixture), "not-a-dict"])
    assert result["total"] == 3
    assert result["valid"] == 1
    assert len(result["errors"]) == 2


def test_multiple_missing_counts_row_once() -> None:
    result = validate_entities([{"entity_id": "x"}])
    assert result["valid"] == 0
    assert len(result["errors"]) == 1


def test_bad_confidence_is_warning(entity: dict[str, Any]) -> None:
    entity["confidence"] = "maybe"
    result = validate_entities([entity])
    assert result["valid"] == 1
    assert len(result["warnings"]) == 1


def test_invalid_span(annotation: dict[str, Any]) -> None:
    annotation.update(start=10, end=5)
    result = validate_annotations([annotation])
    assert result["valid"] == 0
    assert "start >= end" in result["errors"][0]


def test_annotation_confidence_range(annotation: dict[str, Any]) -> None:
    annotation["confidence"] = 1.5
    assert len(validate_annotations([annotation])["warnings"]) == 1


def test_document_language_warning(document: dict[str, Any]) -> None:
    document["language"] = "english"
    assert len(validate_documents([document])["warnings"]) == 1
