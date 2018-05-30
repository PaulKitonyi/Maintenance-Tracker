from app import create_app
import unittest
import os
import json

class MaintenanceTrackerTestCase(unittest.TestCase):
    """This class represents the maintenance tracker test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.request = {
            "device_type": "Printer",
            "request_type": "Repair",
            "department": "Accounts",
            "description": "Not working",
            }

    def test_api_can_create_request(self):
        """Test POST request"""
        res = self.client.post('/users/requests', data=self.request)
        self.assertEqual(res.status_code, 201)

    def test_api_can_get_all_requests(self):
        """Test GET request"""
        res = self.client.get('/users/requests')
        self.assertEqual(res.status_code, 200)

    def test_api_can_get_single_request(self):
        """Test GET request by id"""
        res = self.client.get('/users/requests/1')
        self.assertEqual(res.status_code, 200)

    def test_api_can_edit_request(self):
        """Test PUT request"""
        res = self.client.put('/users/requests/1', data=self.request)
        self.assertEqual(res.status_code, 200)

    def test_api_can_delete_request(self):
        """Test DELETE request"""
        res = self.client.delete('/users/request/1')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()