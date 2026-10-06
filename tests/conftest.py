"""Shared fixtures."""

from typing import Any

import pytest


@pytest.fixture
def entity() -> dict[str, Any]:
    return {
        "entity_id": "NER-0001",
        "entity_text": "Indian Army",
        "entity_type": "MIL_ORG",
        "subtype": "SERVICE",
        "confidence": "high",
    }


@pytest.fixture
def source() -> dict[str, Any]:
    return {
        "source_id": "SRC-001",
        "source_name": "Wikipedia",
        "url": "https://en.wikipedia.org",
        "domain": "wikipedia.org",
        "source_type": "encyclopedia",
        "credibility_tier": "C",
    }


@pytest.fixture
def document() -> dict[str, Any]:
    return {
        "doc_id": "DOC-001",
        "source_id": "SRC-001",
        "url": "https://example.com",
        "fetch_time": "2026-10-07T12:00:00Z",
        "raw_bytes_hash": "sha256:abc123",
        "tier": "raw",
    }


@pytest.fixture
def annotation() -> dict[str, Any]:
    return {
        "doc_id": "DOC-001",
        "start": 0,
        "end": 11,
        "text": "Indian Army",
        "entity_id": "NER-0001",
        "entity_type": "MIL_ORG",
        "tier": "gold",
    }
