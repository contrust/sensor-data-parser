import logging
import sys

from sqlalchemy import create_engine

from sensor_data_parser.argparser import get_argument_parser
from sensor_data_parser.config import LOGGING_FORMAT
from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.parsers import HexStringParser
from sensor_data_parser.internal.repositories import PressurePacketRepository


def main() -> None:
    parser = get_argument_parser()
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
        pressure_packets_parser = HexStringParser(data)
        packets = pressure_packets_parser.to_pressure_packets()
        pressure_packet_repository = PressurePacketRepository(engine)
        pressure_packet_repository.save_all(packets)


if __name__ == "__main__":
    main()
