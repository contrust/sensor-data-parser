import pytest
from faker import Faker

from src.constants import (
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX,
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN,
    PRESSURE_PACKET_PRESSURE_VALUE_MAX,
    PRESSURE_PACKET_PRESSURE_VALUE_MIN,
    PRESSURE_PACKET_STATUS,
)
from src.models.pressure_packet import PressurePacket


@pytest.fixture()
def status() -> str:
    return PRESSURE_PACKET_STATUS


@pytest.fixture()
def current_value_counter(faker: Faker) -> int:
    return faker.random_int(
        PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN,
        PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX,
    )


@pytest.fixture()
def pressure_value(faker: Faker) -> int:
    return faker.random_int(
        PRESSURE_PACKET_PRESSURE_VALUE_MIN, PRESSURE_PACKET_PRESSURE_VALUE_MAX
    )


@pytest.fixture()
def correct_pressure_packet(
    status, current_value_counter, pressure_value
) -> PressurePacket:
    return PressurePacket(
        status=status,
        current_value_counter=current_value_counter,
        pressure_value=pressure_value,
    )
