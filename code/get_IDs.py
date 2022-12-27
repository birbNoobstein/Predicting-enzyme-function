#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:17:36 2022

@author: ana
"""

import numpy as np
import subprocess as sp
from constants import path_to_bin, path_to_pssmP, path_IDbin, path_IDpssm

def extract_IDs(path, path_ID):
    names = sp.run(['ls', path], capture_output=True).stdout
    names = str(names).lstrip('b\'').rstrip('\'\\n').split('\\n')
    name_split = lambda x: x.split('.')[0]
    names = np.array([name_split(x) for x in names])
    np.savetxt(path_ID, 
               names,
               fmt='%s')
    

def main():
    extract_IDs(path_to_bin, path_IDbin)
    extract_IDs(path_to_pssmP, path_IDpssm)


if __name__ == '__main__':
    main()