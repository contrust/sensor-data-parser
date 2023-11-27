import pytest

from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.parsers import HexStringParser
from sensor_data_parser.internal.repositories import PressurePacketRepository


@pytest.mark.parametrize("data", ("80110000", "8000000080010101"))
def test_save_all_saves_the_same_amount_of_packets(
    pressure_packet_repository: PressurePacketRepository, data: str
):
    packets = HexStringParser(data).to_pressure_packets()
    assert pressure_packet_repository.count() == 0
    pressure_packet_repository.save_all(packets)
    assert pressure_packet_repository.count() == len(packets)


def test_save_all_adds_the_same_models(
        pressure_packet_repository: PressurePacketRepository,
        pressure_packet: PressurePacket):
    db_pressure_packet = pressure_packet_repository.get(1)
    assert db_pressure_packet is None
    pressure_packet_repository.save_all([pressure_packet])
    db_pressure_packet = pressure_packet_repository.get(1)
    assert db_pressure_packet == pressure_packet
