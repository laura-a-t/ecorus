from flask import request, Blueprint
from werkzeug.exceptions import HTTPException
from sqlalchemy.orm.exc import NoResultFound

from api.api.util import make_response
from api.db.db import session
from api.db.models import Person, Office

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


@blueprint.route('/<person_id>', methods=['GET'], strict_slashes=False)
def get(person_id):
    with session() as sess:
        try:
            person = sess.query(Person).filter_by(id=person_id).one()
        except NoResultFound:
            return make_response(f"Person with id {person_id} does not exist", 404)
        return make_response("Success", 200, person=person.to_dict())


@blueprint.route('/<person_id>', methods=['DELETE'], strict_slashes=False)
def delete(person_id):
    with session() as sess:
        try:
            person = sess.query(Person).filter_by(id=person_id).one()
            sess.delete(person)
        except NoResultFound:
            return make_response(f"Person with id {person_id} does not exist", 404)
        return make_response(f"Person with id {person_id} was deleted", 200, person=person.to_dict())


@blueprint.route('/<person_id>', methods=['PUT'], strict_slashes=False)
def put(person_id):
    modified_person = request.json
    increment_age = modified_person.get('age', False)
    name = modified_person.get('name')
    with session() as sess:
        try:
            person = sess.query(Person).filter_by(id=person_id).one()
            if increment_age:
                person.age = person.age + 1
            if name:
                person.name = name
        except NoResultFound:
            return make_response(f"Person with id {person_id} does not exist", 404)
        return make_response("Success", 200, person=person.to_dict())


@blueprint.route('/', methods=['POST'], strict_slashes=False)
def post():
    data = request.json
    office_id = data.get('office_id')
    office = None
    with session() as sess:
        if office_id:
            try:
                office = sess.query(Office).filter_by(id=office_id).one()
            except NoResultFound:
                return make_response(f"Office with id {office_id} does not exist, did not create person entry", 404)
        new_person = Person(
            name=data['name'],
            age=data['age'],
            office_id=office,
            office=office
        )
        sess.add(new_person)
        sess.flush()
        return make_response(f"Created person with id {new_person.id}", 200, person=new_person.to_dict())

