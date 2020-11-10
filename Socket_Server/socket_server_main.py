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
import writing_influxDB_jointState

## def run():
    ################# Step 0 #####################
# Initiialize the servor - Setup the socket :
HOST = '172.21.19.109'
PORT = 50000
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
    client_db = writing_influxDB_jointState.write_into_db()
    ###########################################
    ########## Step 3 #########################
    # Creation of a thread to deal with the connection (enable the client to end the connection):
    # This thread is also listening to the client
    conn_client = {}  
    th_Client = class_thread_client.ThreadClient(connexion,conn_client,client_db)
    ## The client is also writing the jointState in InfluxDb
    th_Client.start()

    ###########################################
    ######### Step 1 #########################
    # Creation of the database we want to write in in influxDB
    client_db = writing_influxDB_jointState.write_into_db()
    ###########################################

    ###########################################
    ######### Step 4 #########################
    # Creation of a thread that deal with the BtnMasherApplication
    
    ###########################################
    ######### Step 5 ##########################
    # Creation of a thread that will write the information in a file / whatever for now


    ###########################################
    
    # Mémorize connection in dictionnary 
    it = th_Client.getName()        # id of thread
    th_Client.conn_client[it] = connexion
    print "Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1])
    # Dialogue avec le client :
    connexion.send("You are connected. Send your message.")