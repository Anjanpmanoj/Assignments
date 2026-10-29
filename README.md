\# Engineering Assignments



This repository contains two Python assignments covering data conversion and object-oriented programming.



\## Assignment 1: CSV to JSON



\*\*Folder:\*\* `assignment-1-csv-to-json/`



This assignment contains a Python script for converting CSV data into JSON format.



Files:

\- `csvtojson.py` — Python script.

\- `students.csv` — Input data.

\- `students.json` — JSON output.



\## Assignment 2: Drone Observation



\*\*Folder:\*\* `assignment-2-drone-observation/`



This assignment organises drone observation and sensor-related functionality into reusable Python modules.



Key files and modules:

\- `main.py` — Main entry point.

\- `flightlog/flight\_record.py` — Flight record module.

\- `flightlog/reading.py` — Reading module.

\- `flightlog/sensors.py` — Sensor module.

\- `flightlog/errors.py` — Error-handling module.



\## Technologies



\- Python

\- CSV and JSON

\- Object-oriented programming

\- Modular code organisation



\## Repository Structure



```text

Assignments/

├── README.md

├── assignment-1-csv-to-json/

│   ├── csvtojson.py

│   ├── students.csv

│   └── students.json

└── assignment-2-drone-observation/

&#x20;   ├── README.md

&#x20;   ├── main.py

&#x20;   └── flightlog/

&#x20;       ├── \_\_init\_\_.py

&#x20;       ├── errors.py

&#x20;       ├── flight\_record.py

&#x20;       ├── reading.py

&#x20;       └── sensors.py

```
## Assignment 4: API Client, Data Parser and Unit Tests

**Folder:** `Assignment-4-apiclient/`

A Python application that retrieves user data from a REST API, parses and validates JSON responses, cleans data using Pandas, and exports the results to CSV.

**Features:**
- HTTP GET requests using the Requests library
- REST API integration and JSON parsing
- Data validation and cleaning with Pandas
- Error handling for unsuccessful HTTP responses
- Unit tests using `unittest` and mocked HTTP responses

**Key files:**
- `api_client.py` — Fetches data from the API.
- `data_parser.py` — Validates and cleans user records.
- `main.py` — Runs the application and exports the data.
- `tests/test_api_client.py` — Tests the API client and parser.
- `requirements.txt` — Lists Python dependencies.

**Technologies:** Python, Requests, REST APIs, HTTP, JSON, Pandas, unittest.

**Run the project:**

```bash
python main.py
```

**Run the tests:**

```bash
python -m unittest discover -s tests -v
```




