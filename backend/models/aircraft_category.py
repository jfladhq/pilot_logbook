from typing import Optional
from sqlmodel import (
    Column,
    Integer,
    String,
    Field
)
from db.base import Base

class AircraftCategory(Base, table=True):
    idAircraftCategory: int | None = Field(default=None, primary_key=True)
    shortName: str = Field(sa_column=Column(String(45)))
    name: str = Field(sa_column=Column(String(45)))
