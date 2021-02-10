from flask import jsonify, request
from flask_restful import Resource

from helper_functions import verify_credentials
from mongodb import get_user_balance
from posted_data import username_password


class Balance(Resource):
    def post(self):
        username, password = username_password(request.get_json())

        ret_json, error = verify_credentials(username, password)
        if error:
            return jsonify(ret_json)

        return get_user_balance(username)
