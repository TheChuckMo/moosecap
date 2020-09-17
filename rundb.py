#!/bin/env python

import pony
from db.models import *

pony.options.CUT_TRACEBACK = False

from db.models import *

db.bind('sqlite', '/home/chuck/Projects/tecap/tecap.db', create_db=True)

db.generate_mapping(create_tables=True)

