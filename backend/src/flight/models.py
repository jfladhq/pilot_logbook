from decimal import Decimal
from datetime import date, time, datetime
from typing import ClassVar, Optional, TYPE_CHECKING
from pydantic import BaseModel
from sqlmodel import (
    Column,
    Field,
    VARCHAR,
    Boolean,
    DECIMAL,
    TIMESTAMP,
    UniqueConstraint,
    func,
    Relationship,
    Integer,
    #SQLModel
)
from sqlalchemy.orm import RelationshipProperty

if TYPE_CHECKING:
    from models.airline_identifier import AirlineIdentifier
    from models.aircraft_category import AircraftCategory
    from models.pilot_type import PilotType
    from src.user.models import User
    from src.airport.models import Airport
    from models.aircraft import Aircraft

#from models import *
from db.base import Base, SQLModelBase

class Flight_Airport(SQLModelBase, table=True):
    flight_id: int = Field(default=None, foreign_key="flight.id", primary_key=True)
    airport_id: int = Field(default=None, foreign_key="airport.id", primary_key=True)

class Flight(Base, table=True):
    #__tablename__ = "Flight"
    date: date
    aircraftIdentity: str = Field(sa_column=Column(VARCHAR(9), nullable=False))
    departure: time
    arrival: time
    totalFlightDuration: Decimal = Field(sa_column=Column(DECIMAL(6, 2), nullable=False))
    dayLanding: int | None
    nightLanding: int | None
    actualInstrument: Decimal | None = Field(sa_column=Column(DECIMAL(6, 2)))
    simulatedInstrumentUnderHood: Decimal | None = Field(sa_column=Column(DECIMAL(6, 2)))
    atd: Decimal | None = Field(sa_column=Column(DECIMAL(6,2), comment="UND"))
    atdInstrument: Decimal | None = Field(sa_column=Column(DECIMAL(6,2), comment="UND"))
    hold: int | None
    fullFlightSim: Decimal | None = Field(sa_column=Column(DECIMAL(6,2)))
    groundTrainer: Decimal | None = Field(sa_column=Column(DECIMAL(6,2)))
    lineCheck: bool = Field(sa_column=Column(Boolean, default=False))
    crossCountryTime: Decimal | None = Field(sa_column=Column(DECIMAL(6, 2)))
    initialOperatingExperience: bool | None = Field(sa_column=Column(Boolean))
    remarks: str | None = Field(sa_column=Column(VARCHAR(255)))
    approaches: int | None
    approachType: str | None = Field(sa_column=Column(VARCHAR(255), comment="UND"))
    crewMemberName: str = Field(sa_column=Column(VARCHAR(100), nullable=False))
    flightNumber: str = Field(sa_column=Column(VARCHAR(6), nullable=False))
    fileName: str = Field(VARCHAR(50))
    course: str = Field(sa_column=Column(VARCHAR(4), comment="UND"))
    lesson: str = Field(sa_column=Column(VARCHAR(10), comment="UND"))
    status: str = Field(sa_column=Column(VARCHAR(3), comment="UND"))
    instructor: str = Field(sa_column=Column(VARCHAR(10), comment="UND"))
    oral: Decimal = Field(sa_column=Column(DECIMAL(6,2), comment="UND"))
    dtl: Optional[int] = Field(sa_column=Column(Integer, comment="Daytime Landings UND"))
    ntl: Optional[int] = Field(sa_column=Column(Integer, comment="Nighttime Landings UND"))
    timestamp: Optional[datetime] = Field(
        default=func.now(),
        sa_type=TIMESTAMP(timezone=True),
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )
    to_airport_id: int = Field(default=None,foreign_key="airport.id")
    from_airport_id: int = Field(default=None,foreign_key="airport.id")
    aircraft_id: int = Field(default=None,foreign_key="aircraft.id")
    airlineidentifier_id: int = Field(default=None,foreign_key="airlineidentifier.id")
    aircraftcategory_id: int = Field(default=None,foreign_key="aircraftcategory.id")
    pilottype_id: int = Field(default=None, foreign_key="pilottype.id")
    user_id: int = Field(foreign_key="user.id")
    __table_args__ = (UniqueConstraint("date", "departure", "arrival", "totalFlightDuration"),)
    
    to_airport: Optional["Airport"] = Relationship(sa_relationship=RelationshipProperty(
            "Airport",
            primaryjoin="Flight.to_airport_id == Airport.id",
            lazy="joined",
            #uselist=False
        )
    )
    from_airport: Optional["Airport"] = Relationship(sa_relationship=RelationshipProperty(
            "Airport",
            primaryjoin="Flight.from_airport_id == Airport.id",
            lazy="joined",
            #uselist=False
        )
    )
    aircraft: Optional["Aircraft"] = Relationship(
        sa_relationship=RelationshipProperty(
            "Aircraft",
            primaryjoin="Flight.aircraft_id == Aircraft.id",
            lazy="joined",
            #uselist=False
        )
    )
    airline_identifier: Optional["AirlineIdentifier"] = Relationship(
        sa_relationship=RelationshipProperty(
            "AirlineIdentifier", 
            primaryjoin="Flight.airlineidentifier_id == AirlineIdentifier.id",
            lazy="joined",
            #uselist=False
        )
    )
    aircraft_category: "AircraftCategory" = Relationship(
        sa_relationship=RelationshipProperty(
            "AircraftCategory", 
            primaryjoin="Flight.aircraftcategory_id == AircraftCategory.id", 
            lazy="joined",
            #uselist=False
        )
    )
    pilot_type: "PilotType" = Relationship(
        sa_relationship=RelationshipProperty(
            "PilotType", 
            primaryjoin="Flight.pilottype_id == PilotType.id", 
            lazy="joined",
            #back_populates="flights",
            #uselist=True
            #uselist=False
        ),
    )
    user: "User" = Relationship(back_populates="flights", sa_relationship_kwargs={'lazy': 'joined'})
    to_airports: Optional[list["Airport"]] | None = Relationship(
        link_model=Flight_Airport
    )
    #to_airport: Airport | None = Relationship(back_populates="flights_to")

    #to_airport: Airport = Relationship(sa_relationship=relationship(
    #       "Airport",
    #       primaryjoin="Flight.to_airport_id == Airport.id",
    #       lazy="joined",
    #       #uselist=True
    #   )
    #)
