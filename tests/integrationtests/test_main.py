from datetime import datetime
from decimal import Decimal

import pytest
from sqlalchemy import Inspector, inspect
from sqlmodel import select

from borm.models import Angebotsvariante, Tarifeinschraenkung, Unterschrift, Vertrag, Zaehler, ZusatzAttribut
from borm.models.bo.angebot import Angebot
from borm.models.bo.geschaeftspartner import Geschaeftspartner


class TestAngebot:
    @pytest.mark.usefixtures("initialize_session")
    def test_existence_of_tables(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
        """
        test for the existence of tables
        """
        insp: Inspector = inspect(initialize_session.bind)
        name_of_tables = insp.get_table_names()
        assert "angebot" in name_of_tables

    def test_add_and_read_row(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
        """
        test to add a row to an existing table and read it
        """
        session = initialize_session
        testangebot = Angebot(angebotsnummer="125")
        testzaehler = Zaehler(zaehlerkonstante=Decimal("12.25"))
        session.add(testangebot)
        session.add(testzaehler)
        session.commit()

        # read and check row
        statement = select(Angebot)
        retrieved_angebot = session.exec(statement)
        for angebot in retrieved_angebot:
            assert angebot.angebotsnummer == "125"
        statement2 = select(Zaehler)
        retrieved_zaehler = session.exec(statement2).unique()
        for zaehler in retrieved_zaehler:
            assert zaehler.zaehlerkonstante == Decimal("12.25")

    def test_read_cond_row(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
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

    def test_read_write_linked_entries(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
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

    def test_read_write_1_2_relationship(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
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

    def test_read_write_many_many_relationship(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
        """
        test to write and read rows of a 1-2 relationship
        """
        session = initialize_session
        testvariante = Angebotsvariante(version="test")
        testangebot1 = Angebot(angebotsnummer="125", varianten=[testvariante])

        unterschrift1 = Unterschrift(name="ersteUnterschrift")
        unterschrift2 = Unterschrift(name="zweiteUnterschrift")
        unterschrift3 = Unterschrift(name="dritteUnterschrift")
        vertrag1 = Vertrag(unterzeichnervp1=[unterschrift1, unterschrift2], unterzeichnervp2=[unterschrift3])

        session.add(unterschrift1)
        session.add(unterschrift2)
        session.add(unterschrift3)
        session.add(vertrag1)
        session.add(testvariante)
        session.add(testangebot1)
        session.commit()
        session.refresh(testvariante)
        session.refresh(testangebot1)
        session.refresh(vertrag1)
        session.refresh(unterschrift1)
        session.refresh(unterschrift2)
        session.refresh(unterschrift3)

        statement = select(Vertrag)
        results = session.exec(statement)
        for vertrag in results:
            assert vertrag.unterzeichnervp1[0].name == "ersteUnterschrift"
            assert vertrag.unterzeichnervp1[1].name == "zweiteUnterschrift"
            assert vertrag.unterzeichnervp2[0].name == "dritteUnterschrift"

        statement2 = select(Angebot)
        results = session.exec(statement2)
        for angebot in results:
            assert angebot.varianten[0].version == "test"

    def test_add_and_read_row_lists(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
        """
        test to add a row to an existing table and read it
        """
        session = initialize_session
        testtarifeinschraenkung = Tarifeinschraenkung(zusatzprodukte=["produkt1", "produkt2", "produkt3"])
        session.add(testtarifeinschraenkung)
        session.commit()

        # read and check row
        statement = select(Tarifeinschraenkung)
        retrieved_tarifeinschraenkung = session.exec(statement).unique()
        for tarifeinschraenkung in retrieved_tarifeinschraenkung:
            assert tarifeinschraenkung.zusatzprodukte[0] == "produkt1"

    def test_zusatz_attribut(self, initialize_session) -> None:  # type: ignore[no-untyped-def]
        """
        test to add a row to an existing table and read it
        """
        session = initialize_session
        test_zusatz_attribut = ZusatzAttribut(name="erstes", wert=Decimal("12.25"))
        test_zusatz_attribut2 = ZusatzAttribut(name="zweites", wert=datetime(2024, 1, 1))
        session.add(test_zusatz_attribut)
        session.add(test_zusatz_attribut2)
        session.commit()

        # read and check row
        statement = select(ZusatzAttribut)
        retrieved_zusatz_attribut = session.exec(statement).unique()
        for zusatz_attribut in retrieved_zusatz_attribut:
            assert (zusatz_attribut.name == "erstes" and zusatz_attribut.wert == Decimal("12.25")) or (
                zusatz_attribut.name == "zweites" and zusatz_attribut.wert == datetime(2024, 1, 1)
            )
