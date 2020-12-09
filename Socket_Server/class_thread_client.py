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
import datetime

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
#        self.list_msg_touched = []
#        self.list_msg_untouched = []
        
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
                if self.list_msg[2]=='touched':
                    time_relativ_use.list_msg_touched = self.list_msg
                    print("Point11")
#                    print(datetime.datetime.strptime(self.list_msg[0],'%Y-%m-%d %H:%M:%S.%f'))
#                    time_relativ_use.time_t1 = datetime.datetime.strptime(str(self.list_msg[0]),'%Y-%m-%d %H:%M:%S.%f')
#                    print("time_relativ_use.time_t1 = ", time_relativ_use.time_t1)
                if self.list_msg[2]=='untouched':
#                    print('Point 0')
                    time_relativ_use.list_msg_untouched = self.list_msg
#                    time_relativ_use.time_t2 = datetime.datetime.strptime(str(self.list_msg[0]),'%Y-%m-%d %H:%M:%S.%f')
                    print('POINT 12')
                    time_relativ_use.compare_time()
            except:
                pass
#'''            try:
#                if compare == True:
#                    print("Point 1")
#                    self.list_msg.append(True)
#                    data = writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(self.list_msg)
#                    writing_influxDB_BtnMasher_robot.write_data(data,self.client_db)
#                    print("Good job pilz")
#                else:
#                    print("Point 2")
#                    self.list_msg.append(False)
#                    data = writing_influxDB_BtnMasher_robot.split_socketmsg_into_jsonbody(self.list_msg)
#                    writing_influxDB_BtnMasher_robot.write_data(data,self.client_db)
#                    print("Sorry but issue")
#            except:
#                ## if we are not having the msg of the jointstate, it is because we are receiving the timeReference
#                #print("solve issue")
#                pass
#'''
            ## add if I want to deal with a time relativ
#                print("okidoki?")
#                print message
#                self.timeReference = message
#                print self.timeReference
#                print("OKIDOKI")
            # Make the msg followed for all the clients :
            ######################
            for cle in self.conn_client:
                if cle != nom:      # do not send it back to the one who emit it
                    self.conn_client[cle].send(message)
                    
        # CLose the connection :
        self.connection.close()      # cut connexion from the server with client
        del self.conn_client[nom]        # suppress his entrance from the dictionnary
        print "Client %s disconnected." % nom
        # Le thread se termine ici    