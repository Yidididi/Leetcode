# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:04:08 2020

@author: MagicDi
"""

arr= [1,2,2,1,1,3]

############################
# First Atempt
def uniqueOccurrences(arr):
    dic = {}
    for ar in arr:
        if ar in dic:
            dic[ar] += 1
        else:
            dic[ar] = 1
    occur = [dic[ar] for ar in dic.keys()]
    occur_set = (occur)
    if len(occur) == len(occur_set):
        return True
    else:
        return False
uniqueOccurrences(arr)

############################
# Second: use collection module
def uniqueOccurrences(arr):
    from collections import Counter
    cnt = Counter(arr).values()
    return len(cnt)==len(set(cnt))
uniqueOccurrences(arr)

