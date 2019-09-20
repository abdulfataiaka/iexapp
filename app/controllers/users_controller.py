from config.db import db
from app.models.user_stock import UserStock
from app.models.transaction import Transaction
from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import AuthMiddleware


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/stocks', methods=['GET'])
@AuthMiddleware.verify_token
def user_stocks():
    stocks = UserStock.query.filter_by(user_id=request.user.id).all()
    stocks = [stock.serialize() for stock in stocks]
    return jsonify(dict(message='User stocks fetched successfully', stocks=stocks)), 200


@bp.route('/transactions', methods=['GET'])
@AuthMiddleware.verify_token
def user_transactions():
    records = Transaction.query.filter_by(user_id=request.user.id).all()
    records = [record.serialize() for record in records]
    return jsonify(dict(message='User transactions fetched successfully', transactions=records)), 200
