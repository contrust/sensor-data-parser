from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, validates

from sensor_data_parser.config import (
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX,
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN,
    PRESSURE_PACKET_PRESSURE_VALUE_MAX,
    PRESSURE_PACKET_PRESSURE_VALUE_MIN,
    PRESSURE_PACKET_STATUS,
)
from sensor_data_parser.internal.errors import FieldValueValidationError


class Base(DeclarativeBase):
    pass


class PressurePacket(Base):
    __tablename__ = "pressure_packet"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    current_value_counter = Column(Integer())
    status = Column(String(2))
    pressure_value = Column(Float())

    @validates("current_value_counter")
    def validate_current_value_counter(self, key: str, value: int) -> int:
        if not (
            PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN
            <= value
            <= PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX
        ):
            raise FieldValueValidationError(key, value)
        return value

    @validates("pressure_value")
    def validate_pressure_value(self, key: str, value: float) -> float:
        if not (
            PRESSURE_PACKET_PRESSURE_VALUE_MIN
            <= value
            <= PRESSURE_PACKET_PRESSURE_VALUE_MAX
        ):
            raise FieldValueValidationError(key, value)
        return value

    @validates("status")
    def validate_status(self, key: str, value: str) -> str:
        if value != PRESSURE_PACKET_STATUS:
            raise FieldValueValidationError(key, value)
        return value
