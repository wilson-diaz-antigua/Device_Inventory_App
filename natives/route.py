
import json
from flask import jsonify, request
import pandas as pd


import subprocess
from natives import app
from natives.models import *
from natives.parsing import *

from flask_cors import cross_origin

db.init_app(app)

voyceSchemas = Voyce_Schema(many=True)
voyceSchema = Voyce_Schema()


@app.route('/read', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        searchquery =  request.json["serial"]

        if searchquery:
            results = Voyce.query.filter(Voyce.SN.icontains(searchquery) ).all()
        else:
            results =  Voyce.query.all()
        out = voyceSchemas.dump(results)
        response = jsonify(out)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    


@app.route('/create', methods=['POST','GET'])
def create():
    output = {
    "Command": "get",
    "Output": {
        "0x954A00E7B0026": {
            "name": "LL 001",
            "wifiAddress": "c4:2a:d0:5f:ca:b0",
            "serialNumber": "F9FZ5J5KMF3M"
        },
        "0x1459941A41402E": {
            "name": "LL 002",
            "wifiAddress": "4c:b9:10:97:e9:ed",
            "serialNumber": "GG7FFKTQQ1GC"
        },  
        "0x1459FR41A41402E": {
            "name": "LL 03",
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
    
    addToDB="False"
    deviceCount =len(output['Output'])-1
    print(deviceCount)

          
    if request.method == 'POST':
        addToDB = request.json["accept"]
         
        if addToDB =="True":
            print(addToDB) 
            for name, info in output['Output'].items():
                if name != 'Errors':
                    data = Voyce( Hospital=info['name'].split(' ')[0],
                            Device = info['name'].split(' ')[1],
                            SN = info['serialNumber'],
                            MAC =info['wifiAddress'],
                            DateAdded = date.today())
                    db.session.add(data)
                    db.session.commit()

        return jsonify({'results': 'success'})
    print(addToDB) 
    if request.method == 'GET':
        try:
        
            # cmd = 'cfgutil -f --format JSON get name serialNumber wifiAddress'
            # result = subprocess.run(
            #     cmd, shell=True, capture_output=True, text=True, check=True)
            # output = json.loads(str(result.stdout))

            # if addToDB:
            #     print("triggered "+ str( addToDB))
            
            # df.to_sql(name='voyce_device', con=db.engine, index=False,if_exists= 'append')
            # col=[]
            # added=[]
            # for index in df.index:
            #     col.append( f"Device {df['Device'][index]} at {df['Hospital'][index]}  has been added")
                
            #     added.append({"response" : col[index] })
            response= jsonify({"results": f"{deviceCount} devices ready"})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response


        except subprocess.CalledProcessError:
            return jsonify({'results': 'nothing to add'})
        
    
@app.route('/edit/<id>/', methods=["PUT"])
def edit(id):
    article = Voyce.query.get(id)
    
    hospital = request.json["hospital"]
    device = request.json["device"]
    
    article.Hospital = hospital
    article.Device = device
    db.session.commit()
    response =voyceSchema.jsonify(article)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    
