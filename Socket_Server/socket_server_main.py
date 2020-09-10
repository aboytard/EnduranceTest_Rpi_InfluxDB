
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:48:12 2020

@author: ubuntu
"""
import socket, sys, threading
import time
from datetime import datetime
import RPi.GPIO as GPIO
import csv
import class_thread_client
import class_thread_emission
import writing_influxDB_jointState
import writing_influxDB_BtnMasher_robot


''' Importing a module from another folder'''
sys.path.append('/home/ubuntu/Repo_BtnMasher_Rpi')
import BtnDefinition


## def run():
    ################# Step 0 #####################
# Initiialize the servor - Setup the socket :
HOST = '10.4.11.117'
PORT = 5005
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "The link with the chosen address socket failed."
    sys.exit()
print "Servor ready, waiting for answer.."
mySocket.listen(5)
###############################################


######################## Starting main ##############

while 1:    
    ######### Step 1  ##########
    # Accept the connection of client
    connexion, adresse = mySocket.accept()
    ####################################################
    
    ###########################################
    ######### Step 2 #########################
    # Creation of the database we want to write in in influxDB
    
    ##client_db = writing_influxDB_jointState.write_into_db() ## if we want to deal with the jointState
    ## with fewer information
    client_db=writing_influxDB_BtnMasher_robot.write_into_db()
    
    ###########################################
    ########## Step 3 #########################
    # Creation of a thread to deal with the connection (enable the client to end the connection):
    # This thread is also listening to the client
    conn_client = {}  
    th_Client = class_thread_client.ThreadClient(connexion,conn_client,client_db)
    th_Client.setDaemon(True)
    th_E = class_thread_emission.Thread_Send_BtnState(connexion,"Btn1","Btn2")
    th_E.setDaemon(True)
    ## The client is also writing the jointState in InfluxDb
    th_Client.start()
    th_E.start()
    
    # Memorize connection in dictionnary 
    it = th_Client.getName()        # id of thread
    th_Client.conn_client[it] = connexion
    print "Client %s connected, adresse IP %s, port %s." %\
    (it, adresse[0], adresse[1])
    # Dialogue avec le client :
    connexion.send("You are connected. Send your message.")
    ###########################################


    ###########################################

    ###########################################
    
        ###########################################
    ######### Step 4#########################
    # Launch the BtnMasherApplication
    import BtnMasherApplication
    ###########################################


    ###########################################
    ######### Step 3 #########################
    # Creation of a real-time analysor
    
    ###########################################
    ######### Step 5 ##########################
    # Creation of a thread that will write the information in a file / whatever for now


    ###########################################
    

#
#    th_Client.stop()
#    th_E.stop()