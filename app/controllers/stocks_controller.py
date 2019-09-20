from app.models.stock import Stock
from app.helpers.iex_cloud import IEXCloud
from flask import Blueprint, request, jsonify


bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@bp.route('/', methods=['GET'])
def stocks():
    stocks = [stock.serialize() for stock in Stock.query.all()]
    return jsonify(dict(message='Stocks fetched successfully', stocks=stocks)), 200

@bp.route('/<symbol>/price', methods=['GET'])
def stock_price(symbol):
    if not Stock.query.filter_by(symbol=symbol).first():
        return jsonify(dict(message='Symbol provided not yet support')), 404

    price = IEXCloud.price(symbol)
    if not price:
        return jsonify(dict(message='Stock price could not be fetched')), 500
    return jsonify(dict(message='Stock price fetched successfully', price=price)), 200
