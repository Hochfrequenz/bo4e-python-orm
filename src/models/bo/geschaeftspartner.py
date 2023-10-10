from typing import TYPE_CHECKING, Optional

from bo4e.enum.anrede import Anrede
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from sqlalchemy import ARRAY, Boolean, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ..com.adresse import Adresse

from db.base_class import Base


class Geschaeftspartner(Base):
    __tablename__ = "geschaeftspartner"
    id: Mapped[int] = mapped_column(primary_key=True)  # need a primary key
    name1: Mapped[str] = mapped_column(String(30))
    gewerbekennzeichnung: Mapped[bool] = mapped_column(Boolean)
    geschaeftspartnerrolle: Mapped[list[Geschaeftspartnerrolle]] = mapped_column(
        ARRAY(Enum(Geschaeftspartnerrolle, name="Geschaeftspartnerrolle")), nullable=False
    )

    anrede: Mapped[Optional[Anrede]] = mapped_column(Enum(Anrede, name="Anrede"), nullable=True)

    name2: Mapped[Optional[str]] = mapped_column(String(30))
    """
    Zweiter Teil des Namens.
    Hier kann der eine Erweiterung zum Firmennamen oder bei Privatpersonen beispielsweise der Vorname dagestellt werden.
    Beispiele: Bereich Süd oder Nina
    """

    name3: Mapped[Optional[str]] = mapped_column(String(30))
    """
    Dritter Teil des Namens.
    Hier können weitere Ergänzungen zum Firmennamen oder bei Privatpersonen Zusätze zum Namen dagestellt werden.
    Beispiele: und Afrika oder Sängerin
    """
    #: Handelsregisternummer des Geschäftspartners
    hrnummer: Mapped[Optional[str]] = mapped_column(String(30))
    #: Amtsgericht bzw Handelsregistergericht, das die Handelsregisternummer herausgegeben hat
    amtsgericht: Mapped[Optional[str]] = mapped_column(String(30))
    #: Bevorzugte Kontaktwege des Geschäftspartners
    kontaktweg: Mapped[Optional[Kontaktart]] = mapped_column(Enum(Kontaktart, name="Kontaktart"))
    #: Die Steuer-ID des Geschäftspartners; Beispiel: "DE 813281825"
    umsatzsteuer_id: Mapped[Optional[str]] = mapped_column(String(30))
    #: Die Gläubiger-ID welche im Zahlungsverkehr verwendet wird; Z.B. "DE 47116789"
    glaeubiger_id: Mapped[Optional[str]] = mapped_column(String(30))
    #: E-Mail-Adresse des Ansprechpartners. Z.B. "info@hochfrequenz.de"
    e_mail_adresse: Mapped[Optional[str]] = mapped_column(String(30))
    #: Internetseite des Marktpartners
    website: Mapped[Optional[str]] = mapped_column(String(30))
    #: Adressen der Geschäftspartner, an denen sich der Hauptsitz befindet

    # Define a one-to-one relationship with Adresse
    adresse_id = mapped_column(ForeignKey("adresse.id"))
    partneradresse: Mapped["Adresse"] = relationship(back_populates="geschaeftspartner")

    def __repr__(self) -> str:
        return f"Geschaeftspartner(id={self.id!r}, Name1={self.name1!r})"
