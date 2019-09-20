from config.db import db


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(5), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    stock_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.TIMESTAMP, nullable=False)
    txntype = db.Column(db.String, nullable=False)

    def serialize(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            symbol=self.symbol,
            volume=self.volume,
            stock_price=self.stock_price,
            total_price=self.total_price,
            datetime=self.datetime,
            txntype=self.txntype
        )
