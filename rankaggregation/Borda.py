#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:28:16 2020

@author: araj
"""

#


import numpy as np
import itertools
    
def scores(ranks):
    ranks=ranks.astype(int)
    
    scores={}
    for k in range(np.min(ranks),np.max(ranks)+1):
        scores[k]=0
        
    for i in ranks:
        for j in range(len(i)):
            for k in range(np.min(ranks),np.max(ranks)+1):
                if i[j]==k:
                    scores[k] +=1*(j+1)
    return scores


    
    
def solutions(ranks):
   
 
    fd = {}   
    for key, value in scores(ranks).items(): 
        if value not in fd: 
            fd[value] = [key] 
        else: 
            fd[value].append(key)
            
    new_dict={}
    for a in np.sort(list(map(int,fd.keys()))).tolist():
        new_dict[a]=fd[a]
        
        
    k=list(new_dict.values())
    c=list(itertools.product(*list(map(list,list(map(itertools.permutations,k))))))
    
    d=[]
    for i in range(len(c)):
        d.append(list(map(list,c[i])))
    
    g=[]
    for i in range(len(d)):
        g.append([ item for elem in d[i] for item in elem])
    return g
