from typing import Optional
from sqlmodel import (
    Column,
    Integer,
    Relationship,
    String,
    Field
)
from db.base import Base

class Airport(Base, table=True):
    #id = Column(Integer, primary_key=True)
    code: str = Field(String(3), nullable=False)
    name: str | None = Field(String(100))
    city: str | None = Field(String(50))
    state: str | None = Field(String(4))
    flight1 = Relationship(back_populates="to_airport")
    flight2 = Relationship(back_populates="from_airport")
