import datetime
from app.models.stock import Stock
from app.helpers.iex_cloud import IEXCloud
from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import AuthMiddleware
from app.middlewares.validator_middleware import ValidatorMiddleware
from app.controllers.helpers.stocks_controller_helper import StocksControllerHelper


bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@bp.route('/', methods=['GET'])
def stocks():
    stocks = [stock.serialize() for stock in Stock.query.all()]
    return jsonify(dict(message='Stocks fetched successfully', stocks=stocks)), 200


@bp.route('/<symbol>/price', methods=['GET'])
def stock_price(symbol):
    if not Stock.query.filter_by(symbol=symbol).first():
        return jsonify(dict(error='Symbol provided not yet support')), 404

    price = IEXCloud.price(symbol)
    if not price:
        return jsonify(dict(error='Stock price could not be fetched')), 500
    return jsonify(dict(message='Stock price fetched successfully', price=price)), 200


@bp.route('/<symbol>/purchase/<int:volume>', methods=['POST'])
@AuthMiddleware.verify_token
@ValidatorMiddleware.stock_purchase
def stock_purchase(symbol, volume):
    StocksControllerHelper.finalize_purchase(request)

    data = dict(
        symbol=request.symbol,
        volume=request.volume,
        wallet_amount=request.user.wallet.amount,
        total_price=request.total
    )

    return jsonify(dict(message=f'Stock purchase successful', data=data))
