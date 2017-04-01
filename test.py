import os
import unittest
import flaskapi
import requests
import json

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.json(), {'hello': 'world'})


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = flaskapi.app.test_client()

    def test_api_source(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data()), {'hello': 'world'})


if __name__ == "__main__":
    unittest.main()