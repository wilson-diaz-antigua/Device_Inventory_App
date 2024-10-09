
from datetime import date

from . import ma
from .db import db


class Voyce(db.Model):
    __tablename__ = 'voyce_device'
    id = db.Column(db.Integer, primary_key=True)

    Hospital = db.Column(db.Text)
    Device = db.Column(db.Text)
    SN = db.Column(db.Text, unique=True)
    MAC = db.Column(db.Text, unique=True)
    DateAdded = db.Column(db.DateTime, default=date.today())


class Voyce_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Voyce
        load_instance = True
