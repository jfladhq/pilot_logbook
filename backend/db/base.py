from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlmodel import SQLModel
from core.config import settings

class Base(SQLModel):
    __table_args__: object = {"schema": settings.DB_SCHEMA}
    __name__: str
    # Generates table name based on class name
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__