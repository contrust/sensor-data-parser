import pytest

from src.converters.hex_string_to_int import hex_string_to_int
from src.expections.parsing_exception import ParsingException


@pytest.mark.parametrize("hex_string", ["ll", "ao", "x"])
def test_not_hex_string_raises_parsing_exception(hex_string):
    with pytest.raises(ParsingException):
        hex_string_to_int("ll")


@pytest.mark.parametrize(
    "hex_string,excepted", [("ff", 255), ("3a", 58), ("0", 0)]
)
def test_hex_string_is_parsed_correctly(hex_string: str, excepted: int):
    assert hex_string_to_int(hex_string) == excepted
