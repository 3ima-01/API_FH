from sqlalchemy import String, Double
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Coils(Base):
    __tablename__ = "coils"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    mex = mapped_column(Double())


class Rods(Base):
    __tablename__ = "rods"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    mex = mapped_column(Double())
