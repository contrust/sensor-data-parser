import argparse

from sensor_data_parser.config.constants import SQLITE_DB_PATH


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse a hex string from stdin to pressure packets and save them in a db,\n"
        "where the string is divided into chunks of size 8,\n"
        "and a chunk has the following format:\n"
        "the first 2 chars are always '80',\n"
        "the next 2 chars is the number of a packet in hexadecimal representation [00-7f] "
        "which should be unique,\n"
        "the next 4 chars is the pressure value of a packet in the hexadecimal representation.\n\n"
        "If a chunk doesn't match the format, it's not saved to the db.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--create-db",
        action="store_true",
        help="create db for saving pressure packets",
    )
    parser.add_argument(
        "--db-path",
        default=SQLITE_DB_PATH,
        help=f"specify the path of the sqlite db where packets are gonna be saved, "
        f"{SQLITE_DB_PATH} by default",
    )
    parser.add_argument(
        "--debug", action="store_true", help="set debug logging level"
    )
    return parser
