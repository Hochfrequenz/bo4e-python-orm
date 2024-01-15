from sqlmodel import SQLModel, create_engine

import borm.db.base
from borm.db.postgresql_db.auxiliary import get_url

engine = create_engine(get_url(), echo=True)


# create database and tables
def create_db(engine) -> None:
    SQLModel.metadata.create_all(engine)
