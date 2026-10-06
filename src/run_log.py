"""Experiment run logging: every data-producing run writes experiments/RUN-*.json."""

import hashlib
import json
import subprocess
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

EXPERIMENTS_DIR = Path("experiments")


class RunLog:
    """Log a data-producing run (inputs, outputs, warnings, errors, runtime)."""

    def __init__(self, task: str) -> None:
        self.task = task
        self._started = time.monotonic()
        self.timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.git_hash = self._get_git_hash()
        self.config_hash = ""
        self.inputs: dict[str, Any] = {}
        self.outputs: dict[str, Any] = {}
        self.warnings: list[str] = []
        self.errors: list[str] = []
        self.runtime_seconds = 0.0

    @staticmethod
    def _get_git_hash() -> str:
        """Short hash of HEAD, or ``unknown`` outside a repo / without commits."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
            )
            return result.stdout.strip()[:8] or "unknown"
        except (OSError, subprocess.CalledProcessError):
            return "unknown"

    def set_config_hash(self, config_path: Path) -> None:
        """Hash a config file (first 8 hex chars of SHA-256)."""
        if config_path.exists():
            self.config_hash = hashlib.sha256(config_path.read_bytes()).hexdigest()[:8]

    def add_input(self, name: str, count: int, hash_val: str | None = None) -> None:
        self.inputs[name] = {"count": count, "hash": hash_val}

    def add_output(self, name: str, count: int, hash_val: str | None = None) -> None:
        self.outputs[name] = {"count": count, "hash": hash_val}

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def save(self, runtime_seconds: float | None = None) -> Path:
        """Write the log and return its path. Runtime defaults to time since creation."""
        self.runtime_seconds = (
            runtime_seconds if runtime_seconds is not None else time.monotonic() - self._started
        )
        data = {
            "timestamp": self.timestamp,
            "task": self.task,
            "git_hash": self.git_hash,
            "config_hash": self.config_hash,
            "inputs": self.inputs,
            "outputs": self.outputs,
            "warnings": self.warnings,
            "errors": self.errors,
            "runtime_seconds": self.runtime_seconds,
        }
        EXPERIMENTS_DIR.mkdir(exist_ok=True)
        stamp = self.timestamp.replace("-", "").replace(":", "").replace("T", "-")
        path = EXPERIMENTS_DIR / f"RUN-{stamp}-{self.task}.json"
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return path
