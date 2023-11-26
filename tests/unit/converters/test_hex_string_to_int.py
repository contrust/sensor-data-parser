import pytest

from sensor_data_parser.internal.converters.hex_string_converter import (
    HexStringConverter,
)
from sensor_data_parser.internal.errors.parsing_error import ParsingError


@pytest.mark.parametrize("hex_string", ["ll", "ao", "x"])
def test_not_hex_string_raises_parsing_exception(hex_string):
    with pytest.raises(ParsingError):
        HexStringConverter(hex_string).to_int()


@pytest.mark.parametrize(
    "hex_string,excepted", [("ff", 255), ("3a", 58), ("0", 0)]
)
def test_hex_string_is_parsed_correctly(hex_string: str, excepted: int):
    assert HexStringConverter(hex_string).to_int() == excepted
