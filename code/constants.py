# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 13:47:22 2022

@author: Ana
"""

keys = ['1', '2', '3', '4', '5', '6', '7']
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

pssm_keys = ['-','A','B','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','U','*','O','J']

pssm_idx = [i for i in range(len(pssm_keys)) if pssm_keys[i] in aa]

path_to_fasta = '/mnt/e/DS/Predicting-enzyme-function/dataset/fasta/'
path_to_bin = '/mnt/e/DS/Predicting-enzyme-function/dataset/binary/'
path_to_pssmR = '/mnt/e/DS/Predicting-enzyme-function/dataset/pssm_raw/'
path_to_pssmP = '/mnt/e/DS/Predicting-enzyme-function/dataset/pssm_parsed/'
path_to_pssmA = '/mnt/c/Users/Ana/AppData/Local/R/win-library/4.2/PSSMCOOL/extdata/'


path_preID = '/mnt/e/DS/Predicting-enzyme-function/ids.txt'
path_ID = '/mnt/e/DS/Predicting-enzyme-function/dataset/IDs.txt'

path_ctdc = '/mnt/e/DS/Predicting-enzyme-function/dataset/ctdc.csv'