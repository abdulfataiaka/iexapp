from config.db import db


class UserStock(db.Model):
    __tablename__ = 'user_stocks'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(5), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            symbol=self.symbol,
            volume=self.volume
        )
