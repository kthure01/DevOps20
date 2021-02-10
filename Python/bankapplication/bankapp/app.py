from flask import Flask

from bankapp.views.index import bp as index_bp
from bankapp.views.login import bp as login_bp
from bankapp.views.logout import bp as logout_bp
from bankapp.views.register import bp as register_bp
from bankapp.views.profile import bp as profile_bp
from bankapp.views.edit_account import bp as edit_account_bp

from bankapp.logic.session import is_loggedin

MAIN_LINKS = [
    {
        'name': 'Dashboard',
        'href': '/profile'
    },
    {
        'name': 'New Bank Account',
        'href': '/account'
    },
]

app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.jinja_env.globals.update(
    is_loggedin=is_loggedin,
    MAIN_LINKS=MAIN_LINKS
)

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(register_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(edit_account_bp)
