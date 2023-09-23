from flask import Flask, render_template,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////Users/wilson/Desktop/native/VD.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db= SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)

class Voyce(db.Model):
    __tablename__ = 'voyce_device'
    
    id = db.Column(db.Integer, primary_key=True)

    Hospital = db.Column(db.Text)
    Device = db.Column(db.Text)
    SN = db.Column(db.Text, unique=True)
    MAC = db.Column(db.Text, unique=True)
    DateAdded = db.Column(db.Text, default = datetime.utcnow)

class VoyceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Voyce
        load_instance = True 


@app.route('/read',methods=['GET'])
def index():
    
    data = Voyce.query.all()
    voyceSchema = VoyceSchema(many=True)
    out= voyceSchema.dump(data)
    response = jsonify(out)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





if __name__ == '__main__':
    app.run( host='127.0.0.1',port=8080, debug=True)


