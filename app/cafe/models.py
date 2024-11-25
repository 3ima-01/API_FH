from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from sqlalchemy import Integer, String


class Cafe(Base):
    __tablename__ = "cafe"

    id: Mapped[int] = mapped_column(primary_key=True)
    location: Mapped[str] = mapped_column(String(255))
    fish: Mapped[str] = mapped_column(String(255))
    weight: Mapped[str] = mapped_column(String(50))
    count: Mapped[int] = mapped_column(Integer)
    price: Mapped[str] = mapped_column(String(50))
