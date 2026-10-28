from flightlog import (
    FlightRecord,
    TemperatureSensor,
    HumiditySensor,
    BatterySensor,
    FlightLogError,
)


def main():
    try:
        flight = FlightRecord(
            flight_code="FLIGHT-207",
            position=(9.9312, 76.2673),
            altitude=135.0,
        )

        sensors = [
            TemperatureSensor("TEMP-01"),
            HumiditySensor("HUM-01"),
            BatterySensor("BAT-01"),
        ]

        values = [31.2, 64, 11.8]

        for sensor, value in zip(sensors, values):
            reading = sensor.capture(value)
            flight.record(reading)

        flight.report()

    except FlightLogError as error:
        print("Flight error:", error)


if __name__ == "__main__":
    main()