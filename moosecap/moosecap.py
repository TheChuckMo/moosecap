from flask import Flask
from moosecap.db.models import *


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


db.bind('sqlite', '/home/chuck/Projects/tecap/tecap.db', create_db=True)

db.generate_mapping(create_tables=True)
