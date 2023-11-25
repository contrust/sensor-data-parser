from typing import Iterable

from sqlalchemy import Engine

from src.models.pressure_packet import PressurePacket
from src.repositories.session_repository import SessionRepository


class PressurePacketRepository(SessionRepository):
    def __init__(self, engine: Engine):
        super().__init__(engine)

    def get(self, current_value_counter: int) -> PressurePacket:
        return self.session.get(PressurePacket, current_value_counter)

    def save_all(self, packets: Iterable[PressurePacket]) -> None:
        self.session.add_all(packets)
        self.session.commit()
