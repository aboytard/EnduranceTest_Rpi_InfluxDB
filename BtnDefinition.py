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
PushBtn2_Port = 31

GPIO.setup(PushBtn1_Port, GPIO.IN)
GPIO.setup(PushBtn2_Port, GPIO.IN)