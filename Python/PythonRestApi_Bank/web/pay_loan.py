from flask import request, jsonify
from flask_restful import Resource

from helper_functions import verify_credentials
from messages import message_loan_paid_fail, message_loan_paid_successfully
from mongodb import available_amount, debt_amount, update_account_balance, update_debt
from posted_data import username_password_amount


class PayLoan(Resource):
    def post(self):
        username, password, money = username_password_amount(request.get_json())

        ret_json, error = verify_credentials(username, password)
        if error:
            return jsonify(ret_json)

        cash = available_amount(username)

        if cash < money:
            return message_loan_paid_fail()

        debt = debt_amount(username)
        update_account_balance(username, cash - money)
        update_debt(username, debt - money)

        return message_loan_paid_successfully()
