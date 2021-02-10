from flask import Blueprint, render_template, redirect, request
from bankapp.logic.views import login_required
from bankapp.logic.session import get_current_user
from bankapp.logic.account import create_account, get_account
from bankapp.forms.BankAccountForm import BankAccountForm

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/account/<account_id>', methods=['POST', 'GET'])
@bp.route('/account', defaults={'account_id': None}, methods=['POST', 'GET'])
@login_required
def show(account_id=None):
    person = get_current_user()
    account = get_account(account_id) if account_id else None

    form = BankAccountForm(request.form)

    if request.method == 'POST' and form.validate():
        if not account:
            account = create_account(
                name=form.name.data, user=person)

        if account:
            return redirect('/account/{}'.format(str(account.id)))

    return render_template('edit_account.html', form=form, account=account)
