from sqlmodel import MetaData, create_engine, Session
from sqlalchemy.orm import sessionmaker
from core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    future=True,
    pool_size=settings.SQLALCHEMY_POOLSIZE,
    max_overflow=5,
    # pool_recycle=3600,
)
session: Session = sessionmaker(class_=Session, autocommit=False, autoflush=False, bind=engine, future=True)
metadata = MetaData(schema=settings.DB_SCHEMA)
metadata.reflect(bind=engine)