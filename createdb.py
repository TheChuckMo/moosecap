#!/bin/env python

from moosecap.db.models import db
import os

from pony.orm import db_session

DB_NAME = 'moose_capacity.db'
DB_CONNECT = os.path.join(os.path.abspath(os.getcwd()), DB_NAME)

db.bind('sqlite', DB_CONNECT, create_db=True)

db.generate_mapping(create_tables=True)

# Create Work Domains
with db_session:
    domain1 = db.Domain(name="Business Projects", bat="BUSP", enabled=True)
    domain2 = db.Domain(name="Team Projects", bat="INTP", enabled=True)
    domain3 = db.Domain(name="Operational Support", bat="OPSUP", enabled=True)
    domain4 = db.Domain(name="Operational Maintenance", bat="OPMAIN", enabled=True)

with db_session:
    tech1 = db.Technology(name="Unix Compute", bat="UNIXCOMP", enabled=True)
    tech2 = db.Technology(name="Windows Compute", bat="WINCOMP", enabled=True)
    tech3 = db.Technology(name="Enterprise Directory", bat="ENTDIR", enabled=True)
    tech4 = db.Technology(name="Enterprise Mail", bat="ENTMAIL", enabled=True)
    tech5 = db.Technology(name="Storage and Backups", bat="STORBCK", enabled=True)
    tech6 = db.Technology(name="DevOps Automation", bat="DEVOPS", enabled=True)

with db_session:
    contrib1 = db.Contributor(name="Sam Henry", bat="henrys", rate=1)
    contrib2 = db.Contributor(name="Betty Smith", bat="smiths", rate=1)
    contrib3 = db.Contributor(name="Tom Hanks", bat="hankst", rate=0.5)
    contrib4 = db.Contributor(name="Sue Winner", bat="winners", rate=0.75)
    contrib5 = db.Contributor(name="Timmy Twotone", bat="twotonet", rate=1)

with db_session:
    contribtech1 = db.ContributorTechnology(contributor=contrib1, technology=tech1, factor=1)
