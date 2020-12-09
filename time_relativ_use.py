#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:28:26 2020

@author: ubuntu
"""

import datetime

t0 = datetime.datetime.utcnow()
t1=t0
t2=t0
time_start = t0
time_t1_plus_delta_t = t0
time_zero = datetime.timedelta(0,0,0)
list_msg_touched = []
list_msg_untouched = []


def compare_time():
    L=list_msg_touched
    l=list_msg_untouched ## I had to put a intermediate list, without it, the program was not recognizing the element of the list
    t1 = datetime.datetime.strptime(L[0],'%Y-%m-%d %H:%M:%S.%f')
    t2 = datetime.datetime.strptime(l[0],'%Y-%m-%d %H:%M:%S.%f')
    if (time_t1_plus_delta_t - t1 > time_zero and time_t1_plus_delta_t - t2 <time_zero):
        print ('Btn was well pressed by the robot')
        return True
    else:
        print('write into database error driver')
        return False
        
