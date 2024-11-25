from uuid import UUID, uuid4
from sqlalchemy import ForeignKey, text, CHAR, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from app.auth.models import Roles


class Users(Base):
    __tablename__ = "users"
    user_id: Mapped[UUID] = mapped_column(CHAR(36), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), default=1)
    is_blocked: Mapped[bool] = mapped_column(
        default=text("False"), server_default=text("False")
    )

    role: Mapped["Roles"] = relationship("Roles", back_populates="user")
    profile: Mapped["Profiles"] = relationship("Profiles", back_populates="user")
    points: Mapped["Points"] = relationship("Points", back_populates="user")

    def __str__(self):
        return self.email


class UnverifiedUsers(Base):
    __tablename__ = "unverified_users"
    user_id: Mapped[UUID] = mapped_column(CHAR(36), primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    verify_code: Mapped[str] = mapped_column(String(255), unique=True)

    def __str__(self):
        return self.email
