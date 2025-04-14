from sqlmodel import (
    Column,
    Integer,
    String,
    Field
)
from db.base import Base


class Report(Base, table=True):
    #id = Column(Integer, primary_key=True)
    shortName: str = Field(sa_column=Column(String(45), nullable=False))
    name: str = Field(sa_column=Column(String(45), nullable=False))