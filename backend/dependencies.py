from collections.abc import Generator
import logging
from typing import Annotated

from fastapi import Depends
from db.session import engine
#from fastapi import HTTPException, Depends, status
#from fastapi.security import SecurityScopes
from sqlmodel import Session


# async def get_db() -> AsyncGenerator:
#     async with get_session() as session:
#         # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
#         try:
#             yield session
#         except Exception as e:
#             logging.error(f"Error getting database session: {e}")
#             raise
def get_db() -> Generator[Session, None, None]:
    #session = SessionLocal()
    # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
    with Session(engine) as session:
        yield session
# reusable_oauth2 = OAuth2PasswordBearer(
#     tokenUrl=f"{settings.API_V1_STR}/login/access-token"
# )
#SessionDep = Annotated[Session, Depends(get_db)]

# def get_current_user(session: SessionDep, token: TokenDep) -> User:
#     try:
#         payload = jwt.decode(
#             token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
#         )
#         token_data = TokenPayload(**payload)
#     except (InvalidTokenError, ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#         )
#     user = session.get(User, token_data.sub)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     if not user.is_active:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return user


# CurrentUser = Annotated[User, Depends(get_current_user)]

#TokenDep = Annotated[str, Depends(reusable_token)]
    # try:
    #     yield session
    #     session.commit()
    # except Exception as e:
    #     logging.error(f"Error getting database session: {e}")
    #     raise
    # finally:
    #     session.close()
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")