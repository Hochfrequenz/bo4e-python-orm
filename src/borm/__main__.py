from sqlalchemy import create_engine
from sqlmodel import SQLModel

import borm.db.base
from borm.db.postgresql_db.auxiliary import get_url
from borm.testing import add_row, read_cond, read_link, read_row


# create database
def create_db(engine) -> None:
    SQLModel.metadata.create_all(engine)


# main
def main() -> None:
    engine = create_engine(get_url(), echo=True)
    create_db(engine)
    add_row(engine)
    read_row(engine)
    read_cond(engine)
    read_link(engine)


if __name__ == "__main__":
    main()
