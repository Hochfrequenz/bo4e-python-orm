from sqlalchemy import create_engine
from sqlmodel import SQLModel

import borm.db.base
from borm.db.postgresql_db.auxiliary import get_url
from borm.db.postgresql_db.create_db import create_db, engine
from borm.testing import read_link


# main
def main() -> None:
    create_db(engine)


def playing() -> None:
    read_link(engine)


if __name__ == "__main__":
    main()
