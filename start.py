from api.api.app import create_app


app = create_app()


def run_dev_app():
    app.run(host='0.0.0.0', port=8080, debug=False)
