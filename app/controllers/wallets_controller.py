from config.db import db
from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import AuthMiddleware


bp = Blueprint('wallets', __name__, url_prefix='/wallets')


@bp.route('/deposit', methods=['POST'])
@AuthMiddleware.verify_token
def deposit():
    amount = int(request.form.get('amount'))
    wallet = request.user.wallet
    wallet.amount = wallet.amount + amount
    db.session.commit()
    return jsonify(dict(message='Wallet deposit was successful', total=wallet.amount)), 200
