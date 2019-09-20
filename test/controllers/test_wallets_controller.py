from test.base_test import BaseTest
from app.helpers.helper import Helper


class TestWalletController(BaseTest):
    def test_deposit(self):
        self.create_user(username='newuser', password='password')
        token = Helper.token(1, 'newuser')
        headers = dict(Token=token)
        data = dict(amount=1000)
        response = self.client.post('/wallets/deposit', data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('total' in response.json)
        self.assertEqual(response.json['total'], 1000)
