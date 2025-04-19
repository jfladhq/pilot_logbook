# from typing import List, Optional
# from sqlmodel import VARCHAR, Boolean, Column, Field, Integer, Relationship, String
# from db.base import Base
# import models as models
# class User(Base, table=True):
#     #id: int | None = Field(default=None, primary_key=True)
#     admin: bool = Field(sa_column=Column(Boolean, default=False))
#     username: str = Field(sa_column=Column(String(100), nullable=False, unique=True))
#     email: str = Field(sa_column=Column(VARCHAR(100), nullable=False, unique=True))
#     firstName: str = Field(sa_column=Column(String(100), nullable=False))
#     lastName: str = Field(sa_column=Column(String(100), nullable=False))
#     password: str = Field(sa_column=Column(VARCHAR(100), nullable=False))
#     resetPassword: bool = Field(sa_column=Column(Boolean, nullable=False, server_default="0"))
#     loginAttempts: int = Field(sa_column=Column(Integer, nullable=False, server_default="0"))
#     maxLoginAttempts: int = Field(sa_column=Column(Integer, nullable=False, server_default="5"))
#     flights: List["models.Flight"] = Relationship(back_populates="user", sa_relationship_kwargs={'lazy': 'selectin'})
#     #flights: List["Flight"] | None = Relationship(back_populates="user")


# class Token(Base):
#     access_token: str
#     token_type: str
#     user: User


# class TokenData(Base):
#     username: str | None = None
#     scopes: list[str] = []


# class NewUser(Base):
#     username: str
#     firstName: str
#     lastName: str
#     password: str
#     email: str