from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str


class UserCreate(UserBase):
    firstname: str
    lastname: str
    age: int


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class UpdateUser(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None