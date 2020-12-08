#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:28:26 2020

@author: ubuntu
"""

import datetime

t0 = datetime.datetime.utcnow()

time_start = t0
time_t1 = t0
time_t1_plus_delta_t = t0
time_t2 = t0
time_zero = datetime.timedelta(0,0,0)

def compare_time():
    if (time_t1_plus_delta_t - time_t1 > time_zero and time_t1_plus_delta_t - time_t2 <time_zero):
        print ('Btn was well pressed by the robot')
        return True
    else:
        print('write into database error driver')
        return False
        

