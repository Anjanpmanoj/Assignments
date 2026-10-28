from numbers import Real

from .errors import InvalidReadingError
from .reading import Reading


class Sensor:
    """Base class for drone sensors."""

    def __init__(self, sensor_id, label, unit):
        if not isinstance(sensor_id, str) or not sensor_id.strip():
            raise InvalidReadingError("Sensor ID is required.")

        self.sensor_id = sensor_id
        self.label = label
        self.unit = unit

    def capture(self, value):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise InvalidReadingError(
                "Measurement must be numeric."
            )

        self.validate(value)
        return Reading(self.label, value, self.unit)

    def validate(self, value):
        """Override this method for sensor-specific rules."""
        pass


class TemperatureSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, "Temperature", "C")

    def validate(self, value):
        if not -80 <= value <= 80:
            raise InvalidReadingError(
                "Temperature is outside the supported range."
            )


class HumiditySensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, "Humidity", "%")

    def validate(self, value):
        if not 0 <= value <= 100:
            raise InvalidReadingError(
                "Humidity must be between 0 and 100."
            )


class BatterySensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, "Battery", "V")

    def validate(self, value):
        if value < 0:
            raise InvalidReadingError(
                "Battery voltage cannot be negative."
            )