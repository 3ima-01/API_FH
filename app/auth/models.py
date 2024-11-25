from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship


class Roles(Base):
    __tablename__ = "roles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    permissions: Mapped[int] = mapped_column()

    user: Mapped[list["Users"]] = relationship("Users", back_populates="role")
    permissions: Mapped[list["Permissions"]] = relationship(
        "Permissions", secondary="role_permissions"
    )

    def __str__(self):
        return self.name


class Permissions(Base):
    __tablename__ = "permissions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(String(255))

    roles: Mapped[list["Roles"]] = relationship("Roles", secondary="role_permissions")

    def __str__(self):
        return self.name


class Role_Permissions(Base):
    __tablename__ = "role_permissions"
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True
    )
