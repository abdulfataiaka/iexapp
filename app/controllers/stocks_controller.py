from app.models.stock import Stock
from flask import Blueprint, request, jsonify


bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@bp.route('', methods=['GET'])
def stocks():
    stocks = [stock.serialize() for stock in Stock.query.all()]
    return jsonify(dict(message='Stocks fetched successfully', stocks=stocks)), 200
