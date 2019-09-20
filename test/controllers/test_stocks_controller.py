import requests_mock
from test.base_test import BaseTest
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
