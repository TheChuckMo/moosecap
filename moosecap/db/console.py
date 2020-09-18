#!/usr/bin/env python

from moosecap.db.model import db
import os, sys
import click

from pony.orm import db_session

DB_NAME = 'moosecap.db'
DB_CONNECT = os.path.join(os.path.abspath(os.getcwd()), DB_NAME)


def bind_db(create_tables: bool = False):
    """Bind to the database file."""
    db.bind('sqlite', DB_CONNECT, create_db=True)
    db.generate_mapping(create_tables=create_tables)


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
    """Create database and tables."""
    bind_db(create_tables=True)


@modb.command()
@click.confirmation_option()
def load_base():
    """Load default domains."""
    bind_db()
    click.echo('loading domain')
    with db_session:
        domain1 = db.Domain(name="Business Projects", bat="busp", enabled=True)
        domain2 = db.Domain(name="Team Projects", bat="intp", enabled=True)
        domain3 = db.Domain(name="Operational Support", bat="opsup", enabled=True)
        domain4 = db.Domain(name="Operational Maintenance", bat="opmain", enabled=True)

    click.echo('loading technology')
    with db_session:
        tech1 = db.Technology(name="Unix Compute", bat="unixcomp", enabled=True)
        tech2 = db.Technology(name="Windows Compute", bat="wincomp", enabled=True)
        tech3 = db.Technology(name="Enterprise Directory", bat="entdir", enabled=True)
        tech4 = db.Technology(name="Enterprise Mail", bat="entmail", enabled=True)
        tech5 = db.Technology(name="Storage and Backups", bat="storbck", enabled=True)
        tech6 = db.Technology(name="DevOps Automation", bat="devops", enabled=True)

    click.echo('loading team')
    with db_session:
        team = db.Team(name="Infrastructure Team", bat="infrteam", enabled=True)

        click.echo('loading coordinator')
        coordinator = db.Coordinator(name="Ron Swanson", bat="swansonr", rate=1, coordinate=team)

        click.echo('loading contributor')
        contrib1 = db.Contributor(name="Sam Henry", bat="henrys", rate=1, member=team)
        contrib2 = db.Contributor(name="Betty Smith", bat="smiths", rate=1, member=team)
        contrib3 = db.Contributor(name="Tom Hanks", bat="hankst", rate=0.5, member=team)
        contrib4 = db.Contributor(name="Sue Winner", bat="winners", rate=0.75, member=team)
        contrib5 = db.Contributor(name="Timmy Twotone", bat="twotonet", rate=1, member=team)

    click.echo('loading contributor_technology')
    with db_session:
        click.echo('get contributors')
        contrib1 = db.Contributor.get(bat="henrys")
        contrib2 = db.Contributor.get(bat="smiths")
        contrib3 = db.Contributor.get(bat="hankst")
        contrib4 = db.Contributor.get(bat="winners")
        contrib5 = db.Contributor.get(bat="twotonet")

        click.echo('get technologies')
        tech1 = db.Technology.get(bat="unixcomp")
        tech2 = db.Technology.get(bat="wincomp")
        tech3 = db.Technology.get(bat="entdir")
        tech4 = db.Technology.get(bat="entmail")
        tech5 = db.Technology.get(bat="storbck")
        tech6 = db.Technology.get(bat="devops")

        click.echo('contributor technologies')
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


if __name__ == "__main__":
    modb()
