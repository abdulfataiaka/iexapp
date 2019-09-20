import os
from config.db import DB
from app import create_app
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        app = create_app(dict(dburl=os.getenv('TEST_DATABASE_URL')))
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            DB.setup()

    def tearDown(self):
        pass
