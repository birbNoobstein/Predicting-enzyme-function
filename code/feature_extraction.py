# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:57:14 2022

@author: Ana
"""
import pandas as pd

from Bio import SeqIO
from constants import path_ID, path_to_fasta, path_ctdc
from protlearn.features import ctdc
from protlearn.preprocessing import remove_unnatural

""" 
    EXTRACT FEATURES USING PROTLEARN
"""

def append_truths(features):
    IdEc = pd.read_csv('./dataset/IdEc.csv', index_col='ID')
    IdEc['class'] = IdEc['EC'].apply(lambda x: x.split('.')[0].strip())
    features['class'] = pd.Series(features.index, index=features.index).map(lambda x: IdEc.loc[x, 'class'])
    return features

def main():
    with open(path_ID) as handle:
        IDs = [ID.strip() for ID in handle.readlines()]
    
    features = None
    for ID in IDs:
        seq = [str(s.seq) for s in SeqIO.parse(path_to_fasta+ID+'.fasta', 'fasta')]
        seq = remove_unnatural(seq)
        if len(seq) > 0:
            extracted = ctdc(seq)
            if features is None:
                features = pd.DataFrame(extracted[0], columns=extracted[1], index=[ID])
            else:
                features = pd.concat([features, pd.DataFrame(extracted[0], columns=extracted[1], index=[ID])])
    features = append_truths(features)
    features.to_csv('./dataset/ctdc.csv')

if __name__ == '__main__':
    main()