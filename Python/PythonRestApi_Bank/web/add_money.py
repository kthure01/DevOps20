from flask import request, jsonify
from flask_restful import Resource

from helper_functions import verify_credentials
from messages import message_amount_invalid, message_amount_added_successfully
from mongodb import update_account_balance, BANK, available_amount
from posted_data import username_password_amount


class AddMoney(Resource):
    def post(self):
        username, password, money = username_password_amount(request.get_json())

        ret_json, error = verify_credentials(username, password)
        if error:
            return jsonify(ret_json)

        if money <= 0:
            return message_amount_invalid()

        cash = available_amount(username)
        money -= 1  # Transaction fee
        # Add transaction fee to bank account
        bank_cash = available_amount(BANK)
        update_account_balance(BANK, bank_cash + 1)

        # Add remaining to user
        update_account_balance(username, cash + money)

        return message_amount_added_successfully()
