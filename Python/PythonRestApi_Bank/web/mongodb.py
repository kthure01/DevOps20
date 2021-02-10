from flask import jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client.MoneyManagementDB
users = db["Users"]

USERNAME = "Username"
PASSWORD = "Password"
OWN = "Own"
DEPT = "Debt"
SET = "$set"
ID = "_id"
BANK = "BANK"


def user_exist(username) -> bool:
    """
    Check if username exists

    :param username:
    :return: True of False
    """
    if users.find({USERNAME: username}).count() == 0:
        return False
    else:
        return True


def create_new_account(username, hashed_password):
    """
    Adds user to database

    :param username:
    :param hashed_password:
    :return: Nothing
    """
    users.insert({
        USERNAME: username,
        PASSWORD: hashed_password,
        OWN: 0,
        DEPT: 0
    })


def get_hashed_password(username) -> bytes:
    """
    Takes the username and returns the hashed password

    :param username:
    :return: Hashed password
    """
    hashed_password = users.find({
        USERNAME: username
    })[0][PASSWORD]

    return hashed_password


def available_amount(username) -> int:
    return users.find({
        USERNAME: username
    })[0][OWN]


def debt_amount(username) -> int:
    return users.find({
        USERNAME: username
    })[0][DEPT]


def update_account_balance(username, balance):
    users.update({
        USERNAME: username
    }, {
        SET: {
            OWN: balance
        }
    })


def update_debt(username, balance):
    users.update({
        USERNAME: username
    }, {
        SET: {
            DEPT: balance
        }
    })


def get_user_balance(username):
    retJson = users.find({
        USERNAME: username
    }, {
        PASSWORD: 0,  # projection
        ID: 0
    })[0]

    return jsonify(retJson)


def delete_user_account(username):
    users.delete_one({
        USERNAME: username
    })


def get_all_users():
    retJson = users.find({})

    return jsonify(retJson)
