#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:42:44 2020

@author: ubuntu
"""

import logging
import datetime

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.INFO)

# define file handler and set formatter
file_handler = logging.FileHandler('/home/ubuntu/Repo_BtnMasher_Rpi/Log_BtnMasherApplication/logfile'+str(datetime.datetime.utcnow())+'.log')
formatter    = logging.Formatter('\n%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

