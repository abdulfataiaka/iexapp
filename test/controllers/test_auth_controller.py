from test.base_test import BaseTest


class TestAuthController(BaseTest):
    def test_login(self):
        response = self.app.post('/auth/login')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Login should be successful')

    def test_register(self):
        data = dict(username="hello", password="password", password_confirmation="password")
        response = self.app.post('/auth/register', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json)
        self.assertTrue('token' in response.json)
