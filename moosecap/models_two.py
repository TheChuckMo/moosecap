from decimal import Decimal
from pony.orm import *
from pony.flask import Pony, db_session

db = Database()


def db_init_app(app):
    """Init Pony in Flask app."""
    Pony(app)


def db_bind(connect: str, create_tables: bool = False):
    """Bind to database."""
    db.bind('sqlite', connect, create_db=True)
    db.generate_mapping(create_tables=create_tables)

    return db


class Person(db.Entity):
    bat = PrimaryKey(str, 30)
    name = Required(str)
    display = Optional(str)
    email = Optional(str)
    manage = Optional('Team', reverse='manager')
    team = Optional('Team', reverse='members')
    work_unit_ratio = Optional(str)
    note = Optional(str)
    extra = Optional(Json)
    technology_skills = Set('Technology_Skill')


class Organization(db.Entity):
    bat = PrimaryKey(str, 30)
    name = Required(str, 220)
    display = Optional(str)
    note = Optional(str)
    domains = Set('Domain')
    work_unit_name = Required(str, default='hour')
    work_unit_per_week = Required(int, default=40)
    work_unit_admin_ratio = Required(Decimal, precision=3, scale=2, default="0.20")
    teams = Set('Team')
    extra = Optional(Json)


class Team(db.Entity):
    bat = PrimaryKey(str, 30)
    name = Required(str)
    organization = Required(Organization)
    display = Optional(str)
    note = Optional(str)
    domains = Set('Domain')
    extra = Optional(Json)
    systems = Set('System')
    categories = Set('Category_Allocation')
    manager = Optional(Person, reverse='manage')
    members = Set(Person, reverse='team')


class Category(db.Entity):
    bat = PrimaryKey(str, 30)
    name = Required(str)
    display = Optional(str)
    teams = Set('Category_Allocation')
    note = Optional(str)
    extra = Optional(Json)


class Domain(db.Entity):
    bat = PrimaryKey(str, 30)
    name = Required(str)
    organization = Required(Organization)
    display = Optional(str)
    note = Optional(str)
    teams = Set(Team)
    systems = Set('System')
    extra = Optional(Json)


class Object(db.Entity):
    bat = PrimaryKey(str, 30)
    name = Required(str)
    display = Optional(str)
    note = Optional(str)
    reliability = Optional(Decimal, precision=6, scale=5, default="0.95555")
    tier = Optional(int, default=1)
    extra = Optional(Json)


class Technology(Object):
    dependencies = Set('Technology_Dependency')
    people = Set('Technology_Skill')


class System(Object):
    domain = Optional(Domain)
    team = Optional(Team)
    system_dependencies = Set('System', reverse='system_dependencies')
    technology_dependencies = Set('Technology_Dependency')


class Technology_Dependency(db.Entity):
    system = Required(System)
    technology = Required(Technology)
    weight = Required(int, default=1)
    PrimaryKey(system, technology)


class Technology_Skill(db.Entity):
    technology = Required(Technology)
    person = Required(Person)
    level = Required(int, default=1)
    PrimaryKey(technology, person)


class Category_Allocation(db.Entity):
    category = Required(Category)
    team = Required(Team)
    ratio = Required(Decimal, precision=3, scale=2, default="0.25")
    PrimaryKey(category, team)

