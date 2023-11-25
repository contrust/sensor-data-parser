# Sensor data parser
A parser of data from a sensor.
# Data format
Data is a hex string that is divided into chunks of size 8, and a chunk has the following format:

| Variable | Indexes | Description |
| -- |---------| -- |
| Status | 0-1     | Packet indentifier in hex representation which should always be equal to '80' |
| Current value counter | 2-3     | Current value counter in hex representation [00-7f], which should be unique |
| Pressure value | 4-7 | Pressure value in in hex representation |

# Dependencies
You can install the dependencies with poetry
```sh
poetry install --no-interaction --no-root
```
Or build a docker image from the Dockerfile file. 

# Usage
Data should be passed through stdin.
```sh
python3 main.py [-h] [--create-db] [--db-path DB_PATH]
```
| Option | Description                           |
| - |---------------------------------------|
| -h, --help | Show the help message and exit        |
| --create-db | Create db for saving pressure packets |
| --db-path DB_PATH | Specify the path of the sqlite db where packets are gonna be saved, sqlite.db by default |


