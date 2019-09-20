import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DB:
    @classmethod
    def config(cls, dburl):
        return {
            'SQLALCHEMY_DATABASE_URI': dburl,
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        }

    @classmethod
    def init(cls, app, dburl):
        with app.app_context():
            app.config.from_mapping(cls.config(dburl))
            db.init_app(app)
