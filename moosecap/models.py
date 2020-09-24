from sqlalchemy import Sequence, Column, String, Integer, ForeignKey, Numeric, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Organization(Base):
    """Organization."""
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    work_unit_name = Column(String(30))
    work_unit_per_week = Column(Integer)
    work_unit_admin_ratio = Column(Numeric(precision=3, scale=2))
    note = Column(Text(520))
    extra = Column(JSON)
    teams = relationship("Team", backref="organization")
    domains = relationship("Domain", backref="organization")
    members = relationship("Person", backref="organization")
    categories = relationship("Category", backref="organization")

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Team(Base):
    """Team."""
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    note = Column(Text(520))
    extra = Column(JSON)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    manager_id = Column('Person', ForeignKey('person.id'))
    manager = relationship('Person')
    categories = relationship('TeamCategory', backref='category')
    domains = relationship('TeamDomain', backref='domain')
    # technologies =
    # systems =

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Category(Base):
    """Category."""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    note = Column(Text(520))
    extra = Column(JSON)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    teams = relationship('TeamCategory', backref='team')

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class TeamDomain(Base):
    """Team domain association."""
    __tablename__ = 'team_domain'
    team_id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    domain_id = Column(Integer, ForeignKey('domain.id'), primary_key=True)


    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)

class TeamCategory(Base):
    """Team category association."""
    __tablename__ = 'team_category'
    team_id = Column(Integer, ForeignKey('team.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), primary_key=True)
    allocation = Column(Numeric(precision=3, scale=2))

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Person(Base):
    """Person."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    email = Column(String(220))
    work_unit_ratio = Column(Numeric(precision=3, scale=2))
    note = Column(Text(520))
    extra = Column(JSON)
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship('Team', backref='members')
    organization_id = Column(Integer, ForeignKey('organization.id'))
    #technology_skills = Set('Technology_Skill')

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Domain(Base):
    """Domain."""
    __tablename__ = 'domain'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    note = Column(Text(520))
    extra = Column(JSON)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    #teams = relationship('Team', backref='domain')
    #systems = Set('System')
    #organization = Required(Organization)

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)
