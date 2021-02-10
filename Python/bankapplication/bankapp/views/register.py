from flask import Blueprint, render_template, request, redirect
from bankapp.logic.session import register_user
from bankapp.forms.RegisterForm import RegisterForm


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/register', methods=['POST', 'GET'])
def show():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = register_user(
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            password=form.password.data,
        )

        if user:
            return redirect('/login?user_id={}'.format(str(user.id)))
    return render_template('register.html', form=form)
