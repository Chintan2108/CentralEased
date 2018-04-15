# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:29:42 2018

@author: asus
"""

import json

from flask import Flask, request, Response
app = Flask(__name__)

from main import predict, decode
import pandas as pd

@app.route('/api', methods=['POST'])
def api():
    
    print('in')
    
    postData = request.json     
    imgData = postData['imgData']    
    
    #print(imgData)    
    
    dbs = {} 
    
    label, lblname = predict(decode(imgData))
    print(lblname)
    df = pd.read_csv('final.csv', index_col = 0)
    
    indexValues  = df.columns.values
    data = df.loc[label]  
    dbNames = list(set(indexValues) - set(['label', 'name']))
    
    for dbName in dbNames:
        
        db = {}       
        ref = pd.read_csv('database-new/' + dbName + '.csv')        
        reqId = data[dbName]        
        reqData = ref.loc[ref['id'] == reqId]
        #print(reqData)       
                
        for column in reqData:        
            if not column == 'image':            
                value = reqData[column].tolist()               
                if not value==[]:
                    value = value[0]                   
                    #print(type(value))                   
                    if isinstance(value, long):
                        value = str(value).strip('L')                   
                    #print(column, value)
                    db[column] = value
        if not db == {}:
            dbs[dbName] = db   
    
    print(dbs)
    
    return Response(response=json.dumps(dbs), status=200, mimetype="application/json")
        
          
    
    
    