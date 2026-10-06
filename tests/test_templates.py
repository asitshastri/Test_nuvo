"""Templates must keep their required sections and reference the evidence doc."""

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "REVIEW.md": [
        "What Was Promised",
        "What Was Delivered",
        "Tests",
        "Regressions",
        "Gate Decision",
    ],
    "PHASE_REPORT.md": [
        "Summary",
        "Tasks Completed",
        "Key Numbers",
        "Gate",
        "Decisions Made",
        "Risks",
        "Next Steps",
        "Reproducibility",
    ],
    "EXP.md": ["Hypothesis", "Baseline", "Change", "Fixed slice", "Metrics", "Decision", "Reason"],
}


@pytest.mark.parametrize("name", REQUIRED)
def test_sections_and_reference(name: str) -> None:
    text = (ROOT / "templates" / name).read_text(encoding="utf-8")
    for section in REQUIRED[name]:
        assert f"## {section}" in text, f"{name} missing {section}"
    assert "docs/01_EVIDENCE_AND_DECISIONS.md" in text
