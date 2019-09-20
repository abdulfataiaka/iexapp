import os
import jwt
from config.db import db
from flask import Blueprint, request, jsonify
from app.models.user import User
from app.middleware.validator_middleware import ValidatorMiddleware

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    return 'Login should be successful'

@bp.route('/register', methods=['POST'])
@ValidatorMiddleware.register
def register():
    user = User(username=request.username, password=request.password)
    db.session.add(user)
    db.session.commit()
    token = jwt.encode({'username': user.username, 'id': user.id }, os.getenv('SECRET_KEY'), algorithm='HS256')

    return jsonify({
        'message': 'Registration was successful',
        'token': token.decode()
    })
