import unittest
from data_importer.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def test_fetch_mobile_data(self):
        client = APIClient("https://api.restful-api.dev/objects")
        data = client.fetch_mobile_data()
        self.assertIsInstance(data, list)
