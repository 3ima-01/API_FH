from uuid import UUID, uuid4
from sqlalchemy import CHAR, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from sqlalchemy.orm import relationship


class Profiles(Base):
    __tablename__ = "profiles"
    uuid: Mapped[UUID] = mapped_column(CHAR(36), primary_key=True, default=uuid4)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.user_id"))

    name: Mapped[str] = mapped_column(String(255), default="default_name")
    avatar: Mapped[str] = mapped_column(String(255), default="https://ibb.co/p4cF1Vj")
    bio: Mapped[str] = mapped_column(String(255), default="")
    lvl: Mapped[int] = mapped_column(default=0)

    user: Mapped["Users"] = relationship("Users", back_populates="profile")

    def __str__(self):
        return self.name
