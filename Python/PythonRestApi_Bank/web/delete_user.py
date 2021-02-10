from flask import request
from flask_restful import Resource

from helper_functions import verify_account
from messages import message_user_dont_exist, message_user_deleted
from mongodb import delete_user_account
from posted_data import username_password


class DeleteUser(Resource):
    def delete(self):
        username, password = username_password(request.get_json())

        existing_user = verify_account(username, password)

        if not existing_user:
            return message_user_dont_exist()

        delete_user_account(username)
        return message_user_deleted()
