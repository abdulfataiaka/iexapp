from unittest import TestCase
from app.helpers.validator import Validator

class TestValidator(TestCase):
    def test_username(self):
        self.assertTrue(Validator.username('user'))
        self.assertTrue(Validator.username('user12345'))
        self.assertFalse(Validator.username('12345'))
        self.assertFalse(Validator.username('12345user'))
