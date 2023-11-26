import pytest

from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.repositories import PressurePacketRepository


@pytest.fixture()
def pressure_packet_repository(engine):
    repository = PressurePacketRepository(engine)
    PressurePacket.metadata.create_all(engine)
    yield repository
    PressurePacket.metadata.drop_all(engine)
