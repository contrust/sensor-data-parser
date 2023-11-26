import logging
import sys

from sqlalchemy import create_engine

from sensor_data_parser.argparser.parser import get_parser
from sensor_data_parser.config.constants import LOGGING_FORMAT
from sensor_data_parser.internal.models.pressure_packet import PressurePacket
from sensor_data_parser.internal.parsing.parse_pressure_packets import (
    parse_pressure_packets,
)
from sensor_data_parser.internal.repositories.pressure_packet_repository import (
    PressurePacketRepository,
)


def main():
    parser = get_parser()
    args = parser.parse_args()
    logging.basicConfig(
        format=LOGGING_FORMAT,
        level=logging.DEBUG if args.debug else logging.INFO,
    )
    engine = create_engine(f"sqlite:///{args.db_path}", echo=True)
    if args.create_db:
        PressurePacket.metadata.create_all(bind=engine)
    else:
        data = sys.stdin.read()
        packets = parse_pressure_packets(data)
        pressure_packet_repository = PressurePacketRepository(engine)
        pressure_packet_repository.save_all(packets)


if __name__ == "__main__":
    main()
