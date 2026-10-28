# Drone Monitoring and Flight Record System

## 1. Project Overview

This project implements a simple drone monitoring system using Python. It records flight details such as the drone's location and altitude, and collects measurements from different sensors, including temperature, humidity, and battery voltage.

The project is designed using object-oriented programming principles, with reusable classes, inheritance, composition, custom exceptions, and a modular package structure.

## 2. Project Structure

```text
drone_monitor/
├── main.py
└── flightlog/
    ├── __init__.py
    ├── errors.py
    ├── reading.py
    ├── sensors.py
    └── flight_record.py
```

### File Descriptions

- **main.py:** Entry point of the application. Creates sensors, collects readings, and generates a flight report.
- **errors.py:** Defines custom exceptions for invalid sensor readings and flight details.
- **reading.py:** Contains the `Reading` class, which represents an individual sensor measurement.
- **sensors.py:** Defines the base `Sensor` class and specialized temperature, humidity, and battery sensor classes.
- **flight_record.py:** Contains the `FlightRecord` class, which stores flight information and collected measurements.
- **__init__.py:** Exposes the package classes and exceptions for convenient imports.

## 3. Features

- Stores a flight identifier, geographical coordinates, and altitude.
- Supports temperature, humidity, and battery voltage sensors.
- Validates sensor measurements and flight details.
- Uses custom exceptions to handle invalid inputs.
- Collects multiple sensor readings in a single flight record.
- Generates a readable flight report.
- Uses a modular structure to make the code easier to maintain and extend.

## 4. Object-Oriented Programming Concepts

### Classes and Objects

Classes such as `Sensor`, `Reading`, and `FlightRecord` represent different components of the system. Objects are created from these classes to store and process flight data.

### Inheritance

`TemperatureSensor`, `HumiditySensor`, and `BatterySensor` inherit from the common `Sensor` class. This allows them to reuse common functionality while implementing their own validation rules.

### Composition

A `FlightRecord` contains multiple `Reading` objects. This allows a single flight record to hold measurements collected from different sensors.

### Exception Handling

Custom exceptions, including `InvalidReadingError` and `InvalidFlightError`, are used to report invalid measurements and flight details. These errors are handled in the main application.

### Modular Programming

The project separates related functionality into different modules within the `flightlog` package. This improves code organization, readability, and reusability.

## 5. Requirements

- Python 3.7 or later compatible interpreter
- No external Python packages are required

The code is intended to be compatible with Python 3.7 and later versions.

## 6. How to Run

Open a terminal in the `drone_monitor` project directory and execute:

```bash
python main.py
```

The program creates a flight record, captures sample readings from the sensors, and displays the resulting flight report.

## 7. Sample Output

```text
Flight Report
-------------
Flight: FLIGHT-207
Position: (9.9312, 76.2673)
Altitude: 135.0 m
Measurements:
Temperature = 31.2 C
Humidity = 64 %
Battery = 11.8 V
```

## 8. Possible Improvements

The system could be extended with timestamps for measurements, data storage, JSON export, additional sensor types, automated unit tests, and integration with real drone hardware.

## Conclusion

This project demonstrates how object-oriented programming and modular design can be used to build a reusable drone monitoring system. Separating sensors, readings, flight records, and exception handling makes the implementation easier to understand, maintain, and extend.
