#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:45:50 2020

@author: ubuntu
"""

import RPi.GPIO as GPIO
from time import sleep  
import time
import datetime
import sys

'''Import the module to have the Btn Definition'''
import BtnDefinition 

"""Get the last BtnMasherApplication_DB and add a incremental number on it"""
#import Logger_BtnMasherApplication
#Logger_BtnMasherApplication.logger.addHandler(Logger_BtnMasherApplication.file_handler) # Define in which way and where we want to log the data 

"""Create the DB and see how we want to print the data"""
sys.path.append('/home/ubuntu/Repo_BtnMasher_Rpi/Socket_Server_Rpi')
import writing_influxDB_BtnMasher_robot
client=writing_influxDB_BtnMasher_robot.write_into_db()

''' Import the time_relativ_use'''
import time_relativ_use

'''Use the thread defined in the socket.server.main'''

 
def my_callback_Btn1(channel):                
    print "Btn1"
#    """Call a function in the writing_json_body module that adapt with data we want to write in the DB"""
#    writing_influxDB_BtnMasher_robot.write_data(writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(writing_influxDB_BtnMasher_robot.list_msg),client)
#    """Call a function in the Logger_BtnMasherApplication module that adapt with data we want to write in the logfile"""
#    Logger_BtnMasherApplication.logger.info(writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(writing_influxDB_BtnMasher_robot.list_msg))
    time_relativ_use.time_t1_plus_delta_t = datetime.datetime.utcnow()
    BtnDefinition.bool_send_msg_Btn1State = True
    
    
    
def my_callback_Btn2(channel): 
    print "BTN2" 
#    """Call a function in the writing_json_body module that adapt with data we want to write in the DB"""
#    writing_influxDB_BtnMasher_robot.write_data(writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(writing_influxDB_BtnMasher_robot.list_msg),client)
#    """Call a function in the Logger_BtnMasherApplication module that adapt with data we want to write in the logfile"""
#    Logger_BtnMasherApplication.logger.info(writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(writing_influxDB_BtnMasher_robot.list_msg))
    time_relativ_use.time_t1_plus_delta_t = datetime.datetime.utcnow()
    BtnDefinition.bool_send_msg_Btn2State = True
    


        
GPIO.add_event_detect(BtnDefinition.PushBtn1_Port, GPIO.BOTH, callback=my_callback_Btn1, bouncetime = 500) 
GPIO.add_event_detect(BtnDefinition.PushBtn2_Port, GPIO.BOTH, callback=my_callback_Btn2, bouncetime = 500)



"""
add variable time of simulation
raw input ??
"""

i=0
try:
    sleep(6000)         # wait 300 seconds  ## DEFINE THE TIME OF SIMULATION
    print "Time's up. Finished!"  
except KeyboardInterrupt:
    GPIO.cleanup()
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
        
