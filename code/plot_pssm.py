# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:13:55 2022

@author: Ana
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from constants import aa_order
"""
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
"""


data_loc = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/test/'

#model = Sequential()

#model.add(Convolution2D(4, 3))

def main():
    plt.rcParams["figure.figsize"] = (15,50)
    
    f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
    image = np.loadtxt(data_loc+'Q9AL94'+'.txt')[:, aa_order]
    image2 = np.loadtxt(data_loc+'Q9BRT8'+'.txt')[:, aa_order]
    image3 = np.loadtxt(data_loc+'Q9BU02'+'.txt')[:, aa_order]
    image4 = np.loadtxt(data_loc+'Q9BUB5'+'.txt')[:, aa_order]
    ax1.imshow(image)
    ax2.imshow(image2)
    ax3.imshow(image3)
    ax4.imshow(image4)
    
    
    #img = plt.imshow(np.loadtxt(data_loc+'Q9J5A4'+'.txt')[:, aa_order])
    #plt.savefig(data_loc+'Q9J5A4_img.png')
    

if __name__ == '__main__':
    main()