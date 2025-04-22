from typing import List
from schemas.base import Base
#from src.flight.schemas import FlightBase

class UserBase(Base):
    username: str
    firstName: str
    lastName: str
    email: str

    #flights: List[FlightBase]
class User(UserBase):
    id: int
    admin: bool
    resetPassword: bool
    loginAttempts: int
    maxLoginAttempts: int

class Token(Base):
    access_token: str
    token_type: str
    user: User


class TokenData(Base):
    username: str | None = None
    scopes: list[str] = []


class NewUser(UserBase):
    password: str
