"""Summarize all experiment run logs."""

import json
from pathlib import Path
from typing import Any

from src.run_log import EXPERIMENTS_DIR


def list_all_runs(exp_path: Path = EXPERIMENTS_DIR) -> list[dict[str, Any]]:
    """Load every readable ``RUN-*.json``; unreadable files are skipped."""
    runs: list[dict[str, Any]] = []
    if not exp_path.exists():
        return runs
    for log_file in sorted(exp_path.glob("RUN-*.json")):
        try:
            runs.append(json.loads(log_file.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
    return runs


def summarize_runs(exp_path: Path = EXPERIMENTS_DIR) -> str:
    """Return (and print) a text summary of all runs."""
    runs = list_all_runs(exp_path)
    lines = [f"Total runs: {len(runs)}"]
    if runs:
        by_task: dict[str, int] = {}
        for run in runs:
            task = str(run.get("task", "unknown"))
            by_task[task] = by_task.get(task, 0) + 1
        lines.append("Runs by task:")
        lines += [f"  {t}: {n} run(s)" for t, n in sorted(by_task.items())]
        lines.append(f"Total runtime: {sum(r.get('runtime_seconds', 0) for r in runs):.1f}s")
        errors = sum(len(r.get("errors", [])) for r in runs)
        if errors:
            lines.append(f"Errors detected: {errors}")
    text = "\n".join(lines)
    print(text)
    return text


if __name__ == "__main__":
    summarize_runs()
