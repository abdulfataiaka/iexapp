from test.base_test import BaseTest


class TestValidatorMiddleware(BaseTest):
    def test_login(self):
        self.create_user(username="newuser", password="password")
        data = dict(username="user", password="password")
        response = self.client.post('/auth/login', data=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['error'], 'Login credentials are invalid')

    def test_register_invalid_username(self):
        data = dict(username="1234user")
        response = self.client.post('/auth/register', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Username should be string of alphabets optionally followed by numbers')

    def test_register_no_password(self):
        data = dict(username="user")
        response = self.client.post('/auth/register', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Password should be a non empty string')

    def test_register_password_mismatch(self):
        data = dict(username="user", password="password")
        response = self.client.post('/auth/register', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Passwords provided do not match')
