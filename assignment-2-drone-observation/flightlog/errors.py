class FlightLogError(Exception):
    """Base exception for flight log errors."""


class InvalidReadingError(FlightLogError):
    """Raised when a sensor measurement is invalid."""


class InvalidFlightError(FlightLogError):
    """Raised when flight details are invalid."""