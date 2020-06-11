from flask import Flask, make_response

from api.api import offices, persons
from api.db.db import EngineSingleton
from api.db.models import Base
from api.utils import get_config

ENDPOINTS = [
    ('/office', offices.blueprint),
    ('/person', persons.blueprint),
]


def index():
    """
    Health check
    """
    return make_response(), 200


def init_schema():
    db_config = get_config('DB')
    engine = EngineSingleton(db_config).get_engine()
    Base.metadata.create_all(engine, checkfirst=True)


def setup_endpoints(application):
    application.add_url_rule('/', 'index', index, methods=['GET'])
    application.add_url_rule('/init_schema', 'init_schema', init_schema, methods=['GET'])
    for prefix, blueprint in ENDPOINTS:
        application.register_blueprint(blueprint, url_prefix=prefix)


def create_app():
    application = Flask(__name__)
    setup_endpoints(application)

    return application
