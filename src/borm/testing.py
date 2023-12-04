from sqlalchemy import create_engine
from sqlmodel import Session

from borm.db.postgresql_db.auxiliary import get_url
from borm.models.bo.angebot import Angebot

engine = create_engine(get_url(), echo=True)


with Session(engine) as session:
    angebot = Angebot(angebotsnummer="125")
    session.add(angebot)
    session.commit()
