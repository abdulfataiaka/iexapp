from config.db import DB
from cli import dbsetup
from dotenv import load_dotenv
from flask import Flask, jsonify
from .controllers.auth import bp as auth

load_dotenv()

def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(auth)

    # setting up database
    DB.init(app)
    app.cli.add_command(dbsetup)

    @app.route('/')
    def root():
        return jsonify({'message': 'Welcome to iexapp api endpoints'})

    return app
