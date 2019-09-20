import os
from config.db import DB, db
from app import create_app
from unittest import TestCase
from app.models.user import User
from werkzeug.security import generate_password_hash

class BaseTest(TestCase):
    def setUp(self):
        self.app = create_app(dict(dburl=os.getenv('TEST_DATABASE_URL')))
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            DB.setup()

    def tearDown(self):
        pass

    def create_user(self, username, password):
        with self.app.app_context():
            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
