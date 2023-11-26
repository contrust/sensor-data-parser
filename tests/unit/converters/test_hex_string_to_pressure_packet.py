import pytest

from sensor_data_parser.internal.converters.hex_string_converter import (
    HexStringConverter,
)
from sensor_data_parser.internal.errors.parsing_error import ParsingError


@pytest.mark.parametrize("hex_string", ("8000000", "800000000"))
def test_hex_string_to_pressure_packet_raises_parsing_error_when_len_not_8(
    hex_string: str,
):
    with pytest.raises(ParsingError):
        HexStringConverter(hex_string).to_pressure_packet()


@pytest.mark.parametrize(
    "hex_string,expected_status,expected_current_value_counter,expected_pressure_value",
    (("80000000", "80", 0, 0), ("807fffff", "80", 127, 65535)),
)
def test_hex_string_to_pressure_packet_is_parsed_correctly(
    hex_string,
    expected_status,
    expected_current_value_counter,
    expected_pressure_value,
):
    parsed_packet = HexStringConverter(hex_string).to_pressure_packet()
    assert parsed_packet.status == expected_status
    assert (
        parsed_packet.current_value_counter == expected_current_value_counter
    )
    assert parsed_packet.pressure_value == expected_pressure_value
