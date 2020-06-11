from flask import jsonify


def make_response(message, status, **kwargs):
    response = jsonify(
        {
            'message': message,
            **kwargs
        }
    )
    response.status = str(status)
    return response
