import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DB:
    @classmethod
    def config(cls):
        return {
            'SQLALCHEMY_DATABASE_URI': os.getenv('DATABASE_URL'),
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        }

    @classmethod
    def init(cls, app):
        with app.app_context():
            app.config.from_mapping(cls.config())
            db.init_app(app)

    @classmethod
    def setup(cls):
        db.drop_all()
        db.create_all()
