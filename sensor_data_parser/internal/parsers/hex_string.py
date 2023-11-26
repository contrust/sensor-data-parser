import logging

from sensor_data_parser.internal.errors import ParsingError, ValidationError
from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.utils import chunks


class HexStringParser:
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
            current_value_counter=HexStringParser(
                self.hex_string[2:4]
            ).to_int(),
            pressure_value=HexStringParser(self.hex_string[4:8]).to_int(),
        )

    def to_pressure_packets(self) -> list[PressurePacket]:
        packets = []
        for chunk in chunks(self.hex_string, 8):
            logging.debug("Trying to parse a new chunk.")
            try:
                packet = HexStringParser(chunk).to_pressure_packet()
                packets.append(packet)
            except (ParsingError, ValidationError) as e:
                logging.error(e)
        return packets
