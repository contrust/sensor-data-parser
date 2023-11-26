import argparse

from sensor_data_parser.config.constants import SQLITE_DB_PATH


def get_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Parse a hex string from stdin to pressure packets and save them"
            " in a db,\nwhere the string is divided into chunks of size"
            " 8,\nand a chunk has the following format:\nthe first 2 chars are"
            " always '80',\nthe next 2 chars is the number of a packet in"
            " hexadecimal representation [00-7f] which should be unique,\nthe"
            " next 4 chars is the pressure value of a packet in the"
            " hexadecimal representation.\n\nIf a chunk doesn't match the"
            " format, it's not saved to the db."
        ),
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
        help=(
            "specify the path of the sqlite db where packets are gonna be"
            f" saved, {SQLITE_DB_PATH} by default"
        ),
    )
    parser.add_argument(
        "--debug", action="store_true", help="set debug logging level"
    )
    return parser
