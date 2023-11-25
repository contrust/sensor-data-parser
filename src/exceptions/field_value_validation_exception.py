from src.exceptions.validation_exception import ValidationException


class FieldValueValidationException(ValidationException):
    def __init__(self, field_name: str, field_value):
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self):
        return f"{self.field_name} can't be equal to {self.field_value}."
