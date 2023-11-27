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
    "hex_string,expected",
    (("80000000", ("80", 0, 0)), ("807fffff", ("80", 127, 65535))),
)
def test_hex_string_to_pressure_packet_is_parsed_correctly(
    hex_string: str,
    expected: tuple
):
    parsed_packet = HexStringParser(hex_string).to_pressure_packet()
    assert ((parsed_packet.status,
            parsed_packet.current_value_counter,
            parsed_packet.pressure_value) == expected)


@pytest.mark.parametrize(
    "data,expected", (("80ff0000", []),
                      ("79000000", []),
                      ("80000000", [("80", 0, 0)]),
                      ("8000000079000000800100010",
                       [('80', 0, 0), ('80', 1, 1)]),
                      ("807b8038000080390000803a00008"
                       "03b0000803c0000803d0000803e00"
                       "00803f00", [("80", 123, 32824)])))
def test_hex_string_to_pressure_packets_is_parsed_correctly(
        data: str, expected: list[tuple]):
    packets = HexStringParser(data).to_pressure_packets()
    assert len(packets) == len(expected)
    for packet, expected_packet in zip(packets, expected):
        assert (packet.status, packet.current_value_counter,
                packet.pressure_value) == expected_packet
