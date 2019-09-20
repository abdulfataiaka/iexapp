import os
import requests


class IEXCloud:
    @classmethod
    def get(cls, path):
        token = os.getenv('IEX_CLOUD_TOKEN')
        baseurl = os.getenv('IEX_CLOUD_BASEURL')
        response = requests.get(f'{baseurl}{path}?token={token}')
        return response

    @classmethod
    def price(cls, symbol):
        try:
            response = cls.get(f'/stock/{symbol}/price')
            return float(response.text)
        except:
            return None
