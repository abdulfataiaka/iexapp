import os
import jwt


class Helper:
    @classmethod
    def amount(cls, value):
        return float(f'{value:.2f}')

    @classmethod
    def token(cls, uid, username):
        try:
            return jwt.encode(
                dict(username=username, id=uid),
                os.getenv('SECRET_KEY'),
                algorithm='HS256'
            ).decode()
        except Exception:
            return None

    @classmethod
    def payload(cls, token):
        try:
            return jwt.decode(
                token.encode(),
                os.getenv('SECRET_KEY'),
                algorithms=['HS256']
            )
        except Exception as ex:
            return None
