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
'''
add raw input?
'''
PushBtn1_Port = 19
PushBtn2_Port = 29

GPIO.setup(PushBtn1_Port, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(PushBtn2_Port, GPIO.IN,pull_up_down = GPIO.PUD_UP)

bool_send_msg_Btn1State = False
bool_send_msg_Btn2State = False