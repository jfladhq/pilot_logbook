from sqlmodel import (
    Column,
    Field,
    String,
    #SQLModel
    Boolean,
    Relationship
)
from db.base import Base

class PilotType(Base,table=True):
    #id: int | None = Field(default=None, primary_key=True)
    shortName: str = Field(sa_column=Column(String(45), nullable=False))
    name: str = Field(sa_column=Column(String(45), nullable=False))
    pic: bool = Field(sa_column=Column(Boolean, default=False))

    #flights: list["Flight"] = Relationship(back_populates="pilot_type",sa_relationship_kwargs={"uselist": True})