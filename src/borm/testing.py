from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlmodel import Session, select

from borm.db.postgresql_db.auxiliary import get_url
from borm.models.bo.angebot import Angebot
from borm.models.bo.geschaeftspartner import Geschaeftspartner

"""
Simple playground for basic operation in SQLModel.
"""


# example of adding something
def add_row(engine: Engine) -> None:
    with Session(engine) as session:
        geschaeftspartner = Geschaeftspartner(name1="Test")
        angebot = Angebot(angebotsnummer="125", angebotsgeber=geschaeftspartner)
        session.add(angebot)
        session.commit()


# example of reading something simple
def read_row(engine: Engine) -> None:
    with Session(engine) as session:
        statement = select(Angebot)
        results = session.exec(statement)
        for angebot in results:
            print(angebot)


# example of reading something with condition
def read_cond(engine: Engine) -> None:
    with Session(engine) as session:
        statement = select(Angebot).where(Angebot.angebotsnummer == "125")
        results = session.exec(statement)
        for angebot in results:
            print(angebot)


# example of reading something with link
def read_link(engine: Engine) -> None:
    with Session(engine) as session:
        statement = select(Angebot, Geschaeftspartner).where(
            Angebot.angebotsgeber_id == Geschaeftspartner.geschaeftspartner_sqlid
        )
        results = session.exec(statement).unique()
        for angebot, partner in results:
            print(angebot, partner)
