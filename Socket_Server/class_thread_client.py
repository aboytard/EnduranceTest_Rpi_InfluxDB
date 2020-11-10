#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:49:42 2020

@author: ubuntu
"""

import socket, sys, threading
"""Create the DB and see how we want to print the data"""
import writing_influxDB_jointState


stop_thread = False

class ThreadClient(threading.Thread):
    '''Use a thread object to deal with the connection of clients'''
    def __init__(self, conn,conn_client,client_db):
        threading.Thread.__init__(self)
        self.connexion = conn
        self.conn_client = conn_client ## put it as a attribute of the thread
        self.client_db = client_db
        
    def run(self):
        # Dialog with the client :
        nom = self.getName()        # get the name of each thread client connected
        while 1:
            msgClient = self.connexion.recv(4096)
            if msgClient.upper() == "END" or msgClient =="":
                break
            message =  "%s" % (msgClient)
            print message
            json_boy_jointState = writing_influxDB_jointState.split_socketmsg_into_jsonbody(message)
            writing_influxDB_jointState.write_data(json_boy_jointState,self.client_db)
            # Make the msg followed for all the clients :
            for cle in self.conn_client:
                if cle != nom:      # ne pas le renvoyer à l'émetteur
                    self.conn_client[cle].send(message)
                    
        # Fermeture de la connexion :
        self.connexion.close()      # cut connexion from the server with client
        del self.conn_client[nom]        # supprimer son entrée dans le dictionnaire
        print "Client %s disconnected." % nom
        # Le thread se termine ici    