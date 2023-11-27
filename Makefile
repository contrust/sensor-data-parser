init:
	python3.11 -m pip install --no-cache-dir poetry=="1.7.1" && \
	python3.11 -m poetry install --no-interaction
shell:
	python3.11 -m poetry shell
test:
	pytest
coverage:
	pytest --cov=sensor_data_parser
lint:
	isort .
	autopep8 .
check_lint:
	isort --check --diff .
	flake8 .
lock:
	python3.11 -m poetry lock
	sudo chown -R ${USER} poetry.lock
