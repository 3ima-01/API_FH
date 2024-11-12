from pydantic import BaseModel, EmailStr, Field


class UnverifyUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)


class User(BaseModel):
    email: EmailStr
    password: str
