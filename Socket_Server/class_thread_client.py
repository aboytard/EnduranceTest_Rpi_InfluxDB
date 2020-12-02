#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:49:42 2020

@author: ubuntu
"""

import socket, sys, threading
"""Create the DB and see how we want to print the data"""
#import writing_influxDB_jointState
import writing_influxDB_BtnMasher_robot
import time

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
        
    def run(self):
        # Dialog with the client :
        nom = self.getName()        # get the name of each thread client connected
        while 1:
            msgClient = self.connection.recv(4096)
            if msgClient.upper() == "END" or msgClient =="":
                break
            message =  "%s" % (msgClient)
            print message
            try :
                list_msg = message.split(";")
                if list_msg[2]=='touched':
                    time_relativ_use.time_t1 = time.time()
                if list_msg[2]=='untouched':
                    time_relativ_use.time_t2 = time.time()
                    compare = time_relativ_use.compare_time()
                    if compare == True:
                        list_msg.append(True)
                        data = writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(list_msg)
                        self.client_db.write_points(data)
                    else:
                        list_msg.append(False)
                        data = writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(list_msg)
                        self.client_db.write_points(data)
            except:
                ## if we are not having the msg of the jointstate, it is because we are receiving the timeReference
                #print("solve issue")
                pass
            ## add if I want to deal with a time relativ
#                print("okidoki?")
#                print message
#                self.timeReference = message
#                print self.timeReference
#                print("OKIDOKI")
            # Make the msg followed for all the clients :
            for cle in self.conn_client:
                if cle != nom:      # do not send it back to the one who emit it
                    self.conn_client[cle].send(message)
                    
        # CLose the connection :
        self.connection.close()      # cut connexion from the server with client
        del self.conn_client[nom]        # suppress his entrance from the dictionnary
        print "Client %s disconnected." % nom
        # Le thread se termine ici    