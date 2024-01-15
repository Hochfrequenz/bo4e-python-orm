import pytest  # type: ignore
from sqlmodel import Session

from borm.db.postgresql_db.auxiliary import get_url  # type: ignore[import-untyped]
from borm.db.postgresql_db.create_db import engine  # type: ignore


@pytest.fixture(scope="module")
def initialize_session():
    session = Session(engine)
    # Teardown: close session
    yield session
    session.close()
