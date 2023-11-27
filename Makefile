init:
	python3.11 -m pip install --no-cache-dir poetry=="1.7.1" && \
	python3.11 -m poetry install --no-interaction
shell:
	python3.11 -m poetry shell
test:
	python3.11 -m pytest
coverage:
	python3.11 -m pytest --cov=sensor_data_parser
lint:
	python3.11 -m isort .
	python3.11 -m autopep8 .
check_lint:
	python3.11 -m isort --check --diff .
	python3.11 -m flake8 .
lock:
	python3.11 -m poetry lock
	sudo chown -R ${USER} poetry.lock
