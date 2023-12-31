import pytest

from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.parsers import HexStringParser
from sensor_data_parser.internal.repositories import PressurePacketRepository


@pytest.mark.parametrize("data", ("80110000", "8000000080010101"))
def test_save_all_saves_the_same_amount_of_packets(
    pressure_packet_repository: PressurePacketRepository, data: str
):
    packets = HexStringParser(data).to_pressure_packets()
    count_before = pressure_packet_repository.count()
    pressure_packet_repository.save_all(packets)
    count_after = pressure_packet_repository.count()
    assert count_after - count_before == len(packets)


def test_save_all_adds_the_same_models(
        pressure_packet_repository: PressurePacketRepository,
        pressure_packet: PressurePacket):
    db_pressure_packet = pressure_packet_repository.get(1)
    assert db_pressure_packet is None
    pressure_packet_repository.save_all([pressure_packet])
    db_pressure_packet = pressure_packet_repository.get(1)
    assert (db_pressure_packet.current_value_counter ==
            pressure_packet.current_value_counter)
    assert db_pressure_packet.pressure_value == pressure_packet.pressure_value
    assert db_pressure_packet.status == pressure_packet.status
