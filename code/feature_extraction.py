# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:20:26 2022

@author: Ana
"""

import pandas as pd
from Bio import SeqIO
from constants import path_ID, path_to_fasta, path_ctd, path_aac, path_ngram, path_truths
from protlearn.features import ctd, ngram, aac
from protlearn.preprocessing import remove_unnatural

""" 
    EXTRACT FEATURES USING PROTLEARN
"""

def append_truths(features):
    IdEc = pd.read_csv(path_truths, index_col='ID')
    IdEc['class'] = IdEc['EC'].apply(lambda x: x.split('.')[0].strip())
    features['class'] = pd.Series(features.index, index=features.index).map(lambda x: IdEc.loc[x, 'class'])
    return features

def features_write(IDs, func, path):
    features = None
    for ID in IDs:
        seq = [str(s.seq) for s in SeqIO.parse(path_to_fasta+ID+'.fasta', 'fasta')]
        seq = remove_unnatural(seq)
        if len(seq) > 0:
            e1 = func(seq)
            
            if features is None:
                features = (pd.DataFrame(e1[0], columns=[e+'c' for e in e1[1]], index=[ID]))
               
            else:
                features = pd.concat([features, pd.DataFrame(e1[0], columns=[e+'c' for e in e1[1]], index=[ID])])
                

    
    features = append_truths(features)
    features.to_csv(path)

def main():
    with open(path_ID) as handle:
        IDs = [ID.strip() for ID in handle.readlines()]
    
    features_write(IDs, ctd, path_ctd)
    features_write(IDs, aac, path_aac)
    features_write(IDs, ngram, path_ngram)

if __name__ == '__main__':
    main()