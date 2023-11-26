from sensor_data_parser.internal.errors.parsing_error import ParsingError
from sensor_data_parser.internal.models.pressure_packet import PressurePacket


class HexStringConverter:
    def __init__(self, hex_string: str):
        self.hex_string = hex_string

    def to_int(self) -> int:
        try:
            return int(self.hex_string, 16)
        except ValueError:
            raise ParsingError(f"Can't convert {self.hex_string} to int.")

    def to_pressure_packet(self) -> PressurePacket:
        if len(self.hex_string) != 8:
            raise ParsingError("The length of the string is not equal to 8.")
        return PressurePacket(
            status=self.hex_string[0:2],
            current_value_counter=HexStringConverter(
                self.hex_string[2:4]
            ).to_int(),
            pressure_value=HexStringConverter(self.hex_string[4:8]).to_int(),
        )
