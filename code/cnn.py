# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:13:55 2022

@author: Ana
"""
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D

map_loc = '/mnt/e/DS//Predicting-enzyme-function/dataset/test/'
bin_seq = []
IDs = ['A0A0A1GKA2', 'A0A0A2IJP3', 'A0A0A2JY25', 'A0A0A2JYK3']
y = [1, 1, 2, 2]


for seqID in IDs:
    bin_seq.append(np.loadtxt(map_loc+seqID+'.txt'))

model = Sequential()

model.add(Convolution2D(4, 3))