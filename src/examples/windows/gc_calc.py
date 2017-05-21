#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:51:02 2016

@author: jessime
"""

from sys import argv

def calc(seq):
    """Calculate GC content of sequence as a percent."""
    gc = (seq.count('G')+seq.count('C'))/len(seq)
    gc = '{}%\n'.format(str(int(gc*100)))
    out = 'C:/Users/JMK/Documents/GitHub/Excision/results/tutorial/gc.txt'
    with open(out, 'w') as outfile:
        outfile.write(gc)

if __name__ == '__main__':
    calc(argv[1])
