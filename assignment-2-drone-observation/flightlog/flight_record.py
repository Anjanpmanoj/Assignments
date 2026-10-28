from numbers import Real

from .errors import InvalidFlightError
from .reading import Reading


class FlightRecord:
    """Stores flight information and collected measurements."""

    def __init__(self, flight_code, position, altitude):
        if not isinstance(flight_code, str) or not flight_code.strip():
            raise InvalidFlightError("Flight code is required.")

        latitude, longitude = position

        if (
            isinstance(latitude, bool)
            or not isinstance(latitude, Real)
            or not -90 <= latitude <= 90
        ):
            raise InvalidFlightError("Invalid latitude.")

        if (
            isinstance(longitude, bool)
            or not isinstance(longitude, Real)
            or not -180 <= longitude <= 180
        ):
            raise InvalidFlightError("Invalid longitude.")

        if isinstance(altitude, bool) or not isinstance(altitude, Real):
            raise InvalidFlightError("Altitude must be numeric.")

        self.flight_code = flight_code
        self.position = (latitude, longitude)
        self.altitude = altitude
        self.measurements = []

    def record(self, reading):
        if not isinstance(reading, Reading):
            raise InvalidFlightError(
                "Only valid Reading objects can be recorded."
            )

        self.measurements.append(reading)

    def report(self):
        print("\nFlight Report")
        print("-------------")
        print("Flight:", self.flight_code)
        print("Position:", self.position)
        print("Altitude:", self.altitude, "m")
        print("Measurements:")

        if not self.measurements:
            print("No measurements collected.")
            return

        for item in self.measurements:
            print(item.describe())