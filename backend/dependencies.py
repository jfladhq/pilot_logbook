from db.session import session
from fastapi import HTTPException, Depends, status
from fastapi.security import SecurityScopes
from sqlmodel import Session


def get_db():
    db: Session = session()
    try:
        yield db
    finally:
        db.close()
