from fastapi.params import Security
from dependencies import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from models.pilot_type import PilotType

router = CRUDRouter(
    schema=PilotType,
    db_model=PilotType,
    db=get_db,
    prefix="/pilot-type",
    tags=["pilot type"],
    delete_all_route=False,
    get_one_route=False,
)
