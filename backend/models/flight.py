from datetime import date, time
from sqlmodel import (
    Column,
    Integer,
    VARCHAR,
    DATE,
    Boolean,
    DECIMAL,
    ForeignKey,
    TIMESTAMP,
    TIME,
    func,
    Relationship
)
from db.base import Base

class Flight(Base,table=True):
    idFlight: int = Column(Integer, primary_key=True)
    date: date = Column(DATE, nullable=False) # type: ignore
    aircraftType: str = Column(VARCHAR(3), nullable=False)
    aircraftIdentity: str = Column(VARCHAR(9), nullable=False)
    fromAirport: str = Column(VARCHAR(3), nullable=False)
    toAirport: str = Column(VARCHAR(3), nullable=False)
    departure: time = Column(TIME)
    arrival: time = Column(TIME)
    dayLanding: int = Column(Integer)
    nightLanding: int = Column(Integer)
    actualInstrument: float = Column(DECIMAL(6, 2))
    simulatedInstrumentUnderHood: float = Column(DECIMAL(6, 2))
    hold: int = Column(Integer)
    simulator: float = Column(DECIMAL(6, 2))
    crossCountryTime: float = Column(DECIMAL(6, 2))
    totalFlightDuration: float = Column(DECIMAL(6, 2), nullable=False)
    initialOperatingExperience: bool = Column(Boolean)
    crewMemberName: str = Column(VARCHAR(100), nullable=False)
    flightNumber: str = Column(VARCHAR(4), nullable=False)
    timestamp: timestamp = Column( # type: ignore
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        default=func.now(),
        onupdate=func.now(),
    )
    AirlineIdentifier_idAirlineIdentifier: int = Column(
        Integer, ForeignKey("AirlineIdentifier.idAirlineIdentifier"), nullable=False
    )

    AircraftCategory_idAircraftCategory: int = Column(
        Integer, ForeignKey("AircraftCategory.idAircraftCategory"), nullable=False
    )
    PilotType_idPilotType: int = Column(Integer, ForeignKey("PilotType.idPilotType"), nullable=False)
    User_idUser: int = Column(Integer, ForeignKey("User.idUser"), nullable=False)

    airline_identifier = Relationship(
       sa_relationship_kwargs={"primaryjoin":"Flight.AirlineIdentifier_idAirlineIdentifier==AirlineIdentifier.idAirlineIdentifier", "lazy": "joined"}
    )
    aircraft_category = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Flight.AircraftCategory_idAircraftCategory=AircraftCategory.idAircraftCategory","lazy":"joined"}
    )
    pilot_type = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Flight.PilotType_idPilotType=PilotType.idPilotType", "lazy":"joined"}
    )
    user = Relationship(
        sa_relationship_kwargs={"primaryjoin":"Flight.User_idUser=User.idUser","lazy":"joined"}
    )
