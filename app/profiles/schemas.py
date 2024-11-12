from pydantic import BaseModel, Field


class Profile(BaseModel):
    name: str
    avatar: str
    bio: str = Field(max_length=255)
    lvl: int
