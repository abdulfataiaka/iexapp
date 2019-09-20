import os
import jwt


class Helper:
    @classmethod
    def token(cls, uid, username):
        return jwt.encode(
            dict(username=username, id=uid),
            os.getenv('SECRET_KEY'),
            algorithm='HS256'
        ).decode()
