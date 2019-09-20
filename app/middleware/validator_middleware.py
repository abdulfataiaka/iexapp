from flask import request, jsonify
from werkzeug.security import generate_password_hash

from app.models.user import User
from app.helpers.validator import Validator


class ValidatorMiddleware:
    @classmethod
    def register(cls, func):
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
            elif User.query.filter_by(username=username).first():
                message = 'Username taken by an existing user'

            if not message:
                request.username = username
                request.password = generate_password_hash(password.strip())
                return func(*args, **kwargs)

            return jsonify({'error': message}), 400
        return wrapper
