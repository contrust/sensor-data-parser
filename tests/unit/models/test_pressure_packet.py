import pytest

from src.exceptions.field_value_validation_exception import (
    FieldValueValidationException,
)


@pytest.mark.parametrize("wrong_status", ("81", "0", "800"))
def test_wrong_status_raise_validation_exception(
    pressure_packet, wrong_status
):
    with pytest.raises(FieldValueValidationException):
        pressure_packet.status = wrong_status


@pytest.mark.parametrize("wrong_current_value_counter", (128, -1, 2341))
def test_not_in_range_current_value_counter_raise_validation_exception(
    pressure_packet, wrong_current_value_counter
):
    with pytest.raises(FieldValueValidationException):
        pressure_packet.current_value_counter = wrong_current_value_counter


@pytest.mark.parametrize("wrong_pressure_value", (4123423, -1, 65536))
def test_not_in_range_pressure_value_raise_validation_exception(
    pressure_packet, wrong_pressure_value
):
    with pytest.raises(FieldValueValidationException):
        pressure_packet.pressure_value = wrong_pressure_value
