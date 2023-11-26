from typing import Iterable

from sqlalchemy import Engine

from sensor_data_parser.internal.models import PressurePacket
from sensor_data_parser.internal.repositories.session import SessionRepository


class PressurePacketRepository(SessionRepository):
    def __init__(self, engine: Engine):
        super().__init__(engine)

    def get(self, current_value_counter: int) -> PressurePacket:
        return self.session.get(PressurePacket, current_value_counter)

    def count(self):
        return self.session.query(PressurePacket).count()

    def save_all(self, packets: Iterable[PressurePacket]) -> None:
        self.session.add_all(packets)
        self.session.commit()
