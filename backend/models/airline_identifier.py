from sqlmodel import (
    Column,
    Field,
    String,
    VARCHAR
    #SQLModel
)
from db.base import Base

class AirlineIdentifier(Base, table=True):
    #id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(45), nullable=False))
    letterCode: str = Field(sa_column=Column(String(2), nullable=False))
    accountCode: str | None = Field(sa_column=Column(VARCHAR(3), nullable=False))
