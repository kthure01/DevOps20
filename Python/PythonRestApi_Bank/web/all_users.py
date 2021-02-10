from flask_restful import Resource

from mongodb import get_all_users


class AllUsers(Resource):
    def get(self):
        return get_all_users()
