from app import app
import unittest
import json


class TestUsers(unittest.TestCase):
    """This class represents the maintenance tracker test case for users"""

    def setUp(self):
        self.client = app.test_client()
        self.data = {
            "user": {
                "username": "paulo",
                "email": "paul@gmail.com",
                "password": "paul1234",
                "confirm_password": "paul1234"
            },
            "auth": {
                "email": "paul@gmail.com",
                "password": "paul1234",
            }

        }

    def test_user_sign_up(self):
        """Test user can register in the app"""
        res = self.client.post('/api/v1/users',data=json.dumps(dict(self.data["user"])),
        content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_empty_field(self):
        """Check a user wont give empty field while signing up"""
        self.data["user"]["username"] = ""
        res = self.client.post('/api/v1/users',data=json.dumps(dict(self.data["user"])),
        content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_confirm_password(self):
        """Test password and confirm password match"""
        self.data["user"]["confirm_password"] = "random"
        res = self.client.post(
            '/api/v1/users',
            data=json.dumps(dict(self.data["user"])),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 400)

    def test_unregistered_user_cannot_login(self):
        """Test unregistered user cannot Login the app"""
        res = self.client.post('/api/v1/login', data=self.data["auth"])
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()