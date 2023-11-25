test:
	pytest
coverage:
	pytest --cov
lint:
	isort src tests
	black --config pyproject.toml src tests
check_lint:
	isort --check --diff src tests
	black --config pyproject.toml --check src tests
	flake8 --config pyproject.toml src tests
lock:
	poetry lock
	sudo chown -R ${USER} poetry.lock
install:
	pip install --no-cache-dir poetry && \
	poetry config virtualenvs.create false && \
	poetry install --no-interaction --no-root
