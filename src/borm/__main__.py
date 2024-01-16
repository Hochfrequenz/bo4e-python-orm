from sqlalchemy import create_engine
from sqlmodel import SQLModel

import borm.db.base
from borm.db.postgresql_db.auxiliary import get_url
from borm.db.postgresql_db.create_db import create_db, engine


# main
def main() -> None:
    create_db(engine)


if __name__ == "__main__":
    main()
