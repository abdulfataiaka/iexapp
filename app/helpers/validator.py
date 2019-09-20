import re


class Validator:
    @classmethod
    def username(cls, value):
        return type(value) is str and (not not re.match('^[a-z]+[0-9]*$', value))
