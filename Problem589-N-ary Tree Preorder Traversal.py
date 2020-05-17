# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:38:55 2020

@author: MagicDi
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
##########################
# Iteration 
# Time: O(n)
# Space: O(n)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res
    
##########################
# Reecursive   
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res