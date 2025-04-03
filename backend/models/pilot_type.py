from typing import Optional
from sqlmodel import (
    Column,
    Field,
    Integer,
    String,
)
from db.base import Base

class PilotType(Base,table=True):
    idPilotType: int | None = Field(default=None, primary_key=True)
    shortName: str = Field(sa_column=Column(String(45), nullable=False))
    name: str = Field(sa_column=Column(String(45), nullable=False))
