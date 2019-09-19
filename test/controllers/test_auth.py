from unittest import TestCase
from flask import url_for
from iexapp.app import create_app

class TestAuth(TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()

    def test_login(self):
        response = self.app.post('/auth/login')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Login should be successful')

    def test_register(self):
        response = self.app.post('/auth/register')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Registration should be successful')
