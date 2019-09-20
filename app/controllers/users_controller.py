from config.db import db
from flask import Blueprint, request, jsonify
from app.middlewares.auth_middleware import AuthMiddleware


bp = Blueprint('users', __name__, url_prefix='/users')
