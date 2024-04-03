from flask import Flask
import os
from flask_sqlalchemy import  SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'showroom.db')

db = SQLAlchemy(app)

from showroom import routes