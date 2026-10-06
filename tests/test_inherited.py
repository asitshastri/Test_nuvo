"""Tests for inherited asset loading and the locked inherited CSVs."""

from pathlib import Path

import pytest
import yaml

from src.inherited import (
    ambiguous_abbreviations,
    checksum_inherited,
    generate_report,
    load_entities,
    load_sources,
    sha256_file,
)

ROOT = Path(__file__).resolve().parent.parent
CHECKSUMS = ROOT / "configs" / "inherited_checksums.yaml"


def test_sha256_file(tmp_path: Path) -> None:
    f = tmp_path / "t.txt"
    f.write_bytes(b"test content")
    assert sha256_file(f) == (
        "sha256:6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72"
    )


def test_load_and_checksum(tmp_path: Path) -> None:
    e, s, out = tmp_path / "e.csv", tmp_path / "s.csv", tmp_path / "c.yaml"
    e.write_text("entity_id,entity_text\nNER-0001,Indian Army\n")
    s.write_text("source_id,source_name\nSRC-001,Wikipedia\n")
    assert len(load_entities(e)) == 1
    assert len(load_sources(s)) == 1
    result = checksum_inherited(e, s, out)
    assert result["entities_csv"]["rows"] == 1
    assert yaml.safe_load(out.read_text())["sources_csv"]["sha256"] == sha256_file(s)


def test_ambiguous_abbreviations(tmp_path: Path) -> None:
    e = tmp_path / "e.csv"
    e.write_text(
        "entity_id,entity_text,abbreviations,notes\n"
        "1,Indian Army,IA,Abbrev ambiguous\n"
        "2,Iowa,IA,\n"
        "3,Navy,NV,\n"
    )
    assert [a for a, _ in ambiguous_abbreviations(load_entities(e))] == ["IA"]


@pytest.mark.skipif(not CHECKSUMS.exists(), reason="checksums not generated yet")
class TestLockedInherited:
    def _spec(self) -> dict[str, dict[str, object]]:
        return yaml.safe_load(CHECKSUMS.read_text())  # type: ignore[no-any-return]

    @pytest.mark.parametrize("key", ["entities_csv", "sources_csv"])
    def test_checksum_and_rows_unchanged(self, key: str) -> None:
        spec = self._spec()[key]
        path = ROOT / str(spec["path"])
        assert sha256_file(path) == spec["sha256"], "inherited CSV was modified"
        assert len(load_entities(path)) == spec["rows"]

    def test_expected_counts(self) -> None:
        spec = self._spec()
        assert spec["entities_csv"]["rows"] == 992
        assert spec["sources_csv"]["rows"] == 207

    def test_report_generates(self) -> None:
        spec = self._spec()
        report = generate_report(
            load_entities(ROOT / str(spec["entities_csv"]["path"])),
            load_sources(ROOT / str(spec["sources_csv"]["path"])),
        )
        assert "Total: 992" in report and "Total: 207" in report


def test_checksums_txt_matches_files() -> None:
    txt = ROOT / "data" / "inherited" / "CHECKSUMS.txt"
    assert txt.exists()
    for line in txt.read_text().splitlines():
        digest, name = line.split("  ", 1)
        assert sha256_file(ROOT / "data" / "inherited" / name) == f"sha256:{digest}"


def test_changing_a_byte_breaks_checksum(tmp_path: Path) -> None:
    spec = yaml.safe_load(CHECKSUMS.read_text())["entities_csv"]
    copy = tmp_path / "copy.csv"
    data = bytearray((ROOT / spec["path"]).read_bytes())
    assert sha256_file(copy := _write(copy, bytes(data))) == spec["sha256"]
    data[0] ^= 1
    assert sha256_file(_write(copy, bytes(data))) != spec["sha256"]


def _write(path: Path, data: bytes) -> Path:
    path.write_bytes(data)
    return path
