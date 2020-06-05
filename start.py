from main.api.app import create_app


if __name__ == '__main__':
    """
    Normally I would add a pre-fork server instead of using the development server, and Nginx as a web server
    """
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=False)
