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

    def __str__(self):
        return f"Stadt {self.name}"


class Building(db.Model):
    __tablename__ = 'buildings'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    entries: Mapped[List['Entrie']] = relationship(
        back_populates='gebaeude',
        uselist=True
    )

    def __str__(self):
        return f"Gebäude {self.name}"


class Entrie(db.Model):
    __tablename__ = 'entries'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    nummer: Mapped[str] = mapped_column(nullable=True)
    funktion: Mapped[str] = mapped_column(nullable=True)
    raumnummer: Mapped[str] = mapped_column(nullable=True)

    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'), nullable=True)
    gebaeude_id: Mapped[int] = mapped_column(ForeignKey('buildings.id'), nullable=True)

    city: Mapped['City'] = relationship(
        back_populates='entries',
        foreign_keys=[city_id],
        uselist=False
    )
    gebaeude: Mapped['Building'] = relationship(
        back_populates='entries',
        foreign_keys=[gebaeude_id],
        uselist=False
    )
