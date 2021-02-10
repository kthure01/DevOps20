from flask import Blueprint, render_template, request, redirect
from bankapp.logic.session import login
from bankapp.forms.LoginForm import LoginForm


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/login', methods=['POST', 'GET'])
def show():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = login(
            email=form.email.data,
            password=form.password.data
        )

        if user:
            return redirect('/profile/{}'.format(str(user.id)))
    return render_template('login.html', form=form)
