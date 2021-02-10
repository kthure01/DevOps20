from flask import Flask, request, render_template
from flask_restful import Api, Resource

from calculator import add, subtract, multiply, division

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users': 0
})


class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set": {"num_of_users": new_num}})
        return str("Hello user " + str(new_num))


class Add(Resource):
    def post(self):
        posted_data = request.get_json()
        return add(posted_data)


class Subtract(Resource):
    def post(self):
        return subtract(request.get_json())


class Multiply(Resource):
    def post(self):
        return multiply(request.get_json())


class Divide(Resource):
    def post(self):
        return division(request.get_json())


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")
api.add_resource(Visit, "/hello")


@app.route('/')
def index():
    # return "Hello World!"
    return render_template("index.html")


@app.route('/hello_world')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
