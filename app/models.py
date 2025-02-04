from app import db
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class City(db.Model):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    entries: Mapped[List['Entrie']] = relationship(
        back_populates='city',
        uselist=True
    )


class Entrie(db.Model):
    __tablename__ = 'entries'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True, comment='Name/Bezeichnung')
    nummer: Mapped[str] = mapped_column(nullable=True, comment='Nummer')
    funktion: Mapped[str] = mapped_column(nullable=True, comment='Funktion')
    gebaeude: Mapped[str] = mapped_column(nullable=True, comment='Gebäude')
    raumnummer: Mapped[str] = mapped_column(nullable=True, comment='Raumnummer')

    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))

    city: Mapped['City'] = relationship(
        back_populates='entries',
        foreign_keys=[city_id],
        uselist=False
    )
