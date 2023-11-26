import logging

from sensor_data_parser.internal.converters.hex_string_converter import (
    HexStringConverter,
)
from sensor_data_parser.internal.errors.parsing_error import ParsingError
from sensor_data_parser.internal.errors.validation_error import ValidationError
from sensor_data_parser.internal.models.pressure_packet import PressurePacket
from sensor_data_parser.internal.utils.sequence.chunks import chunks


def parse_pressure_packets(data: str) -> list[PressurePacket]:
    packets = []
    for chunk in chunks(data, 8):
        logging.debug("Trying to parse a new chunk.")
        try:
            packet = HexStringConverter(chunk).to_pressure_packet()
            packets.append(packet)
        except (ParsingError, ValidationError) as e:
            logging.error(e)
    return packets
