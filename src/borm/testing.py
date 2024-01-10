from sqlalchemy import create_engine
from sqlmodel import Session

from borm.db.postgresql_db.auxiliary import get_url
from borm.models.bo.angebot import Angebot
from borm.models.bo.geschaeftspartner import Geschaeftspartner

engine = create_engine(get_url(), echo=True)


with Session(engine) as session:
    # geschaeftspartner = Geschaeftspartner(name1="Test")
    angebot = Angebot(angebotsnummer="125")  # , angebotsgeber=geschaeftspartner)
    session.add(angebot)
    session.commit()
