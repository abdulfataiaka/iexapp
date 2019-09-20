from functools import wraps
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import User
from app.helpers.validator import Validator


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
