from sqlalchemy import Engine
from sqlalchemy.orm import Session


class SessionRepository:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = Session(bind=engine)
