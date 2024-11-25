from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Trophys(Base):
    __tablename__ = "trophys"

    id: Mapped[int] = mapped_column(primary_key=True)
    fish: Mapped[str] = mapped_column(String(255))
    base_weight: Mapped[str] = mapped_column(String(50))
    rare_weight: Mapped[str] = mapped_column(String(50))
