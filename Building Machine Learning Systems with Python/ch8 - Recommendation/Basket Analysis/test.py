#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:06:16 2017

@author: saurabh
"""

a = [(1, 3), (1, 5), (2, 3), (2, 5), (3, 5)]
C = set()
for i in a:
    for j in a:
        if (i == j):
            continue
        S1 = set()
        for ii in i:
            S1.add(ii)
        for jj in j:
            S1.add(jj)
        temp_tuple = tuple(S1)
        if len(temp_tuple) != len(i) + 1:
            continue
        C.add(temp_tuple)
print list(C)

import itertools;
xss = (1, 3), (1, 5), (2, 3), (2, 5), (3, 5);
items = sorted({x for xs in xss for x in xs});
print(list(itertools.combinations(items, 4)))