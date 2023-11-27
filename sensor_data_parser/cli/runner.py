import logging
import sys
from typing import Sequence, TextIO

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from sensor_data_parser.cli.parser import get_argument_parser
from sensor_data_parser.config import LOGGING_FORMAT
from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.parsers import HexStringParser
from sensor_data_parser.internal.repositories import PressurePacketRepository


class CommandsRunner:
    def __init__(self, stream: TextIO = sys.stdin):
        self._parser = get_argument_parser()
        self._args = None
        self._engine = None
        self._stream = stream

    def parse_arguments(self, args: Sequence[str] = None):
        self._args = self._parser.parse_args(args)

    def run(self):
        self._set_logging_basic_config()
        self._set_engine()
        if self._args.create_tables:
            self._create_tables()
        else:
            self._parse_stream_and_save_to_db()

    def _set_engine(self):
        self._engine = create_engine(
            f"sqlite:///{self._args.db_path}", echo=True)

    def _set_logging_basic_config(self):
        logging.basicConfig(
            format=LOGGING_FORMAT,
            level=logging.DEBUG if self._args.debug else logging.INFO,
        )

    def _create_tables(self):
        PressurePacket.metadata.create_all(bind=self._engine)

    def _parse_stream_and_save_to_db(self):
        data = self._stream.read()
        pressure_packets_parser = HexStringParser(data)
        packets = pressure_packets_parser.to_pressure_packets()
        pressure_packet_repository = PressurePacketRepository(self._engine)
        try:
            pressure_packet_repository.save_all(packets)
        except SQLAlchemyError as e:
            logging.error(e)
