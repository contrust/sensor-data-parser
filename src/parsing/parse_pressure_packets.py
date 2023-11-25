import logging

from src.converters.hex_string_to_pressure_packet import (
    hex_string_to_pressure_packet,
)
from src.expections.parsing_exception import ParsingException
from src.expections.validation_exception import ValidationException
from src.models.pressure_packet import PressurePacket
from src.utils.list.chunks import chunks


def parse_pressure_packets(data: str) -> list[PressurePacket]:
    packets = []
    for chunk in chunks(data, 8):
        logging.debug("Trying to parse a new chunk.")
        try:
            packet = hex_string_to_pressure_packet(chunk)
            packets.append(packet)
        except (ParsingException, ValidationException) as e:
            logging.error(e)
    return packets
