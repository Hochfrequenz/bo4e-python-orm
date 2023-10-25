from typing import Optional

from bo4e.enum.landescode import Landescode
from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from borm.db.base_class import Base


class Adresse(Base):
    __tablename__ = "adresse"
    id: Mapped[int] = mapped_column(primary_key=True)
    #: Die Postleitzahl; z.B: "41836"
    postleitzahl: Mapped[str] = mapped_column(String(30))
    #: Bezeichnung der Stadt; z.B. "Hückelhoven"
    ort: Mapped[str] = mapped_column(String(30))
    #: Bezeichnung des Ortsteils; z.B. "Mitte"
    ortsteil: Mapped[Optional[str]] = mapped_column(String(30))
    #: Bezeichnung der Straße; z.B. "Weserstraße"
    strasse: Mapped[Optional[str]] = mapped_column(String(30))
    #: Hausnummer inkl. Zusatz; z.B. "3", "4a"
    hausnummer: Mapped[Optional[str]] = mapped_column(String(30))
    #: Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt
    postfach: Mapped[Optional[str]] = mapped_column(String(30))
    #: Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    adresszusatz: Mapped[Optional[str]] = mapped_column(String(30))
    #: Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    co_ergaenzung: Mapped[Optional[str]] = mapped_column(String(30))
    #: Offizieller ISO-Landescode
    landescode: Mapped[Landescode] = mapped_column(Enum(Landescode, name="Landescode", default="DE"))
    # todo: add xor for strasse oder postfach

    def __repr__(self) -> str:
        return f"Adresse(id={self.id!r}, Postleitzahl={self.postleitzahl!r}, Ort={self.ort!r})"
