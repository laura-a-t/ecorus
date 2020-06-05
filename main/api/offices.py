from flask import jsonify, request, Blueprint
from werkzeug.exceptions import HTTPException

from main.api.util import make_response

blueprint = Blueprint('offices', __name__)


@blueprint.errorhandler(Exception)
def handle_error(e):
    status_code = 500
    if isinstance(e, HTTPException):
        status_code = e.code
    return make_response(
        f"Operation failed with error: {type(e).__name__}: {str(e)}",
        status_code
    )


@blueprint.route('/<office_id>', methods=['GET'])
def get(office_id):
    return make_response(f"Office id {office_id}", 200)


@blueprint.route('/<office_id>', methods=['DELETE'])
def delete(office_id):
    # Check that office has no employees; If it has employees, raise 400 error
    return make_response(f"Office with id {office_id} was removed from the database", 200)


@blueprint.route('/add_employee/<person_id>', methods=['PUT'])
def add_employee(person_id):
    # Check if employ
    # Check if employee already works in an office; If yes return message that they changed office
    return make_response("Added person to office", 200)


@blueprint.route('/remove_employee/<person_id>', methods=['PUT'])
def remove_employee(person_id):
    return make_response(f"Removed employee with id {person_id}", 200)


@blueprint.route('/', methods=['POST'])
def post():
    office = request.json
    return make_response("Created office with id xxx", 200, office=office)
