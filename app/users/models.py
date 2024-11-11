from uuid import UUID, uuid4
from sqlalchemy import text, CHAR, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    uuid: Mapped[UUID] = mapped_column(CHAR(36), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))

    role_id: Mapped[int] = mapped_column(default=text("0"), server_default=text("0"))
    is_blocked: Mapped[bool] = mapped_column(
        default=text("False"), server_default=text("False")
    )

    poins = relationship("Point", back_populates="user")
