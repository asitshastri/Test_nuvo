.PHONY: help setup lint format type test ci clean

help:
	@echo "Defence Corpus Development"
	@echo "setup:  Install dependencies"
	@echo "lint:   Run ruff"
	@echo "format: Format code"
	@echo "type:   Type check"
	@echo "test:   Run pytest"
	@echo "ci:     Run all checks (non-mutating)"
	@echo "clean:  Clean cache"

setup:
	pip install -e ".[dev]"

lint:
	ruff check .

format:
	black src/ tests/
	ruff check . --select I --fix

type:
	mypy src/ --strict

test:
	pytest tests/ -v --cov=src

ci:
	ruff check .
	black --check src/ tests/
	mypy src/ --strict
	pytest tests/ -v --cov=src
	@echo "All checks passed"

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache -o -name .mypy_cache -o -name .ruff_cache \) -exec rm -rf {} + || true
