from flask import request, Blueprint
from werkzeug.exceptions import HTTPException
from sqlalchemy.orm.exc import NoResultFound

from main.api.util import make_response
from main.db.db import session
from main.db.models import Office, Person

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


@blueprint.route('/<office_id>', methods=['GET'], strict_slashes=False)
def get(office_id):
    with session() as sess:
        try:
            office = sess.query(Office).filter_by(id=office_id).one()
        except NoResultFound:
            return make_response(f"Office with id {office_id} does not exist", 404)
        return make_response(f"Office with id {office_id}", 200, office=office.to_dict())


@blueprint.route('/<office_id>', methods=['DELETE'], strict_slashes=False)
def delete(office_id):
    with session() as sess:
        try:
            office = sess.query(Office).filter_by(id=office_id).one()
            sess.delete(office)
        except NoResultFound:
            return make_response(f"Office with id {office_id} does not exist", 404)
        return make_response(f"Deleted office with id {office_id}", 200, office=office.to_dict())


@blueprint.route('/add_employee', methods=['PUT'], strict_slashes=False)
def add_employee():
    data = request.json
    if 'office_id' not in data or 'person_id' not in data:
        return make_response("Both office_id and person_id need to be supplied", 404)
    office_id = data['office_id']
    person_id = data['person_id']
    with session() as sess:
        try:
            sess.query(Person).filter_by(id=person_id).update({"office_id": office_id})
        except NoResultFound:
            return make_response(f"No person with id {person_id} exists", 404)
        return make_response(
            f"Person with id {person_id} was added to office with id {office_id}",
            200,
        )


@blueprint.route('/remove_employee', methods=['PUT'], strict_slashes=False)
def remove_employee():
    data = request.json
    if 'office_id' not in data or 'person_id' not in data:
        return make_response("Both office_id and person_id need to be supplied", 404)
    office_id = data['office_id']
    person_id = data['person_id']
    with session() as sess:
        try:
            sess.query(Person).filter_by(id=person_id).update({"office_id": None})
        except NoResultFound:
            return make_response(f"No person with id {person_id} exists", 404)
        return make_response(
            f"Person with id {person_id} was removed from office with id {office_id}",
            200,
        )


@blueprint.route('/', methods=['POST'], strict_slashes=False)
def post():
    data = request.json
    with session() as sess:
        new_office = Office(
            name=data['name']
        )
        sess.add(new_office)
        sess.flush()
        return make_response(f"Created office with id {new_office.id}", 200, office=new_office.to_dict())
