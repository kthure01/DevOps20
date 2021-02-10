def add_or_sub_or_multi(function_name: str) -> bool:
    return function_name == "add" \
           or function_name == "subtract" \
           or function_name == "multiply"


def any_variable_is_missing(posted_data) -> bool:
    return "x" not in posted_data \
           or "y" not in posted_data


def division(function_name: str) -> bool:
    return function_name == "division"


def division_by_zero(posted_data) -> bool:
    return int(posted_data["y"]) == 0


def verify_validity_of_posted_data(posted_data, function_name) -> int:
    if add_or_sub_or_multi(function_name):
        if any_variable_is_missing(posted_data):
            return 301  # Missing parameter
        else:
            return 200
    elif division(function_name):
        if any_variable_is_missing(posted_data):
            return 301
        elif division_by_zero(posted_data):
            return 302
        else:
            return 200
    else:
        return 305


def get_x_and_y_parameters(posted_data) -> {int, int}:
    x = posted_data["x"]
    y = posted_data["y"]
    x = int(x)
    y = int(y)
    return x, y
