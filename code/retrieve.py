#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 17:17:39 2022

@author: ana
"""
import numpy as np
import pandas as pd

path = '/media/ana/New Volume/DS/Predicting-enzyme-function/'
p_all = 'data_ID.txt'
p_done = 'data_ID_done.txt'

with open(path+p_all) as handle:
    all_IDs = set(ID.split('.')[0] for ID in handle.readlines())
    
aac = pd.read_csv('../dataset/aac.csv', index_col=0)
ctd = pd.read_csv('../dataset/ctd.csv', index_col=0)
data = pd.read_csv('../dataset/ngram.csv', index_col=0)
data = data.join(ctd[ctd.columns[0:-1]])
data = data.join(aac[aac.columns[0:-1]])
    
IDs = all_IDs.difference(set(data.index))
print(len(IDs))

#for ID in IDs:
    