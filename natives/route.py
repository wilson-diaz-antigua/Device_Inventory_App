
import json
from flask import jsonify, request
import pandas as pd


import subprocess
from natives import app
from natives.models import *
from natives.parsing import *


db.init_app(app)

voyceSchemas = Voyce_Schema(many=True)
voyceSchema = Voyce_Schema()


@app.route('/read', methods=['GET'])
def index():

    data = Voyce.query.all()
    out = voyceSchemas.dump(data)
    response = jsonify(out)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/create', methods=['GET'])
def create():
    try:
        # cmd = 'cfgutil -f --format JSON get name serialNumber wifiAddress'
        # result = subprocess.run(
        #     cmd, shell=True, capture_output=True, text=True, check=True)
        # output = json.loads(str(result.stdout))
        output = {
            "Command": "get",
            "Output": {
                "0x954A00E7B0026": {
                    "name": "ATEST 001",
                    "wifiAddress": "c4:2a:d0:5f:ca:b0",
                    "serialNumber": "F9FZ5J5KMF3M"
                },
                "0x1459941A41402E": {
                    "name": "ATEST 002",
                    "wifiAddress": "4c:b9:10:97:e9:ed",
                    "serialNumber": "GG7FFKTQQ1GC"
                },  
                "0x1459FR41A41402E": {
                    "name": "ATEST 03",
                    "wifiAddress": "4c:b9:10:97:e9:ed",
                    "serialNumber": "GG7FFKTQQ1GC"
                },
                "Errors": {
                    "0x1459941A41402E": {},
                    "0x954A00E7B0026": {}
                }
            },
            
            "Type": "CommandOutput",
            "Devices": [
                "0x954A00E7B0026",
                "0x1459941A41402E"
            ]}
        df = pd.DataFrame(Data(output))
        
        # df.to_sql(name='voyce_device', con=db.engine, index=False,if_exists= 'append')
        # col=[]
        # added=[]
        # for index in df.index:
        #     col.append( f"Device {df['Device'][index]} at {df['Hospital'][index]}  has been added")
            
        #     added.append({"response" : col[index] })
        return jsonify({"results": f"{len(df.index)} devices have been added"})


    except subprocess.CalledProcessError:
        return jsonify({'error': 'nothing'})
    
    
@app.route('/edit/<id>/', methods=['PUT'])
def edit(id):
    article = Voyce.query.get(id)
    
    hospital = request.json["Hospital"]
    device = request.json["Device"]
    
    article.Hospital = hospital
    article.Device = device
    db.session.commit()
    
    return voyceSchema.jsonify(article)
    
