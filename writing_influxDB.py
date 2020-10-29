#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:46 2020

@author: ubuntu
"""

### Module to set the data we want to write in InfluxDB and in the logfile

from influxdb import InfluxDBClient
import datetime
import BtnDefinition
'''
From BtnDefinition I find which Port I am using and how to use them afterwards
'''

###
'''
creation de la DB
'''
def write_into_db():
    client=InfluxDBClient(host="localhost",port="8086")
    client.create_database('BtnMasherApplication_DB_Test') ## Always writing in the same DB for now
    print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
    client.switch_database('BtnMasherApplication_DB_Test')
    return client


def json_body_define(PushBtn_Port):
    print('lancement?')
    if PushBtn_Port == BtnDefinition.PushBtn1_Port:
        json_body = [
            {
                "measurement": "NewResponse",
                "tags": {
                    "requestName": "Btn1_Pressed_Time",
                    "requestType": "GET"
                },
                "time":datetime.datetime.utcnow(),
                 "fields": {
                    "Btn1_Pressed": True,
                    "Btn2_Pressed": False
                            }
            }
        ]
    if PushBtn_Port == BtnDefinition.PushBtn2_Port:       
        json_body = [
            {
                "measurement": "NewResponse",
                "tags": {
                    "requestName": "Btn1_Pressed_Time",
                    "requestType": "GET"
                },
                "time":datetime.datetime.utcnow(),
                 "fields": {
                    "Btn1_Pressed": False,
                    "Btn2_Pressed": True
                            }
            }
        ]
    return json_body

def write_data(data,client):
    print('on ecrit?')
    client.write_points(data)

#json_body = json_body_define(NameFunctionCalling)
#client.write_points(json_body)
#results=client.query('SELECT * FROM NewResponse')
#login_points=list(results.get_points(measurement='NewResponse',tags={"requestName": "Login"}))
#print(login_points)    

