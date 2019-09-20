from config.db import db
from app.models.stock import Stock

class StocksSeeder:
    @classmethod
    def run(cls):
        uber = Stock(symbol='uber', volume=5000000)
        apple = Stock(symbol='aapl', volume=5000000)

        db.session.add(uber)
        db.session.add(apple)
        db.session.commit()
