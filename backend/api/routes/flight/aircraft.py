from dependencies import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
import schemas as schemas
from models.aircraft import Aircraft
router = CRUDRouter(
    schema=schemas.Aircraft,
    create_schema=schemas.Aircraft,
    db_model=Aircraft,
    db=get_db,
    prefix="/aircraft",
    tags=["aircraft"],
    delete_all_route=False,
    get_one_route=False,
)