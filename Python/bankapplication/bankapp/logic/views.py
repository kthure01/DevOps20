from bankapp.logic.session import is_loggedin
from flask import redirect
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not is_loggedin():
            return redirect('/')
        return f(*args, **kwargs)
    return wrapper
