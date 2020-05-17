# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:11:35 2020

@author: MagicDi
"""

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
############################
# Linear search, X y start together
# Time complexity: O(N)
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        start = 1
        end = 1000
        res = []
        while (start <= 1000 and end >= 1):
            if customfunction.f(start,end) > z:
                end -= 1
            elif customfunction.f(start,end) < z:
                start += 1
            else:
                res.append([start,end])
                end -= 1
                start += 1
        return res

     