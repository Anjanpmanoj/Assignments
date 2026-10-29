# API Data Explorer

A Python project that fetches user data from a REST API, validates and cleans the JSON response, converts the records into a Pandas DataFrame, and exports the result to CSV.

## Features

- HTTP GET requests using Requests
- HTTP error handling
- JSON response parsing
- Validation of required user fields
- Data cleaning using Pandas
- CSV export
- Unit tests using `unittest` and mocked HTTP responses

## Requirements

- Python 3.11 or compatible
- Requests
- Pandas

## Setup

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The program retrieves sample users from JSONPlaceholder and writes the processed data to `users.csv`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

The tests mock HTTP responses, allowing the client and parser to be tested without relying on a live API.

## Technologies

Python, Requests, REST APIs, HTTP, JSON, Pandas, unittest.
