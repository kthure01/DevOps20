from flask import Blueprint, render_template, redirect
from bankapp.models.Person import Person
from bankapp.logic.views import login_required
from bankapp.logic.session import get_current_user
from bson.objectid import ObjectId

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/profile/<user_id>')
@bp.route('/profile', defaults={'user_id': None})
@login_required
def show(user_id=None):
    person = Person.objects(id=ObjectId(user_id)).get() if user_id else\
        get_current_user()

    if not person:
        return redirect('/')

    return render_template('profile.html', person=person)
