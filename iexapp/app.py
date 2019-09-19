from flask import Flask, jsonify
from .controllers.auth import bp as auth

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth)

    @app.route('/')
    def root():
        return jsonify({'message': 'Welcome to iexapp api endpoints'})

    return app
