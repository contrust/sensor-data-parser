test:
	pytest
coverage:
	pytest --cov
lint:
	isort .
	black --config pyproject.toml .
check_lint:
	isort --check --diff .
	black --config pyproject.toml --check .
	flake8 --config pyproject.toml .
lock:
	poetry lock
	sudo chown -R ${USER} poetry.lock
install:
	pip install --no-cache-dir poetry && \
	poetry config virtualenvs.create false && \
	poetry install --no-interaction --no-root
