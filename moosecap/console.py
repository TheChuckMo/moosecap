from moosecap.models_two import db_bind, db_session
import os
import yaml
import click

DB_NAME = 'moosecap.db'
DB_CONNECT = os.path.join(os.path.abspath(os.getcwd()), DB_NAME)

_data: dict = {}
_default_data_file_ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'default.yml')

if os.path.exists(_default_data_file_):
    with open(_default_data_file_, 'r') as fd:
        _data = yaml.safe_load(fd)


def load_entity(name: str, Entity, entries: list):
    """Load Entity data."""
    click.echo(f'{name} defaults')

    with db_session:
        for _entry in entries:
            if Entity.get(bat=_entry["bat"]):
                click.echo(f'skipping {_entry["bat"]}')
            else:
                click.echo(f'writing {_entry["bat"]}')
                Entity(**_entry)


@click.group('modb')
def modb():
    """DB CLI entry"""
    pass


@modb.command()
@click.confirmation_option()
def delete():
    """Delete database file."""
    os.remove(DB_CONNECT)


@modb.command()
@click.confirmation_option()
def create():
    """Create database tables."""
    db_bind(DB_CONNECT, create_tables=True)


@modb.group('load')
def load_db():
    """Load entity sample data."""
    pass


@load_db.command()
@click.confirmation_option()
def org():
    """Sample organization."""
    db = db_bind(DB_CONNECT)

    click.echo('loading organization')
    load_entity("organization", db.Organization, _data.get("organization"))


@load_db.command()
@click.confirmation_option()
def category():
    """Sample category entities."""
    db = db_bind(DB_CONNECT)

    click.echo('loading category')
    load_entity("category", db.Category, _data.get("category"))


@load_db.command()
@click.confirmation_option()
def domain():
    """Sample domain entities."""
    db = db_bind(DB_CONNECT)

    click.echo('writing domain')
    with db_session:
        _entries = []
        for _entry in _data.get("domain"):
            click.echo(f'getting org {_entry["organization"]["bat"]}')
            _entry["organization"] = db.Organization.get(bat=f'{_entry["organization"]["bat"]}')
            _entries.append(_entry)

        load_entity("domain", db.Domain, _entries)


@load_db.command()
@click.confirmation_option()
def team():
    """Sample team entities."""
    db = db_bind(DB_CONNECT)

    click.echo('writing team')
    with db_session:
        _entries = []
        for _entry in _data.get("team"):
            click.echo(f'getting org {_entry["organization"]["bat"]}')
            _entry["organization"] = db.Organization.get(bat=f'{_entry["organization"]["bat"]}')
            _entries.append(_entry)

        load_entity("team", db.Team, _entries)


@load_db.command()
@click.confirmation_option()
def allocation():
    """Sample category allocation."""
    db = db_bind(DB_CONNECT)

    click.echo('team category allocation')
    with db_session:
        _entries = []
        for _entry in _data.get("category_allocation"):
            click.echo(f'getting team {_entry["team"]["bat"]}')
            _entry["team"] = db.Team.get(bat=f'{_entry["team"]["bat"]}')

            click.echo(f'getting category {_entry["category"]["bat"]}')
            _entry["category"] = db.Category.get(bat=f'{_entry["category"]["bat"]}')

            if db.Category_Allocation.get(**_entry):
                click.echo(f'skipping {_entry["category"].name}')
            else:
                click.echo(f'writing {_entry["category"].name}')
                db.Category_Allocation(**_entry)


@load_db.command()
@click.confirmation_option()
def technology():
    """Sample technology entities."""
    db = db_bind(DB_CONNECT)

    click.echo('writing technology')
    load_entity("technology", db.Technology, _data.get("technology"))


@load_db.command()
@click.confirmation_option()
def person():
    """Sample person entities."""
    db = db_bind(DB_CONNECT)

    click.echo('writing person')
    load_entity("person", db.Person, _data.get("person"))

