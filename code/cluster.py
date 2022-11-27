# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:47:27 2022

@author: Ana
"""
import argparse
import pandas as pd
import numpy as np


from Bio import Align
from Bio import SeqIO
from Bio import pairwise2

from constants import keys, aa

def checking():
    ...
    
def clustering(name, i):
    if type(name) is str:
        enzyme_list = []
        for enzyme in SeqIO.parse(name+'.fasta', 'fasta'):
            enzyme_list.append(enzyme)
    else:
        enzyme_list = name
        
    df = pd.DataFrame({'seq':enzyme_list})
    df['len'] = df['seq'].apply(lambda x: len(x.seq))
    df = df.sort_values('len', ascending=False).reset_index(drop=True)
    print(df)