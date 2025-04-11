import os
from typing import ClassVar
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEV: ClassVar = True
    SERVER: ClassVar = False
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ["http://127.0.0.1:9000", "http://127.0.0.1:3000"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "LogbookAPI"
    PROJECT_ROOT: ClassVar = os.path.dirname(os.path.dirname(__file__))

    DB_SERVER: str = ""
    DB_PORT: str = ""
    DB_SCHEMA: str = ""
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_NAME: str = ""

    SQLALCHEMY_POOLSIZE: int = 2
    SQLALCHEMY_DATABASE_URI: str = (
         f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    )

    class Config:
        case_sensitive = True


settings = Settings()
