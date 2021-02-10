from mongoengine import *


DEFAULT_ACCOUNT_NAME = 'Primary'


class BankAccount(Document):
    name = StringField(default=DEFAULT_ACCOUNT_NAME)
    holding = IntField(default=0)
