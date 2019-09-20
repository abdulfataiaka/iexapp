from test.base_test import BaseTest


class TestStocksController(BaseTest):
    def test_stocks(self):
        response = self.client.get('/stocks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.json)
        self.assertTrue('stocks' in response.json)
        self.assertTrue(len(response.json['stocks']) is 1)
