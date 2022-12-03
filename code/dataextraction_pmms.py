# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:12:40 2022

@author: Ana
"""
import time
import numpy as np

from Bio import SeqIO
from Bio.Blast.Applications import NcbipsiblastCommandline

from constants import keys, aa, path_to_fasta, path_to_bin, path_to_pssmA, path_to_pssmR

""" 
    Using PSI-BLAST returns PSSM matrices (writes them in files), also writes
    fasta and one-hot encoded sequence
"""

def one_hot_encode(seq):
    arr = np.zeros([len(seq.seq), len(aa)])
    for s in range(len(seq.seq)):
        if seq.seq[s] in aa:
            arr[s, aa.index(seq.seq[s])] = 1
    np.savetxt(path_to_bin+seq.id+'.txt', arr, fmt='%d')
    

def call_psiblast(names):
    # CALL PSIBLAST and WRITE ALL 3 files
    train = []
    test = []
    sequences = []
    for name in names:
        sequences = sequences + list(SeqIO.parse(name, 'fasta'))
        
    
    for e, seq in enumerate(sequences):
        one_hot_encode(seq)
        SeqIO.write(seq, path_to_fasta+seq.id+'.fasta', 'fasta')
        psi = NcbipsiblastCommandline(cmd='psiblast', 
                                      query='./dataset/fasta/'+seq.id+'.fasta', 
                                      db='./swiss/uniprot_sprot.fasta', 
                                      evalue=0.002, 
                                      num_iterations='3', 
                                      out_pssm=path_to_pssmR+seq.id+'.asn',
                                      out_ascii_pssm=path_to_pssmA+seq.id+'.pssm',
                                      num_threads=3)
        psi()
        x = np.random.uniform(low=0.0, high=1.0)
        if x <= 0.3:
            test.append(seq.id)
        else:
            train.append(seq.id)
        if e % 500 == 0:
            print(e, 'done')


def main():
    t1 = time.time()
    names = []
    for key in keys:
        names.append('temp/by_class/class'+key+'.fasta')
        
    call_psiblast(names)
    
    t2 = time.time()
    print('Psiblast took', str(round((t2-t1)/60, 2)) + 'min')
    
    
    
    
if __name__ == '__main__':
    main()