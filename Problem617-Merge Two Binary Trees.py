# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:50:40 2020

@author: MagicDi
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        new = TreeNode()
        if t1 and t2:
            new.val = t1.val+t2.val
            new.left = self.mergeTrees(t1.left,t2.left)
            new.right = self.mergeTrees(t1.right,t2.right)
            return new
        elif t1:
            new.val = t1.val
            new.left = t1.left
            new.right = t1.right
            return new
        elif t2:
            new.val = t2.val
            new.left = t2.left
            new.right = t2.right
            return new

###########################
            # Optimization
    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        else:
            t1.val = t1.val+t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
            return t1