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


''' Import the time_relativ_use'''
import time_relativ_use

'''Use the thread defined in the socket.server.main'''

 
def my_callback_Btn1(channel):                
    print "Btn1" # To see on the shell if we match with the Btn Pressing noise
    time_relativ_use.time_t1_plus_delta_t = datetime.datetime.utcnow() # Log the time of the Btn Pressing in another module so it can be easily found
    BtnDefinition.bool_send_msg_Btn1State = True #enable the Thread_Send_Btn_State to send the socket message
    
    
    
def my_callback_Btn2(channel): 
    print "BTN2" 
    time_relativ_use.time_t1_plus_delta_t = datetime.datetime.utcnow()
    BtnDefinition.bool_send_msg_Btn2State = True
    


#there is 2 second between Btn1_Pressed and Btn2_Pressed so the bouncetime can be define inferior to 1000ms
GPIO.add_event_detect(BtnDefinition.PushBtn1_Port, GPIO.BOTH, callback=my_callback_Btn1, bouncetime = 500)  
GPIO.add_event_detect(BtnDefinition.PushBtn2_Port, GPIO.BOTH, callback=my_callback_Btn2, bouncetime = 500)



"""
add variable time of simulation
raw input ??
"""


try:
    sleep(6000)         # DEFINE THE TIME OF SIMULATION
    print "Time's up. Finished!"  
except KeyboardInterrupt:
    GPIO.cleanup()
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
        
