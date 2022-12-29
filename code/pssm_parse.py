# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:21:41 2022

@author: Ana
"""
#import matplotlib.pyplot as plt
import numpy as np


from constants import pssm_idx, path_to_pssmR, path_to_pssmP, path_ID

""" 
    PARSING PSSM MATRICES FROM PSI-BLAST OUTPUT
"""

def get_IDs(path):
    IDs = []
    with open(path) as handle:
        for line in handle.readlines():
            IDs.append(line.split('.')[0].strip())

    np.savetxt(path_ID, 
               np.array(IDs),
               fmt='%s')
    return IDs

def clean(x):
    if x[-1] == ',':
        return int(x[0:-1])
    return int(x)

def get_pssm(ID, clean):
    pssm = []
    pause = True
    with open(path_to_pssmR+ID+'.asn') as handle:
        for line in handle.readlines():
            if not pause:
                if line.strip() == '},':
                    pause = True
                else:
                    pssm.append(line.strip())
            if line.strip() == 'scores {':
                pause = False
    pssm = clean(np.array(pssm))
    pssm = pssm.reshape(int(pssm.shape[0]/28), 28)[:,pssm_idx]
    np.savetxt(path_to_pssmP+ID+'.txt', pssm, fmt='%.2f')



def main():
    IDs = get_IDs(path_ID)
    cln = np.vectorize(clean)
    for ID in IDs:
       get_pssm(ID, cln)

    
if __name__ == '__main__':
    main()