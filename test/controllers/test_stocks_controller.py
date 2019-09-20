import requests_mock
from app.models.user import User
from test.base_test import BaseTest
from app.helpers.helper import Helper
from app.helpers.iex_cloud import IEXCloud

class TestStocksController(BaseTest):
    def test_stocks(self):
        response = self.client.get('/stocks/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json)
        self.assertTrue('stocks' in response.json)
        self.assertTrue(len(response.json['stocks']) is 1)

    def test_stock_price_uber(self):
        response = self.client.get('/stocks/uber/price')
        self.assertEqual(response.status_code, 404)

    def test_stock_price_aapl(self):
        with requests_mock.mock() as mock:
            symbol = 'aapl'
            url = IEXCloud.url(f'/stock/{symbol}/price')
            mock.get(url, text='34.5')

            # make request actions
            response = self.client.get(f'/stocks/{symbol}/price')
            self.assertEqual(response.status_code, 200)
            self.assertTrue('price' in response.json)
            self.assertEqual(response.json['price'], 34.5)

    def test_stock_purchase(self):
        self.create_user(username='newuser', password='password', amount=5000)
        token = Helper.token(1, 'newuser')
        headers = dict(Token=token)

        with requests_mock.mock() as mock:
            symbol = 'aapl'
            volume = 10
            url = IEXCloud.url(f'/stock/{symbol}/price')
            mock.get(url, text='100.0')

            # make request actions
            response = self.client.post(f'/stocks/{symbol}/purchase/{volume}', headers=headers)
            self.assertEqual(response.status_code, 200)
            with self.app.app_context():
                amount = User.query.get(1).wallet.amount
            self.assertEqual(amount, 4000)

    def test_stock_sell(self):
        self.create_user(username='newuser', password='password', amount=1000, volume=1000)
        token = Helper.token(1, 'newuser')
        headers = dict(Token=token)

        with requests_mock.mock() as mock:
            symbol = 'aapl'
            volume = 10
            url = IEXCloud.url(f'/stock/{symbol}/price')
            mock.get(url, text='100.0')

            # make request actions
            response = self.client.post(f'/stocks/{symbol}/sell/{volume}', headers=headers)
            self.assertEqual(response.status_code, 200)
            with self.app.app_context():
                amount = User.query.get(1).wallet.amount
            self.assertEqual(amount, 2000)
