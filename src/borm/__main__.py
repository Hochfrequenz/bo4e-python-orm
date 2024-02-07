"""
__main__ module.
This module serves as the entry point for the application when executed as a script.
"""
from borm.db.postgresql_db.create_db import create_db


def main() -> None:
    """
    collects everything to be executed when running borm.
    creates database and tables for existing SQLModel classes
    """
    create_db()


if __name__ == "__main__":
    main()
