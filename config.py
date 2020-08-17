import os
from flask import Flask

DATABASE_PATH = os.path.abspath(os.path.dirname(__file__)) + '/database'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(DATABASE_PATH, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 's3cr3et'
