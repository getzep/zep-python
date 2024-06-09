.PHONY: all format lint test coverage

all: help

coverage:
	poetry run pytest --cov \
		--cov-config=.coveragerc \
		--cov-report xml \
		--cov-report term-missing:skip-covered

format:
	poetry run ruff check --select I --fix .
	poetry run ruff format .

lint:
	poetry run mypy --exclude tests src/
	poetry run ruff check src/

test:
	poetry run pytest tests