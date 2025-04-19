# #from typing import Optional, List
# from sqlmodel import (
#     Column,
#     Integer,
#     Relationship,
#     String,
#     Field
# )
# from db.base import Base
# #from models.flight import Flight

# class Airport(Base, table=True):
#     #id = Column(Integer, primary_key=True)
#     code: str = Field(String(3), nullable=False)
#     name: str | None = Field(String(100))
#     city: str | None = Field(String(50))
#     state: str | None = Field(String(4))
    
#     #flights_to: list["Flight"] = Relationship(back_populates="to_airport")
#     #from_airports: List = Relationship(back_populates="from_airport")
