from mongoengine import *
from bankapp.models.BankAccount import BankAccount

class Person(Document):
    firstname = StringField()
    lastname = StringField()
    password = StringField()
    email = StringField()
    accounts = ListField(ReferenceField(BankAccount))
