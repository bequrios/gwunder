from flask import Flask

from app.api import api_bp
from app.routes import web_bp


def create_app(config=None):
    app = Flask(__name__, static_folder="static", template_folder="templates")

    if config:
        app.config.update(config)

    app.register_blueprint(api_bp)
    app.register_blueprint(web_bp)

    return app
