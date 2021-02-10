import bcrypt

from mongodb import get_hashed_password


def generate_hashed_password(password) -> bytes:
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


def verify_password(username, password) -> bool:
    hashed_pw = get_hashed_password(username)

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False
