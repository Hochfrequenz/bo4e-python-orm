import pytest
from sqlalchemy import Inspector, inspect
from sqlmodel import select

from borm.models.bo.angebot import Angebot  # type: ignore
from borm.models.bo.geschaeftspartner import Geschaeftspartner  # type: ignore


class TestAngebot:
    @pytest.mark.usefixtures("initialize_session")
    def test_existence_of_tables(self, initialize_session) -> None:
        """
        test for the existence of tables
        """
        insp: Inspector = inspect(initialize_session.bind)
        name_of_tables = insp.get_table_names()
        assert "angebot" in name_of_tables

    def test_add_and_read_row(self, initialize_session) -> None:
        """
        test to add a row to an existing table and read it
        """
        session = initialize_session
        testangebot = Angebot(angebotsnummer="125")
        session.add(testangebot)
        session.commit()

        # read and check row
        statement = select(Angebot)
        retrieved_angebot = session.exec(statement)
        for angebot in retrieved_angebot:
            assert angebot.angebotsnummer == "125"
        session.delete(testangebot)
        session.commit()

    def test_read_cond_row(self, initialize_session) -> None:
        """
        test to add a row to an existing table and read it with conditions
        """
        session = initialize_session
        testangebot1 = Angebot(angebotsnummer="125", anfragereferenz="anfrage1")
        testangebot2 = Angebot(angebotsnummer="215", anfragereferenz="anfrage2")
        session.add(testangebot1)
        session.add(testangebot2)
        session.commit()

        # read and check row
        statement = select(Angebot).where(Angebot.angebotsnummer == "215")
        retrieved_angebot = session.exec(statement)
        for angebot in retrieved_angebot:
            assert angebot.anfragereferenz == "anfrage2"
        session.delete(testangebot1)
        session.delete(testangebot2)
        session.commit()

    def test_read_write_linked_entries(self, initialize_session) -> None:
        """
        test to write and read connected rows of two different tables
        """
        session = initialize_session
        testgeschaeftspartner1 = Geschaeftspartner(glaeubiger_id="123", amtsgericht="Leipzig")
        testgeschaeftspartner2 = Geschaeftspartner(glaeubiger_id="321", amtsgericht="Berlin")
        testangebot1 = Angebot(angebotsnummer="125", anfragereferenz="anfrage1", angebotsgeber=testgeschaeftspartner1)
        testangebot2 = Angebot(angebotsnummer="215", anfragereferenz="anfrage2", angebotsgeber=testgeschaeftspartner2)
        session.add(testgeschaeftspartner1)
        session.add(testgeschaeftspartner2)
        session.add(testangebot1)
        session.add(testangebot2)
        session.commit()
        statement = select(Angebot, Geschaeftspartner).where(
            Angebot.angebotsgeber_id == Geschaeftspartner.geschaeftspartner_sqlid
        )
        results = session.exec(statement).unique()
        for angebot, partner in results:
            assert (angebot.angebotsnummer == "125" and partner.glaeubiger_id == "123") or (
                angebot.angebotsnummer == "215" and partner.glaeubiger_id == "321"
            )

        session.delete(testgeschaeftspartner1)
        session.delete(testgeschaeftspartner2)
        session.delete(testangebot1)
        session.delete(testangebot2)
        session.commit()

    def test_read_write_1_2_relationship(self, initialize_session) -> None:
        """
        test to write and read rows of a 1-2 relationship
        """
        session = initialize_session
        testgeschaeftspartner1 = Geschaeftspartner(glaeubiger_id="123", amtsgericht="Leipzig")
        testgeschaeftspartner2 = Geschaeftspartner(glaeubiger_id="321", amtsgericht="Berlin")
        testangebot1 = Angebot(
            angebotsnummer="125",
            anfragereferenz="anfrage1",
            angebotsgeber=testgeschaeftspartner1,
            angebotsnehmer=testgeschaeftspartner2,
        )
        session.add(testgeschaeftspartner1)
        session.add(testgeschaeftspartner2)
        session.add(testangebot1)
        session.commit()
        statement = select(Angebot, Geschaeftspartner).where(
            Angebot.angebotsgeber_id == Geschaeftspartner.geschaeftspartner_sqlid
        )
        results = session.exec(statement).unique()
        for angebot, partner in results:
            assert angebot.angebotsnummer == "125" and partner.glaeubiger_id == "123"

        statement = select(Angebot, Geschaeftspartner).where(
            Angebot.angebotsnehmer_id == Geschaeftspartner.geschaeftspartner_sqlid
        )
        results = session.exec(statement).unique()

        for angebot, partner in results:
            assert angebot.angebotsnummer == "125" and partner.glaeubiger_id == "321"

        session.delete(testgeschaeftspartner1)
        session.delete(testgeschaeftspartner2)
        session.delete(testangebot1)
        session.commit()
