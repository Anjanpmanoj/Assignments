
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users(url=API_URL, timeout=10):
    """Fetch user records from a REST API."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Expected the API to return a list of users")

    return data
