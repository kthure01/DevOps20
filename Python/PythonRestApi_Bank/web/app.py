from flask import Flask, render_template
from flask_restful import Api

from add_money import AddMoney
from all_users import AllUsers
from balance import Balance
from delete_user import DeleteUser
from pay_loan import PayLoan
from register import Register
from take_loan import TakeLoan
from transfer import Transfer

app = Flask(__name__)
api = Api(app)

api.add_resource(Register, '/register')
api.add_resource(AddMoney, '/add')
api.add_resource(Transfer, '/transfer')
api.add_resource(Balance, '/balance')
api.add_resource(TakeLoan, '/takeloan')
api.add_resource(PayLoan, '/payloan')
api.add_resource(DeleteUser, '/delete')
api.add_resource(AllUsers, '/all')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
