from test.base_test import BaseTest
from app.helpers.helper import Helper


class TestUsersController(BaseTest):
    def test_user_stocks(self):
        self.create_user(username='newuser', password='password')
        token = Helper.token(1, 'newuser')
        headers = dict(Token=token)
        response = self.client.get('/users/stocks', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('stocks' in response.json)

    def test_user_transactions(self):
        self.create_user(username='newuser', password='password')
        token = Helper.token(1, 'newuser')
        headers = dict(Token=token)
        response = self.client.get('/users/transactions', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('transactions' in response.json)
