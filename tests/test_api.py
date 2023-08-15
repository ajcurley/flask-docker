import unittest

from flask_docker.app import app


class TestAPI(unittest.TestCase):
    """API unit tests"""

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_status(self):
        """Test the /status endpoint"""
        resp = self.client.get("/status")
        self.assertEqual(resp.status_code, 200)

    def test_randomize_default(self):
        """Test the /randomize endpoint with default arguments"""
        resp = self.client.get("/randomize")
        self.assertEqual(resp.status_code, 200)
        value = resp.json["detail"]
        self.assertTrue(value >= 0 and value <= 100)

    def test_randomize_parameters(self):
        """Test the /randomize endpoint with parameters"""
        resp = self.client.get("/randomize?lower=50&upper=50")
        self.assertEqual(resp.status_code, 200)
        value = resp.json["detail"]
        self.assertEqual(value, 50)

    def test_randomize_parameters_invalid_type(self):
        """Test the /randomize endpoint with invalid type parameters"""
        resp = self.client.get("/randomize?lower=invalid")
        self.assertEqual(resp.status_code, 400)

    def test_randomize_parameters_invalid_range(self):
        """Test the /randomize endpoint with an invalid range parameters"""
        resp = self.client.get("/randomize?lower=50&upper=20")
        self.assertEqual(resp.status_code, 400)
