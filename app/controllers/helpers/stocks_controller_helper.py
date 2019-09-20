from config.db import db
from datetime import datetime
from app.helpers.helper import Helper
from app.models.user_stock import UserStock
from app.models.transaction import Transaction


class StocksControllerHelper:
    @classmethod
    def finalize_purchase(cls, request):
        user = request.user
        stock = request.stock
        symbol = request.symbol
        volume = request.volume
        price = request.price
        total = request.total

        request.user.wallet.amount = Helper.amount(user.wallet.amount - total)
        request.stock.volume = stock.volume - volume
        db.session.commit()
        cls.update_user_stock(user.id, symbol, volume)
        cls.update_transaction(user.id, symbol, volume, price, total, 'purchase')

    @classmethod
    def finalize_sell(cls, request):
        user = request.user
        stock = request.stock
        price = request.price
        total = request.total
        symbol = request.symbol
        volume = request.volume
        user_stock = request.user_stock

        request.user.wallet.amount = Helper.amount(user.wallet.amount + total)
        request.stock.volume = stock.volume + volume
        request.user_stock.volume = user_stock.volume - volume
        db.session.commit()
        cls.update_transaction(user.id, symbol, volume, price, total, 'sell')


    @classmethod
    def update_user_stock(cls, user_id, symbol, volume):
        user_stock = UserStock.query.filter_by(symbol=symbol, user_id=user_id).first()
        if user_stock is None:
            user_stock = UserStock(user_id=user_id, symbol=symbol, volume=volume)
            db.session.add(user_stock)
        else:
            user_stock.volume = user_stock.volume + volume
        db.session.commit()

    @classmethod
    def update_transaction(cls, user_id, symbol, volume, price, total, txttype):
        transaction = Transaction(
            user_id=user_id,
            symbol=symbol,
            volume=volume,
            stock_price=price,
            total_price=total,
            datetime=datetime.now(),
            txntype=txttype
        )
        db.session.add(transaction)
        db.session.commit()
