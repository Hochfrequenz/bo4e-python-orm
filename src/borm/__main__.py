from sqlalchemy import create_engine
from sqlmodel import SQLModel

import borm.db.base
from borm.db.postgresql_db.auxiliary import get_url
from borm.db.postgresql_db.create_db import create_db, engine
from borm.testing import add_row, read_cond, read_link, read_row


# main
def main() -> None:
    create_db(engine)


def playing() -> None:
    add_row(engine)
    read_row(engine)
    read_cond(engine)
    read_link(engine)


if __name__ == "__main__":
    main()
