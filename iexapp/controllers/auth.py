from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    return 'Login should be successful'

@bp.route('/register', methods=['POST'])
def register():
    return 'Registration should be successful'
