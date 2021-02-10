from flask import jsonify

message_text = "Message"
status_code_text = "Status_Code"


def error_message(status_code):
    ret_json = {
        message_text: "An error happened",
        status_code_text: status_code
    }
    return jsonify(ret_json)


def success_message(message):
    ret_json = {
        message_text: message,
        status_code_text: 200
    }
    return jsonify(ret_json)
