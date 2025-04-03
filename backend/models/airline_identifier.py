from typing import Optional
from sqlmodel import (
    Column,
    Field,
    Integer,
    String,
)
from db.base import Base

class AirlineIdentifier(Base,table=True):
    idAirlineIdentifier: int | None = Field(default=None, primary_key=True)
    name: str = Column(String(45), nullable=False)
    letterCode: str = Column(String(2), nullable=False)
    accountCode: int = Column(Integer)
