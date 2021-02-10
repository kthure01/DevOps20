from flask import jsonify


def generate_return_dictionary(status, msg) -> dict:
    retJson = {
        "status": status,
        "msg": msg
    }
    return jsonify(retJson)


def message_signup_success() -> dict:
    return generate_return_dictionary(
        200,
        "You successfully signed up for the API"
    )


def message_user_fail() -> dict:
    return generate_return_dictionary(
        301,
        'Invalid Username'
    )


def message_user_dont_exist() -> dict:
    return generate_return_dictionary(
        301,
        'Received username is invalid'
    )


def message_password_fail() -> dict:
    return generate_return_dictionary(
        302,
        'Invalid Password'
    )


def message_amount_insufficient() -> dict:
    return generate_return_dictionary(
        303,
        'You are out of money, please Add Cash or take a loan'
    )


def message_amount_invalid() -> dict:
    return generate_return_dictionary(
        304,
        'The money amount entered must be greater than 0'
    )


def message_amount_added_successfully() -> dict:
    return generate_return_dictionary(
        200,
        'Amount Added Successfully to account'
    )


def message_loan_added_successfully() -> dict:
    return generate_return_dictionary(
        200,
        'Loan Added to Your Account'
    )


def message_loan_paid_successfully() -> dict:
    return generate_return_dictionary(
        200,
        'Loan paid successfully'
    )


def message_loan_paid_fail() -> dict:
    return generate_return_dictionary(
        303,
        'Not Enough Cash in your account'
    )


def message_user_deleted() -> dict:
    return generate_return_dictionary(
        200,
        'Account deleted'
    )
