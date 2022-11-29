# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:09:37 2022

@author: Ana
"""
import pandas as pd
import numpy as np
import subprocess as sp

from Bio import Align
from Bio import SeqIO
from Bio.Blast.Applications import NcbipsiblastCommandline

from constants import keys, aa
    
        
def extract_enzymes(ipt):
    
    by_class = {}
    
    extracted = {'ID':[], 'EC':[], 'len':[]}
    
    for key in keys:
        by_class.update({key:[]})
        
    with open(ipt) as handle:
        for seq in SeqIO.UniprotIO.UniprotIterator(handle):
            if 'recommendedName_ecNumber' in seq.annotations.keys():
                if len(seq.annotations['recommendedName_ecNumber']) == 1:
                    if not seq.annotations['recommendedName_ecNumber'][-1] == '-':
                        if len(seq.seq) > 50 and len(seq.seq) < 5000:
                            if 'sequence_fragment' not in seq.annotations.keys():
                                by_class[seq.annotations['recommendedName_ecNumber'][0].split('.')[0]].append(seq)
                                extracted['ID'].append(seq.id)
                                extracted['EC'].append(seq.annotations['recommendedName_ecNumber'][0]),
                                extracted['len'].append(len(seq.seq))

    for key in keys:  
        name = 'temp/by_class/class'+key+'.fasta'   
        SeqIO.write(by_class[key], name, "fasta")
        
    pd.DataFrame(extracted).to_csv('dataset/IdEc.csv', index=False)
    return by_class
    



def cluster(name):
    sp.run(['/mnt/e/DS/cdhit/cd-hit', '-i', name+'.fasta', '-o', name+'.fasta', '-c', '0.4',  '-n', '2', '-d', '0', '-T', '6'])
    
    
def split_traintest(names):
    train = []
    test = []
    sequences = []
    for name in names:
        sequences = sequences + list(SeqIO.parse(name, 'fasta'))
        
    
    for e, seq in enumerate(sequences):
        one_hot_encode(seq)
        SeqIO.write(seq, './dataset/fasta/'+seq.id+'.fasta', 'fasta')
        psi = NcbipsiblastCommandline(cmd='psiblast', 
                                      query='./dataset/fasta/'+seq.id+'.fasta', 
                                      db='./swiss/uniprot_sprot.fasta', 
                                      evalue=0.002, 
                                      num_iterations='3', 
                                      out_pssm='./dataset/pssm/'+seq.id+'.asn',
                                      num_threads=3)
        psi()
        x = np.random.uniform(low=0.0, high=1.0)
        if x <= 0.3:
            test.append(seq.id)
        else:
            train.append(seq.id)
        if e % 1000 == 0:
            print(e, 'done')
        
    pd.DataFrame(test).to_csv('dataset/testID.csv', index=False)
    pd.DataFrame(train).to_csv('dataset/trainID.csv', index=False)
    
    
    
    
def get_pssm(name):
    sp.run(['psiblast', '-q', name+'_reduced.fasta', '-out_pssm', name, '-inclusion_ethresh', '0.002'])
    
def one_hot_encode(seq):
    """
    df = pd.DataFrame({'seq':[a for a in seq.seq]})
    pd.get_dummies(df['seq']).to_csv('./dataset/binary/'+path+'.csv', index=False)
    """
    arr = np.zeros([len(seq.seq), len(aa)])
    for s in range(len(seq.seq)):
        if seq.seq[s] in aa:
            arr[s, aa.index(seq.seq[s])] = 1
    np.savetxt('./dataset/binary/'+seq.id+'.txt', arr, fmt='%d')
