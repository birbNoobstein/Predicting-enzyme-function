# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:18:57 2022

@author: Ana
"""

import numpy as np
import matplotlib.pyplot as plt


def normalize(mtx):
    vec = np.ndarray.sum(mtx, axis=1)
    print(vec)
    return mtx/vec

mtx = np.loadtxt('../dataset/test/A0A0A1GKA2.txt')

mtx_normed = normalize(mtx)
print(mtx_normed)
print(np.sum(mtx_normed, axis=0))
