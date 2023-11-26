init:
	pip install --no-cache-dir poetry && \
	poetry install --no-interaction
shell:
	poetry shell
test:
	pytest
coverage:
	pytest --cov
lint:
	isort .
	autopep8 .
check_lint:
	isort --check --diff .
	flake8 .
lock:
	poetry lock
	sudo chown -R ${USER} poetry.lock
