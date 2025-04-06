from datetime import date, time, datetime
from typing import Optional
from sqlmodel import (
    Column,
    Field,
    VARCHAR,
    Boolean,
    DECIMAL,
    TIMESTAMP,
    func,
    Relationship,
    #SQLModel
)
from models.airline_identifier import AirlineIdentifier
from models.aircraft_category import AircraftCategory
from models.pilot_type import PilotType
from models.user import User
from models import *
from db.base import Base

class Flight(Base, table=True):
    #id: int | None = Field(default=None, primary_key=True)
    date: date
    aircraftType: str = Field(sa_column=Column(VARCHAR(3), nullable=False))
    aircraftIdentity: str = Field(sa_column=Column(VARCHAR(9), nullable=False))
    fromAirport: str = Field(sa_column=Column(VARCHAR(3), nullable=False))
    toAirport: str = Field(sa_column=Column(VARCHAR(3), nullable=False))
    departure: time
    arrival: time
    dayLanding: int | None
    nightLanding: int | None
    actualInstrument: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    simulatedInstrumentUnderHood: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    hold: int | None
    simulator: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    crossCountryTime: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    totalFlightDuration: float = Field(sa_column=Column(DECIMAL(6, 2), nullable=False))
    initialOperatingExperience: bool | None = Field(sa_column=Column(Boolean))
    crewMemberName: str = Field(sa_column=Column(VARCHAR(100), nullable=False))
    flightNumber: str = Field(sa_column=Column(VARCHAR(4), nullable=False))
    timestamp: Optional[datetime] = Field(
        default=func.now(),
        sa_type=TIMESTAMP(timezone=True),
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )
    airlineidentifier_id: int = Field(default=None,foreign_key="airlineidentifier.id")
    aircraftcategory_id: int = Field(default=None,foreign_key="aircraftcategory.id")
    pilottype_id: int = Field(default=None, foreign_key="pilottype.id")
    user_id: int = Field(default=None, foreign_key="user.id")

    airline_identifier: AirlineIdentifier = Relationship(
        sa_relationship_kwargs={"primaryjoin": "airlineidentifier_id==airlineidentifier.id","lazy":"joined"}
    )
    aircraft_category: AircraftCategory = Relationship(
        sa_relationship_kwargs={"primaryjoin": "aircraftcategory_id==aircraftcategory.id","lazy":"joined"}
    )
    # aircraft_category: AircraftCategory = Relationship(
    #      sa_relationship_kwargs={"primaryjoin": "Flight.AircraftCategory_id=AircraftCategory.id","lazy":"joined"}
    # )
    pilot_type: PilotType = Relationship(
        sa_relationship_kwargs={"primaryjoin": "pilottype_id==pilottype.id","lazy":"joined"}
    )
    user: User = Relationship(
        sa_relationship_kwargs={"primaryjoin": "user_id==user.id","lazy":"joined"}
    )
    # user: User = Relationship(
    #     sa_relationship_kwargs={"primaryjoin":"Flight.User_id=User.id","lazy":"joined"}
    # )
