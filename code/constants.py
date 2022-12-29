# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 13:47:22 2022

@author: Ana
"""

keys = ['1', '2', '3', '4', '5', '6', '7']
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
aa_order = [5, 0, 17, 9, 10, 7, 15, 16, 1, 12, 11, 13, 8, 14, 6, 2, 3, 4, 19, 18]

pssm_keys = ['-','A','B','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','U','*','O','J']

pssm_idx = [i for i in range(len(pssm_keys)) if pssm_keys[i] in aa]

path_to_fasta = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/fasta/'
path_to_bin = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/binary/'
path_to_pssmR = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/pssm_raw/'
path_to_pssmP = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/pssm_parsed/'


path_truths = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/IdEc.csv'

path_ID = '/media/ana/New Volume/DS/Predicting-enzyme-function/data_ID.txt'
path_IDbin = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/ID_bin.txt'
path_IDpssm = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/ID_pssm.txt'

path_ctd = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/ctd.csv'
path_aac = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/aac.csv'
path_ngram = '/media/ana/New Volume/DS/Predicting-enzyme-function/dataset/ngram.csv'