from flask import Flask, make_response

from api.api import offices, persons

ENDPOINTS = [
    ('/office', offices.blueprint),
    ('/person', persons.blueprint),
]


def index():
    """
    Health check
    """
    return make_response(), 200


def setup_endpoints(application):
    application.add_url_rule('/', 'index', index, methods=['GET'])
    for prefix, blueprint in ENDPOINTS:
        application.register_blueprint(blueprint, url_prefix=prefix)


def create_app():
    application = Flask(__name__)
    setup_endpoints(application)

    return application
