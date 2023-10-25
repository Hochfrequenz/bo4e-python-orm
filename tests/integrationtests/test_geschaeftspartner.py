"""
Integration tests for the postgresql_app
"""
from bo4e.enum.anrede import Anrede
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from sqlalchemy import inspect
from sqlalchemy.engine.reflection import Inspector

from borm.models.bo.geschaeftspartner import Geschaeftspartner  # type: ignore


class TestGeschaeftspartner:
    def test_existence_of_tables(self, initialize_db) -> None:
        """
        test for the existence of tables
        """
        insp: Inspector = inspect(initialize_db.bind)

        name_of_tables = insp.get_table_names()

        assert "geschaeftspartner" in name_of_tables

    def test_create_and_retrieve_geschaeftspartner(self, initialize_db) -> None:
        """
        test create and retrieve a Geschaeftspartner
        """
        session = initialize_db
        # Create a Geschaeftspartner record
        new_geschaeftspartner = Geschaeftspartner(
            name1="Test GmbH",
            gewerbekennzeichnung=False,
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
            anrede=Anrede.HERR,
        )
        session.add(new_geschaeftspartner)
        session.commit()

        # Retrieve the created Geschaeftspartner from the database
        retrieved_geschaeftspartner = session.query(Geschaeftspartner).filter_by(id=new_geschaeftspartner.id).first()

        # Assertions to check if the retrieved Geschaeftspartner matches the created one
        assert retrieved_geschaeftspartner.name1 == "Test GmbH"
        assert retrieved_geschaeftspartner.gewerbekennzeichnung is False
        assert Geschaeftspartnerrolle.KUNDE in retrieved_geschaeftspartner.geschaeftspartnerrolle
        assert retrieved_geschaeftspartner.anrede == Anrede.HERR

        # Clean up: Delete the test Geschaeftspartner
        session.delete(new_geschaeftspartner)
        session.commit()

    def test_update_geschaeftspartner(self, initialize_db) -> None:
        """
        Test to update table_geschaeftspartner
        """
        session = initialize_db
        # Create a Geschaeftspartner record
        new_geschaeftspartner = Geschaeftspartner(
            name1="Test GmbH",
            gewerbekennzeichnung=False,
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
            anrede=Anrede.HERR,
        )
        session.add(new_geschaeftspartner)
        session.commit()

        # Update the Geschaeftspartner attributes
        new_geschaeftspartner.name1 = "Test AG"
        new_geschaeftspartner.gewerbekennzeichnung = True
        session.commit()

        # Retrieve the updated geschaeftspartner from the database
        updated_geschaeftspartner = session.query(Geschaeftspartner).filter_by(id=new_geschaeftspartner.id).first()

        # Assertions to check if the address attributes were updated correctly
        assert updated_geschaeftspartner.name1 == "Test AG"
        assert updated_geschaeftspartner.gewerbekennzeichnung is True

        session.delete(new_geschaeftspartner)
        session.commit()
