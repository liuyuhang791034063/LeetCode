# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       Symmetric binary tree
   Description:
   Author:           God
   date：            2018/11/7
-------------------------------------------------
   Change Activity:  2018/11/7
-------------------------------------------------
"""

__author__ = 'God'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)

    def compare(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val == node2.val:
            if self.compare(node1.left, node2.right) and self.compare(node1.right, node2.left):
                return True
        return False
