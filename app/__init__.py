import os
from cli import dbsetup
from config.db import DB
from dotenv import load_dotenv
from flask import Flask, jsonify
from app.controllers.auth_controller import bp as auth
from app.controllers.users_controller import bp as users
from app.controllers.stocks_controller import bp as stocks
from app.controllers.wallets_controller import bp as wallets

load_dotenv()

def create_app(config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(stocks)
    app.register_blueprint(wallets)

    # setting up database
    dburl = os.getenv('DATABASE_URL')
    if config is not None:
        dburl = config['dburl']
    DB.init(app, dburl)

    # register app commands
    app.cli.add_command(dbsetup)

    @app.route('/')
    def root():
        return jsonify({'message': 'Welcome to iexapp api endpoints'})

    return app
