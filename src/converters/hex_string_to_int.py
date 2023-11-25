from src.exceptions.parsing_exception import ParsingException


def hex_string_to_int(hex_string: str) -> int:
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ParsingException(f"Can't convert {hex_string} to int.")
