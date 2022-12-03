# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:12:40 2022

@author: Ana
"""
import time

import pandas as pd
import subprocess as sp

from Bio import SeqIO

from constants import keys

""" 
    Reduce SwissProt.xml, keep only ENZYMES:
        - with length at least 50 and at most 5000 AA
        - with only 1 EC number (single function)
        - with AT MOST 40 % IDENTITY between samples from same functional class
"""
def extract_enzymes(ipt):
    # PARSE XML, write each class to seperate file
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
    

def reduce(names):
    # REMOVE SEQUENCES TOO SIMILAR WITH ONE ANOTHER
    for name in names:
        sp.run(['/mnt/e/DS/cdhit/cd-hit', '-i', name+'.fasta', '-o', name+'.fasta', '-c', '0.4',  '-n', '2', '-d', '0', '-T', '6'])

def main():
    path_to_input = 'uniprot_sprot.xml'
    path_to_output = './temp/by_class/class'
    
    t1 = time.time()
    extract_enzymes(path_to_input)
    t2 = time.time()
    print('Extraction took', str(round((t2-t1)/60, 2)) + 'min')
    
    names = []
    for key in keys:
        names.append(path_to_output+key)
        
    reduce(names)
    t3 = time.time()
    print('Aligning took', str(round((t3-t2)/60, 2)) + 'min')
    
    
    
    
if __name__ == '__main__':
    main()