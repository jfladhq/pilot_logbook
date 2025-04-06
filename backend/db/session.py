from sqlmodel import MetaData, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from core.config import settings
# engine = AsyncEngine(create_engine(
#     settings.SQLALCHEMY_DATABASE_URI,
#     future=True,
#     pool_size=settings.SQLALCHEMY_POOLSIZE,
#     max_overflow=5,
#     # pool_recycle=3600,
# ))
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    future=True,
    echo=True,
    connect_args={
        "server_settings": {"search_path": settings.DB_SCHEMA}
    }
    # pool_recycle=3600,
)

# async def init_db():
#     # await database.connect()
#     async with engine.begin() as conn:
#         # await conn.run_sync(Base.metadata.create_all)
#         await conn.run_sync(MetaData().create_all)

# async def get_session() -> AsyncGenerator[AsyncSession, None]:
#     """Get a session for the database connection."""
#     session = sessionmaker(
#         engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with session() as session:
#         yield session
AsyncSessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
#session: Session = sessionmaker(class_=Session, autocommit=False, autoflush=False, bind=engine, future=True)
#metadata = MetaData(schema=settings.DB_SCHEMA)
#metadata.reflect(bind=engine)