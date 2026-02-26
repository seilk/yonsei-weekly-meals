PYTHON ?= python3

.PHONY: update test

update:
	$(PYTHON) -m src.main

test:
	$(PYTHON) -m pytest -q
