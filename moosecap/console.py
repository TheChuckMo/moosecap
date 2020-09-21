from moosecap.db import db_session
from moosecap.models import db_bind
import os
import click

DB_NAME = 'moosecap.db'
DB_CONNECT = os.path.join(os.path.abspath(os.getcwd()), DB_NAME)


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


@modb.command()
@click.confirmation_option()
def load_base():
    """Load default data."""
    db = db_bind(DB_CONNECT)
    click.echo('writing domain')
    with db_session:
        db.Domain(name="Business Projects", bat="busp", enabled=True)
        db.Domain(name="Team Projects", bat="intp", enabled=True)
        db.Domain(name="Operational Support", bat="opsup", enabled=True)
        db.Domain(name="Operational Maintenance", bat="opmain", enabled=True)

    click.echo('writing technology')
    with db_session:
        db.Technology(name="Unix Compute", bat="ucompute", enabled=True)
        db.Technology(name="Windows Compute", bat="wcompute", enabled=True)
        db.Technology(name="Enterprise Directory", bat="edirectory", enabled=True)
        db.Technology(name="Enterprise Mail", bat="email", enabled=True)
        db.Technology(name="Storage and Backups", bat="strnbck", enabled=True)
        db.Technology(name="DevOps Automation", bat="devops", enabled=True)

    click.echo('writing team')
    with db_session:
        team = db.Team(name="Infrastructure Team", bat="infrateam", enabled=True)

        click.echo('writing coordinator')
        db.Coordinator(name="Ron Swanson", bat="swansonr", rate=1, coordinate=team)

        click.echo('writing contributor')
        db.Contributor(name="Sam Henry", bat="henrys", rate=1, member=team)
        db.Contributor(name="Betty Smith", bat="smiths", rate=1, member=team)
        db.Contributor(name="Tom Hanks", bat="hankst", rate=0.5, member=team)
        db.Contributor(name="Sue Winner", bat="winners", rate=0.75, member=team)
        db.Contributor(name="Timmy Twotone", bat="twotonet", rate=1, member=team)

    click.echo('writing contributor_technology')
    with db_session:
        click.echo('get contributors')
        contrib1 = db.Contributor.get(bat="henrys")
        contrib2 = db.Contributor.get(bat="smiths")
        contrib3 = db.Contributor.get(bat="hankst")
        contrib4 = db.Contributor.get(bat="winners")
        contrib5 = db.Contributor.get(bat="twotonet")

        click.echo('get technologies')
        tech1 = db.Technology.get(bat="ucompute")
        tech2 = db.Technology.get(bat="wcompute")
        tech3 = db.Technology.get(bat="edirectory")
        tech4 = db.Technology.get(bat="email")
        tech5 = db.Technology.get(bat="strnbck")
        tech6 = db.Technology.get(bat="devops")

        click.echo('writing contributor technologies')
        db.Contributor_Technology(contributor=contrib1, technology=tech1, factor=1)
        db.Contributor_Technology(contributor=contrib1, technology=tech4, factor=1)
        db.Contributor_Technology(contributor=contrib1, technology=tech6, factor=1)
        db.Contributor_Technology(contributor=contrib2, technology=tech2, factor=1)
        db.Contributor_Technology(contributor=contrib2, technology=tech3, factor=1)
        db.Contributor_Technology(contributor=contrib2, technology=tech5, factor=1)
        db.Contributor_Technology(contributor=contrib3, technology=tech2, factor=1)
        db.Contributor_Technology(contributor=contrib3, technology=tech3, factor=1)
        db.Contributor_Technology(contributor=contrib3, technology=tech4, factor=1)
        db.Contributor_Technology(contributor=contrib4, technology=tech5, factor=1)
        db.Contributor_Technology(contributor=contrib4, technology=tech3, factor=1)
        db.Contributor_Technology(contributor=contrib5, technology=tech3, factor=1)
        db.Contributor_Technology(contributor=contrib5, technology=tech6, factor=1)
