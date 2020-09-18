from pony.orm import Database, PrimaryKey, Required, Optional, Set, composite_key

from pony.orm.ormtypes import Decimal, Json

db = Database()


class Object(db.Entity):
    bat = Required(str, max_len=10, unique=True, index=True)
    name = Required(str, max_len=120, unique=True, index=True)
    owner = Optional(lambda: Person, cascade_delete=False)
    note = Optional(str, nullable=True)
    enabled = Optional(bool, default=False)
    info = Optional(Json)


class Technology(Object):
    tier = Required(int, min=1, max=3, default=1)
    maturity_factor = Required(int, min=1, max=5, default=1)
    teams = Set(lambda: Team, cascade_delete=False)
    engineers = Set(lambda: ContributorTechnology, cascade_delete=False)


class Person(db.Entity):
    bat = Required(str, max_len=10, unique=True, index=True)
    name = Required(str, unique=True, max_len=120)
    email = Optional(str, unique=True, max_len=120)
    # percent person works full time
    rate = Required(Decimal, precision=3, scale=2, default=1.00)
    owns = Set(Object, cascade_delete=False)
    note = Optional(str)
    info = Optional(Json)


class Contributor(Person):
    contributes = Optional(lambda: Team, cascade_delete=False)
    technologies = Set(lambda: ContributorTechnology)


class ContributorTechnology(db.Entity):
    contributor = Required(Contributor, cascade_delete=False)
    technology = Required(Technology, cascade_delete=False)
    factor = Optional(int, min=1, max=5, default=1)
    composite_key(contributor, technology)


class Coordinator(Person):
    coordinates = Optional(lambda: Team, cascade_delete=False)


class Group(db.Entity):
    # id = PrimaryKey(int, auto=True)
    bat = Required(str, max_len=10, unique=True, index=True)
    name = Required(str, max_len=50, unique=True)
    note = Optional(str, nullable=True)
    enabled = Optional(bool, default=False)
    info = Optional(Json)


class Domain(Group):
    allocations = Set(lambda: DomainAllocation)
    # teams = Set(lambda: Team, cascade_delete=False)


class DomainAllocation(db.Entity):
    domain = Required(Domain, cascade_delete=False)
    team = Required(lambda: Team, cascade_delete=False)
    # percent of time allocated to this work domain
    # total for a team must equal 100%
    allocation = Required(Decimal, precision=3, scale=2, default=1.00)
    composite_key(domain, team)


class Team(Group):
    # full time hours per week
    full_time = Optional(int, min=0, max=169, default=40)
    # team coordinator
    coordinator = Optional(Coordinator, cascade_delete=False)
    # team contributors
    contributors = Set(Contributor, cascade_delete=False)
    # work domains (category/zone/type/area)
    work_domains = Set(DomainAllocation, cascade_delete=False)
    # technology tools required
    technologies = Set(Technology, cascade_delete=False)


