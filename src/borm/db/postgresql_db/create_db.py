"""
This module provides functionality related to the PostgreSQL database in the context of the borm application.
"""

from sqlmodel import SQLModel, create_engine

import borm.db.base  # noqa # pylint: disable=unused-import
from borm.db.postgresql_db.auxiliary import get_url

engine = create_engine(get_url(), echo=True)


def create_db() -> None:
    """
    Create database tables based on the SQLModel metadata.

    This function connects to the PostgreSQL database using the specified engine,
    then creates tables for all SQLModel classes defined in the application.


    Make sure to call this function after defining all SQLModel classes and before running any queries.
    """
    SQLModel.metadata.create_all(engine)