#class Flight(FlightBase, table=True):
    #to_airport: "Airport" | None = relationship("Airport", foreign_keys=to_airport_id)

    # to_airport: Mapped[Airport] = Relationship(sa_relationship=relationship(
    #         "Airport",
    #         primaryjoin="Flight.to_airport_id == Airport.id",
    #         lazy="joined",
    #         #uselist=True
    #     )
    # )
        #foreignkey="flight.to_airport_id",
        #back_populates="airports",
        # sa_relationship_kwargs={"lazy": "joined",
        #                         "uselist": False,
        #                         "primaryjoin": "flight.to_airport_id==airport.id"}
        # sa_relationship=RelationshipProperty(
        #     "Airport",
        #     primaryjoin="foreign(Flight.to_airport_id) == Airport.id",
        #     lazy="joined",
        # )
    #)


#class Flight(FlightBase, table=True):
    #pass
    # to_airport: 'Airport' | None = Relationship(sa_relationship=RelationshipProperty(
    #         primaryjoin="Flight.to_airport_id==Airport.id",
    #         lazy="joined",
    #         #uselist=False
    #     )
    # )
    #to_airport: Airport | None = Relationship(back_populates="airports", foreign_keys="to_airport_id")
    #to_airport: Airport | None = Relationship(sa_relationship=RelationshipProperty("Airport"))
#class FlightAll(FlightBase):
    #to_airport: Airport
