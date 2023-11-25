import logging
import sys

from sqlalchemy import create_engine

from src.argparser.parser import get_parser
from src.constants import LOGGING_FORMAT
from src.models.pressure_packet import PressurePacket
from src.parsing.parse_pressure_packets import parse_pressure_packets
from src.repositories.pressure_packet_repository import PressurePacketRepository


def main():
    logging.basicConfig(format=LOGGING_FORMAT)
    parser = get_parser()
    args = parser.parse_args()
    engine = create_engine(f"sqlite:///{args.db_path}", echo=True)
    if args.create_db:
        PressurePacket.metadata.create_all(bind=engine)
    else:
        data = sys.stdin.read()
        pressure_packet_repository = PressurePacketRepository(engine)
        packets = parse_pressure_packets(data)
        pressure_packet_repository.save_all(packets)


if __name__ == '__main__':
    main()
