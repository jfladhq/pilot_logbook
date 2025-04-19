from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from dependencies import get_db
#from fastapi.datastructures import UploadFile
#from fastapi.params import File
#from fastapi import Depends, HTTPException
#from sqlalchemy.sql.expression import select, insert
#from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
#from datetime import datetime
#import pandas as pd
#import schemas as schemas
from src.flight import models
from src.flight import schemas

router = CRUDRouter(
    schema=schemas.Flight,
    db_model=models.Flight,
    #create_schema=models.FlightBase,
    #update_schema=models.FlightBase,
    db=get_db,
    prefix="/flight",
    tags=["flight"],
    delete_all_route=False,
)
# router = APIRouter(
#     prefix="/flight",
#     tags=["flight"],
# )

# @router.get("/", response_model=schemas.Flight)
# def read_flights(db = Depends(get_db)):
#     flights = db.execute(select(models.Flight)).scalars().all()
#     return flights