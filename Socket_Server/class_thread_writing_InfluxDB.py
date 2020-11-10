#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:50:27 2020

@author: ubuntu
"""

def write_into_db():
    client=InfluxDBClient(host="localhost",port="8086")
    client.create_database('BtnMasherApplication_DB_Test') ## Always writing in the same DB for now
    print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
    client.switch_database('BtnMasherApplication_DB_Test')
    return client


def json_body_define(PushBtn_Port): # Add a parameter in order to change the name of the measurement for different test
    if PushBtn_Port == BtnDefinition.PushBtn1_Port:
        json_body = [
            {
                "measurement": "Test",
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
                "measurement": "Test",
                "tags": {
                    "requestName": "Btn2_Pressed_Time",
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
    client.write_points(data)