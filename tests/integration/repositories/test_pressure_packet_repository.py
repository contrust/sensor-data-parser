import pytest

from sensor_data_parser.internal.parsing.parse_pressure_packets import (
    parse_pressure_packets,
)


@pytest.mark.parametrize("data", ("80110000", "8000000080010101"))
def test_save_all_saves_the_same_amount_of_packets(
    pressure_packet_repository, data
):
    packets = parse_pressure_packets(data)
    assert pressure_packet_repository.count() == 0
    pressure_packet_repository.save_all(packets)
    assert pressure_packet_repository.count() == len(packets)


def test_save_all_adds_the_same_models(
    pressure_packet_repository, pressure_packet
):
    assert (
        pressure_packet_repository.get(pressure_packet.current_value_counter)
        is None
    )
    pressure_packet_repository.save_all([pressure_packet])
    assert (
        pressure_packet_repository.get(pressure_packet.current_value_counter)
        == pressure_packet
    )
