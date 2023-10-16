"""
Integration tests for the postgresql_app
"""
from bo4e.enum.landescode import Landescode
from sqlalchemy import inspect
from sqlalchemy.engine.reflection import Inspector

from src.models.bo.geschaeftspartner import Geschaeftspartner  # type: ignore
from src.models.com.adresse import Adresse  # type: ignore


class TestAdresse:
    def test_existence_of_tables(self, initialize_db) -> None:
        """
        test for the existence of tables
        """
        insp: Inspector = inspect(initialize_db.bind)

        name_of_tables = insp.get_table_names()

        assert "adresse" in name_of_tables

    def test_create_and_retrieve_address(self, initialize_db) -> None:
        """
        test to create and retrieve an address
        """
        session = initialize_db
        # Create an address record
        new_address = Adresse(
            postleitzahl="12345", ort="Teststadt", strasse="Teststraße", hausnummer="42", landescode="DE"
        )
        session.add(new_address)
        session.commit()

        # Retrieve the created address from the database
        retrieved_address = session.query(Adresse).filter_by(id=new_address.id).first()

        # Assertions to check if the retrieved address matches the created one
        assert retrieved_address.postleitzahl == "12345"
        assert retrieved_address.ort == "Teststadt"
        assert retrieved_address.strasse == "Teststraße"
        assert retrieved_address.hausnummer == "42"

        # Clean up
        session.delete(new_address)
        session.commit()

    def test_update_address(self, initialize_db) -> None:
        """
        Test to update table_adress
        """
        session = initialize_db
        # Create an address record
        new_address = Adresse(postleitzahl="54321", ort="Stadt", strasse="Straße", hausnummer="1", landescode="DE")
        session.add(new_address)
        session.commit()

        # Update the address attributes
        new_address.postleitzahl = "67890"
        new_address.ort = "Neue Stadt"
        session.commit()

        # Retrieve the updated address from the database
        updated_address = session.query(Adresse).filter_by(id=new_address.id).first()

        # Assertions to check if the address attributes were updated correctly
        assert updated_address.postleitzahl == "67890"
        assert updated_address.ort == "Neue Stadt"

        session.delete(new_address)
        session.commit()
