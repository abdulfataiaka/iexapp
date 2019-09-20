from config.db import db
from app.models.user import User
from app.helpers.helper import Helper
from flask import Blueprint, request, jsonify
from app.middleware.validator_middleware import ValidatorMiddleware


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['POST'])
@ValidatorMiddleware.login
def login():
    user = request.user  # user binded in middleware to request object
    token = Helper.token(user.id, user.username)
    return jsonify(dict(message='Login was successful', token=token)), 200


@bp.route('/register', methods=['POST'])
@ValidatorMiddleware.register
def register():
    # username and password binded in middleware to request object
    user = User(username=request.username, password=request.password)
    db.session.add(user)
    db.session.commit()
    token = Helper.token(user.id, user.username)
    return jsonify(dict(message='Registration was successful', token=token)), 201
