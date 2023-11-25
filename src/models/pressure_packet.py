import logging

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import validates

from src.constants import (
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX,
    PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN,
    PRESSURE_PACKET_PRESSURE_VALUE_MAX,
    PRESSURE_PACKET_PRESSURE_VALUE_MIN,
    PRESSURE_PACKET_STATUS,
)
from src.expections.field_value_validation_exception import (
    FieldValueValidationException,
)
from src.models.base import Base


class PressurePacket(Base):
    __tablename__ = "pressure_packet"

    current_value_counter = Column(Integer(), primary_key=True)
    status = Column(String(2))
    pressure_value = Column(Float())

    @validates("current_value_counter")
    def validate_current_value_counter(self, key, address):
        if not (
            PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MIN
            <= address
            < PRESSURE_PACKET_CURRENT_VALUE_COUNTER_MAX
        ):
            raise FieldValueValidationException(key, address)
        return address

    @validates("pressure_value")
    def validate_pressure_value(self, key, address):
        if not (
            PRESSURE_PACKET_PRESSURE_VALUE_MIN
            <= address
            < PRESSURE_PACKET_PRESSURE_VALUE_MAX
        ):
            raise FieldValueValidationException(key, address)
        return address

    @validates("status")
    def validate_status(self, key, address):
        if address != PRESSURE_PACKET_STATUS:
            raise FieldValueValidationException(key, address)
        return address
