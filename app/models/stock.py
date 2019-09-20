from config.db import db


class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(5), unique=True, nullable=False)
    volume = db.Column(db.Integer, default=0, nullable=False)

    def serialize(self):
        return dict(
            id=self.id,
            symbol=self.symbol,
            volume=self.volume
        )
