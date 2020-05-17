# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:09:45 2020

@author: MagicDi
"""

arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr = [6,4,7,9,1,5,3]

##########################
# First
def sortByBits(arr):
    ind = [sum(1 for i in list(bin(a)) if i=='1') for a in arr]
    
    dic = {}
    for i in range(len(ind)):
        if ind[i] in dic.keys():
            dic[ind[i]].append(arr[i])
        else:
            dic[ind[i]] = [arr[i]]
    l = []
    for j in sorted(dic.keys()):
        l.extend(sorted(dic[j]))
    return l
sortByBits(arr)

#############################
# Second
def sortByBits(arr):
    arr.sort(key=sort_key)
    return arr
def sort_key(t):
    one = 0
    k = t
    print('------------',t)
    while k:
        if k %2 == 1:
            one += 1
        k = k//2
    print(one,k,t)
    return (one,t)
sortByBits(arr)     

###############################
# Third
def sortByBits(arr):
    return sorted(arr,key = lambda x: (bin(x)[2:].count('1'),x))