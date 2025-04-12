from datetime import date, time, datetime
from typing import Optional
from sqlmodel import (
    Column,
    Field,
    VARCHAR,
    Boolean,
    DECIMAL,
    TIMESTAMP,
    ForeignKey,
    Table,
    UniqueConstraint,
    func,
    Relationship,
    Integer
    #SQLModel
)
from sqlalchemy.orm import RelationshipProperty
from models.airline_identifier import AirlineIdentifier
from models.aircraft_category import AircraftCategory
from models.pilot_type import PilotType
from models.user import User
from models import *
from db.base import Base

class Flight(Base, table=True):
    date: date
    aircraftIdentity: str = Field(sa_column=Column(VARCHAR(9), nullable=False))
    departure: time
    arrival: time
    totalFlightDuration: float = Field(sa_column=Column(DECIMAL(6, 2), nullable=False))
    dayLanding: int | None
    nightLanding: int | None
    actualInstrument: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    simulatedInstrumentUnderHood: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    atd: float | None = Field(sa_column=Column(DECIMAL(6,2), comment="UND"))
    atdInstrument: float | None = Field(sa_column=Column(DECIMAL(6,2), comment="UND"))
    hold: int | None
    fullFlightSim: float | None = Field(sa_column=Column(DECIMAL(6,2)))
    groundTrainer: float | None = Field(sa_column=Column(DECIMAL(6,2)))
    lineCheck: bool = Field(Boolean, default=False)
    crossCountryTime: float | None = Field(sa_column=Column(DECIMAL(6, 2)))
    initialOperatingExperience: bool | None = Field(sa_column=Column(Boolean))
    remarks: str | None = Field(sa_column=Column(VARCHAR(255)))
    approaches: int | None
    crewMemberName: str = Field(sa_column=Column(VARCHAR(100), nullable=False))
    flightNumber: str = Field(sa_column=Column(VARCHAR(4), nullable=False))
    fileName: str = Field(VARCHAR(50))
    course: str = Field(sa_column=Column(VARCHAR(4), comment="UND"))
    lesson: str = Field(sa_column=Column(VARCHAR(10), comment="UND"))
    status: str = Field(sa_column=Column(VARCHAR(3), comment="UND"))
    instructor: str = Field(sa_column=Column(VARCHAR(10), comment="UND"))
    oral: float = Field(sa_column=Column(DECIMAL(6,2), comment="UND"))
    dtl: Optional[int] = Field(sa_column=Column(Integer, comment="Daytime Landings UND"))
    ntl: Optional[int] = Field(sa_column=Column(Integer, comment="Nighttime Landings UND"))
    timestamp: Optional[datetime] = Field(
        default=func.now(),
        sa_type=TIMESTAMP(timezone=True),
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )
    to_airport_id: int = Field(foreign_key="airport.id")
    from_airport_id: int = Field(foreign_key="airport.id")
    aircraft_id: int = Field(foreign_key="aircraft.id")
    airlineidentifier_id: int = Field(default=None,foreign_key="airlineidentifier.id")
    aircraftcategory_id: int = Field(default=None,foreign_key="aircraftcategory.id")
    pilottype_id: int = Field(default=None, foreign_key="pilottype.id")
    user_id: int = Field(default=None, foreign_key="user.id")
    __table_args__ = (UniqueConstraint(date, departure, arrival, totalFlightDuration),)
    
    to_airport: Airport = Relationship(
        sa_relationship=RelationshipProperty(
            "Airport",
            foreign_keys=to_airport_id
            )
        )
    from_airport: Airport = Relationship(sa_relationship=RelationshipProperty(
        "Airport",
        foreign_keys=from_airport_id
        )
    )
    aircraft: Aircraft = Relationship(
        sa_relationship=RelationshipProperty(
            "Aircraft",
            foreign_keys=aircraft_id
        )
    )
    airline_identifier: AirlineIdentifier = Relationship(
        sa_relationship=RelationshipProperty(
            "AirlineIdentifier", 
            primaryjoin="foreign(Flight.airlineidentifier_id) == AirlineIdentifier.id", 
            uselist=True
        )
    )
    aircraft_category: AircraftCategory = Relationship(
        sa_relationship=RelationshipProperty(
            "AircraftCategory", 
            primaryjoin="foreign(Flight.aircraftcategory_id) == AircraftCategory.id", 
            uselist=True
        )
    )
    pilot_type: PilotType = Relationship(
        sa_relationship=RelationshipProperty(
            "PilotType", 
            primaryjoin="foreign(Flight.pilottype_id) == PilotType.id", 
            uselist=True
        ),
    )
    user: User = Relationship(
        sa_relationship=RelationshipProperty(
            "User", 
            primaryjoin="foreign(Flight.user_id) == User.id", 
            uselist=True
        ),
    )
    to_airports: Optional[list[Airport]] = Relationship(
        sa_relationship=RelationshipProperty(
            "Airport",
            secondary="Flight_Airport",
            #relationship("Airport", secondary="Flight_Airport", lazy="joined")
        )
    )


Flight_Airport = Table(
    "Flight_Airport",
    Base.metadata,
    Column(
        "flight_id",
        Integer,
        ForeignKey("Flight.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column(
        "airport_id",
        Integer,
        ForeignKey("Airport.id"),
        nullable=False
    )
)