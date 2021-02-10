from encryption import verify_password
from messages import message_user_fail, message_password_fail
from mongodb import user_exist


def verify_account(username, password) -> bool:
    if not user_exist(username):
        return False

    successful_verification = verify_password(username, password)
    return successful_verification


def verify_credentials(username, password):
    if not user_exist(username):
        return message_user_fail(), True

    correct_pw = verify_account(username, password)

    if not correct_pw:
        return message_password_fail(), True

    return None, False
