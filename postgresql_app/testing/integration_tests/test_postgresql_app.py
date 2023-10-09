import pytest
from bo4e.enum.anrede import Anrede
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.landescode import Landescode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.bo.geschaeftspartner import Geschaeftspartner
from models.com.adresse import Adresse
from postgresql_app.auxiliary import get_url
#from db.base import Base
from sqlalchemy import inspect
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.reflection import Inspector



#create engine
engine = create_engine( get_url() )
def test_existence_of_tables(db_engine = engine):
    insp: Inspector = inspect(db_engine)

    name_of_tables = insp.get_table_names()

    assert "geschaeftspartner" in name_of_tables
    assert "adresse" in name_of_tables



def test_create_and_retrieve_address( db_engine = engine):
    Session = sessionmaker( bind=db_engine )
    session = Session()
    # Create an address record
    new_address = Adresse(
        postleitzahl="12345",
        ort="Teststadt",
        strasse="Teststraße",
        hausnummer="42",
        landescode = Landescode.DE
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

    # Clean up: Delete the test Geschaeftspartner
    session.delete(new_address)
    session.commit()
    session.close()



def test_create_and_retrieve_geschaeftspartner( db_engine = engine):
    Session = sessionmaker( bind=db_engine )
    session = Session()
    # Create an address record
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
    session.close()

def test_update_address( db_engine = engine ):
    Session = sessionmaker( bind=db_engine )
    session = Session()
    # Create an address record
    new_address = Adresse(postleitzahl="54321", ort="Stadt", strasse="Straße", hausnummer="1", landescode = Landescode.DE)
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

    #session.delete(new_address)
    session.commit()
    session.close()