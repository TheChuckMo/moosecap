from .models import *
import click
from flask import g, current_app
from flask.cli import with_appcontext
from sqlalchemy import engine_from_config
from sqlalchemy.orm import Session, sessionmaker, scoped_session


def init_app(app):
    """Prepare db on application."""
    app.teardown_appcontext(close_session)
    app.cli.add_command(cli_db)


def get_engine():
    """Get SQLAlchemy engine"""
    if 'engine' not in g:
        g.engine = engine_from_config(current_app.config.get("database"))

    return g.engine


def open_session() -> Session:
    """Prepare SQLAlchemy database session."""
    if 'session' not in g:
        if 'Session' not in g:
            g.Session = sessionmaker(bind=get_engine())
        g.session = g.Session()

    return g.session


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


@cli_db.command('config')
@with_appcontext
def cli_db_config():
    """Create the database."""
    # click.echo(f'all: {current_app.config}')
    click.echo(f'database: {current_app.config.get("database")}')


@cli_db.command('tables')
@with_appcontext
def cli_db_tables():
    """List database tables."""
    click.echo('list database tables from metadata.')
    #_session = open_session()
    for table in Base.metadata.sorted_tables:
        click.echo('---')
        click.echo(f'{table.name}:')
        click.echo(f'  key: {table.key}')
        click.echo(f'  primary_key: {table.primary_key}')
        click.echo(f'  foreign_keys:')
        for key in table.foreign_keys:
            click.echo(f'    - foreign_key: {key}')


@cli_db.command('create')
@with_appcontext
def cli_db_create():
    """Create the database."""
    # click.echo(f'all: {current_app.config}')
    click.echo(f'database: {current_app.config.get("database")}')
    click.echo('creating database tables.')
    Base.metadata.create_all(bind=get_engine())


@cli_db.command('drop')
@with_appcontext
def cli_db_drop():
    """Create the database."""
    # click.echo(f'all: {current_app.config}')
    click.echo(f'database: {current_app.config.get("database")}')
    click.echo('dropping database tables.')
    Base.metadata.drop_all(bind=get_engine())
