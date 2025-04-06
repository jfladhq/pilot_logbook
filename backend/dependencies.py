from collections.abc import AsyncGenerator
import logging
from db.session import AsyncSessionFactory
from fastapi import HTTPException, Depends, status
from fastapi.security import SecurityScopes
from sqlmodel import Session


async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        try:
            yield session
        except Exception as e:
            logging.error(f"Error getting database session: {e}")
            raise