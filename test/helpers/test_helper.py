from unittest import TestCase
from app.helpers.helper import Helper

class TestHelper(TestCase):
    def test_token(self):
        expected = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImR1bW15IiwiaWQiOjF9.O-Lz9IAv58Soa4Lk0Cr0ccpnMUa-060kvsC6budrH10'
        token = Helper.token(1, 'dummy')
        self.assertEqual(token, expected)
