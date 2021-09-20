# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 23:34:09 2021

@author: shubh
"""
import pandas as pd

massages = pd.read_csv("smsspamcollection/SMSSpamCollection",sep='\t',names=['label',"massage"])