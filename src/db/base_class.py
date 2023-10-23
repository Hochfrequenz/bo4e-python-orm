"""
Declaration of Base class
"""
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, registry

mapper_registry = registry()
metadata: MetaData = MetaData()


class Base(DeclarativeBase):
    # pylint: disable=too-few-public-methods
    """
    Base class which inherits from DeclarativeBase
    """
    metadata = metadata
