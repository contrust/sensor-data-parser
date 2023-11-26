import pytest

from sensor_data_parser.internal.errors import FieldValueValidationError
from sensor_data_parser.internal.models import PressurePacket


@pytest.mark.parametrize("wrong_status", ("81", "0", "800"))
def test_wrong_status_raise_validation_exception(
    pressure_packet: PressurePacket, wrong_status: str
):
    with pytest.raises(FieldValueValidationError):
        pressure_packet.status = wrong_status


@pytest.mark.parametrize("wrong_current_value_counter", (128, -1, 2341))
def test_not_in_range_current_value_counter_raise_validation_exception(
    pressure_packet: PressurePacket, wrong_current_value_counter: int
):
    with pytest.raises(FieldValueValidationError):
        pressure_packet.current_value_counter = wrong_current_value_counter


@pytest.mark.parametrize("wrong_pressure_value", (4123423, -1, 65536))
def test_not_in_range_pressure_value_raise_validation_exception(
    pressure_packet: PressurePacket, wrong_pressure_value: int
):
    with pytest.raises(FieldValueValidationError):
        pressure_packet.pressure_value = wrong_pressure_value
