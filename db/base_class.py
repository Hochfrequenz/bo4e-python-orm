from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, registry

mapper_registry = registry()
metadata: MetaData = MetaData()


class Base(DeclarativeBase):
    metadata = metadata
    pass
