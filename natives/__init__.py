
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

load_dotenv(".env")

app = Flask(__name__)
CORS(app)

sqlite= os.getenv("SQLITE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
ma = Marshmallow(app)

from natives import route
