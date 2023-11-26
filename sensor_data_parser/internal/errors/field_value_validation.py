from typing import Any

from sensor_data_parser.internal.errors.validation import ValidationError


class FieldValueValidationError(ValidationError):
    def __init__(self, field_name: str, field_value: Any):
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self):
        return f"{self.field_name} can't be equal to {self.field_value}."
