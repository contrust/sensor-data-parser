import pytest

from sensor_data_parser.internal.errors import ParsingError
from sensor_data_parser.internal.parsers import HexStringParser


@pytest.mark.parametrize("hex_string", ["ll", "ao", "x"])
def test_not_hex_string_raises_parsing_exception(hex_string):
    with pytest.raises(ParsingError):
        HexStringParser(hex_string).to_int()


@pytest.mark.parametrize(
    "hex_string,excepted", [("ff", 255), ("3a", 58), ("0", 0)]
)
def test_hex_string_is_parsed_correctly(hex_string: str, excepted: int):
    assert HexStringParser(hex_string).to_int() == excepted


@pytest.mark.parametrize("hex_string", ("8000000", "800000000"))
def test_hex_string_to_pressure_packet_raises_parsing_error_when_len_not_8(
    hex_string: str,
):
    with pytest.raises(ParsingError):
        HexStringParser(hex_string).to_pressure_packet()


@pytest.mark.parametrize(
    "hex_string,expected_status,"
    "expected_current_value_counter,expected_pressure_value",
    (("80000000", "80", 0, 0), ("807fffff", "80", 127, 65535)),
)
def test_hex_string_to_pressure_packet_is_parsed_correctly(
    hex_string,
    expected_status,
    expected_current_value_counter,
    expected_pressure_value,
):
    parsed_packet = HexStringParser(hex_string).to_pressure_packet()
    assert parsed_packet.status == expected_status
    assert (
        parsed_packet.current_value_counter == expected_current_value_counter
    )
    assert parsed_packet.pressure_value == expected_pressure_value


@pytest.mark.parametrize("data", ("80ff0000", "79000000"))
def test_parse_pressure_packets_does_not_return_invalid_models(data: str):
    assert HexStringParser(data).to_pressure_packets() == []


@pytest.mark.parametrize("data", ("80000000",))
def test_parse_pressure_packets_returns_valid_models(data: str):
    assert len(HexStringParser(data).to_pressure_packets()) == 1


@pytest.mark.parametrize("data", ("800000007900000080010000",))
def test_parse_pressure_packets_continues_parsing_after_failed_parsing(
    data: str,
):
    assert len(HexStringParser(data).to_pressure_packets()) == 2
