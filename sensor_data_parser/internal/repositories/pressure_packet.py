from typing import Iterable

from sqlalchemy import Engine

from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.repositories.session import SessionRepository


class PressurePacketRepository(SessionRepository):
    def __init__(self, engine: Engine):
        super().__init__(engine)

    def get(self, packet_id: int) -> PressurePacket:
        return self.session.get(PressurePacket, packet_id)

    def count(self) -> int:
        return self.session.query(PressurePacket).count()

    def save_all(self, packets: Iterable[PressurePacket]) -> None:
        self.session.bulk_save_objects(packets)
        self.session.commit()
