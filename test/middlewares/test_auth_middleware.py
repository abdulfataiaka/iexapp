from test.base_test import BaseTest
from app.helpers.helper import Helper


class TestAuthMiddleware(BaseTest):
    def test_verify_token(self):
        token = Helper.token(1, 'newuser')  # not user with token created using 'newuser'
        headers = dict(Token=token)
        data = dict(amount=10)
        response = self.client.post('/wallets/deposit', data=data, headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertTrue('error' in response.json)
        self.assertEqual(response.json['error'], 'Expects a valid token to be provided')
