#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:35:57 2020

@author: araj
"""
import numpy as np
def matrix(ranks):
    
    matr=np.zeros((len(ranks),len(ranks)))
    for i in range(len(ranks)):
        for j in range(len(ranks)):
            if i <j:
                if ranks[i]<ranks[j]:
                    matr[i][j]=1
            if ranks[i]>ranks[j]:
                matr[j][i]=1
    return matr.astype(int)
