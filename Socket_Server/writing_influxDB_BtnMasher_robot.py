#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:49:31 2020

@author: ubuntu
"""

### Module to set the data we want to write in InfluxDB and in the logfile

from influxdb import InfluxDBClient
import datetime
import class_thread_client
from dateutil.parser import parse



def write_into_db():
    #creation of the db and define the client of the databases in influxdb
    client=InfluxDBClient(host="localhost",port="8086")
    client.create_database('BtnMasherApplication_DB_Test') ## Always writing in the same DB for now
    print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
    client.switch_database('BtnMasherApplication_DB_Test')
    return client




def split_socketmsg_into_jsonbody(list_msg):
    # Convert the list of information into json_body to enable writing in influxdb
    json_body_jointState = [
            {
                "measurement": "BtnMasherApplication_Test_v3", # choosing the name of the measurements before a test
                "tags": {
                    "requestName": "Btn_State_Test",
                    "requestType": "GET"
                },
                "time":list_msg[0], # getting the time the button was pressed (detected by the Rpi)
                 "fields": {
                    "Btn_name": list_msg[1],
                    "Btn_State": list_msg[2],
                    "In_Time_Interval": list_msg[3]
                            }
            }
        ]
    return json_body_jointState


def write_data(data,client):
    #write the data in Influxdb thanks to the client we created
    client.write_points(data)

