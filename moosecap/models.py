from sqlalchemy import Sequence, Column, String, Integer, ForeignKey, Numeric, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Organization(Base):
    """Organization."""
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    work_unit_name = Column(String(30))
    work_unit_per_week = Column(Integer)
    work_unit_admin_ratio = Column(Numeric(precision=3, scale=2))
    note = Column(Text(520))
    extra = Column(JSON)
    domains = relationship("Domain", backref="organization")
    people = relationship("Person", backref="organization")
    teams = relationship("Team", backref="organization")
    categories = relationship("Category", backref="organization")

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Team(Base):
    """Team."""
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    note = Column(Text(520))
    extra = Column(JSON)
    # organization_id = Column(Integer, ForeignKey='organization.id')
    #domains = Set('Domain')
    #systems = Set('System')
    #categories = Set('Category_Allocation')
    #manager = Column(Person, reverse='manage')
    #members = Set(Person, reverse='team')

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Category(Base):
    """Category."""
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    note = Column(Text(520))
    extra = Column(JSON)
    #organization_id = Column(Integer, ForeignKey='organization.id')
    #teams = Set('Category_Allocation')

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Person(Base):
    """Person."""
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    email = Column(String(220))
    work_unit_ratio = Column(Numeric(precision=3, scale=2))
    note = Column(Text(520))
    extra = Column(JSON)
    #organization_id = Column(Integer, ForeignKey='organization.id')
    #manage = Column('Team', reverse='manager')
    #team = Column('Team', reverse='members')
    #technology_skills = Set('Technology_Skill')

    def __repr__(self):
        return "<id(id='%s', bat='%s', name='%s')>" % (self.id, self.bat, self.name)


class Domain(Base):
    """Domain."""
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True)
    bat = Column(String(30), unique=True, index=True)
    name = Column(String(120), unique=True)
    display = Column(String(220))
    note = Column(Text(520))
    extra = Column(JSON)
    #organization_id = Column(Integer, ForeignKey='organization.id')
    #teams = relationship('Team', backref='domain')
    #systems = Set('System')
    #organization = Required(Organization)
