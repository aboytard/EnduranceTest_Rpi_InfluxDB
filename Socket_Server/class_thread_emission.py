#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:35:56 2020

@author: ubuntu
"""

import socket,sys,threading
import time
import datetime
import RPi.GPIO as GPIO
import BtnDefinition

sys.path.append('/home/ubuntu/Repo_BtnMasher_Rpi')
import time_relativ_use


'''Define the class that will send the BtnState coming from the BtnMasherApplication to the computer '''
'''I could just have one button and two thread running but I chose to define the two button in this class to use only one thread '''
class Thread_Send_BtnState(threading.Thread):
    
    def __init__(self,conn,name_Btn1,name_Btn2):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.name_Btn1 = name_Btn1
        self.name_Btn2 = name_Btn2
        self.bool_position_Btn1 = True
        self.bool_position_Btn1_sendMsg = False
        self.bool_position_Btn2 = True
        self.bool_position_Btn2_sendMsg = False
        self.msg = "pressed"
        
    def run(self):
        while 1:
            if BtnDefinition.bool_send_msg_Btn1State == True:
                self.connexion.send(str(time_relativ_use.time_t1_plus_delta_t)+";"+self.name_Btn1+";"+self.msg)
                BtnDefinition.bool_send_msg_Btn1State = False # we want the socket message to be sent only one
            if BtnDefinition.bool_send_msg_Btn2State == True:
                self.connexion.send(str(time_relativ_use.time_t1_plus_delta_t)+";"+self.name_Btn2+";"+self.msg)
                BtnDefinition.bool_send_msg_Btn2State = False

                
        
