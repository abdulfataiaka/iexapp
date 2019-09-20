from functools import wraps
from app.models.user import User
from flask import request, jsonify
from app.models.stock import Stock
from app.helpers.helper import Helper
from app.helpers.iex_cloud import IEXCloud
from app.helpers.validator import Validator
from werkzeug.security import generate_password_hash, check_password_hash


class ValidatorMiddleware:
    @classmethod
    def login(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username = request.form.get('username')
            password = request.form.get('password')

            if not Validator.username(username):
                message = 'Username should be string of alphabets optionally followed by numbers'
                return jsonify({'error': message}), 400

            user = User.query.filter_by(username=username).first()
            if not user or not check_password_hash(user.password, password):
                message = 'Login credentials are invalid'
                return jsonify({'error': message}), 401

            request.user = user
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def register(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username = request.form.get('username')
            password = request.form.get('password')
            password_confirmation = request.form.get('password_confirmation')

            message = None
            if not Validator.username(username):
                message = 'Username should be string of alphabets optionally followed by numbers'
            elif type(password) is not str or password.strip() == '':
                message = 'Password should be a non empty string'
            elif password != password_confirmation:
                message = 'Passwords provided do not match'

            if message:
                return jsonify({'error': message}), 400
            elif User.query.filter_by(username=username).first():
                message = 'Username taken by an existing user'
                return jsonify({'error': message}), 409

            request.username = username
            request.password = generate_password_hash(password.strip())
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def stock_purchase(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            symbol = request.view_args.get('symbol')
            volume = request.view_args.get('volume')

            stock = Stock.query.filter_by(symbol=symbol).first()
            if not stock:
                return jsonify(dict(error='Symbol provided not yet support')), 404

            price = IEXCloud.price(symbol)
            if not price:
                return jsonify(dict(error='Stock price could not be fetched')), 500

            if volume > stock.volume:
                return jsonify(dict(error='Volume is more than available stock volume')), 400

            total = Helper.amount(volume * price)
            amount = request.user.wallet.amount
            if total > amount:
                return jsonify(dict(error=f'Wallet amount {amount} is less than the total price {total}')), 400

            request.symbol = symbol
            request.volume = volume
            request.stock = stock
            request.price = price
            request.total = total
            return func(*args, **kwargs)
        return wrapper
