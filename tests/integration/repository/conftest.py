import pytest

from src.models.pressure_packet import PressurePacket
from src.repositories.pressure_packet_repository import (
    PressurePacketRepository,
)


@pytest.fixture()
def pressure_packet_repository(engine):
    repository = PressurePacketRepository(engine)
    PressurePacket.metadata.create_all(engine)
    yield repository
    PressurePacket.metadata.drop_all(engine)
