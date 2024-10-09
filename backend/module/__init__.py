
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from .db import db

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
db_file_path = '/app/db/mock.db'
app = Flask(__name__)
CORS(app)
sqlite='sqlite:///' + os.path.join(db_file_path)
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['CORS_HEADERS'] = 'Content-Type'

ma = Marshmallow(app)
db.init_app(app)
from . import route

#%% 
import os
basedir = os.path.abspath(os.path.dirname(__file__))

sqlite='sqlite:///' + os.path.join(basedir, 'db', 'mock.db')
print(sqlite)
# %%
