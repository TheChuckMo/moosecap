from .models import Organization, Team, Category, Person, Domain
import click
from flask import g, current_app
from flask.cli import with_appcontext
from sqlalchemy import engine_from_config
from sqlalchemy.orm import Session
from .config import cfg


def init_app(app):
    """Prepare db on application."""
    app.teardown_appcontext(close_session)
    app.cli.add_command(cli_db)


def open_session() -> Session:
    """Prepare SQLAlchemy database session."""
    if 'db' not in g:
        _engine = engine_from_config(current_app.config.get("database"))
        g.db = Session(bind=_engine)

    return g.db


def close_session(e=None):
    """Close all sessions with database."""
    session = g.pop('db', None)

    if session is not None:
        session.close_all()


@click.group('db')
def cli_db():
    """Database cli."""
    pass


@cli_db.command('open')
@with_appcontext
def cli_db_open():
    """Open a database session."""
    click.echo('open database session.')
    _session = open_session()
    click.echo(f'{_session}')


@cli_db.command('create')
@with_appcontext
def cli_db_create():
    """Create the database."""
    print(f'{current_app.config.get("database")}')
    _session = open_session()
