# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:08:57 2020

@author: MagicDi
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recurBST(self,cn,l):
            if cn != None:
                recurBST(self,cn.left,l)
                l.append(cn.val)
                recurBST(self,cn.right,l)
        cn = root
        l = []
        recurBST(self,cn,l)
        res = r = TreeNode(l[0])
        for i in range(len(l)-1):
            r.left,r.right = None,TreeNode(l[i+1])
            r = r.right
        return res
            