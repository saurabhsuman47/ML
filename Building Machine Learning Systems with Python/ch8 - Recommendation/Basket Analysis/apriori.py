"""
Created on Wed Mar 29 09:20:07 2017

@author: saurabh.s1
"""

from load_data import load_data
import pickle

def check(c, t):
    return c == t.intersection(c)
    
def apriori(input_file):
    
    T, counts = load_data(input_file)
    
    frequent_itemsets = {}
    minsupport = 3000
    valid = set(k for k,v in counts.items() if v > minsupport)
    
    idx = 1
    L = set()
    for item in valid:
        L.add(frozenset([item]))  
        frequent_itemsets.update({frozenset([item]) : counts[item]})
    print idx, len(L)
    
    idx += 1
    
    while L:
        C = set()
        for i in L:
            for j in L:
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
                t1 = frozenset(temp_tuple)
                C.add(t1)
        L = set()
        for c in C:
            c_support = 0
            remove_T = []
            for t in T:
                if len(t) < len(c):
                    remove_T.append(t)
                    continue
                if check(c, t):
                    c_support += 1
            if c_support >= minsupport:
                L.add(c)
                frequent_itemsets.update({c : c_support})
            for remove_t in remove_T:
                T.remove(remove_t)            
        print idx, len(L)
        idx += 1     
    
    #pickle.dump(frequent_itemsets, open("frequent_itemsets.dat", "w"))

if __name__ == '__main__':
    input_file = "retail.dat"
    apriori(input_file)
