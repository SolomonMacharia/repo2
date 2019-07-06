
import json
import unittest
from flask_testing import TestCase

from app import create_app
from app.config import TestingConfig



def register_user(self, email, password):
    return self.client.post(
        '/auth/register',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=TestingConfig)
        self.client = self.app.test_client()

    def test_registration(self):
        """Test for user registration"""
        with self.client:
            response = register_user(self, 'solomon@gmail.com', 'python')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == '201')
            self.assertTrue(data['message'] == 'successfully registered')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
