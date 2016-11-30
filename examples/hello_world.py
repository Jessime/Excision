#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:29:09 2016

@author: jessime
"""

def hello():
    out = '/home/jessime/Code/Excision/results/tutorial/hello.txt'
    with open(out, 'w') as outfile:
        outfile.write('HelloWorld!\n')

if __name__ == '__main__':
    hello()