#     __tablename__ = "Flight"
#     #id: Optional[int]
#     #to_airport_id: int | None = Field(default=None, foreign_key="airport.id")
#     to_airport: Airport | None = Relationship(sa_relationship=RelationshipProperty("Airport", foreign_keys=FlightBase.to_airport_id))

    # from_airport: Optional[Airport]
    # aircraft: Optional[Aircraft]
    # airline_identifier:  Optional[AirlineIdentifier]
    # aircraft_category:  Optional[AircraftCategory]
    # pilot_type:  Optional[PilotType]
    # user:  Optional[User]
    # to_airports: Optional[list[Airport]]
    # to_airport: Airport = Relationship(sa_relationship_kwargs={
    #         "primaryjoin": "Flight.to_airport_id==Airport.id",
    #         "lazy": "joined",
    #         "viewonly": True,
    #     }
    # )
    #     sa_relationship=RelationshipProperty(
    #         "Airport",
    #         primaryjoin="foreign(Flight.to_airport_id) == Airport.id",
    #         lazy="joined"
    #     )
    #     #uselist=False
    # )
    # to_airport: Airport = Relationship(
    #     sa_relationship=RelationshipProperty(
    #         "Airport",
    #         primaryjoin="foreign(Flight.to_airport_id) == Airport.id",
    #         lazy="joined",
    #         #uselist=False
    #     )
    # )
    # to_airport: Optional[Airport] = Relationship(
    #     # sa_relationship=RelationshipProperty(
    #     #     "Airport",
    #     #     primaryjoin="foreign(Flight.to_airport_id) == Airport.id",
    #     #     uselist=False
    #     # )
    #     #link_model=Airport
    #     back_populates="Airport",
    #     #useList=True
    # )
    # from_airport: Optional[Airport] = Relationship(
    #     # sa_relationship=RelationshipProperty(
    #     #     "Airport",
    #     #     primaryjoin="foreign(Flight.from_airport_id) == Airport.id",
    #     #     uselist=False
    #     # )
    #     back_populates="Airport",
    #     #useList=True
    # )
    # aircraft: Aircraft = Relationship(
    #     sa_relationship=RelationshipProperty(
    #         "Aircraft",
    #         primaryjoin="foreign(Flight.aircraft_id) == Aircraft.id",
    #         uselist=False
    #     )
    # )
    # airline_identifier: AirlineIdentifier = Relationship(
    #     sa_relationship=RelationshipProperty(
    #         "AirlineIdentifier", 
    #         primaryjoin="foreign(Flight.airlineidentifier_id) == AirlineIdentifier.id", 
    #         uselist=False
    #     )
    # )
    # aircraft_category: AircraftCategory = Relationship(
    #     sa_relationship=RelationshipProperty(
    #         "AircraftCategory", 
    #         primaryjoin="foreign(Flight.aircraftcategory_id) == AircraftCategory.id", 
    #         uselist=False
    #     )
    # )
    # pilot_type: "PilotType" = Relationship(
    #     sa_relationship=RelationshipProperty(
    #         "PilotType", 
    #         #primaryjoin="foreign(Flight.pilottype_id) == PilotType.id", 
    #         lazy="joined",
    #         back_populates="flights",
    #         #uselist=True
    #         #uselist=False
    #     ),
    # )
    # user: "User" = Relationship(
    #     #back_populates="flights",
    #     sa_relationship=RelationshipProperty("User", lazy="joined",
    #                                           #back_populates="flights"
    #                                           )
    # )

    #Relationship(
        #sa_relationship=RelationshipProperty(
        #    "User", 
        #     primaryjoin="foreign(Flight.user_id) == User.id", 
        #     uselist=True
        #),
        #sa_relationship_kwargs={"lazy": "joined", "uselist": True},
        #back_populates="flights", 
        #sa_relationship_kwargs={"uselist": True}
    #)
    # to_airports: list[Airport] | None = Relationship(
    #     link_model=Flight_Airport
    # )