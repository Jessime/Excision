#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 01:09:28 2016

@author: jessime
"""

import numpy as np

def squared_sum(in_list):
    """Finds the sum of squares of a list of numbers.
    
    Parameters
    ----------
    in_list : [int/float]
        The numbers to be squared
        
    Returns
    -------
    result : float
        Sum of the square of each number in in_list
    """
    result = np.sum(np.asarray(in_list)**2)
    return result
    
def seen(reference, new_list):
    """Finds unique values in a second list that haven't previously been seen.
    
    reference : list
        First list, used to check the other list
    new_list : list
        Second list, in which we are searching for new items
        
    Returns
    -------
    unique : list
        Single instances of all unique items in new_list
    """
    unique = list(set(new_list).difference(set(reference)))
    return unique