# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:12:40 2022

@author: Ana
"""
import time
import argparse

from data_preprocess_helpers import extract_enzymes, cluster, one_hot_encode, split_traintest
from constants import keys


def ohc():
    for key in keys:
        name = 'temp/by_class/class'+key+'_reduced.fasta'
        one_hot_encode(name)

def reduce(names):
    for name in names:
        cluster(name)
        

    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', 
                        type=str, 
                        default='data/uniprot_sprot.xml', 
                        help='uniprot XML file to reduce')
    parser.add_argument('--output', 
                        type=str, 
                        default='data/enzymes.xml',
                        help='Where to output reducted file')

    args = parser.parse_args()
    
    ipt = args.input
    opt = args.output
    
    t1 = time.time()
    extract_enzymes(ipt)
    t2 = time.time()
    print('Extraction took', str(round((t2-t1)/60, 2)) + 'min')
    names = []
    for key in keys:
        names.append('./temp/by_class/class'+key)
        
    reduce(names)
    split_traintest(names)
    
    t3 = time.time()
    print('Aligning took', str(round((t3-t2)/60, 2)) + 'min')
    
    
    
    
if __name__ == '__main__':
    main()