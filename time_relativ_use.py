#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:28:26 2020

@author: ubuntu
"""

import time

t0 = time.time()

time_start = t0
time_t1 = t0
time_t1_plus_delta_t = t0
time_t2 = t0

def compare_time():
    if (time_t1_plus_delta_t - time_t1 > 0 and time_t1_plus_delta_t - time_t2 <0):
        print ('Btn was well pressed by the robot')
    else:
        #        print('There is an issue')
        print('write into database error driver')
    pass


