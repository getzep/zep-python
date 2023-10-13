.PHONY: all format lint test test coverage docs

all: help

coverage:
	poetry run pytest --cov \
		--cov-config=.coveragerc \
		--cov-report xml \
		--cov-report term-missing:skip-covered

docs:
	poetry run pdoc --html --output-dir docs zep_python

format:
	poetry run black .
	poetry run ruff --select I --fix .

lint:
	poetry run mypy --exclude tests zep_python/
	poetry run black . --check
	poetry run ruff zep_python/

test:
	poetry run pytest tests
