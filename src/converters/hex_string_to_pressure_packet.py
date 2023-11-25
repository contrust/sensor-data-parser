from src.converters.hex_string_to_int import hex_string_to_int
from src.exceptions.parsing_exception import ParsingException
from src.models.pressure_packet import PressurePacket


def hex_string_to_pressure_packet(hex_string: str) -> PressurePacket | None:
    if len(hex_string) != 8:
        raise ParsingException("The length of the string is not equal to 8.")
    return PressurePacket(
        status=hex_string[0:2],
        current_value_counter=hex_string_to_int(hex_string[2:4]),
        pressure_value=hex_string_to_int(hex_string[4:8]),
    )
