from db.base import Base

class PilotType(Base):
    id: int
    shortName: str
    name: str
    pic: bool | None
