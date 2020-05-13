# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:57:08 2020

@author: MagicDi
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 0
        try:
            i = str(num).index('6')
        except ValueError:
            return num
        
        strnum = list(str(num))
        strnum[i] = '9'
        return int(''.join(strnum))