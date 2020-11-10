#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:18:18 2020

@author: mathieu
"""

# Use thread to deal with parallel connection

import socket, sys, threading
import time
from datetime import datetime
import RPi.GPIO as GPIO
import csv

            

class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        # Dialog with the client :
        nom = self.getName()        # get the name of each thread client connected
        while 1:
            msgClient = self.connexion.recv(1024)
            t_currentState = msgClient
            print(t_currentState)
            try:
                th_Writer.line_add_csv = th_Writer.split_msg_towrite(t_currentState,head)
            except:
                pass
            if msgClient.upper() == "END" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient)
            print message
            # Faire suivre le message à tous les autres clients :
            for cle in conn_client:
                if cle != nom:      # ne pas le renvoyer à l'émetteur
                    conn_client[cle].send(message)
                    
        # Fermeture de la connexion :
        self.connexion.close()      # cut connexion from the server with client
        del conn_client[nom]        # supprimer son entrée dans le dictionnaire
        print "Client %s disconnected." % nom
        # Le thread se termine ici    
       
        
class ThreadEcritureCsv(threading.Thread):
   '''object thread dealing with the writing of the log file in the Rpi'''
   def __init__(self, line_add_csv, name_file):
       threading.Thread.__init__(self)
       self.line_add_csv = line_add_csv
       self.name_file = name_file
       self.list_line_add = [line_add_csv]
       
   def run(self):
       i=0
       while 1:  
           
           try:
               file = open(self.name_file,'aw') # Open the file
           except :
               pass
           writer = csv.writer(file) ## Have to put there to not have error
           if self.line_add_csv != self.list_line_add[-1]:
               writer.writerow(self.line_add_csv)
               self.list_line_add.append(self.line_add_csv) ## we add in only after writing it
           time.sleep(1)
           i += 1
           
   def split_msg_towrite(self,msgServer,column_towrite):
       msg_writen = msgServer.split(";")
       if msg_writen[0] == column_towrite[0]:
           return [msg_writen[1],'','','']
       if msg_writen[0] == column_towrite[1]:
           return ['',msg_writen[1],'','']
       if msg_writen[0] == column_towrite[2]:
           return ['','',msg_writen[1],'']
       if msg_writen[0] == column_towrite[3]:
           return ['','','',msg_writen[1]]
       else:
           print("No Message to write??")
           pass   

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


# Waiting and take care of clients:
conn_client = {}                # Dictionnary of client's connection
stop_thread = False

######################## Starting main ##############

while 1:    
    ######### Step 1  ##########
    # Accept the connection of client
    connexion, adresse = mySocket.accept()
    ####################################################
    ########## Step 2 #########################
    # Creation of a thread to deal with the connection (enable the client to end the connection):
    # This thread is also listening to the client
    th_Client = ThreadClient(connexion)
    th_Client.start()

    ###########################################
    ######### Step 4 #########################
    # Creation of a thread that deal with the BtnMasherApplication
    
    ###########################################
    ######### Step 5 ##########################
    # Creation of a thread that will write the information in a csv file
    head = ['th_Btn1.name','th_Btn2.name','position 2','position 3'] #### What information do we want
# TO DO    ## Waiting that both application work separately before dealing with mutex
    th_Writer = ThreadEcritureCsv(head,'Test_Rpi_Simulation.csv')
    th_Writer.start()

    ###########################################
    
    # Mémorize connection in dictionnary 
    it = th_Client.getName()        # id of thread
    conn_client[it] = connexion
    print "Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1])
    # Dialogue avec le client :
    connexion.send("You are connected. Send your message.")

    


