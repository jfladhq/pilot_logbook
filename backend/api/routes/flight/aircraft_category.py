from dependencies import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
import schemas as schemas
from models.aircraft_category import AircraftCategory
router = CRUDRouter(
    schema=schemas.AircraftCategory,
    create_schema=schemas.AircraftCategory,
    db_model=AircraftCategory,
    db=get_db,
    prefix="/aircraft-category",
    tags=["aircraft-category"],
    delete_all_route=False,
    get_one_route=False,
)