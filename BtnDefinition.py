#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:36:55 2020

@author: ubuntu
"""
'''
Set up the Rpi
'''

import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BOARD)     # set up BOARD GPIO numbering 

#For this test, we are always using the same port so I decided to have them set in this module

PushBtn1_Port = 19 
PushBtn2_Port = 29

GPIO.setup(PushBtn1_Port, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(PushBtn2_Port, GPIO.IN,pull_up_down = GPIO.PUD_UP)

# I have define the sending of the socket here because it was easier to find the data
# However I am looking forward using future to have directly the value coming from the thread
bool_send_msg_Btn1State = False
bool_send_msg_Btn2State = False