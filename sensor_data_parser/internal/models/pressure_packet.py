import logging

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, validates

from sensor_data_parser.config.constants import (
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX,
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN,
    PRESSURE_PACKET_PRESSURE_VALUE_MAX,
    PRESSURE_PACKET_PRESSURE_VALUE_MIN,
    PRESSURE_PACKET_STATUS,
)
from sensor_data_parser.internal.errors.field_value_validation_error import (
    FieldValueValidationError,
)


class Base(DeclarativeBase):
    pass


class PressurePacket(Base):
    __tablename__ = "pressure_packet"

    current_value_counter = Column(Integer(), primary_key=True)
    status = Column(String(2))
    pressure_value = Column(Float())

    @validates("current_value_counter")
    def validate_current_value_counter(self, key, value):
        if not (
            PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN
            <= value
            <= PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX
        ):
            raise FieldValueValidationError(key, value)
        return value

    @validates("pressure_value")
    def validate_pressure_value(self, key, value):
        if not (
            PRESSURE_PACKET_PRESSURE_VALUE_MIN
            <= value
            <= PRESSURE_PACKET_PRESSURE_VALUE_MAX
        ):
            raise FieldValueValidationError(key, value)
        return value

    @validates("status")
    def validate_status(self, key, value):
        if value != PRESSURE_PACKET_STATUS:
            raise FieldValueValidationError(key, value)
        return value
