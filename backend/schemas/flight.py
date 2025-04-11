from .base import Base
from datetime import date, time
from schemas.aircraft_category import AircraftCategory
from schemas.pilot_type import PilotType


class Flight(Base):
    id: int | None
    date: date
    aircraftType: str
    aircraftIdentity: str
    fromAirport: str
    toAirport: str
    departure: time
    arrival: time
    dayLanding: int | None
    nightLanding: int | None
    actualInstrument: float | None
    simulatedInstrumentUnderHood: float | None
    hold: int | None
    simulator: float | None
    crossCountryTime: float | None
    totalFlightDuration: float
    initialOperatingExperience: bool | None
    crewMemberName: str
    flightNumber: str
    AirlineIdentifier_id: int
    AircraftCategory_id: int
    PilotType_id: int

    aircraft_category: AircraftCategory
    pilot_type: PilotType
