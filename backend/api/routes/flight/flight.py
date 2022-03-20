from dependencies import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
import schemas as schemas
import models as models


router = CRUDRouter(
    schema=schemas.Flight,
    db_model=models.Flight,
    db=get_db,
    prefix="/flight",
    tags=["flight"],
)
