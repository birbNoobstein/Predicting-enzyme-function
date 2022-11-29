# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:21:41 2022

@author: Ana
"""
import numpy as np
from constants import pssm_idx

pssm = []
pause = True
with open('E:/DS/Predicting-enzyme-function/dataset/test/A0A0A2JY30.asn') as handle:
    for line in handle.readlines():
        if not pause:
            if line.strip() == '},':
                pause = True
            else:
                pssm.append(line.strip())
        if line.strip() == 'scores {':
            pause = False
        
def clean(x):
    if x[-1] == ',':
        return int(x[0:-1])
    return int(x)

cln = np.vectorize(clean)

pssm = cln(np.array(pssm))
pssm = pssm.reshape(int(pssm.shape[0]/28), 28)[:,pssm_idx]
np.set_printoptions(threshold=np.inf)
print(pssm)