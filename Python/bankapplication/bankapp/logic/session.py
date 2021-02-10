from bankapp.models.Person import Person
from bankapp.models.BankAccount import BankAccount
from flask import session
from bson.objectid import ObjectId


def register_user(email, firstname, lastname, password):

    account = BankAccount()
    account.save()

    person = Person(email=email, firstname=firstname,
                    lastname=lastname,
                    password=password, accounts=[account])

    person.save()

    return person


def login(email, password):
    person = Person.objects(email=email).get()

    if not person:
        return False

    if password != person.password:
        return False

    session['user_id'] = str(person.id)

    return person


def is_loggedin():
    return 'user_id' in session


def get_current_user():
    if not is_loggedin():
        return None

    return Person.objects(id=ObjectId(session['user_id'])).get()
