from app import app 
from flask import Flask
from flask_testing import TestCase


class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000', content_type='html/text')
        self.assertTrue(b'default page:' in response.data) 


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = flaskapi.app.test_client()

    def test_source(self):
        response = self.app.get('/todo/api/v1.0/countries?target=source')
        self.assertis(json.loads(response.get_data()), [{"name": "United Kingdom", "isoCode": "GB"},{"name": "Ireland", "isoCode": "IE"}])
    
    def test_destination(self):
        response = self.app.get('/todo/api/v1.0/countries?target=destination')
        self.assertis(json.loads(response.get_data()), [ {"name": "Spain", "isoCode": "ES"},{"name": "France", "isoCode": "FR"}])


if __name__ == "__main__":
    unittest.main()