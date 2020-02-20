#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:26:12 2020

@author: araj
"""
import numpy as np
import itertools

def kendallTau(A, B):
    pairs = itertools.combinations(range(0, len(A)), 2)
    distance = 0
    for x, y in pairs:
        a = A[x] - A[y]
        b = B[x] - B[y]
        if (a * b < 0):
            distance += 1
    return distance
     
    
def solutions(ranks):
    min_dist = np.inf
    best_rank = None
    n_voters, n_candidates = ranks.shape
    solution=[]
    minimum_distances=[]
    for candidate_rank in itertools.permutations(range(n_candidates)):
        dist = np.sum(kendallTau(candidate_rank, rank) for rank in ranks)
        if dist <= min_dist:
            min_dist = dist
            minimum_distances.append(min_dist)
            best_rank = candidate_rank
            solution.append(candidate_rank)
    indexes = [i for i, x in enumerate(minimum_distances) if x == min(minimum_distances)]
    return min_dist,list(map(list,[solution[i] for i in indexes]))
