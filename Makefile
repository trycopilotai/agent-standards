PYTHON ?= python3

.PHONY: check lint ci
check:
	$(PYTHON) -B scripts/check.py

lint:
	$(PYTHON) -B vendor/lint/lint.py --cwd . --all

ci:
	$(PYTHON) -B scripts/ci_check.py //:check
