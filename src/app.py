from flask import Flask
from routes import register_routes


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    register_routes(app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=5000)