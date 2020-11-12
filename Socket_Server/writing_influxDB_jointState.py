#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:46 2020

@author: ubuntu
"""

### Module to set the data we want to write in InfluxDB and in the logfile

from influxdb import InfluxDBClient
import datetime
import class_thread_client

###
'''
creation of the DB
'''
def write_into_db():
    client=InfluxDBClient(host="localhost",port="8086")
    client.create_database('BtnMasherApplication_DB_Test') ## Always writing in the same DB for now
    print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
    client.switch_database('BtnMasherApplication_DB_Test')
    return client




def split_socketmsg_into_jsonbody(message):
    list_msg = message.split(";")
    #time_relativ = list_msg[0] - timeReference ## This line is the reason why it is not working yet
    #Does not work properly because we have str(datetime)
    '''I need to reconvert the str(datetime) into datetime without loosing information    '''
    json_body_jointState = [
            {
                "measurement": "JointState",
                "tags": {
                    "requestName": "JointState",
                    "requestType": "GET"
                },
                "time":list_msg[0],
                 "fields": {
                    "Joint1": list_msg[1],
                    "Joint2": list_msg[2],
                    "Joint3": list_msg[3],
                    "Joint4": list_msg[4],
                    "Joint5": list_msg[5],
                    "Joint6": list_msg[6]
                            }
            }
        ]
    return json_body_jointState


def write_data(data,client):
    client.write_points(data)

#json_body = json_body_define(NameFunctionCalling)
#client.write_points(json_body)
#results=client.query('SELECT * FROM NewResponse')
#login_points=list(results.get_points(measurement='NewResponse',tags={"requestName": "Login"}))
#print(login_points)    

