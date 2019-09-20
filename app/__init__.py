import os
from cli import dbsetup
from config.db import DB
from dotenv import load_dotenv
from flask import Flask, jsonify
from .controllers.auth_controller import bp as auth

load_dotenv()

def create_app(config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # register blueprints
    app.register_blueprint(auth)

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
