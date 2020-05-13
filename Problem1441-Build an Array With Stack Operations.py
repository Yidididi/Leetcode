# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:48:43 2020

@author: MagicDi
"""
#############################
# Option 1:
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        arr = []
        if arr==target:
            return res
        
        i = 1
        while arr != target and i<= n:
            arr.append(i)
            res.append('Push')
            if arr[len(arr)-1] != target[len(arr)-1]:
                del arr[len(arr)-1]
                res.append('Pop')
            i += 1
        return res

#############################
# Option 2:   
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        val = 1
        for i in target:
            for j in range(val,i):
                res.append('Push')
                res.append('Pop')
            res.append('Push')
            val = i+1
        return res