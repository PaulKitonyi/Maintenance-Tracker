from app import app
import unittest
import json

class MaintenanceTrackerTestCase(unittest.TestCase):
    """This class represents the maintenance tracker test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client()
        self.request = {"device type" : "Laptops", "request type" : "repair", "department":"Accounts", "description":"display issuessassdssdfd"}

    def test_api_can_create_request(self):
        """Test POST request"""
        res = self.client.post('/users/requests', data=json.dumps(self.request), content_type='application/json')
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
        self.client.post('/users/requests', data=json.dumps(self.request), content_type='application/json')
        res = self.client.put('/users/requests/1', data=json.dumps(self.request), content_type='application/json')
        print(res.get_data())
        self.assertEqual(res.status_code, 200)

    def test_api_can_delete_request(self):
        """Test DELETE request"""
    
        res = self.client.delete('/users/requests/1',content_type='application/json')
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()