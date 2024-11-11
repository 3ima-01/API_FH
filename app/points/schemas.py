from pydantic import BaseModel, Field

from app.points.enums import FishEnum, LocationEnum


class Point(BaseModel):
    title: str = Field(max_length=64)
    fish: FishEnum
    location: LocationEnum
    coords: str = Field(example="666.666")

    images: list[str]
