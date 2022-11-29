# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 13:47:22 2022

@author: Ana
"""

keys = ['1', '2', '3', '4', '5', '6', '7']
aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

pssm_keys = ['-','A','B','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','U','*','O','J']

pssm_idx = [i for i in range(len(pssm_keys)) if pssm_keys[i] in aa]