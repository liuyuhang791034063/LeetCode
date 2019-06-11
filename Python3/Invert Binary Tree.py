# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Symmetric Tree
   Description:
   Author:           God
   date：            2018/9/25
-------------------------------------------------
   Change Activity:  2018/9/25
-------------------------------------------------
"""
__author__ = 'God'

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None :
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        # root.left, root.right = root.right, root.left
        return root

