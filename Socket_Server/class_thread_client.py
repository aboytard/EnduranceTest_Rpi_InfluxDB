#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:49:42 2020

@author: ubuntu
"""

import socket, sys, threading

### add the time_relativ_use
sys.path.append('/home/ubuntu/Repo_BtnMasher_Rpi')
import time_relativ_use

stop_thread = False

class ThreadClient(threading.Thread):
    '''Use a thread object to deal with the connection of clients'''
    def __init__(self, conn,conn_client,client_db):
        threading.Thread.__init__(self)
        self.connection = conn
        self.conn_client = conn_client ## put it as a attribute of the thread
        self.client_db = client_db
        self.timeReference = ""
        self.list_msg=[]

        
    def run(self):
        # Dialog with the client :
        #############
        nom = self.getName()        # get the name of each thread client connected
        while 1:
            msgClient = self.connection.recv(1024)
            if msgClient.upper() == "END" or msgClient =="":
                break
            message = "%s" %(msgClient)
            print "*" + msgClient + "*"
            try :
                self.list_msg = msgClient.split(";")
                if self.list_msg[2]=='touched': # knowing in which phase we are
                    #I am logging the whole message in order to process the time comparison during the time_interval the robot is moving from Btn1 to Btn2
                    time_relativ_use.list_msg_touched = self.list_msg 
                if self.list_msg[2]=='untouched':
                    time_relativ_use.list_msg_untouched = self.list_msg
                    time_relativ_use.compare_time(self.client_db)# comparing the time after the socket information flow is done / the other thread are done
            except:
                pass
            ######################
            for cle in self.conn_client:
                if cle != nom:      # do not send it back to the one who emit it
                    self.conn_client[cle].send(message)
                    
        # CLose the connection :
        self.connection.close()      # cut connexion from the server with client
        del self.conn_client[nom]        # suppress his entrance from the dictionnary
        print "Client %s disconnected." % nom
        # Le thread is done here   