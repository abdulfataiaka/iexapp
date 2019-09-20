from config.db import db
from app.models.user_stock import UserStock
from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import AuthMiddleware


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/stocks', methods=['GET'])
@AuthMiddleware.verify_token
def user_stocks():
    stocks = UserStock.query.filter_by(user_id=request.user.id).all()
    stocks = [stock.serialize() for stock in stocks]
    return jsonify(dict(message='User stocks fetch successfully', stocks=stocks)), 200
