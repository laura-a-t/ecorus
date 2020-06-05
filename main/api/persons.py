from flask import jsonify, request, Blueprint
from werkzeug.exceptions import HTTPException

from main.api.util import make_response

blueprint = Blueprint('persons', __name__)


@blueprint.errorhandler(Exception)
def handle_error(e):
    status_code = 500
    if isinstance(e, HTTPException):
        status_code = e.code
    return make_response(
        f"Operation failed with error: {type(e).__name__}: {str(e)}",
        status_code
    )


@blueprint.route('/<person_id>', methods=['GET'])
def get(person_id):
    return make_response(f"Person id {person_id}", 200)


@blueprint.route('/<person_id>', methods=['DELETE'])
def delete(person_id):
    return make_response(f"Person with id {person_id} was removed from the database", 200)


@blueprint.route('/<person_id>', methods=['PUT'])
def put(person_id):
    modified_person = request.json
    if 'age' in modified_person and modified_person['age']:
        message = 'Happy birthday!'
    elif 'name' in modified_person:
        message = 'Changed name to %s' % modified_person['name']
    else:
        message = 'No changes made'
    return make_response(message, 200)


@blueprint.route('/', methods=['POST'])
def post():
    person = request.json
    return make_response("Created person with id xxx", 200, person=person)

