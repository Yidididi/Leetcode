# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:33:20 2020

@author: MagicDi
"""

######################
# Time complexity: O(n)
# Spcae Complexity: O(n) (we are assining new elements in array)
def replaceElements(arr):
    for i in range(len(arr)-1): #O(n)
        arr[i] = max(arr[i+1:]) # O(n)
    arr[-1] = -1
    return arr

#################
# optimization on time complexity O(n)
def replaceElements2(arr):
    final = [-1 for i in range(len(arr))]
    for i in range(len(arr)-1,0,-1):
        if arr[i] > final[i]:
            final[i-1] = arr[i]
        else:
            final[i-1] = final[i]
    return final
    
def replaceElements1(arr):
    maxe = -1
    for i in range(len(arr)-1):
        if arr[i]>=maxe:
            maxe = max(arr[i+1:])
        arr[i] = maxe
    arr[-1] = -1
    return arr

