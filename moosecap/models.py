"""Moose Capacity Database Model."""

from decimal import Decimal
from pony.orm import *

db = Database()


class Object(db.Entity):
    id = PrimaryKey(int, auto=True)
    bat = Required(str, 25, unique=True, index='true')
    name = Required(str, 120, unique=True)
    enabled = Optional(bool, default=True)
    note = Optional(str, 500, nullable=True)
    info = Optional(Json)


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    bat = Required(str, 25, unique=True)
    name = Required(str, 120, unique=True)
    email = Optional(str, 120, unique=True, index='false')
    rate = Required(Decimal, precision=3, scale=2, default="1.00")
    note = Optional(str, 500, nullable=True)
    info = Optional(Json)


class Group(db.Entity):
    id = PrimaryKey(int, auto=True)
    bat = Required(str, 25)
    name = Required(str, 120, unique=True)
    enabled = Optional(bool, default=True)
    note = Optional(str, 500, nullable=True)
    info = Optional(Json)


class Domain(Group):
    teams = Set('Team')


class Team(Group):
    full_time = Optional(int, default=40)
    domains = Set(Domain)
    contributors = Set('Contributor')
    coordinator = Optional('Coordinator')
    maturity = Optional(int, default=1)


class Technology(Object):
    tier = Optional(int)
    maturity = Optional(int, default=1)
    contributors = Set('Contributor_Technology')


class Contributor(Person):
    member = Required(Team)
    technologies = Set('Contributor_Technology')


class Contributor_Technology(db.Entity):
    id = PrimaryKey(int, auto=True)
    factor = Required(int, default=1, unsigned=True)
    technology = Required(Technology)
    contributor = Required(Contributor)


class Coordinator(Person):
    coordinate = Required(Team)


