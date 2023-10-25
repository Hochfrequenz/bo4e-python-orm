import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from borm.db.postgresql_db.auxiliary import get_url  # type: ignore[import-untyped]


@pytest.fixture(scope="module")
def initialize_db():
    engine = create_engine(get_url())
    session = sessionmaker(bind=engine)
    session = session()
    # Teardown: close session, stop and remove container
    yield session
    session.close()
