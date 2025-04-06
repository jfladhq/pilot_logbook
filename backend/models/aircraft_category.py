from sqlmodel import (
    Column,
    String,
    Field,
    #SQLModel
)
from db.base import Base

class AircraftCategory(Base, table=True):
    #id: int | None = Field(default=None, primary_key=True)
    shortName: str = Field(sa_column=Column(String(45)))
    name: str = Field(sa_column=Column(String(45)))
