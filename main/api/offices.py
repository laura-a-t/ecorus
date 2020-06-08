from flask import request, Blueprint
from werkzeug.exceptions import HTTPException
from sqlalchemy.orm.exc import NoResultFound

from main.api.util import make_response
from main.db.db import session
from main.db.models import Office

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
    with session() as sess:
        try:
            office = sess.query(Office).filter_by(id=office_id).one()
        except NoResultFound:
            return make_response(f"Office with id {office_id} does not exist", 404)
        return make_response(f"Office with id {office_id}", 200, office=office.to_dict())


@blueprint.route('/<office_id>', methods=['DELETE'])
def delete(office_id):
    with session() as sess:
        try:
            office = sess.query(Office).filter_by(id=office_id).one()
            sess.delete(office)
        except NoResultFound:
            return make_response(f"Office with id {office_id} does not exist", 404)
        return make_response(f"Deleted office with id {office_id}", 200, office=office.to_dict())


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
    data = request.json
    with session() as sess:
        new_office = Office(
            name=data['name']
        )
        sess.add(new_office)
        sess.flush()
        return make_response(f"Created office with id {new_office.id}", 200, office=new_office.to_dict())
