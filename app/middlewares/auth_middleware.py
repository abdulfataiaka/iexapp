from functools import wraps
from app.models.user import User
from app.helpers.helper import Helper
from flask import request, jsonify


class AuthMiddleware:
    @classmethod
    def verify_token(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Token')
            payload = Helper.payload(token)
            if type(payload) is dict and 'username' in payload and 'id' in payload:
                user = User.query.filter_by(username=payload['username'], id=payload['id']).first()
                if user:
                    request.user = user
                    return func(*args, **kwargs)

            return jsonify(dict(error='Expects a valid token to be provided')), 401
        return wrapper
