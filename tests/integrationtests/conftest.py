import pytest
from sqlmodel import Session

from borm.db.postgresql_db.create_db import engine


@pytest.fixture(scope="module")
def initialize_session():  # type: ignore[no-untyped-def]
    session = Session(engine)
    # Teardown: close session
    yield session
    session.close()
