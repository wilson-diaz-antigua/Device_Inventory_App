
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

sqlite=f"sqlite:////Users/wilson/Desktop/native/mock.db"
supabase=f"sqlite:////Users/wilson/Desktop/native/mock.db"
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
ma = Marshmallow(app)

from natives import route
