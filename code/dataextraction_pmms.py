# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:12:40 2022

@author: Ana
"""
import time
import argparse

from data_preprocess_helpers import extract_enzymes, cluster, one_hot_encode, split_traintest
from constants import keys




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', 
                        type=str, 
                        default='uniprot_sprot.xml', 
                        help='uniprot XML file to reduce')
    parser.add_argument('--output', 
                        type=str, 
                        default='data/enzymes.xml',
                        help='Where to output reducted file')

    args = parser.parse_args()
    
    ipt = args.input
    opt = args.output
    
    t1 = time.time()
    keys = ['3', '4', '5', '6', '7']
    names = []
    for key in keys:
        names.append('temp/by_class/class'+key+'.fasta')
        
    
    split_traintest(names)
    
    t2 = time.time()
    print('Aligning took', str(round((t2-t1)/60, 2)) + 'min')
    
    
    
    
if __name__ == '__main__':
    main()