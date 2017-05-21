#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 01:09:28 2016

@author: jessime
"""

import numpy as np

from sys import argv

def row_col_max(infile):
    matrix = np.loadtxt(infile, delimiter=',')
    max_val = max(matrix.sum(0).max(), matrix.sum(1).max())

    out = 'C:/Users/JMK/Documents/GitHub/Excision/results/tutorial/sum.txt'
    with open(out, 'w') as outfile:
        outfile.write(str(int(max_val)))

def row_col_max_python(infile):
    """This function shows how you could solve this problem without resorting to numpy"""
    pass

if __name__ == '__main__':
    row_col_max(argv[1])
