from flask import Flask
from .config import cfg
from . import db


def create_app():
    """Create instance of Moosecap flask app."""
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY='NOT-A-SECRET-KEY',
        database={'url': 'sqlite:///moosecap.db'}
    )
    app.config.update(cfg.obj)

    db.init_app(app)

    return app
