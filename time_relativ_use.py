#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:28:26 2020

@author: ubuntu
"""
import sys
import datetime

"""Create the DB and see how we want to print the data"""
sys.path.append('/home/ubuntu/Repo_BtnMasher_Rpi/Socket_Server_Rpi')
import writing_influxDB_BtnMasher_robot


t0 = datetime.datetime.utcnow()
t1=t0
t2=t0
time_start = t0
time_t1_plus_delta_t = t0
time_zero = datetime.timedelta(0,0,0)
list_msg_touched = []
list_msg_untouched = []


def compare_time(client_db):
    L=list_msg_touched
    l=list_msg_untouched ## I had to put a intermediate list, without it, the program was not recognizing the element of the list
    t1 = datetime.datetime.strptime(L[0],'%Y-%m-%d %H:%M:%S.%f') # have the string from the message back to the format we want to compare with
    t2 = datetime.datetime.strptime(l[0],'%Y-%m-%d %H:%M:%S.%f')
    if (time_t1_plus_delta_t - t1 > time_zero and time_t1_plus_delta_t - t2 <time_zero):
        print ('Btn was well pressed by the robot') # to see that we were able to compare time
        L[0]=time_t1_plus_delta_t # having the time the Btn_Pressed was detected by the Rpi
        L.append(True)
        data=writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(L)
        writing_influxDB_BtnMasher_robot.write_data(data,client_db)
    else:
        print('write into database error driver')
        l[0]=time_t1_plus_delta_t
        l.append(False)
        data=writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(l)
        writing_influxDB_BtnMasher_robot.write_data(data,client_db)

#I have to initialise it in case we are starting the test from a pose in the area of the btn        
L=[str(t0), 'Btn1', 'touched']
t1 = datetime.datetime.strptime(L[0],'%Y-%m-%d %H:%M:%S.%f')
