from typing import Generator

import pytest
from sqlmodel import Session, SQLModel

from borm.db.postgresql_db.create_db import engine


@pytest.fixture(scope="function")
def initialize_session() -> Generator[Session, None, None]:
    session = Session(engine)
    # Teardown: close session
    yield session
    meta = SQLModel.metadata
    for table in meta.sorted_tables:
        print(f"Clear table {table}")
        session.execute(table.delete())
    session.commit()
    session.close()
