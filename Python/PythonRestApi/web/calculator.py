from return_messages import error_message, success_message
from verification import verify_validity_of_posted_data, get_x_and_y_parameters


def add(posted_data):
    status_code = verify_validity_of_posted_data(posted_data, "add")

    if status_code != 200:
        return error_message(status_code)

    x, y = get_x_and_y_parameters(posted_data)
    return success_message(x + y)


def subtract(posted_data):
    status_code = verify_validity_of_posted_data(posted_data, "subtract")

    if status_code != 200:
        return error_message(status_code)

    x, y = get_x_and_y_parameters(posted_data)
    return success_message(x - y)


def multiply(posted_data):
    status_code = verify_validity_of_posted_data(posted_data, "multiply")

    if status_code != 200:
        return error_message(status_code)

    x, y = get_x_and_y_parameters(posted_data)
    return success_message(x * y)


def division(posted_data):
    status_code = verify_validity_of_posted_data(posted_data, "division")

    if status_code != 200:
        return error_message(status_code)

    x, y = get_x_and_y_parameters(posted_data)
    return success_message(x / y)

