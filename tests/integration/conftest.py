import os

import pytest
from sqlalchemy import Engine, create_engine


@pytest.fixture(scope="session")
def test_db_path() -> str:
    return "test_sqlite.db"


@pytest.fixture(scope="session")
def engine(test_db_path: str) -> Engine:
    yield create_engine(f"sqlite:///{test_db_path}")
    os.remove(test_db_path)
