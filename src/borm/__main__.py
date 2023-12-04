from sqlalchemy import create_engine
from sqlmodel import SQLModel

import borm.db.base
from borm.db.postgresql_db.auxiliary import get_url
from borm.models.bo.angebot import Angebot
from borm.models.bo.geschaeftspartner import Geschaeftspartner

engine = create_engine(get_url(), echo=True)

SQLModel.metadata.create_all(engine)
