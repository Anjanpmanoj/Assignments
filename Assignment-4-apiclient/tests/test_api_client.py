
import unittest
from unittest.mock import Mock, patch

from requests.exceptions import HTTPError

from api_client import fetch_users
from data_parser import parse_users


class TestAPIClient(unittest.TestCase):

    @patch("api_client.requests.get")
    def test_fetch_users_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {"id": 1, "name": "Anu", "email": "anu@example.com"}
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_users()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Anu")
        mock_get.assert_called_once()

    @patch("api_client.requests.get")
    def test_fetch_users_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        with self.assertRaises(HTTPError):
            fetch_users()

    @patch("api_client.requests.get")
    def test_fetch_users_invalid_response(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"message": "not a list"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            fetch_users()

    def test_parse_users(self):
        users = [
            {
                "id": 1,
                "name": " Anu ",
                "email": " anu@example.com ",
                "address": {"city": " Kochi "}
            }
        ]

        df = parse_users(users)

        self.assertEqual(len(df), 1)
        self.assertEqual(df.loc[0, "name"], "Anu")
        self.assertEqual(df.loc[0, "city"], "Kochi")

    def test_parse_users_missing_email(self):
        users = [{"id": 1, "name": "Anu"}]

        with self.assertRaises(ValueError):
            parse_users(users)

    def test_parse_empty_users(self):
        df = parse_users([])

        self.assertTrue(df.empty)
        self.assertEqual(list(df.columns), ["id", "name", "email", "city"])


if __name__ == "__main__":
    unittest.main()
