from typing import ClassVar, Optional
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlmodel import Field, MetaData, SQLModel
from core.config import settings

#metadata = SQLModel.metadata.schema=settings.DB_SCHEMA

#@as_declarative()
meta = MetaData(schema=settings.DB_SCHEMA)
class SQLModelBase(SQLModel):
    #__table_args__: object = {"schema": settings.DB_SCHEMA}
    metadata = meta
    __name__: str
    # Generates table name based on class name
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    #metadata: MetaData = metadata

class Base(SQLModelBase):
    id: int = Field(default=None, primary_key=True)
