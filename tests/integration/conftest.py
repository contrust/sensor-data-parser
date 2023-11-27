import os

import pytest
from sqlalchemy import Engine, create_engine

from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.repositories import PressurePacketRepository


@pytest.fixture(scope="session")
def test_db_path() -> str:
    return "test_sqlite.db"


@pytest.fixture(scope="session")
def engine(test_db_path: str) -> Engine:
    yield create_engine(f"sqlite:///{test_db_path}")
    os.remove(test_db_path)


@pytest.fixture()
def pressure_packet_repository(engine: Engine):
    repository = PressurePacketRepository(engine)
    PressurePacket.metadata.create_all(engine)
    yield repository
    PressurePacket.metadata.drop_all(engine)
