#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:48:05 2022

@author: ana
"""

from Bio import SeqIO

sq = [s.seq for s in SeqIO.parse('./dataset/new_test.fasta', format='fasta')]
print(sq)