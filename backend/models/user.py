from sqlmodel import VARCHAR, Boolean, Column, Field, Integer, SQLModel, String, CHAR
from db.base import Base

class User(Base, table=True):
    #id: int | None = Field(default=None, primary_key=True)
    admin: bool = Field(sa_column=Column(Boolean, nullable=False, default=False))
    username: str = Field(sa_column=Column(String(100), nullable=False, unique=True))
    email: str = Field(sa_column=Column(VARCHAR(100), nullable=False, unique=True))
    firstName: str = Field(sa_column=Column(String(100), nullable=False))
    lastName: str = Field(sa_column=Column(String(100), nullable=False))
    password: str = Field(sa_column=Column(CHAR(100), nullable=False))
    resetPassword: bool = Field(sa_column=Column(Boolean, nullable=False, server_default="0"))
    loginAttempts: int = Field(sa_column=Column(Integer, nullable=False, server_default="0"))
    maxLoginAttempts: int = Field(sa_column=Column(Integer, nullable=False, server_default="5"))
