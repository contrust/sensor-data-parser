# Sensor data parser
A parser of data from a sensor.
# Data format
Data is a hex string that is divided into chunks of size 8, and a chunk has the following format:

| Indexes | Description                                                                  |
|---------|------------------------------------------------------------------------------|
| 0-1     | Packet identifier in hex representation which should always be equal to '80' |
| 2-3     | Current value counter in hex representation [00-7f]                          |
| 4-7     | Pressure value in hex representation                                         |

# Dependencies
If you have pip installed, you can install poetry and create a virtual environment
```sh
make init
```
And then activate it
```sh
make shell
```
Or build a docker image from the Dockerfile file. 

# Usage
Data should be passed through stdin.
```sh
poetry run parser [-h] [--create-db] [--db-path DB_PATH]
```
| Option            | Description                                                                              |
|-------------------|------------------------------------------------------------------------------------------|
| -h, --help        | Show the help message and exit                                                           |
| --create-tables   | Create tables for saving pressure packets                                                |
| --db-path DB_PATH | Specify the path of the sqlite db where packets are gonna be saved, sqlite.db by default |
# Make commands
| Command         | Description                                     |
|-----------------|-------------------------------------------------|
| make init       | Install poetry and create a virtual environment |
| make shell      | Activate the virtual environment                |
| make test       | Run tests                                       |
| make coverage   | Run tests with coverage                         |
| make lint       | Format .py files in the project                 |
| make check_lint | Check if .py files are formatted                |
| make lock       | Create poetry.lock file from pyproject.toml     |