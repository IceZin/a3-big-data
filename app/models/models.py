from sqlalchemy import Sequence, String, func
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class Country(Base):
    __tablename__ = "Tabela_ADBD"
    code: Mapped[str] = mapped_column(String(2), primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    ranking_pos: Mapped[int] = mapped_column(nullable=False, unique=True)
    pib: Mapped[float] = mapped_column(nullable=False)
    universities_on_world_ranking: Mapped[int] = mapped_column(nullable=False)
