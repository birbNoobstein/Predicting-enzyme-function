# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:13:55 2022

@author: Ana
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
"""
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
"""


data_loc = 'E:/DS/Predicting-enzyme-function/dataset/test/'

#model = Sequential()

#model.add(Convolution2D(4, 3))

def main():
    # POPRAVI PATH
    uniEC = pd.read_csv('E:/DS/Predicting-enzyme-function/dataset/IdEc.csv',
                        header=0)
    names = uniEC['ID'].apply(lambda x: data_loc + x + '.txt')
    
    classes_real = pd.get_dummies(uniEC['EC'].apply(lambda x: x[0]))
    
    #print(names)
    #print(classes_real)
    """
    f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
    image = np.loadtxt(data_loc+'Q9AL94'+'.txt')
    image2 = np.loadtxt(data_loc+'P33229'+'.txt')
    image3 = np.loadtxt(data_loc+'Q3KJK8'+'.txt')
    image4 = np.loadtxt(data_loc+'O31819'+'.txt')
    ax1.imshow(image)
    ax2.imshow(image2)
    ax3.imshow(image3)
    ax4.imshow(image4)
    """
    plt.rcParams["figure.figsize"] = (3,20)
    img = plt.imshow(np.loadtxt(data_loc+'Q9J5A4'+'.txt'))
    plt.savefig(data_loc+'Q9J5A4_img.png')
    

if __name__ == '__main__':
    main()