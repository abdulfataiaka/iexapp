import os
from config.db import db
from app import create_app
from unittest import TestCase
from app.models.user import User
from app.models.wallet import Wallet
from app.models.stock import Stock
from app.models.user_stock import UserStock
from werkzeug.security import generate_password_hash

class BaseTest(TestCase):
    def setUp(self):
        self.app = create_app(dict(dburl=os.getenv('TEST_DATABASE_URL')))
        self.app.testing = True
        self.client = self.app.test_client()
        self.dbsetup()
        self.dbseed()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def dbseed(self):
        self.seed_stocks()

    def dbsetup(self):
        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def create_user(self, username, password, amount=0, volume=0):
        with self.app.app_context():
            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()

            wallet = Wallet(user_id=user.id, amount=amount)
            stock = UserStock(user_id=user.id, symbol='aapl', volume=volume)
            db.session.add(wallet)
            db.session.add(stock)
            db.session.commit()


    def seed_stocks(self):
        with self.app.app_context():
            apple = Stock(symbol='aapl', volume=100)
            db.session.add(apple)
            db.session.commit()
