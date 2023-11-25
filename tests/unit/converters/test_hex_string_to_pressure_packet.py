import pytest

from src.converters.hex_string_to_pressure_packet import (
    hex_string_to_pressure_packet,
)
from src.converters.pressure_packet_to_hex_string import (
    pressure_packet_to_hex_string,
)
from src.expections.parsing_exception import ParsingException


@pytest.mark.parametrize("hex_string", ("8000000", "800000000"))
def test_hex_string_to_pressure_packet_raise_parsing_exception_when_len_not_8(
    hex_string: str,
):
    with pytest.raises(ParsingException):
        hex_string_to_pressure_packet(hex_string)


def test_hex_string_to_pressure_packet_returns_the_same_values(
    pressure_packet,
):
    hex_string = pressure_packet_to_hex_string(pressure_packet)
    parsed_packet = hex_string_to_pressure_packet(hex_string)
    assert parsed_packet.status == pressure_packet.status
    assert (
        parsed_packet.current_value_counter
        == pressure_packet.current_value_counter
    )
    assert parsed_packet.pressure_value == pressure_packet.pressure_value
