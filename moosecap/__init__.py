"""Moose Capacity Model."""

__version__ = "0.1.1"

from flask import Flask
from moosecfg.config import MooseConfigurator
from moosecap import db
from moosecap import api
import os
import yaml

MooseConfigurator.LOCAL_FILE_READ = True
MooseConfigurator.LOCAL_FILE_HIDDEN = False

_config_defaults_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'moosecap.yml')
with open(_config_defaults_file, 'r') as fd:
    _config_defaults = yaml.safe_load(fd.read())

cfg = MooseConfigurator(name='moosecap', defaults=_config_defaults, extension='yml')


def create_app():
    """Create instance of Moosecap flask app."""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'NOT-A-SECRET-KEY'
    app.config["database"] = {'sqlalchemy.url': 'sqlite:///moosecap.db'}
    app.config.update(cfg.obj)

    db.init_app(app)

    app.register_blueprint(api.bp, url_prefix='/api')

    return app

