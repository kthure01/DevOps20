from flask import Blueprint, redirect, session


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/logout', methods=['POST', 'GET'])
def show():
    if 'user_id' in session:
        del session['user_id']
    return redirect('/')
