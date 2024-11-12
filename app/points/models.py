from uuid import UUID, uuid4
from sqlalchemy import CHAR, JSON, DateTime, ForeignKey, func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.points.enums import StatusEnum, FishEnum, LocationEnum


class Point(Base):
    __tablename__ = "points"
    uuid: Mapped[UUID] = mapped_column(CHAR(36), primary_key=True, default=uuid4)
    user_uuid: Mapped[UUID] = mapped_column(
        ForeignKey("users.uuid", ondelete="CASCADE")
    )

    title: Mapped[str] = mapped_column(String(255))
    fish: Mapped[FishEnum] = mapped_column(String(255))
    location: Mapped[LocationEnum] = mapped_column(String(255))
    coords: Mapped[str] = mapped_column(String(255))

    images: Mapped[list[str]] = mapped_column(JSON)

    status: Mapped[StatusEnum] = mapped_column(default=StatusEnum.under_moderation)

    create_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    update_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
    )

    user = relationship("User", back_populates="points")
