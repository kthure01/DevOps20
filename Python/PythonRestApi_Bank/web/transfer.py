from flask import jsonify, request
from flask_restful import Resource

from helper_functions import verify_credentials
from messages import message_amount_insufficient, message_amount_invalid, message_user_dont_exist, \
    message_amount_added_successfully
from mongodb import available_amount, user_exist, update_account_balance, BANK
from posted_data import username_password_to_amount


class Transfer(Resource):
    def post(self):
        username, password, to, money = username_password_to_amount(request.get_json())

        ret_json, error = verify_credentials(username, password)
        if error:
            return jsonify(ret_json)

        cash = available_amount(username)
        if cash <= 0:
            return message_amount_insufficient()

        if money <= 0:
            return message_amount_invalid()

        if not user_exist(to):
            return message_user_dont_exist()

        cash_from = available_amount(username)
        cash_to = available_amount(to)
        bank_cash = available_amount(BANK)

        update_account_balance(BANK, bank_cash + 1)
        update_account_balance(to, cash_to + money - 1)
        update_account_balance(username, cash_from - money)

        return message_amount_added_successfully()
