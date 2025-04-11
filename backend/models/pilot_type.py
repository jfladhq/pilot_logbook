from sqlmodel import (
    Column,
    Field,
    String,
    #SQLModel
)
from db.base import Base

class PilotType(Base,table=True):
    #id: int | None = Field(default=None, primary_key=True)
    shortName: str = Field(sa_column=Column(String(45), nullable=False))
    name: str = Field(sa_column=Column(String(45), nullable=False))
