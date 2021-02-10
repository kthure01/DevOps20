from flask import request
from flask_restful import Resource

from messages import message_signup_success, message_user_fail
from encryption import generate_hashed_password
from mongodb import user_exist, create_new_account
from posted_data import username_password


class Register(Resource):
    def post(self):
        username, password = username_password(request.get_json())

        if user_exist(username):
            return message_user_fail()

        hashed_password = generate_hashed_password(password)
        create_new_account(username, hashed_password)

        return message_signup_success()
