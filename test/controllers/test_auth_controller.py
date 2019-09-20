from test.base_test import BaseTest


class TestAuthController(BaseTest):
    def test_login(self):
        data = dict(username="newuser", password="password")
        self.create_user(**data)
        response = self.client.post('/auth/login', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json)
        self.assertTrue('token' in response.json)

    def test_register(self):
        data = dict(username="hello", password="password", password_confirmation="password")
        response = self.client.post('/auth/register', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue('message' in response.json)
        self.assertTrue('token' in response.json)
