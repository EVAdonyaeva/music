include .env
export $(shell sed 's/=.*//' .env)

SOURCE_DIR=src
TESTS_DIR=tests

export PYTHONPATH=$(SOURCE_DIR)

clean: clean-test clean-mypy

clean-mypy:
	rm -rf .mypy_cache

clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -rf .pytest_cache/
	rm -rf .cache/

bandit:
	poetry run bandit -r ./$(SOURCE_DIR)

safety:
	poetry run safety check

lint: flake8 isort-check

flake8:
	poetry run flake8 $(SOURCE_DIR)
	poetry run flake8 $(TESTS_DIR)

isort-check:
	poetry run isort $(SOURCE_DIR) --diff --color --check-only
	poetry run isort $(TESTS_DIR) --diff --color --check-only

isort:
	poetry run isort $(SOURCE_DIR)
	poetry run isort $(TESTS_DIR)

mypy:
	poetry run mypy --pretty -p $(SOURCE_DIR)

test:
	poetry run pytest tests

test_with_coverage:
	poetry run pytest --cov=$(SOURCE_DIR) --cov-config=$(TESTS_DIR)/coverage.ini

run:
	poetry run python $(SOURCE_DIR)/main.py