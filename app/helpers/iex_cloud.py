import os
import requests


class IEXCloud:
    @classmethod
    def url(cls, path):
        token = os.getenv('IEX_CLOUD_TOKEN')
        baseurl = os.getenv('IEX_CLOUD_BASEURL')
        return f'{baseurl}{path}?token={token}'

    @classmethod
    def price(cls, symbol):
        try:
            url = cls.url(f'/stock/{symbol}/price')
            response = requests.get(url)
            return float(response.text)
        except Exception:
            return None
